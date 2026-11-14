import cv2, numpy as np, subprocess, os
from PIL import Image

bonuses_config = [
    {
        "id": "01",
        "banner": "BONO 01",
        "parchment_y": (70, 226),
        "banner_roi_y": (38, 82),
        "parchment_html": """
          <div class="main-title-top" style="top: 96px; font-size: 40px; letter-spacing: 2.5px;">GUÍA DE</div>
          <div class="main-title-bottom" style="top: 140px; font-size: 38px; letter-spacing: 0.8px;">COMBINACIONES</div>
        """,
        "book_inpaint_roi": (318, 390, 175, 320),
        "book_thresh_dark": True,
        "book_html": """
          <div style="position: absolute; top: 335px; left: 172px; width: 155px; text-align: center; font-size: 19px; font-style: italic; font-weight: 600; line-height: 1.15; color: #38123c;">
            Guía de<br>Combinaciones
          </div>
        """
    },
    {
        "id": "02",
        "banner": "BONO 02",
        "parchment_y": (70, 226),
        "banner_roi_y": (38, 82),
        "parchment_html": """
          <div class="main-title-top" style="top: 96px; font-size: 40px; letter-spacing: 2px;">MODELOS DE</div>
          <div class="main-title-bottom" style="top: 140px; font-size: 42px; letter-spacing: 2px;">TIRADAS</div>
        """,
        "book_inpaint_roi": (225, 315, 190, 315),
        "book_thresh_dark": False,
        "book_html": """
          <div style="position: absolute; top: 232px; left: 212px; width: 105px; transform: rotate(-1.5deg);">
            <div class="gold-text" style="font-size: 23px; font-weight: 600; line-height: 1.1; margin-left: 12px;">Modelos</div>
            <div class="gold-text" style="font-size: 21px; font-weight: 600; line-height: 1.1;">de Tiradas</div>
          </div>
        """
    },
    {
        "id": "03",
        "banner": "BONO 03",
        "parchment_y": (70, 235),
        "banner_roi_y": (38, 82),
        "parchment_html": """
          <div class="main-title-top" style="top: 86px; font-size: 36px; letter-spacing: 2px;">GUÍA DE LAS</div>
          <div class="main-title-bottom" style="top: 124px; font-size: 38px; letter-spacing: 1.5px;">POLARIDADES</div>
          <div class="main-title-sub" style="top: 166px; font-size: 28px; letter-spacing: 1.5px;">DE LAS CARTAS</div>
        """,
        "book_inpaint_roi": (420, 520, 160, 330),
        "book_thresh_dark": False,
        "book_html": """
          <div style="position: absolute; top: 432px; left: 165px; width: 160px; text-align: center;">
            <div class="gold-text" style="font-size: 19px; font-weight: 600; line-height: 1.1;">Guía de las</div>
            <div class="gold-text" style="font-size: 24px; font-weight: 600; line-height: 1.1;">Polaridades</div>
            <div class="gold-text" style="font-size: 19px; font-weight: 600; line-height: 1.1;">de las Cartas</div>
          </div>
        """
    },
    {
        "id": "04",
        "banner": "BONO 04",
        "parchment_y": (70, 245),
        "banner_roi_y": (38, 82),
        "parchment_html": """
          <div class="main-title-top" style="top: 96px; font-size: 38px; letter-spacing: 2px;">GUÍA DE LAS</div>
          <div class="main-title-bottom" style="top: 138px; font-size: 30px; letter-spacing: 1px;">PREGUNTAS PODEROSAS</div>
        """,
        "book_inpaint_roi": (252, 365, 175, 315),
        "book_thresh_dark": False,
        "book_html": """
          <div style="position: absolute; top: 275px; left: 172px; width: 145px; text-align: center;">
            <div class="gold-text" style="font-size: 20px; font-weight: 600; line-height: 1.15;">Guía de las</div>
            <div class="gold-text" style="font-size: 24px; font-weight: 600; line-height: 1.15;">Preguntas</div>
            <div class="gold-text" style="font-size: 24px; font-weight: 600; line-height: 1.15;">Poderosas</div>
          </div>
        """
    }
]

for cfg in bonuses_config:
    orig = cv2.imread(f"ciganavisual/assets/images_backup_pt/bonus-{cfg['id']}.webp")
    clean = orig.copy()
    
    # 1. Parchment bilateral smooth gradient fill
    y1, y2 = cfg["parchment_y"]
    x1, x2 = 28, 452
    for y in range(y1, y2):
        left_col = orig[y, x1].astype(np.float32)
        right_col = orig[y, x2].astype(np.float32)
        for x in range(x1, x2 + 1):
            t = (x - x1) / (x2 - x1)
            clean[y, x] = (1 - t) * left_col + t * right_col

    # 2. Inpaint mask
    mask = np.zeros(orig.shape[:2], dtype=np.uint8)
    
    # Banner inpaint
    by1, by2 = cfg["banner_roi_y"]
    banner_roi = orig[by1:by2, 150:330]
    gray_banner = cv2.cvtColor(banner_roi, cv2.COLOR_BGR2GRAY)
    mask_banner = (gray_banner > 100).astype(np.uint8) * 255
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 5))
    mask_banner = cv2.dilate(mask_banner, kernel, iterations=2)
    mask[by1:by2, 150:330] = mask_banner

    # Book cover inpaint
    by1, by2, bx1, bx2 = cfg["book_inpaint_roi"]
    book_roi = orig[by1:by2, bx1:bx2]
    gray_book = cv2.cvtColor(book_roi, cv2.COLOR_BGR2GRAY)
    if cfg["book_thresh_dark"]:
        mask_book = (gray_book < 165).astype(np.uint8) * 255
        mask_book = cv2.dilate(mask_book, np.ones((3,3), np.uint8), iterations=1)
    else:
        mask_book = (gray_book > 90).astype(np.uint8) * 255
        mask_book = cv2.dilate(mask_book, np.ones((3,3), np.uint8), iterations=2)
    mask[by1:by2, bx1:bx2] = mask_book

    final_clean = cv2.inpaint(clean, mask, 5, cv2.INPAINT_TELEA)
    clean_base_path = f"/tmp/clean_bonus_base_{cfg['id']}_prod.png"
    cv2.imwrite(clean_base_path, final_clean)

    # 3. HTML Chrome headless render
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600;1,700&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 480px;
    height: 600px;
    overflow: hidden;
    position: relative;
    background: url('file://{clean_base_path}') no-repeat center center;
    background-size: cover;
    font-family: 'Cormorant Garamond', serif;
  }}
  .banner-text {{
    position: absolute;
    top: 50px;
    left: 0;
    width: 480px;
    text-align: center;
    font-size: 26px;
    font-weight: 700;
    letter-spacing: 4px;
    background: linear-gradient(180deg, #fff2cc 0%, #ffd966 35%, #e5a93b 70%, #bf8019 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 2px 2px rgba(0,0,0,0.8));
  }}
  .main-title-top, .main-title-bottom, .main-title-sub {{
    position: absolute;
    left: 0;
    width: 480px;
    text-align: center;
    font-weight: 600;
    color: #38123c;
    line-height: 1;
  }}
  .gold-text {{
    background: linear-gradient(180deg, #fff2cc 0%, #ffd966 35%, #e5a93b 70%, #bf8019 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 1px 1px rgba(0,0,0,0.6));
  }}
</style>
</head>
<body>
  <div class="banner-text">{cfg['banner']}</div>
  {cfg['parchment_html']}
  {cfg['book_html']}
</body>
</html>
"""
    html_path = f"/tmp/render_bonus_{cfg['id']}_prod.html"
    with open(html_path, "w") as f:
        f.write(html)
        
    png_path = f"/tmp/bonus_{cfg['id']}_prod.png"
    subprocess.run([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless',
        '--disable-gpu',
        '--window-size=480,600',
        '--hide-scrollbars',
        f'--screenshot={png_path}',
        f'file://{html_path}'
    ], check=True)

    im = Image.open(png_path).crop((0, 0, 480, 600))
    webp_path = f"ciganavisual/assets/images/bonus-{cfg['id']}.webp"
    im.save(webp_path, "WEBP", quality=88, method=6)
    print(f"Bonus {cfg['id']} saved to {webp_path} ({os.path.getsize(webp_path)/1024:.1f} KB)")

print("All bonuses compiled successfully!")
