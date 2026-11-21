# scripts/build_html_and_artifact.py
# -*- coding: utf-8 -*-
import json
import os
import html

with open('catalogo/ofertas.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

ofertas = data["ofertas"]
top10_es = [o for o in ofertas if o.get("top10_es")]
top10_es.sort(key=lambda x: x["top10_details"]["rank"])

top10_br = [o for o in ofertas if o.get("top10_br")]
top10_br.sort(key=lambda x: x["top10_details"]["rank"])

print(f"Loaded {len(ofertas)} offers. Generating HTML and Markdown artifact...")

# --- 1. BUILD MARKDOWN ARTIFACT ---
md = []
md.append("# 💎 Catálogo Geral de 400 Ofertas VSL & Low Ticket Whitehat")
md.append("### *Filtros Exclusivos: Top 10 Escalar em Espanhol (ES), Top 10 Escalar no Brasil (PT-BR) e 200 Novas Ofertas BR*")
md.append("")
md.append("> [!NOTE]")
md.append("> **Critério Ético Rigoroso (\"Consciência Limpa / Sem se Explicar pra Deus\")**: Zero nichos pretos, zero promessas milagrosas de cura, zero cassinos/apostas, zero fórmulas de enriquecimento rápido. Produtos focados em habilidades manuais, maternidade, infância sem telas, postura e mobilidade suave, culinária caseira, pets e espiritualidade/fé.")
md.append("")
md.append("---")
md.append("")
md.append("## 🏆 PARTE 1: TOP 10 OFERTAS PARA VALIDAR E ESCALAR COM ALTO ROI EM ESPANHOL (ES)")
md.append("*(Selecionadas a dedo com base em CPM reduzido na América Latina [US$ 1.50 - US$ 3.00], altíssima demanda emocional, ticket acessível [$9.90 - $14.90] e baixíssima taxa de reembolso [<1%])*")
md.append("")

for o in top10_es:
    det = o["top10_details"]
    md.append(f"### 🥇 #{det['rank']} — {o['nome']} (`{o['id']}`)")
    md.append(f"- **Nicho:** {o['nicho']} | **Ticket Front-End:** {o['ticket']}")
    md.append(f"- **Por que vai estourar de ROI (Análise de Escala):** {det['motivo']}")
    md.append(f"- **Estrutura do Funil (AOV Otimizado):** {det['funil']}")
    md.append(f"- **Gancho Principal para VSL / Criativo:** {det['hook']}")
    md.append(f"- **Dork para Meta Ad Library:** `{o['dork']}`")
    md.append("")

md.append("---")
md.append("")
md.append("## 🚀 PARTE 2: TOP 10 OFERTAS PARA VALIDAR E ESCALAR COM ALTO ROI NO BRASIL (PT-BR)")
md.append("*(Selecionadas das 200 novas ofertas para o mercado brasileiro: apelo violento de compra imediata via Pix [R$ 19,90 a R$ 29,90], order bumps inteligentes que elevam o ticket médio acima de R$ 40,00 e solução prática para dores diárias)*")
md.append("")

for o in top10_br:
    det = o["top10_details"]
    md.append(f"### 🇧🇷 #{det['rank']} — {o['nome']} (`{o['id']}`)")
    md.append(f"- **Nicho:** {o['nicho']} | **Ticket Front-End:** {o['ticket']}")
    md.append(f"- **Por que vai estourar de ROI no Brasil:** {det['motivo']}")
    md.append(f"- **Estrutura do Funil (Pix + Order Bumps):** {det['funil']}")
    md.append(f"- **Gancho de VSL / Criativo:** {det['hook']}")
    md.append(f"- **Dork para Meta Ad Library BR:** `{o['dork']}`")
    md.append("")

md.append("---")
md.append("")
md.append("## 🇧🇷 PARTE 3: AS 200 NOVAS OFERTAS LOW TICKET BRASILEIRAS (PT-BR)")
md.append("*(Zero repetição com as 200 internacionais anteriores. 10 nichos estruturados com 20 produtos cada, tickets de R$ 14,90 a R$ 29,90, formato digital e dork de espionagem)*")
md.append("")

br_offers = [o for o in ofertas if o["idioma"] == "PT-BR"]
nichos_br = sorted(list(set(o["nicho"] for o in br_offers)))

for nicho in nichos_br:
    md.append(f"### 📦 Nicho: {nicho} (20 Ofertas)")
    md.append("| # ID | Nome da Oferta | Ticket | Formato | Dork Meta Ad Library |")
    md.append("| :--- | :--- | :---: | :--- | :--- |")
    nicho_items = [o for o in br_offers if o["nicho"] == nicho]
    for item in nicho_items:
        clean_dork = item['dork'].replace('`', '')
        md.append(f"| `{item['id']}` | **{item['nome']}**<br>*{item['descricao'][:75]}...* | **{item['ticket']}** | {item['formato']} | `{clean_dork}` |")
    md.append("")

md.append("---")
md.append("")
md.append("## 🌍 PARTE 4: AS 200 OFERTAS INTERNACIONAIS (ESPANHOL, FRANCÊS E INGLÊS)")
md.append("*(O acervo internacional completo de 200 produtos para modelagem e tradução imediata)*")
md.append("")

int_offers = [o for o in ofertas if o["idioma"] != "PT-BR"]
for lang_code, lang_name, flag in [("ES", "Espanhol (70 Ofertas)", "🇪🇸"), ("FR", "Francês (65 Ofertas)", "🇫🇷"), ("EN", "Inglês (65 Ofertas)", "🇺🇸")]:
    md.append(f"### {flag} {lang_name}")
    md.append("| # ID | Nome da Oferta | Ticket | Dork Meta Ad Library |")
    md.append("| :--- | :--- | :---: | :--- |")
    lang_items = [o for o in int_offers if o["idioma"] == lang_code]
    for item in lang_items:
        clean_dork = item['dork'].replace('`', '')
        md.append(f"| `{item['id']}` | **{item['nome']}** | **{item['ticket']}** | `{clean_dork}` |")
    md.append("")

artifact_path = '/Users/fernandeslf_/.gemini/antigravity/brain/05ae73e9-d3b9-4afa-b2dc-bc477a055db8/catalogo_completo_400_ofertas_e_top10.md'
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(md))

print(f"Artifact markdown gravado com sucesso em: {artifact_path}")

# --- 2. BUILD INTERACTIVE HTML APP ---
html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Catálogo Interativo de 400 Ofertas Whitehat | VSL & Low Ticket</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #0B0F19;
      --card-bg: #131A2B;
      --card-border: rgba(255, 255, 255, 0.08);
      --card-hover: rgba(255, 255, 255, 0.14);
      --primary: #8B5CF6;
      --primary-light: #A78BFA;
      --accent-gold: #F59E0B;
      --accent-green: #10B981;
      --accent-cyan: #06B6D4;
      --text-main: #F3F4F6;
      --text-muted: #9CA3AF;
      --badge-bg: rgba(139, 92, 246, 0.15);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', sans-serif;
      min-height: 100vh;
      padding-bottom: 60px;
    }}
    header {{
      background: linear-gradient(180deg, #161F36 0%, #0B0F19 100%);
      border-bottom: 1px solid var(--card-border);
      padding: 36px 20px 24px;
      text-align: center;
    }}
    .container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 16px;
    }}
    h1 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.2rem;
      font-weight: 700;
      background: linear-gradient(135deg, #FFF 40%, var(--primary-light) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
    }}
    .subtitle {{
      color: var(--text-muted);
      font-size: 0.95rem;
      max-width: 680px;
      margin: 0 auto 20px;
      line-height: 1.5;
    }}
    .stats-bar {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 12px;
      margin-top: 16px;
    }}
    .stat-pill {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--card-border);
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-main);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .stat-pill span {{
      color: var(--primary-light);
    }}

    /* Filters Bar */
    .controls {{
      margin: 24px 0 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .search-box {{
      position: relative;
      width: 100%;
    }}
    .search-box input {{
      width: 100%;
      background: #172036;
      border: 1px solid var(--card-border);
      padding: 14px 20px 14px 46px;
      border-radius: 14px;
      color: #FFF;
      font-size: 0.95rem;
      outline: none;
      transition: all 0.2s;
    }}
    .search-box input:focus {{
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.25);
    }}
    .search-icon {{
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
    }}

    .filter-tabs {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .tab-btn {{
      background: #172036;
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      padding: 9px 16px;
      border-radius: 12px;
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .tab-btn:hover {{
      background: #202D4C;
      color: #FFF;
      border-color: rgba(255,255,255,0.2);
    }}
    .tab-btn.active {{
      background: var(--primary);
      color: #FFF;
      border-color: var(--primary-light);
      box-shadow: 0 4px 14px rgba(139, 92, 246, 0.35);
    }}
    .tab-btn.active-top-es {{
      background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
      color: #FFF;
      border-color: #FBBF24;
      box-shadow: 0 4px 14px rgba(245, 158, 11, 0.4);
    }}
    .tab-btn.active-top-br {{
      background: linear-gradient(135deg, #10B981 0%, #059669 100%);
      color: #FFF;
      border-color: #34D399;
      box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
    }}

    /* Grid & Cards */
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 18px;
    }}
    .card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
      position: relative;
      overflow: hidden;
    }}
    .card:hover {{
      transform: translateY(-3px);
      border-color: var(--card-hover);
      box-shadow: 0 10px 24px rgba(0,0,0,0.35);
    }}
    .card.top10-highlight {{
      border: 1.5px solid var(--accent-gold);
      background: linear-gradient(165deg, rgba(245, 158, 11, 0.08) 0%, #131A2B 60%);
    }}
    .card.top10-br-highlight {{
      border: 1.5px solid var(--accent-green);
      background: linear-gradient(165deg, rgba(16, 185, 129, 0.08) 0%, #131A2B 60%);
    }}
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
      gap: 8px;
    }}
    .badge-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
    }}
    .id-badge {{
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-muted);
      font-family: monospace;
    }}
    .lang-badge {{
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      background: #1E293B;
      color: #94A3B8;
    }}
    .top-badge-es {{
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 6px;
      background: rgba(245, 158, 11, 0.2);
      color: #FBBF24;
      border: 1px solid rgba(245, 158, 11, 0.4);
    }}
    .top-badge-br {{
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 6px;
      background: rgba(16, 185, 129, 0.2);
      color: #34D399;
      border: 1px solid rgba(16, 185, 129, 0.4);
    }}
    .ticket-badge {{
      font-size: 0.85rem;
      font-weight: 800;
      color: #10B981;
      background: rgba(16, 185, 129, 0.12);
      padding: 4px 10px;
      border-radius: 8px;
      white-space: nowrap;
    }}

    .card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #FFF;
      line-height: 1.35;
      margin-bottom: 8px;
    }}
    .card-nicho {{
      font-size: 0.78rem;
      color: var(--primary-light);
      font-weight: 600;
      margin-bottom: 10px;
    }}
    .card-desc {{
      font-size: 0.86rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 16px;
      flex-grow: 1;
    }}
    .bump-box {{
      background: rgba(255, 255, 255, 0.03);
      border-left: 3px solid var(--accent-cyan);
      padding: 8px 12px;
      border-radius: 0 8px 8px 0;
      font-size: 0.78rem;
      color: #CBD5E1;
      margin-bottom: 14px;
    }}
    .bump-box strong {{
      color: var(--accent-cyan);
    }}

    .card-actions {{
      display: flex;
      gap: 8px;
      margin-top: 10px;
    }}
    .btn-copy {{
      flex: 1;
      background: #1E293B;
      border: 1px solid var(--card-border);
      color: #E2E8F0;
      padding: 9px 12px;
      border-radius: 10px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .btn-copy:hover {{
      background: #334155;
      border-color: rgba(255,255,255,0.25);
    }}
    .btn-details {{
      background: rgba(139, 92, 246, 0.15);
      border: 1px solid rgba(139, 92, 246, 0.3);
      color: var(--primary-light);
      padding: 9px 12px;
      border-radius: 10px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .btn-details:hover {{
      background: var(--primary);
      color: #FFF;
    }}

    /* Toast */
    #toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #10B981;
      color: #FFF;
      padding: 12px 20px;
      border-radius: 10px;
      font-weight: 700;
      font-size: 0.88rem;
      box-shadow: 0 8px 24px rgba(0,0,0,0.4);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 999;
    }}
    #toast.show {{
      transform: translateY(0);
      opacity: 1;
    }}

    /* Modal */
    .modal-overlay {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(6px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }}
    .modal-box {{
      background: #131A2B;
      border: 1px solid var(--card-border);
      border-radius: 20px;
      max-width: 620px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 28px;
      position: relative;
      box-shadow: 0 20px 50px rgba(0,0,0,0.6);
    }}
    .modal-close {{
      position: absolute;
      top: 20px;
      right: 20px;
      background: #1E293B;
      border: none;
      color: var(--text-muted);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-weight: bold;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .modal-close:hover {{
      background: #334155;
      color: #FFF;
    }}
    .modal-field {{
      margin-top: 16px;
    }}
    .modal-field label {{
      display: block;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--primary-light);
      margin-bottom: 6px;
    }}
    .modal-field .value {{
      background: #172036;
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 12px 14px;
      font-size: 0.88rem;
      line-height: 1.5;
      color: #E2E8F0;
    }}
    .modal-field code {{
      color: var(--accent-gold);
      font-family: monospace;
    }}

    @media (max-width: 640px) {{
      h1 {{ font-size: 1.6rem; }}
      .grid {{ grid-template-columns: 1fr; }}
      .modal-box {{ padding: 20px; }}
    }}
  </style>
</head>
<body>

<header>
  <div class="container">
    <h1>Catálogo de 400 Ofertas Whitehat</h1>
    <p class="subtitle">
      Espionagem estruturada para VSL e Low Ticket em nichos 100% éticos ("sem se explicar pra Deus").
      Filtre pelos Top 10 mais lucrativos e copie as dorks de busca da Ad Library com 1 clique.
    </p>

    <div class="stats-bar">
      <div class="stat-pill">📊 Total: <span>400 Ofertas</span></div>
      <div class="stat-pill">🔥 Top 10 Espanhol: <span>Escala ES</span></div>
      <div class="stat-pill">🚀 Top 10 Brasil: <span>Escala PT-BR</span></div>
      <div class="stat-pill">🇧🇷 Novas BR: <span>200 Ofertas</span></div>
      <div class="stat-pill">🌍 Internacionais: <span>200 Ofertas</span></div>
    </div>
  </div>
</header>

<main class="container">
  <div class="controls">
    <div class="search-box">
      <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      <input type="text" id="searchInput" placeholder="Buscar por título, nicho, dork ou ID (ex: amigurumi, sono, desfralde, mapas)..." oninput="filterOffers()"/>
    </div>

    <div class="filter-tabs">
      <button class="tab-btn active-top-es" id="tabTopES" onclick="setFilter('top10_es')">🔥 Top 10 Escalar em Espanhol (ES)</button>
      <button class="tab-btn active-top-br" id="tabTopBR" onclick="setFilter('top10_br')">🚀 Top 10 Escalar no Brasil (PT-BR)</button>
      <button class="tab-btn" id="tabBR" onclick="setFilter('br')">🇧🇷 200 Novas Low Ticket BR</button>
      <button class="tab-btn" id="tabINT" onclick="setFilter('int')">🌍 200 Internacionais (ES, FR, EN)</button>
      <button class="tab-btn active" id="tabALL" onclick="setFilter('all')">Todos (400)</button>
    </div>
  </div>

  <div id="resultsCount" style="margin-bottom: 16px; font-size: 0.85rem; color: var(--text-muted); font-weight: 600;">
    Exibindo 400 ofertas
  </div>

  <div class="grid" id="offersGrid">
    <!-- Cards rendered via JS -->
  </div>
</main>

<!-- Details Modal -->
<div class="modal-overlay" id="modalOverlay" onclick="closeModal()">
  <div class="modal-box" onclick="event.stopPropagation()">
    <button class="modal-close" onclick="closeModal()">✕</button>
    <div id="modalContent"></div>
  </div>
</div>

<div id="toast">Dork copiada para a área de transferência!</div>

<script>
  const offersData = {json.dumps(ofertas, ensure_ascii=False)};
  let currentFilter = 'all';

  function setFilter(filterName) {{
    currentFilter = filterName;
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    
    if (filterName === 'all') document.getElementById('tabALL').classList.add('active');
    else if (filterName === 'top10_es') document.getElementById('tabTopES').classList.add('active');
    else if (filterName === 'top10_br') document.getElementById('tabTopBR').classList.add('active');
    else if (filterName === 'br') document.getElementById('tabBR').classList.add('active');
    else if (filterName === 'int') document.getElementById('tabINT').classList.add('active');

    filterOffers();
  }}

  function filterOffers() {{
    const query = document.getElementById('searchInput').value.toLowerCase().trim();
    const grid = document.getElementById('offersGrid');
    
    let filtered = offersData.filter(o => {{
      // Filter tab logic
      if (currentFilter === 'top10_es' && !o.top10_es) return false;
      if (currentFilter === 'top10_br' && !o.top10_br) return false;
      if (currentFilter === 'br' && o.idioma !== 'PT-BR') return false;
      if (currentFilter === 'int' && o.idioma === 'PT-BR') return false;

      // Search query logic
      if (!query) return true;
      const haystack = (o.nome + ' ' + o.nicho + ' ' + o.id + ' ' + o.dork + ' ' + (o.descricao || '')).toLowerCase();
      return haystack.includes(query);
    }});

    // Sort: if top10 selected, order by rank
    if (currentFilter === 'top10_es') {{
      filtered.sort((a,b) => (a.top10_details?.rank || 99) - (b.top10_details?.rank || 99));
    }} else if (currentFilter === 'top10_br') {{
      filtered.sort((a,b) => (a.top10_details?.rank || 99) - (b.top10_details?.rank || 99));
    }}

    document.getElementById('resultsCount').innerText = `Exibindo ${{filtered.length}} de ${{offersData.length}} ofertas`;

    grid.innerHTML = filtered.map(o => {{
      const isTopES = !!o.top10_es;
      const isTopBR = !!o.top10_br;
      const highlightClass = isTopES ? 'top10-highlight' : (isTopBR ? 'top10-br-highlight' : '');

      let rankBadge = '';
      if (isTopES) rankBadge = `<span class="top-badge-es">🏆 #${{o.top10_details.rank}} Top ES</span>`;
      if (isTopBR) rankBadge = `<span class="top-badge-br">🚀 #${{o.top10_details.rank}} Top BR</span>`;

      let flag = '🇧🇷';
      if (o.idioma === 'ES') flag = '🇪🇸';
      else if (o.idioma === 'FR') flag = '🇫🇷';
      else if (o.idioma === 'EN') flag = '🇺🇸';

      const bumpHtml = o.order_bump ? `
        <div class="bump-box">
          <strong>Order Bump Sugerido:</strong> ${{o.order_bump}}
        </div>
      ` : '';

      return `
        <div class="card ${{highlightClass}}">
          <div>
            <div class="card-top">
              <div class="badge-group">
                <span class="id-badge">${{o.id}}</span>
                <span class="lang-badge">${{flag}} ${{o.idioma}}</span>
                ${{rankBadge}}
              </div>
              <span class="ticket-badge">${{o.ticket}}</span>
            </div>
            <div class="card-title">${{o.nome}}</div>
            <div class="card-nicho">${{o.nicho}}</div>
            <div class="card-desc">${{o.descricao}}</div>
            ${{bumpHtml}}
          </div>
          <div class="card-actions">
            <button class="btn-copy" onclick="copyDork('${{encodeURIComponent(o.dork)}}')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
              Copiar Dork
            </button>
            <button class="btn-details" onclick="openDetails('${{o.id}}')">Ver Detalhes</button>
          </div>
        </div>
      `;
    }}).join('');
  }}

  function copyDork(encoded) {{
    const text = decodeURIComponent(encoded);
    navigator.clipboard.writeText(text).then(() => {{
      const toast = document.getElementById('toast');
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2500);
    }});
  }}

  function openDetails(id) {{
    const o = offersData.find(item => item.id === id);
    if (!o) return;

    let extraHtml = '';
    if (o.top10_details) {{
      const d = o.top10_details;
      extraHtml = `
        <div class="modal-field">
          <label>🏆 Motivo do Alto Potencial de Escala & ROI</label>
          <div class="value">${{d.motivo}}</div>
        </div>
        <div class="modal-field">
          <label>💰 Estrutura Completa de Funil (Upsells e Bumps)</label>
          <div class="value">${{d.funil}}</div>
        </div>
        <div class="modal-field">
          <label>🎣 Gancho Recomendado para VSL / Criativos</label>
          <div class="value" style="font-style: italic; color: #FBBF24;">${{d.hook}}</div>
        </div>
      `;
    }}

    const cleanDork = o.dork.replace(/`/g, '');
    const metaLibraryUrl = `https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&q=${{encodeURIComponent(cleanDork)}}&search_type=keyword_unordered`;

    document.getElementById('modalContent').innerHTML = `
      <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px;">
        <span class="id-badge">${{o.id}}</span>
        <span class="lang-badge">${{o.idioma}}</span>
        <span class="ticket-badge">${{o.ticket}}</span>
      </div>
      <h2 style="color:#FFF; font-size:1.4rem; font-weight:700; line-height:1.3; margin-bottom:6px;">${{o.nome}}</h2>
      <p style="color:var(--primary-light); font-size:0.85rem; font-weight:600; margin-bottom:16px;">${{o.nicho}}</p>
      
      <div class="modal-field">
        <label>Descrição do Produto & Ângulo</label>
        <div class="value">${{o.descricao}}</div>
      </div>

      ${{o.order_bump ? `
        <div class="modal-field">
          <label>Order Bump Sugerido</label>
          <div class="value" style="color:var(--accent-cyan);">${{o.order_bump}}</div>
        </div>
      ` : ''}}

      ${{extraHtml}}

      <div class="modal-field">
        <label>Dork de Busca no Meta Ad Library</label>
        <div class="value">
          <code>${{cleanDork}}</code>
        </div>
      </div>

      <div style="margin-top:24px; display:flex; gap:10px;">
        <button class="btn-copy" style="padding:12px;" onclick="copyDork('${{encodeURIComponent(o.dork)}}')">
          Copiar Termo de Busca
        </button>
        <a href="${{metaLibraryUrl}}" target="_blank" class="btn-details" style="padding:12px; text-decoration:none; display:inline-flex; align-items:center; justify-content:center;">
          Abrir na Ad Library ↗
        </a>
      </div>
    `;

    document.getElementById('modalOverlay').style.display = 'flex';
  }}

  function closeModal() {{
    document.getElementById('modalOverlay').style.display = 'none';
  }}

  document.addEventListener('keydown', e => {{
    if (e.key === 'Escape') closeModal();
  }});

  // Initial render
  filterOffers();
</script>

</body>
</html>
"""

with open('catalogo/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

os.makedirs('public', exist_ok=True)
with open('public/catalogo.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("catalogo/index.html e public/catalogo.html gerados com sucesso!")
