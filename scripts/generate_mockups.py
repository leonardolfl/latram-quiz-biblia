import cv2, numpy as np, subprocess, os
from PIL import Image, ImageDraw, ImageFont

# -------------------------------------------------------------
# 1. BUNDLE MOCKUP (480x360)
# -------------------------------------------------------------
orig_b = cv2.imread('ciganavisual/assets/images_backup_pt/bundle-mockup.webp')
mask_b = np.zeros(orig_b.shape[:2], dtype=np.uint8)

# iMac Screen: y=48..105, x=160..355
imac_roi = orig_b[48:105, 160:355]
gray_imac = cv2.cvtColor(imac_roi, cv2.COLOR_BGR2GRAY)
mask_b[48:105, 160:355] = cv2.dilate((gray_imac < 170).astype(np.uint8)*255, np.ones((2,2), np.uint8), iterations=2)

# Tablet: y=178..195, x=105..175
tab_roi = orig_b[178:195, 105:175]
gray_tab = cv2.cvtColor(tab_roi, cv2.COLOR_BGR2GRAY)
mask_b[178:195, 105:175] = cv2.dilate((gray_tab < 160).astype(np.uint8)*255, np.ones((2,2), np.uint8), iterations=2)

# Mobile: y=180..194, x=385..415
mob_roi = orig_b[180:194, 385:415]
gray_mob = cv2.cvtColor(mob_roi, cv2.COLOR_BGR2GRAY)
mask_b[180:194, 385:415] = cv2.dilate((gray_mob < 160).astype(np.uint8)*255, np.ones((2,2), np.uint8), iterations=2)

# Spines: y=242..298, x=245..355
spines_roi = orig_b[242:298, 245:355]
gray_spines = cv2.cvtColor(spines_roi, cv2.COLOR_BGR2GRAY)
mask_b[242:298, 245:355] = cv2.dilate((gray_spines > 95).astype(np.uint8)*255, np.ones((2,2), np.uint8), iterations=1)

clean_b = cv2.inpaint(orig_b, mask_b, 3, cv2.INPAINT_TELEA)

# Draw EL SOL on mobile with PIL
im_b_pil = Image.fromarray(cv2.cvtColor(clean_b, cv2.COLOR_BGR2RGB))
draw_b = ImageDraw.Draw(im_b_pil)
try:
    font_mob = ImageFont.truetype("/System/Library/Fonts/Times.ttc", 8)
except Exception:
    font_mob = ImageFont.load_default()
draw_b.text((388, 182), "EL SOL", fill=(43, 24, 16), font=font_mob)

clean_bundle_base = cv2.cvtColor(np.array(im_b_pil), cv2.COLOR_RGB2BGR)
cv2.imwrite('/tmp/clean_bundle_prod_base.png', clean_bundle_base)

html_b = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600;1,700&family=Cinzel:wght@600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 480px;
    height: 360px;
    overflow: hidden;
    position: relative;
    background: url('file:///tmp/clean_bundle_prod_base.png') no-repeat center center;
    background-size: cover;
  }
  .imac-sub {
    position: absolute;
    top: 51px;
    left: 175px;
    width: 170px;
    text-align: center;
    font-family: 'Cormorant Garamond', serif;
    font-size: 13.5px;
    font-weight: 600;
    color: #2b1810;
  }
  .imac-main {
    position: absolute;
    top: 66px;
    left: 160px;
    width: 200px;
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 14.5px;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #1a151b;
  }
  .imac-bottom {
    position: absolute;
    top: 86px;
    left: 165px;
    width: 190px;
    text-align: center;
    font-family: 'Cormorant Garamond', serif;
    font-size: 12.5px;
    font-weight: 600;
    letter-spacing: 0.5px;
    color: #4a1942;
  }
  .tab-title {
    position: absolute;
    top: 181px;
    left: 105px;
    width: 70px;
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #2b1810;
  }
  .spine-text {
    font-family: 'Cinzel', serif;
    font-size: 6px;
    font-weight: 700;
    letter-spacing: 0.4px;
    text-align: center;
    background: linear-gradient(180deg, #fff2cc 0%, #ffd966 35%, #e5a93b 70%, #bf8019 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 1px 1px rgba(0,0,0,0.8));
  }
  .spine-sub {
    font-family: 'Cormorant Garamond', serif;
    font-size: 5.5px;
    font-weight: 600;
    letter-spacing: 0.4px;
    text-align: center;
    background: linear-gradient(180deg, #fff2cc 0%, #ffd966 35%, #e5a93b 70%, #bf8019 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .spine-1 {
    position: absolute;
    top: 247px;
    left: 242px;
    width: 110px;
  }
  .spine-2 {
    position: absolute;
    top: 280px;
    left: 242px;
    width: 110px;
  }
</style>
</head>
<body>
  <div class="imac-sub">36 Cartas de la</div>
  <div class="imac-main">BARAJA GITANA</div>
  <div class="imac-bottom">&mdash; en MAPAS MENTALES &mdash;</div>
  <div class="tab-title">EL JINETE</div>
  <div class="spine-1">
    <div class="spine-text">36 CARTAS DE LA BARAJA GITANA</div>
    <div class="spine-sub">&mdash; EN MAPAS MENTALES &mdash;</div>
  </div>
  <div class="spine-2">
    <div class="spine-text">36 CARTAS DE LA BARAJA GITANA</div>
    <div class="spine-sub">&mdash; EN MAPAS MENTALES &mdash;</div>
  </div>
</body>
</html>
"""

with open('/tmp/bundle_prod.html', 'w') as f:
    f.write(html_b)

subprocess.run([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless',
    '--disable-gpu',
    '--window-size=480,360',
    '--hide-scrollbars',
    '--screenshot=/tmp/bundle_prod.png',
    'file:///tmp/bundle_prod.html'
], check=True)

im_b = Image.open('/tmp/bundle_prod.png').crop((0, 0, 480, 360))
im_b.save('ciganavisual/assets/images/bundle-mockup.webp', 'WEBP', quality=88, method=6)
print(f"bundle-mockup.webp ({os.path.getsize('ciganavisual/assets/images/bundle-mockup.webp')/1024:.1f} KB)")


# -------------------------------------------------------------
# 2. HERO & PREMIUM MOCKUP
# -------------------------------------------------------------
orig_h = cv2.imread('ciganavisual/assets/images_backup_pt/hero-mockup.webp')
mask_h = np.zeros(orig_h.shape[:2], dtype=np.uint8)

# Central Book Cover text: y=50..145, x=210..325
book_roi = orig_h[50:145, 210:325]
gray_book = cv2.cvtColor(book_roi, cv2.COLOR_BGR2GRAY)
mask_h[50:145, 210:325] = cv2.dilate((gray_book > 85).astype(np.uint8)*255, np.ones((2,2), np.uint8), iterations=2)

# Central Book Spine: y=80..220, x=180..200
spine_roi = orig_h[80:220, 180:200]
gray_spine = cv2.cvtColor(spine_roi, cv2.COLOR_BGR2GRAY)
mask_h[80:220, 180:200] = cv2.dilate((gray_spine > 110).astype(np.uint8)*255, np.ones((2,2), np.uint8), iterations=1)

# Laptop Header: y=108..130, x=80..170
lap_roi = orig_h[108:130, 80:170]
gray_lap = cv2.cvtColor(lap_roi, cv2.COLOR_BGR2GRAY)
mask_h[108:130, 80:170] = cv2.dilate((gray_lap < 165).astype(np.uint8)*255, np.ones((2,2), np.uint8), iterations=2)

# Tablet Header: y=108..130, x=345..415
tab_roi = orig_h[108:130, 345:415]
gray_tab = cv2.cvtColor(tab_roi, cv2.COLOR_BGR2GRAY)
mask_h[108:130, 345:415] = cv2.dilate((gray_tab < 165).astype(np.uint8)*255, np.ones((2,2), np.uint8), iterations=2)

# Notebook Header: y=235..255, x=240..330
noteb_roi = orig_h[235:255, 240:330]
gray_noteb = cv2.cvtColor(noteb_roi, cv2.COLOR_BGR2GRAY)
mask_h[235:255, 240:330] = cv2.dilate((gray_noteb < 165).astype(np.uint8)*255, np.ones((2,2), np.uint8), iterations=2)

# Background book 2: y=32..55, x=80..130
b2_roi = orig_h[32:55, 80:130]
gray_b2 = cv2.cvtColor(b2_roi, cv2.COLOR_BGR2GRAY)
mask_h[32:55, 80:130] = cv2.dilate((gray_b2 < 140).astype(np.uint8)*255, np.ones((2,2), np.uint8), iterations=2)

clean_h = cv2.inpaint(orig_h, mask_h, 3, cv2.INPAINT_TELEA)
cv2.imwrite('/tmp/clean_hero_prod_base.png', clean_h)

html_h = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600;1,700&family=Cinzel:wght@600;700;800&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 480px;
    height: 320px;
    overflow: hidden;
    position: relative;
    background: url('file:///tmp/clean_hero_prod_base.png') no-repeat center center;
    background-size: cover;
  }
  .gold-text {
    background: linear-gradient(180deg, #fff2cc 0%, #ffd966 35%, #e5a93b 70%, #bf8019 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 1px 1px rgba(0,0,0,0.8));
    text-align: center;
  }
  .book-container {
    position: absolute;
    top: 50px;
    left: 212px;
    width: 108px;
    text-align: center;
  }
  .book-line-1 {
    font-family: 'Cinzel', serif;
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 0.5px;
  }
  .book-line-2 {
    font-family: 'Cinzel', serif;
    font-size: 19px;
    font-weight: 800;
    line-height: 0.95;
    letter-spacing: 1px;
  }
  .book-line-3 {
    font-family: 'Cinzel', serif;
    font-size: 19px;
    font-weight: 800;
    line-height: 0.95;
    letter-spacing: 1px;
  }
  .book-line-4 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin-top: 2px;
  }
  .book-sub {
    font-family: 'Cormorant Garamond', serif;
    font-size: 4px;
    font-weight: 600;
    letter-spacing: 0.2px;
    line-height: 1.1;
    margin-top: 3px;
  }
  .laptop-text {
    position: absolute;
    top: 111px;
    left: 80px;
    width: 90px;
    text-align: center;
  }
  .laptop-title {
    font-family: 'Cinzel', serif;
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #1a151b;
  }
  .laptop-sub {
    font-family: 'Cormorant Garamond', serif;
    font-size: 6px;
    font-weight: 600;
    color: #4a1942;
  }
  .tab-text {
    position: absolute;
    top: 111px;
    left: 345px;
    width: 70px;
    text-align: center;
  }
  .tab-title {
    font-family: 'Cinzel', serif;
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #1a151b;
  }
  .tab-sub {
    font-family: 'Cormorant Garamond', serif;
    font-size: 5.5px;
    font-weight: 600;
    color: #4a1942;
  }
  .notebook-text {
    position: absolute;
    top: 236px;
    left: 247px;
    width: 90px;
    text-align: center;
  }
  .notebook-title {
    font-family: 'Cinzel', serif;
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #1a151b;
  }
  .notebook-sub {
    font-family: 'Cormorant Garamond', serif;
    font-size: 6px;
    font-weight: 600;
    color: #4a1942;
  }
  .spiral-2 {
    position: absolute;
    top: 37px;
    left: 85px;
    width: 40px;
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 5px;
    font-weight: 700;
    color: #2b1810;
    line-height: 1.1;
  }
</style>
</head>
<body>
  <div class="book-container">
    <div class="gold-text book-line-1">36 CARTAS DE LA</div>
    <div class="gold-text book-line-2">BARAJA</div>
    <div class="gold-text book-line-3">GITANA</div>
    <div class="gold-text book-line-4">EN MAPAS MENTALES</div>
    <div class="gold-text book-sub">UNA GU&Iacute;A VISUAL PARA COMPRENDER<br>SIGNIFICADOS, POLARIDADES E INTERPRETACIONES</div>
  </div>
  <div class="laptop-text">
    <div class="laptop-title">01 &mdash; EL JINETE</div>
    <div class="laptop-sub">Mensaje &bull; Movimiento</div>
  </div>
  <div class="tab-text">
    <div class="tab-title">COMBINACIONES</div>
    <div class="tab-sub">&bull; Ejemplos importantes &bull;</div>
  </div>
  <div class="notebook-text">
    <div class="notebook-title">24 &mdash; EL CORAZ&Oacute;N</div>
    <div class="notebook-sub">Amor &bull; Emoci&oacute;n</div>
  </div>
  <div class="spiral-2">MODELOS<br>DE TIRADAS</div>
</body>
</html>
"""

with open('/tmp/hero_prod.html', 'w') as f:
    f.write(html_h)

subprocess.run([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless',
    '--disable-gpu',
    '--window-size=480,320',
    '--hide-scrollbars',
    '--screenshot=/tmp/hero_prod.png',
    'file:///tmp/hero_prod.html'
], check=True)

im_h = Image.open('/tmp/hero_prod.png').crop((0, 0, 480, 320))
im_h.save('ciganavisual/assets/images/hero-mockup.webp', 'WEBP', quality=88, method=6)

im_prem = im_h.resize((420, 280), Image.Resampling.LANCZOS)
im_prem.save('ciganavisual/assets/images/premium-mockup.webp', 'WEBP', quality=88, method=6)

print(f"hero-mockup.webp ({os.path.getsize('ciganavisual/assets/images/hero-mockup.webp')/1024:.1f} KB)")
print(f"premium-mockup.webp ({os.path.getsize('ciganavisual/assets/images/premium-mockup.webp')/1024:.1f} KB)")
print("All mockups generated successfully!")
