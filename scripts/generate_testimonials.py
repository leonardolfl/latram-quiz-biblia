import os, json, subprocess
from PIL import Image

testimonials = [
    {
        "id": 1,
        "name": "Carla Martínez",
        "avatar_bg": "#b45309",
        "avatar_text": "CM",
        "status": "en línea",
        "messages": [
            {"type": "received", "text": "¡Hola! Ya me llegó el material <b>36 Cartas del Baralho Gitano en Mapas Mentales</b> y de verdad que es simplemente increíble! 😍", "time": "10:28"},
            {"type": "received", "text": "Súper lindo, ultra práctico y muy claro todo. ✨", "time": "10:28"},
            {"type": "received", "text": "¡Me está ayudando muchísimo a interpretar las cartas con total seguridad!", "time": "10:29"},
            {"type": "sent", "text": "¡Qué alegría tan linda Carla! Me alegra enormemente que te esté gustando y sirviendo tanto. ✨🌹 ¡Cualquier duda estoy a tu disposición!", "time": "10:31"}
        ]
    },
    {
        "id": 2,
        "name": "Mariana Soler",
        "avatar_bg": "#4338ca",
        "avatar_text": "MS",
        "status": "en línea",
        "messages": [
            {"type": "received", "text": "¡Buenas noches! Ya recibí mi material 🎉", "time": "20:34"},
            {"type": "received", "text": "El libro de las <b>36 Cartas en Mapas Mentales</b> está completísimo y súper bien hecho.", "time": "20:35"},
            {"type": "received", "text": "Las combinaciones de amor y vínculos por fin tuvieron sentido para mí 🙏", "time": "20:35"},
            {"type": "received", "text": "¡Ya lo estoy usando en mis consultas y me ayudó un montón!", "time": "20:36"},
            {"type": "sent", "text": "¡Qué felicidad Mariana! Muchísimas gracias por compartirlo, ¡feliz de ser parte de tu camino! ✨", "time": "20:37"}
        ]
    },
    {
        "id": 3,
        "name": "Lucía Fernández",
        "avatar_bg": "#047857",
        "avatar_text": "LF",
        "status": "últ. vez hoy a las 10:41",
        "messages": [
            {"type": "received", "text": "¡Recibí mi material y estoy fascinada! ✨✨", "time": "10:35"},
            {"type": "received", "text": "Muy organizado y didáctico, las explicaciones con mapas mentales hacen toda la diferencia.", "time": "10:36"},
            {"type": "received", "text": "¡Las combinaciones se volvieron mucho más fáciles de entender ahora!", "time": "10:36"},
            {"type": "sent", "text": "¡Qué alegría saberlo Lucía! ✨ El objetivo es justamente darte claridad y seguridad en cada tirada. ¡Cuenta conmigo siempre! 🌹", "time": "10:39"}
        ]
    },
    {
        "id": 4,
        "name": "Valeria Gómez",
        "avatar_bg": "#c2410c",
        "avatar_text": "VG",
        "status": "en línea",
        "messages": [
            {"type": "received", "text": "Chicas, ¡qué hermosa la página de <b>El Zorro</b>! 🦊 Las explicaciones están clarísimas!", "time": "20:44"},
            {"type": "received", "text": "El diseño visual es maravilloso, quedó perfecto para estudiar.", "time": "20:45"},
            {"type": "received", "text": "Hice lecturas hoy y entendí todo mucho más fácil y rápido. ¡Felicitaciones por el trabajo!", "time": "20:46"},
            {"type": "sent", "text": "¡Me alegra muchísimo saberlo Valeria! Muchísimas gracias por el cariño y la confianza! 🦊✨", "time": "20:47"}
        ]
    },
    {
        "id": 5,
        "name": "Sofía Morales",
        "avatar_bg": "#be185d",
        "avatar_text": "SM",
        "status": "en línea",
        "messages": [
            {"type": "received", "text": "Las explicaciones son directas y al grano 👏", "time": "11:28"},
            {"type": "received", "text": "El material hizo que mis estudios fueran mucho más livianos y organizados ✨", "time": "11:28"},
            {"type": "received", "text": "¡Amé la didáctica y los significados claros de cada carta!", "time": "11:29"},
            {"type": "sent", "text": "¡Qué excelente noticia Sofía! Me hace muy feliz que te esté ayudando en tus estudios! ✨ Que disfrutes cada lectura.", "time": "11:31"}
        ]
    },
    {
        "id": 6,
        "name": "Camila Herrera",
        "avatar_bg": "#0e7490",
        "avatar_text": "CH",
        "status": "últ. vez hoy a las 09:40",
        "messages": [
            {"type": "received", "text": "¡Hola! Ya usé el modelo <b>Tirada de 3 Cartas</b> en una consulta hoy 💖", "time": "09:31"},
            {"type": "received", "text": "Me pareció súper práctico y directo.", "time": "09:31"},
            {"type": "received", "text": "Le dio muchísima claridad a mi clienta para entender pasado, presente y futuro.", "time": "09:31"},
            {"type": "received", "text": "¡Un material sumamente profesional!", "time": "09:32"},
            {"type": "sent", "text": "¡Qué maravilla que te haya servido Camila! ✨ Tus consultantes lo van a agradecer mucho.", "time": "09:37"}
        ]
    },
    {
        "id": 7,
        "name": "Valentina Ramos",
        "avatar_bg": "#7c2d12",
        "avatar_text": "VR",
        "status": "en línea",
        "messages": [
            {"type": "received", "text": "¡Hola! Me llegó el material y está simplemente hermoso y muy bien hecho. 😍", "time": "11:43"},
            {"type": "received", "text": "El cuidado en cada detalle es visible, ¡felicitaciones por tanta dedicación!", "time": "11:44"},
            {"type": "received", "text": "Estoy súper motivada para usarlo en mis lecturas y estudios diarios, va a marcar una gran diferencia.", "time": "11:44"},
            {"type": "sent", "text": "¡Qué felicidad saber eso Valentina! ✨ Disfruta muchísimo tu material y cuenta conmigo para lo que necesites.", "time": "11:45"}
        ]
    },
    {
        "id": 8,
        "name": "Elena Castro",
        "avatar_bg": "#6d28d9",
        "avatar_text": "EC",
        "status": "en línea",
        "messages": [
            {"type": "received", "text": "¡Hola! De verdad la calidad es maravillosa 👏", "time": "10:34"},
            {"type": "received", "text": "El contenido es súper práctico para el estudio del día a día.", "time": "10:34"},
            {"type": "received", "text": "¡Las cartas ahora tienen total sentido para mí!", "time": "10:34"},
            {"type": "sent", "text": "¡Qué gran satisfacción saberlo Elena! ✨ Me alegra mucho que te esté aportando tanta claridad.", "time": "10:36"}
        ]
    },
    {
        "id": 9,
        "name": "Daniela Méndez",
        "avatar_bg": "#0f766e",
        "avatar_text": "DM",
        "status": "últ. vez hoy a las 19:30",
        "messages": [
            {"type": "received", "text": "¡Hola! ¡Amé el material! 😍", "time": "19:18"},
            {"type": "received", "text": "Las explicaciones en los mapas mentales ayudan muchísimo a memorizar los significados súper rápido.", "time": "19:18"},
            {"type": "received", "text": "Ya estoy notando muchísima diferencia en la fluidez de mis lecturas.", "time": "19:19"},
            {"type": "sent", "text": "¡Qué genial Daniela! 😍📚 ¡Sigue así con toda esa energía hermosa!", "time": "19:24"}
        ]
    }
]

html_template = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
  body {{
    width: 420px;
    height: 746px;
    overflow: hidden;
    background: #efeae2;
    display: flex;
    flex-direction: column;
    position: relative;
    user-select: none;
  }}
  /* WhatsApp Wallpaper pattern overlay */
  .wallpaper {{
    position: absolute;
    inset: 0;
    opacity: 0.06;
    background-image: radial-gradient(#000 1px, transparent 1px);
    background-size: 16px 16px;
    pointer-events: none;
  }}
  /* Status Bar */
  .status-bar {{
    height: 28px;
    background: #075e54;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    font-size: 12px;
    font-weight: 500;
    z-index: 10;
  }}
  .status-icons {{
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  /* Header */
  .header {{
    height: 60px;
    background: #075e54;
    color: #ffffff;
    display: flex;
    align-items: center;
    padding: 0 12px;
    gap: 10px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.25);
    z-index: 10;
  }}
  .back-btn {{
    font-size: 20px;
    display: flex;
    align-items: center;
    cursor: pointer;
  }}
  .avatar {{
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: {avatar_bg};
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    font-size: 15px;
    flex-shrink: 0;
  }}
  .contact-info {{
    flex: 1;
    overflow: hidden;
  }}
  .contact-name {{
    font-size: 16px;
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .contact-status {{
    font-size: 12px;
    color: #d1fae5;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .header-actions {{
    display: flex;
    align-items: center;
    gap: 18px;
    color: #ffffff;
  }}
  .header-icon {{
    width: 20px;
    height: 20px;
    fill: currentColor;
  }}
  /* Chat Container */
  .chat-area {{
    flex: 1;
    padding: 16px 14px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    overflow: hidden;
    z-index: 5;
  }}
  .date-badge {{
    align-self: center;
    background: #ffffff;
    color: #54656f;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 8px;
    box-shadow: 0 1px 1px rgba(0,0,0,0.1);
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .bubble {{
    max-width: 82%;
    padding: 8px 12px 6px 12px;
    border-radius: 10px;
    font-size: 14px;
    line-height: 1.38;
    position: relative;
    box-shadow: 0 1px 1.5px rgba(0,0,0,0.15);
    word-break: break-word;
  }}
  .bubble.received {{
    align-self: flex-start;
    background: #ffffff;
    color: #111b21;
    border-top-left-radius: 2px;
  }}
  .bubble.sent {{
    align-self: flex-end;
    background: #d9fdd3;
    color: #111b21;
    border-top-right-radius: 2px;
  }}
  .bubble-footer {{
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 4px;
    margin-top: 4px;
    margin-left: 12px;
    float: right;
  }}
  .time {{
    font-size: 11px;
    color: #667781;
  }}
  .checks {{
    width: 16px;
    height: 12px;
    fill: #53bdeb;
  }}
  /* Input bar */
  .footer-bar {{
    height: 60px;
    padding: 8px 10px;
    display: flex;
    align-items: center;
    gap: 8px;
    z-index: 10;
  }}
  .input-box {{
    flex: 1;
    height: 44px;
    background: #ffffff;
    border-radius: 24px;
    display: flex;
    align-items: center;
    padding: 0 14px;
    gap: 10px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.1);
  }}
  .input-placeholder {{
    flex: 1;
    font-size: 15px;
    color: #8696a0;
  }}
  .input-icon {{
    width: 22px;
    height: 22px;
    fill: #8696a0;
  }}
  .mic-button {{
    width: 44px;
    height: 44px;
    background: #00a884;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    box-shadow: 0 1px 2px rgba(0,0,0,0.2);
  }}
  .mic-icon {{
    width: 22px;
    height: 22px;
    fill: #ffffff;
  }}
</style>
</head>
<body>
  <div class="wallpaper"></div>
  <div class="status-bar">
    <span>{status_time}</span>
    <div class="status-icons">
      <svg width="14" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3c-4.97 0-9 4.03-9 9 0 2.12.74 4.07 1.97 5.61L4 21l3.39-.97C8.93 20.26 10.88 21 12 21c4.97 0 9-4.03 9-9s-4.03-9-9-9z"/></svg>
      <svg width="14" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M12 4C7.31 4 3.07 5.9 0 8.98L12 21 24 8.98C20.93 5.9 16.69 4 12 4z"/></svg>
      <svg width="18" height="12" viewBox="0 0 24 24" fill="currentColor"><rect x="1" y="6" width="18" height="12" rx="2"/><rect x="20" y="10" width="2" height="4" rx="1"/></svg>
    </div>
  </div>

  <div class="header">
    <div class="back-btn">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg>
    </div>
    <div class="avatar">{avatar_text}</div>
    <div class="contact-info">
      <div class="contact-name">{name}</div>
      <div class="contact-status">{status}</div>
    </div>
    <div class="header-actions">
      <svg class="header-icon" viewBox="0 0 24 24"><path d="M17 10.5V7c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1v-3.5l4 4v-11l-4 4z"/></svg>
      <svg class="header-icon" viewBox="0 0 24 24"><path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 0 0-1.01.24l-1.57 1.97c-2.83-1.44-5.15-3.75-6.59-6.59l1.97-1.57c.28-.28.36-.67.25-1.02A11.36 11.36 0 0 1 8.5 4c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.5c0-.55-.45-1-1-1z"/></svg>
      <svg class="header-icon" viewBox="0 0 24 24"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
    </div>
  </div>

  <div class="chat-area">
    <div class="date-badge">Hoy</div>
    {messages_html}
  </div>

  <div class="footer-bar">
    <div class="input-box">
      <svg class="input-icon" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm3.5-9c.83 0 1.5-.67 1.5-1.5S16.33 8 15.5 8 14 8.67 14 9.5s.67 1.5 1.5 1.5zm-7 0c.83 0 1.5-.67 1.5-1.5S9.33 8 8.5 8 7 8.67 7 9.5 7.67 11 8.5 11zm3.5 6.5c2.33 0 4.31-1.46 5.11-3.5H6.89c.8 2.04 2.78 3.5 5.11 3.5z"/></svg>
      <div class="input-placeholder">Mensaje</div>
      <svg class="input-icon" viewBox="0 0 24 24"><path d="M16.5 6v11.5c0 2.21-1.79 4-4 4s-4-1.79-4-4V5a2.5 2.5 0 0 1 5 0v10.5c0 .83-.67 1.5-1.5 1.5s-1.5-.67-1.5-1.5V6H9v9.5a3 3 0 0 0 6 0V5a4 4 0 0 0-8 0v12.5c0 3.04 2.46 5.5 5.5 5.5s5.5-2.46 5.5-5.5V6h-1.5z"/></svg>
      <svg class="input-icon" viewBox="0 0 24 24"><path d="M12 12c1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3 1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-1.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
    </div>
    <div class="mic-button">
      <svg class="mic-icon" viewBox="0 0 24 24"><path d="M12 14c1.66 0 2.99-1.34 2.99-3L15 5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3zm5.3-3c0 3-2.54 5.1-5.3 5.1S6.7 14 6.7 11H5c0 3.41 2.72 6.23 6 6.72V21h2v-3.28c3.28-.48 6-3.3 6-6.72h-1.7z"/></svg>
    </div>
  </div>
</body>
</html>
"""

chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
output_dir = "ciganavisual/assets/images"

for t in testimonials:
    msgs_html = ""
    last_time = "10:35"
    for m in t["messages"]:
        last_time = m["time"]
        check_icon = ""
        if m["type"] == "sent":
            check_icon = """<svg class="checks" viewBox="0 0 16 11"><path d="M11.05.7L4.77 6.98l-2.1-2.1L1.25 6.3l3.52 3.52 7.7-7.7L11.05.7zm3.7 0L8.47 6.98l-.73-.73-.99.99 1.72 1.72 7.7-7.7-1.42-1.42z"/></svg>"""
        msgs_html += f"""
        <div class="bubble {m['type']}">
          {m['text']}
          <div class="bubble-footer">
            <span class="time">{m['time']}</span>
            {check_icon}
          </div>
        </div>
        """
    
    full_html = html_template.format(
        avatar_bg=t["avatar_bg"],
        avatar_text=t["avatar_text"],
        name=t["name"],
        status=t["status"],
        status_time=last_time,
        messages_html=msgs_html
    )

    tmp_html = f"/tmp/dep_{t['id']}.html"
    tmp_png = f"/tmp/dep_{t['id']}.png"
    out_webp = os.path.join(output_dir, f"depoimento-{t['id']}.webp")

    with open(tmp_html, "w") as f:
        f.write(full_html)

    # Render via Chrome headless
    cmd = [
        chrome_bin,
        "--headless",
        "--disable-gpu",
        "--window-size=420,746",
        "--hide-scrollbars",
        f"--screenshot={tmp_png}",
        f"file://{tmp_html}"
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Convert to ultra-fast WebP (quality 82)
    im = Image.open(tmp_png)
    im = im.crop((0, 0, 420, 746))
    im.save(out_webp, "WEBP", quality=82, method=6)
    size_kb = os.path.getsize(out_webp) / 1024
    print(f"Generated {out_webp} ({size_kb:.1f} KB)")
