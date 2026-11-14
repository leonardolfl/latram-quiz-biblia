import os, subprocess
import cv2, numpy as np
from PIL import Image

bonuses = [
    {
        "id": "01",
        "banner": "BONO 01",
        "main_title": "GUÍA DE<br><span>COMBINACIONES</span>",
        "clean_parchment_y": (85, 205),
    },
    {
        "id": "02",
        "banner": "BONO 02",
        "main_title": "MODELOS DE<br><span>TIRADAS</span>",
        "clean_parchment_y": (85, 205),
    },
    {
        "id": "03",
        "banner": "BONO 03",
        "main_title": "GUÍA DE<br><span>POLARIDADES</span><br><span style='font-size:22px; letter-spacing:1px;'>DE LAS CARTAS</span>",
        "clean_parchment_y": (80, 230),
    },
    {
        "id": "04",
        "banner": "BONO 04",
        "main_title": "GUÍA DE<br><span>PREGUNTAS PODEROSAS</span>",
        "clean_parchment_y": (85, 205),
    }
]

chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
output_dir = "ciganavisual/assets/images"

for b in bonuses:
    orig_path = f"ciganavisual/assets/images_backup_pt/bonus-{b['id']}.webp"
    img = cv2.imread(orig_path)

    # 1. Row-by-row horizontal parchment fill (seamless parchment texture)
    py1, py2 = b["clean_parchment_y"]
    for y in range(py1, py2):
        img[y, 42:438] = img[y, 28]

    # 2. Fill banner text box with exact sample purple
    banner_color = img[62, 145].tolist()
    cv2.rectangle(img, (155, 48), (325, 76), banner_color, -1)

    tmp_base = f"/tmp/bonus_{b['id']}_clean_base.png"
    cv2.imwrite(tmp_base, img)

    # 3. Render HTML overlay with Google Chrome headless
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 480px;
    height: 600px;
    overflow: hidden;
    position: relative;
    background: url('file://{tmp_base}') no-repeat center center;
    background-size: cover;
  }}
  .banner-text {{
    position: absolute;
    top: 48px;
    left: 0;
    width: 480px;
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 26px;
    font-weight: 800;
    letter-spacing: 3px;
    color: #f7d287;
    text-shadow: 0 1px 2px rgba(0,0,0,0.7), 0 0 1px #a16207;
  }}
  .main-title {{
    position: absolute;
    top: 104px;
    left: 0;
    width: 480px;
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 30px;
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: 1.5px;
    color: #3b173f;
    text-shadow: 0 1px 1px rgba(255,255,255,0.8);
  }}
  .main-title span {{
    font-size: 33px;
    letter-spacing: 0.5px;
  }}
</style>
</head>
<body>
  <div class="banner-text">{b['banner']}</div>
  <div class="main-title">{b['main_title']}</div>
</body>
</html>
"""

    tmp_html = f"/tmp/bonus_{b['id']}.html"
    tmp_png = f"/tmp/bonus_{b['id']}_final.png"
    out_webp = os.path.join(output_dir, f"bonus-{b['id']}.webp")

    with open(tmp_html, "w") as f:
        f.write(html_content)

    subprocess.run([
        chrome_bin,
        "--headless",
        "--disable-gpu",
        "--window-size=480,600",
        "--hide-scrollbars",
        f"--screenshot={tmp_png}",
        f"file://{tmp_html}"
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    im = Image.open(tmp_png)
    im = im.crop((0, 0, 480, 600))
    im.save(out_webp, "WEBP", quality=84, method=6)
    size_kb = os.path.getsize(out_webp) / 1024
    print(f"Generated {out_webp} ({size_kb:.1f} KB)")
