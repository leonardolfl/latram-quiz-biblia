import os, subprocess
from PIL import Image

cards_data = [
    {
        "filename": "01_Cavaleiro.webp",
        "art_img": "/tmp/art_01.png",
        "title": "01 • EL JINETE",
        "subtitle": "MOVIMIENTO",
        "palabras": ["Llegada", "Noticias", "Movimiento", "Iniciativa"],
        "positivo": ["Novedades favorables", "Avance rápido", "Oportunidades en camino", "Determinación para actuar"],
        "alerta": ["Prisa excesiva y precipitación", "Actuar sin comprender el contexto", "Acontecimientos imprevistos"],
        "simbolica": '"Algunos caminos solo comienzan a cambiar verdaderamente cuando existe movimiento."',
        "carta_dia": "Observa lo que está llegando hoy a tu vida y prepárate para tomar la iniciativa con total consciencia.",
        "general": "Representa llegada, impulso activo, noticias y nuevas dinámicas en marcha. Señala situaciones que empiezan a ganar aceleración y pronta resolución.",
        "amor": "Acercamiento de personas, mensajes importantes, reactivación del contacto o alguien tomando la iniciativa afectiva.",
        "trabajo": "Llegada de propuestas, respuestas laborales esperadas, negociaciones activas y avances profesionales tangibles."
    },
    {
        "filename": "14_Raposa.webp",
        "art_img": "/tmp/art_14.png",
        "title": "14 • EL ZORRO",
        "subtitle": "CAUTELA",
        "palabras": ["Cautela", "Observación", "Estrategia", "Interés"],
        "positivo": ["Inteligencia práctica", "Capacidad de adaptación", "Atención al detalle", "Percepción aguda de riesgos"],
        "alerta": ["Desconfianza excesiva", "Oportunismo", "Intenciones ocultas", "Exceso de frialdad o cálculo"],
        "simbolica": '"El Zorro indica la necesidad de ser astuto y cuidadoso, evitando trampas y analizando conductas."',
        "carta_dia": "Actúa con inteligencia y prudencia antes de aceptar propuestas o acuerdos apresurados.",
        "general": "Invita a la observación cuidadosa y a la estrategia mental. Representa astucia y autoprotección ante situaciones donde las apariencias engañan.",
        "amor": "Señala prudencia, necesidad de observar intenciones reales y proteger la propia vulnerabilidad afectiva.",
        "trabajo": "Fuertemente vinculada a la estrategia profesional, competencia en el trabajo y cuidado con intereses ajenos."
    },
    {
        "filename": "24_Coracao.webp",
        "art_img": "/tmp/art_24.png",
        "title": "24 • EL CORAZÓN",
        "subtitle": "AFECTO",
        "palabras": ["Amor", "Afecto", "Emoción", "Pasión"],
        "positivo": ["Amor sincero", "Conexión emocional profunda", "Alegría y calidez afectiva", "Generosidad y entrega"],
        "alerta": ["Idealización romántica", "Guiarse únicamente por la pasión", "Dependencia emocional", "Expectativas desmedidas"],
        "simbolica": '"El corazón ilumina lo valioso afectivamente, pero jamás elimina la necesidad de discernimiento."',
        "carta_dia": "Escucha lo que te dictan tus sentimientos sin perder la claridad y el buen juicio.",
        "general": "Representa sentimientos puros, amor genuino, empatía y todo lo que genera un vínculo emocional significativo.",
        "amor": "Amor correspondido, ternura, reconciliación, profundización de los lazos y apertura afectiva plena.",
        "trabajo": "Trabajo hecho por vocación, satisfacción laboral, realización en lo que amas y proyectos con propósito."
    },
    {
        "filename": "31_Sol.webp",
        "art_img": "/tmp/art_31.png",
        "title": "31 • EL SOL",
        "subtitle": "ÉXITO",
        "palabras": ["Claridad", "Energía", "Éxito", "Vitalidad"],
        "positivo": ["Triunfo y victoria", "Confianza plena", "Crecimiento radiante", "Reconocimiento y luz"],
        "alerta": ["Exceso de soberbia o ego", "Sobreexposición", "Dar el éxito por sentado sin esfuerzo"],
        "simbolica": '"Cuando reina la claridad total, resulta natural canalizar tu energía hacia tus mayores metas."',
        "carta_dia": "Proyecta tu energía con seguridad y avanza con optimismo hacia lo que te corresponde.",
        "general": "Ilumina cualquier área de la vida con vitalidad, verdad, prosperidad y resultados extraordinariamente favorables.",
        "amor": "Felicidad compartida, transparencia de intenciones, calidez, pasión luminosa y armonía de pareja.",
        "trabajo": "Reconocimiento merecido, liderazgo, éxito en negocios o proyectos, alta productividad y abundancia."
    },
    {
        "filename": "33_Chave.webp",
        "art_img": "/tmp/art_33.png",
        "title": "33 • LA LLAVE",
        "subtitle": "SOLUCIÓN",
        "palabras": ["Solución", "Apertura", "Respuesta", "Certeza"],
        "positivo": ["Resolución de conflictos", "Apertura de caminos", "Nuevas oportunidades", "Descubrimiento liberador"],
        "alerta": ["Buscar atajos fáciles", "Creer que solo existe una alternativa", "Intentar abrir puertas equivocadas"],
        "simbolica": '"Una llave no solo desbloquea caminos, sino que revela el poder personal que guardas en tu interior."',
        "carta_dia": "Tienes en tus manos la solución que buscabas: da el paso con total seguridad y convicción.",
        "general": "Representa la resolución definitiva de bloqueos, apertura de caminos providenciales y hallazgo de respuestas certeras.",
        "amor": "Conversación aclaratoria decisiva, superación de trabas y consolidación firme del entendimiento mutuo.",
        "trabajo": "Cierre de acuerdos clave, contratos favorables, oportunidades decisivas y soluciones financieras exitosas."
    }
]

html_template = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 640px;
    height: 480px;
    overflow: hidden;
    background: #fbf7ee;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #2c2523;
    padding: 12px 14px;
    position: relative;
  }}
  .frame {{
    position: absolute;
    inset: 6px;
    border: 1.5px solid #d4af37;
    border-radius: 8px;
    pointer-events: none;
  }}
  .inner-frame {{
    position: absolute;
    inset: 9px;
    border: 0.5px solid rgba(212, 175, 55, 0.4);
    border-radius: 6px;
    pointer-events: none;
  }}
  
  .header {{
    text-align: center;
    margin-bottom: 8px;
    position: relative;
    z-index: 2;
  }}
  .title {{
    font-family: 'Cinzel', serif;
    font-size: 20px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #4a2810;
    text-transform: uppercase;
  }}
  .subtitle {{
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    color: #92400e;
    text-transform: uppercase;
    margin-top: 1px;
  }}

  .grid-container {{
    display: grid;
    grid-template-columns: 208px 196px 208px;
    gap: 8px;
    height: 414px;
    position: relative;
    z-index: 2;
  }}

  .col {{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}

  .box {{
    background: #ffffff;
    border: 1px solid #e8dec8;
    border-radius: 6px;
    padding: 6px 8px;
    box-shadow: 0 1px 2px rgba(74, 40, 16, 0.05);
    display: flex;
    flex-direction: column;
  }}
  .box-title {{
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 4px;
  }}
  .box-content {{
    font-size: 8.5px;
    line-height: 1.35;
    color: #443e38;
  }}
  .box ul {{
    list-style: none;
    padding-left: 0;
  }}
  .box li {{
    position: relative;
    padding-left: 9px;
    margin-bottom: 1px;
  }}
  .box li::before {{
    content: "•";
    position: absolute;
    left: 1px;
    color: #d97706;
    font-weight: bold;
  }}

  .theme-gold .box-title {{ color: #b45309; }}
  .theme-green .box-title {{ color: #047857; }}
  .theme-blue .box-title {{ color: #0369a1; }}
  .theme-rose .box-title {{ color: #be123c; }}
  .theme-purple .box-title {{ color: #6d28d9; }}

  .center-col {{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
  }}
  .art-wrapper {{
    width: 192px;
    height: 266px;
    border-radius: 6px;
    overflow: hidden;
    box-shadow: 0 3px 8px rgba(74, 40, 16, 0.18);
    border: 1.5px solid #d4af37;
    margin-bottom: 6px;
    background: #000;
  }}
  .art-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }}
  .center-box {{
    width: 100%;
    flex: 1;
    background: #fdfbf7;
    border: 1px solid #e2d5b8;
  }}
</style>
</head>
<body>
  <div class="frame"></div>
  <div class="inner-frame"></div>

  <div class="header">
    <div class="title">{title}</div>
    <div class="subtitle">{subtitle}</div>
  </div>

  <div class="grid-container">
    <!-- Left Column -->
    <div class="col">
      <div class="box theme-green" style="flex: 0.85;">
        <div class="box-title">✦ Palabras Clave</div>
        <ul class="box-content">
          {palabras_html}
        </ul>
      </div>

      <div class="box theme-blue" style="flex: 1;">
        <div class="box-title">✦ Potencial Positivo</div>
        <ul class="box-content">
          {positivo_html}
        </ul>
      </div>

      <div class="box theme-rose" style="flex: 1;">
        <div class="box-title">✦ Alerta</div>
        <ul class="box-content">
          {alerta_html}
        </ul>
      </div>

      <div class="box theme-gold" style="flex: 0.95;">
        <div class="box-title">✦ Clave Simbólica</div>
        <div class="box-content" style="font-style: italic;">
          {simbolica}
        </div>
      </div>
    </div>

    <!-- Center Column -->
    <div class="col center-col">
      <div class="art-wrapper">
        <img class="art-img" src="{art_img}" alt="{title}"/>
      </div>
      <div class="box center-box theme-purple">
        <div class="box-title">✦ Carta del Día</div>
        <div class="box-content">
          {carta_dia}
        </div>
      </div>
    </div>

    <!-- Right Column -->
    <div class="col">
      <div class="box theme-gold" style="flex: 1.15;">
        <div class="box-title">✦ Significado General</div>
        <div class="box-content">
          {general}
        </div>
      </div>

      <div class="box theme-rose" style="flex: 1;">
        <div class="box-title">✦ Amor y Relaciones</div>
        <div class="box-content">
          {amor}
        </div>
      </div>

      <div class="box theme-blue" style="flex: 1;">
        <div class="box-title">✦ Dinero y Trabajo</div>
        <div class="box-content">
          {trabajo}
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""

chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
output_dir = "ciganavisual/assets/images"

for c in cards_data:
    palabras_html = "".join([f"<li>{p}</li>" for p in c["palabras"]])
    positivo_html = "".join([f"<li>{p}</li>" for p in c["positivo"]])
    alerta_html = "".join([f"<li>{p}</li>" for p in c["alerta"]])

    rendered_html = html_template.format(
        title=c["title"],
        subtitle=c["subtitle"],
        art_img=c["art_img"],
        palabras_html=palabras_html,
        positivo_html=positivo_html,
        alerta_html=alerta_html,
        simbolica=c["simbolica"],
        carta_dia=c["carta_dia"],
        general=c["general"],
        amor=c["amor"],
        trabajo=c["trabajo"]
    )

    tmp_html = f"/tmp/{c['filename']}.html"
    tmp_png = f"/tmp/{c['filename']}.png"
    out_webp = os.path.join(output_dir, c["filename"])

    with open(tmp_html, "w") as f:
        f.write(rendered_html)

    subprocess.run([
        chrome_bin,
        "--headless",
        "--disable-gpu",
        "--window-size=640,480",
        "--hide-scrollbars",
        f"--screenshot={tmp_png}",
        f"file://{tmp_html}"
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    im = Image.open(tmp_png)
    im = im.crop((0, 0, 640, 480))
    im.save(out_webp, "WEBP", quality=84, method=6)
    size_kb = os.path.getsize(out_webp) / 1024
    print(f"Generated {out_webp} ({size_kb:.1f} KB)")
