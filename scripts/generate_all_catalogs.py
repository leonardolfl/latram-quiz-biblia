# scripts/generate_all_catalogs.py
# -*- coding: utf-8 -*-
import json
import re
import os

print("--- Iniciando compilação do Catálogo Geral (400 Ofertas + Top 10 ES & PT-BR) ---")

# 1. Carregar as 200 ofertas internacionais originais
orig_path = '/Users/fernandeslf_/.gemini/antigravity/brain/05ae73e9-d3b9-4afa-b2dc-bc477a055db8/catalogo_200_ofertas_vsl_whitehat.md'
with open(orig_path, 'r', encoding='utf-8') as f:
    orig_text = f.read()

international_offers = []
lines = orig_text.splitlines()

current_lang = 'ES'
current_section = ''

for i in range(45, 326):
    line = lines[i].strip()
    if '### 🌿 A.' in line or 'Espanhol' in line:
        current_lang = 'ES'
    elif '### ✝️ A.' in line or 'Francês' in line:
        current_lang = 'FR'
    elif '### 📖 A.' in line or 'Inglês' in line:
        current_lang = 'EN'
    if line.startswith('### '):
        current_section = line.replace('### ', '').strip()

    m = re.match(r'^(\d+)\.\s+\*\*(.*?)\*\*(.*)$', line)
    if m:
        num = int(m.group(1))
        title = m.group(2).strip()
        rest = m.group(3).strip()
        
        # dork
        dork_m = re.search(r'\*Dork Meta:\*\s*(`[^`]+`|"[^"]+")', rest)
        dork = dork_m.group(1).replace('`', '').strip() if dork_m else ""
        
        # ticket
        ticket_m = re.search(r'Ticket:\s*([$€R\d\.\,]+)', rest)
        ticket = ticket_m.group(1) if ticket_m else "$9.90"
        
        desc = rest
        desc = re.sub(r'\|\s*\*Dork Meta:\*.*', '', desc).strip()
        desc = desc.lstrip('(').rstrip(')').strip()
        if not desc:
            desc = "Guia prático e visual para iniciantes com materiais complementares prontos."

        international_offers.append({
            "id": f"INT-{num:03d}",
            "num": num,
            "nome": title,
            "descricao": desc,
            "idioma": current_lang,
            "nicho": current_section,
            "dork": dork,
            "ticket": ticket,
            "tipo": "Internacional",
            "top10_es": False,
            "top10_br": False
        })

print(f"Total ofertas internacionais carregadas: {len(international_offers)}")

# 2. Definição das 200 NOVAS Ofertas Low Ticket Brasileiras (PT-BR)
# 10 nichos estruturados, 20 ofertas por nicho = 200 ofertas
br_raw = [
    # Nicho 1: Maternidade, Bebês, Sono e Rotina Infantil (20 ofertas)
    ("Desfralde Lúdico em 7 Dias Sem Traumas", "Maternidade & Infância", "R$ 27,00", "Ebook PDF + Tabela de Recompensas Imprimível", "O método de transição sem brigas que respeita o tempo da criança através de historinhas e reforço positivo.", "\"desfralde sem traumas\" \"baixe agora\"", "Checklist de Sinais de Prontidão por R$ 12,90"),
    ("Manual do Sono do Bebê: Noites Inteiras sem Deixar Chorar", "Maternidade & Infância", "R$ 29,90", "Guia em PDF + Áudios de Ruído Branco & Rotina", "Como ajustar a janela de sono e o ciclo circadiano do bebê para dormir noites completas no berço.", "\"sono do bebe\" \"rotina do sono\"", "Guia dos Saltos de Desenvolvimento por R$ 14,90"),
    ("Guia de Introdução Alimentar Participativa & BLW Seguro", "Maternidade & Infância", "R$ 24,90", "Ebook Ilustrado de Cortes Seguros + Cardápios", "Elimine o medo do engasgo com fotos reais de como cortar frutas, legumes e proteínas para o bebê.", "\"introducao alimentar\" \"cortes seguros\"", "50 Receitinhas para Bebês de 6 a 12 meses por R$ 14,90"),
    ("Desmame Gentil: Transição com Amor e Sem Crises", "Maternidade & Infância", "R$ 27,00", "Guia Prático Passo a Passo em 4 Semanas", "Como reduzir as mamadas noturnas e diurnas com diálogo, carinho e sem traumas para mãe e filho.", "\"desmame gentil\" \"passo a passo\"", "Meditações para a Mãe no Puerpério por R$ 12,90"),
    ("Rotina Encantada: Quadro de Tarefas e Hábitos Visuais", "Maternidade & Infância", "R$ 19,90", "Kit de Fichas Imprimíveis + Imãs Caseiros", "Acabe com a gritaria da manhã e da noite: crianças de 2 a 8 anos cumprem a rotina vendo os ícones coloridos.", "\"quadro de rotina infantil\" \"imprimir\"", "Rotina Noturna com História Ilustrada por R$ 9,90"),
    ("Primeiros Socorros para Mães: Guia Visual de Engasgo e Febre", "Maternidade & Infância", "R$ 27,00", "Infográficos Rápidos de Geladeira + Vídeos Demonstrativos", "A manobra de Heimlich em bebês e crianças explicada em 3 passos visuais para consultar em segundos.", "\"primeiros socorros infantil\" \"engasgo\"", "Guia de Febre e Medicamentos Básicos por R$ 14,90"),
    ("Cardápio Infantil de 30 Dias para Crianças Seletivas", "Maternidade & Infância", "R$ 22,90", "Ebook com Fotos + Lista de Compras Econômica", "Como apresentar novos alimentos e legumes disfarçados em preparações saborosas que as crianças aceitam.", "\"cardapio infantil\" \"crianca seletiva\"", "Ebook Lanchinhos Coloridos por R$ 12,90"),
    ("O Livro das Fórmulas de Calma: Birras e Crises de Ansiedade", "Maternidade & Infância", "R$ 19,90", "Guia de Bolso com Frases que Acalmam Crianças", "O que falar exatamente no momento do choro no supermercado ou em casa sem precisar gritar ou ceder.", "\"como lidar com birras\" \"criança\"", "10 Jogos de Respiração Lúdica por R$ 9,90"),
    ("Massagem Shantala para Cólicas e Gases em Recém-Nascidos", "Maternidade & Infância", "R$ 19,90", "Videoaulas Curtas + Mapa dos Toques em PDF", "Técnica milenar indiana que alivia a dor da barriguinha e fortalece o vínculo nos primeiros meses.", "\"shantala para bebes\" \"colica\"", "Guia do Banho de Balde Relaxante por R$ 9,90"),
    ("Rotina da Manhã sem Estresse para Mães que Trabalham Fora", "Maternidade & Infância", "R$ 17,90", "Checklists Matinais + Organização Prévia da Noite", "Saia de casa na hora certa com uniforme pronto, mochila arrumada e café tomado sem correria nem choro.", "\"rotina da manha\" \"organizacao infantil\"", "Planejador Semanal da Família por R$ 9,90"),
    ("Brincadeiras Sensoriais para Bebês de 6 a 18 Meses", "Maternidade & Infância", "R$ 19,90", "Guia com 60 Atividades com Materiais de Casa", "Desenvolva coordenação motora e curiosidade com gelo, água, caixas de papelão e texturas seguras.", "\"atividades sensoriais bebes\"", "Receitas de Tintas Caseiras Comestíveis por R$ 9,90"),
    ("Guia de Transição do Berço para a Cama Infantil sem Choro", "Maternidade & Infância", "R$ 22,00", "Ebook com Estratégia dos 5 Passos e Proteção", "Como fazer o pequeno dormir sozinho na caminha nova sentindo-se seguro e sem levantar a noite inteira.", "\"transicao berco para cama\"", "Historinha Personalizável da Cama Grande por R$ 9,90"),
    ("Kit de Atividades para Tirar Crianças das Telas", "Maternidade & Infância", "R$ 27,00", "Caderno de 150 Jogos e Dinâmicas Offline", "Substitua o celular e tablet por desafios criativos, caça ao tesouro no quintal e brincadeiras tradicionais.", "\"atividades sem telas\" \"criancas\"", "Kit Passatempos para Viagens de Carro por R$ 12,90"),
    ("Guia da Chupeta e Mamadeira: Como Tirar sem Trauma", "Maternidade & Infância", "R$ 19,90", "Roteiro Afetivo + Conto da Fada da Chupeta", "Método comprovado por odontopediatras para abandonar o hábito sem crises noturnas.", "\"como tirar a chupeta\" \"sem trauma\"", "Diploma de Coragem Imprimível por R$ 7,90"),
    ("Lancheiras Escolares Saudáveis & Práticas: 50 Ideias", "Maternidade & Infância", "R$ 24,90", "Cardápio Mensal com Fotos Reais e Montagem em 5 min", "Opções nutritivas que não murcham nem estragam na mochila e que a criança realmente come na escola.", "\"lancheiras escolares saudaveis\"", "Pães e Muffins Congeláveis para Lancheira por R$ 12,90"),
    ("Rotina Noturna e Relaxamento com Historinhas de Meditação", "Maternidade & Infância", "R$ 19,90", "20 Áudios com Voz Suave + Textos para Ler", "Contos calmantes com respiração guiada para desacelerar o cérebro da criança após um dia agitado.", "\"historinhas para dormir\" \"audios\"", "Trilha Sonora Relaxante de Ninar por R$ 9,90"),
    ("Estimulação da Fala em Casa: Guia Prático de 1 a 3 Anos", "Maternidade & Infância", "R$ 29,90", "Exercícios e Jogos Fonoaudiológicos Caseiros", "Técnicas de interação diária para destravar o vocabulário e a comunicação clara dos primeiros anos.", "\"estimulacao da fala\" \"em casa\"", "Flashcards de Sons e Animais por R$ 12,90"),
    ("Diário do Primeiro Ano do Bebê Imprimível", "Maternidade & Infância", "R$ 19,90", "Template para Álbum e Registro de Marcos", "Guarde memórias, peso, altura, primeiro dente e primeiras palavras em um layout delicado pronto para encadernar.", "\"livro do bebe para imprimir\"", "Cartões Mês a Mês para Fotos por R$ 9,90"),
    ("Mãe Sem Culpa: Gestão de Tempo e Autocuidado no Puerpério", "Maternidade & Infância", "R$ 27,00", "Guia de Organização Mental e Emocional da Mãe", "Como recuperar a identidade, organizar pequenos momentos de descanso e blindar o casamento com a chegada do bebê.", "\"maternidade real\" \"autocuidado\"", "Checklist de Rede de Apoio por R$ 9,90"),
    ("Guia de Adaptação Escolar Tranquila para Berçário e Creche", "Maternidade & Infância", "R$ 22,90", "Roteiro dos Primeiros 15 Dias para Pais e Filhos", "Elimine a ansiedade de separação na porta da escola e crie segurança emocional para seu filho.", "\"adaptacao escolar\" \"creche\"", "Guia de Perguntas para Fazer à Escola por R$ 9,90"),

    # Nicho 2: Educação Lúdica, Alfabetização, Autismo Leve & TDAH (20 ofertas)
    ("Caderno de Alfabetização Fônica e Lúdica (120 Páginas)", "Educação & Neurodiversidade", "R$ 27,00", "PDF de Alta Resolução Pronto para Imprimir", "Associação som-letra com ilustrações cativantes, sílabas simples e treino motor de caligrafia.", "\"caderno de alfabetizacao\" \"imprimir\"", "Jogos de Rimas e Aliterações por R$ 12,90"),
    ("Kit de Estimulação Cognitiva para Crianças com TDAH", "Educação & Neurodiversidade", "R$ 29,90", "Atividades de Foco, Flexibilidade e Controle Inibitório", "Exercícios projetados por psicopedagogos para reter a atenção e trabalhar a autorregulação infantil.", "\"atividades para tdah\" \"estimulacao\"", "Pranchas de Pausa e Respiração por R$ 12,90"),
    ("Rotinas Visuais e Pranchas de Comunicação para Autismo", "Educação & Neurodiversidade", "R$ 29,90", "Sistema PECS em PDF com mais de 200 Fichas", "Facilite a rotina, antecipe transições e reduza crises sensoriais com cartões ilustrados do dia a dia.", "\"rotina visual autismo\" \"pecs\"", "Histórias Sociais de Comportamento por R$ 14,90"),
    ("Caderno de Caligrafia Mágica e Treino Motor Divertido", "Educação & Neurodiversidade", "R$ 19,90", "Fichas de Grafomotricidade do Traço à Letra Cursiva", "Corrija a pegada no lápis e a postura ao escrever com desenhos pontilhados progressivos e dinâmicos.", "\"caligrafia para criancas\" \"treino motor\"", "Atividades de Labirintos com Dedinhos por R$ 9,90"),
    ("100 Jogos de Tabuleiro Pedagógicos para Imprimir em A4", "Educação & Neurodiversidade", "R$ 24,90", "Jogos de Matemática, Leitura e Ciências", "Transforme o estudo em brincadeira de família: imprima, pegue um dado e aprenda jogando.", "\"jogos pedagogicos para imprimir\"", "Baralho de Perguntas Rápidas por R$ 9,90"),
    ("Fichas de Leitura e Sílabas Complexas Ilustradas", "Educação & Neurodiversidade", "R$ 19,90", "Coleção com BR, CR, TR, CH, NH, LH", "Acabe com a dificuldade de leitura das sílabas difíceis com palavras contextualizadas e figuras claras.", "\"fichas de leitura silabas complexas\"", "Mini Livrinhos de Treino de Fluência por R$ 12,90"),
    ("Matemática Sem Medo: Operações Básicas com Métodos Visuais", "Educação & Neurodiversidade", "R$ 22,90", "Guia de Adição, Subtração, Multiplicação e Divisão", "Material concreto no papel (método Montessori e blocos lógicos) que faz qualquer criança entender contas.", "\"matematica ludica\" \"atividades\"", "Dominó de Tabuada Imprimível por R$ 9,90"),
    ("Cartões de Regulação Emocional: Como Nomear Sentimentos", "Educação & Neurodiversidade", "R$ 19,90", "Termômetro das Emoções + 40 Cartas Ilustradas", "Ajude a criança a identificar quando está com raiva, medo, frustração ou alegria e escolher como agir.", "\"regulacao emocional infantil\"", "Painel do Cantinho da Calma por R$ 9,90"),
    ("Atividades de Foco e Atenção Sustentada para Casa", "Educação & Neurodiversidade", "R$ 24,90", "Jogos de 7 Erros, Padrões Visuais e Códigos Secretos", "Treine o cérebro da criança para permanecer em uma tarefa escolar até o fim sem distrações constantes.", "\"atividades de atencao e concentracao\"", "Fichas de Desafio Diário de 10 minutos por R$ 9,90"),
    ("Caderno de Ditados e Raciocínio Lógico Infantil", "Educação & Neurodiversidade", "R$ 19,90", "Exercícios Progressivos com Banco de Palavras", "Fortaleça a ortografia, evite trocas de letras (P/B, F/V) e desenvolva a escrita autônoma.", "\"ditado ilustrado infantil\"", "Cruzadinhas e Caça-Palavras Educativos por R$ 9,90"),
    ("Labirintos e Desafios Motores para Treino de Atenção", "Educação & Neurodiversidade", "R$ 17,90", "80 Labirintos Temáticos com Dificuldade Gradual", "Trabalha planejamento espacial, persistência e foco de forma divertida e sem telas.", "\"labirintos para imprimir infantil\"", "Desenhos Simétricos para Completar por R$ 7,90"),
    ("Flashcards de Vocabulário e Fonemas em Letra Bastão", "Educação & Neurodiversidade", "R$ 19,90", "Mais de 180 Cartões Coloridos para Plastificar", "Excelente para enriquecimento de vocabulário, reforço escolar e crianças em fase inicial de leitura.", "\"flashcards alfabetizacao\"", "Guia de 15 Jogos com Flashcards por R$ 9,90"),
    ("Atividades com Tesoura e Colagem: Coordenação Fina", "Educação & Neurodiversidade", "R$ 19,90", "Linhas Retas, Curvas, Círculos e Bonecos de Montar", "Ensine o corte seguro e preciso com tesoura infantil, essencial para o desenvolvimento da escrita.", "\"atividades recorte e colagem\"", "Máscaras de Animais para Recortar por R$ 9,90"),
    ("Kit de Histórias Sociais para Crianças Neurodivergentes", "Educação & Neurodiversidade", "R$ 29,90", "25 Histórias Ilustradas de Situações Cotidianas", "Como agir no dentista, como dividir brinquedos, como lidar com barulhos altos e festas de aniversário.", "\"historias sociais autismo\"", "Quadro de Escolhas Visuais por R$ 12,90"),
    ("Treino de Tabuada Divertida com Desafios em Cores", "Educação & Neurodiversidade", "R$ 19,90", "Pintura Mágica por Resultados e Rodas de Multiplicação", "A tabuada do 1 ao 10 aprendida sem decoreba chata, através de conexões visuais e pintura.", "\"tabuada divertida para imprimir\"", "Jogo de Batalha Naval da Tabuada por R$ 9,90"),
    ("Caderno de Produção de Pequenos Textos e Interpretação", "Educação & Neurodiversidade", "R$ 22,90", "Fichas com Começo de Frase, Imagem e Roteiro", "Destrave a criatividade dos pequenos para escrever redações simples e coesas com introdução, meio e fim.", "\"producao de texto ensino fundamental\"", "Banco de Ideias de Redação por R$ 9,90"),
    ("Jogos de Memória e Concentração Imprimíveis", "Educação & Neurodiversidade", "R$ 17,90", "12 Jogos Temáticos (Animais, Números, Letras, Emoções)", "Ideal para jogar entre irmãos ou na sala de aula, desenvolvendo memorização de curto prazo.", "\"jogo da memoria para imprimir\"", "Fichas de Quebra-Cabeça de 4 Peças por R$ 7,90"),
    ("Atividades Pedagógicas de Educação Especial Inclusiva", "Educação & Neurodiversidade", "R$ 27,00", "Material Adaptado com Alto Contraste e Fontes Claras", "Perfeito para crianças com dificuldades de aprendizagem, baixa visão ou atraso no desenvolvimento.", "\"educacao especial atividades adaptadas\"", "Guia do Plano de Ensino Individualizado por R$ 14,90"),
    ("Quebra-Cabeças Geométricos e Tangram Pedagógico", "Educação & Neurodiversidade", "R$ 19,90", "Cartas de Desafio de Figuras em Escala Real", "Desenvolve raciocínio geométrico, noção espacial e paciência com as 7 peças milenares do Tangram.", "\"tangram atividades para imprimir\"", "Moldes de Tangram Colorido e Madeira por R$ 7,90"),
    ("Roteiro de Reforço Escolar do 1º ao 5º Ano", "Educação & Neurodiversidade", "R$ 29,90", "Cronograma de Estudos de 20 minutos por Dia", "Preencha as lacunas de aprendizado em português e matemática sem sobrecarregar a rotina da criança.", "\"reforco escolar em casa\"", "Simulados e Avaliações Diagnósticas por R$ 14,90"),

    # Nicho 3: Artesanato Criativo, Feltro, Biscuit, Saboaria & Velas (20 ofertas)
    ("Moldes Prontos de Feltro para Maternidade & Lembrancinhas", "Artesanato & Faça Você Mesmo", "R$ 27,00", "Coleção em Tamanho Real (A4) com Passo a Passo", "Safari, nuvens, ursinhos e anjinhos para produzir enfeites de porta e lembrancinhas de alta procura.", "\"moldes em feltro maternidade\"", "Guia de Ponto Caseado Perfeito por R$ 9,90"),
    ("Biscuit para Iniciantes: Guia de Modelagem sem Molde Caro", "Artesanato & Faça Você Mesmo", "R$ 24,90", "Receita da Massa Caseira + Vídeos de Modelagem", "Aprenda a fazer noivinhos, apliques de laços e chaveiros fofos apenas com as mãos e estacas simples.", "\"biscuit para iniciantes passo a passo\"", "Tabela de Cores e Misturas de Massa por R$ 9,90"),
    ("Saboaria Artesanal Fitoenergética com Base Glicerinada", "Artesanato & Faça Você Mesmo", "R$ 27,00", "Apostila com 30 Formulações de Ervas e Óleos", "Sabonetes cicatrizantes de camomila, argila e lavanda prontos para vender ou presentear com baixo investimento.", "\"sabonetes artesanais receitas\"", "Guia de Embalagens Sustentáveis por R$ 12,90"),
    ("Velas Aromáticas em Potes de Vidro: Cera de Soja e Coco", "Artesanato & Faça Você Mesmo", "R$ 29,90", "Manual Técnico de Queima Limpa e Fixação de Essências", "Aprenda o cálculo exato de essência para pavio de algodão e madeira que perfumam o ambiente de verdade.", "\"fazer velas aromaticas cera vegetal\"", "Etiquetas Prontas Editáveis no Canva por R$ 14,90"),
    ("Laços e Tiaras Infantis de Luxo para Vender em Casa", "Artesanato & Faça Você Mesmo", "R$ 24,90", "Moldes e Medidas de Fitas de Gorgurão e Veludo", "Faça laços perfeitos, boutique, amora e gravatinha que mães de meninas compram semanalmente.", "\"lacos de cabelo passo a passo\"", "Guia de Montagem de Kits de Bebê por R$ 12,90"),
    ("Encadernação Manual e Costura Copta para Cadernos", "Artesanato & Faça Você Mesmo", "R$ 22,90", "Apostila com Diagramas de Furação e Costura", "Crie sketchbooks, cadernos de receitas e planners artesanais com lombada exposta e acabamento elegante.", "\"encadernacao manual costura copta\"", "Miolo Pautado e Pontilhado em PDF por R$ 9,90"),
    ("Cartonagem Prática: Caixas Organizadoras e Maletas", "Artesanato & Faça Você Mesmo", "R$ 27,00", "Gabaritos em Papelão Horlle e Revestimento em Tecido", "Produza caixas rígidas sob medida para joias, documentos e presentes sem precisar de maquinário.", "\"cartonagem passo a passo caixas\"", "Gabarito de Cantos Perfeitos em PDF por R$ 9,90"),
    ("Pintura em Tecido para Panos de Prato com Riscos Prontos", "Artesanato & Faça Você Mesmo", "R$ 19,90", "50 Riscos em Tamanho Real com Guia de Cores", "Frutas, flores e galinhas clássicas com técnicas simples de sombra e luz para panos de prato que vendem rápido.", "\"riscos pintura em tecido panos de prato\"", "Guia de Mistura de Tintas para Tecido por R$ 9,90"),
    ("Biojóias e Acessórios em Resina com Flores Prensadas", "Artesanato & Faça Você Mesmo", "R$ 29,90", "Manual de Secagem Botânica e Aplicação de Resina Epóxi", "Crie brincos, colares e chaveiros transparentes com flores naturais secas sem formar bolhas.", "\"joias em resina flores secas\"", "Guia de Fornecedores de Moldes de Silicone por R$ 12,90"),
    ("Bonecas de Pano Fáceis: Moldes e Passo a Passo", "Artesanato & Faça Você Mesmo", "R$ 24,90", "Moldes do Corpo, Cabelos de Lã e Roupas Troca-Fácil", "Faça bonecas afetivas nostálgicas que encantam mães e crianças com costura reta básica.", "\"bonecas de pano moldes imprimir\"", "Moldes de 5 Vestidinhos Extras por R$ 9,90"),
    ("Personalizados de Luxo em Papelaria Criativa para Festas", "Artesanato & Faça Você Mesmo", "R$ 29,90", "Arquivos de Caixas Milk, Cone e Bala em Studio e PDF", "Aprenda a fazer lembrancinhas de aniversário infantis usando tesoura ou plotter de corte comum.", "\"papelaria personalizada moldes\"", "Paleta de Combinações de Papel Color Plus por R$ 9,90"),
    ("Peças Decorativas em Gesso e Cimento Branco para Casa", "Artesanato & Faça Você Mesmo", "R$ 22,90", "Bandejas, Porta-Velas e Vasinhos Marmorizados", "Mistura correta, desmoldagem rápida e impermeabilização para peças decorativas modernas estilo Pinterest.", "\"artesanato cimento e gesso decoracao\"", "Técnicas de Efeito Granilite e Marmorite por R$ 12,90"),
    ("Lembrancinhas Criativas de Batizado e Maternidade", "Artesanato & Faça Você Mesmo", "R$ 19,90", "30 Modelos Fáceis que Custam Menos de R$ 3,00 Cada", "Mini terços, difusores de vidro, sachês perfumados e caixinhas com custo baixíssimo de fabricação.", "\"lembrancinhas maternidade baratas\"", "Tags de Agradecimento Editáveis por R$ 9,90"),
    ("Aromatizadores de Varetas e Home Sprays Profissionais", "Artesanato & Faça Você Mesmo", "R$ 24,90", "Fórmulas com Álcool de Cereais e Maceração Perfeita", "Como criar fragrâncias duradouras para lojas e casas com alta fixação de aroma.", "\"fazer home spray e aromatizador\"", "Pirâmide Olfativa e Combinações de Essências por R$ 12,90"),
    ("Patchwork Embutido em Isopor para Quadros Decorativos", "Artesanato & Faça Você Mesmo", "R$ 19,90", "Riscos e Guia de Encaixe de Retalhos de Tecido", "Crie quadros de flores, animais e santos sem costurar nenhuma linha, usando apenas estilete e placa pluma.", "\"patchwork embutido riscos\"", "Moldes para Guirlandas de Páscoa e Natal por R$ 9,90"),
    ("Scrapbook de Memórias: Modelos e Layouts Prontos", "Artesanato & Faça Você Mesmo", "R$ 22,90", "Páginas Prontas com Molduras para Fotos e Anotações", "Organize viagens, casamentos e aniversários em álbuns criativos cheios de memória afetiva.", "\"scrapbook para imprimir layouts\"", "Elementos e Figurinhas Digitais para Colagem por R$ 9,90"),
    ("Decoupage em Vidro e Madeira: Técnicas Sem Rugas", "Artesanato & Faça Você Mesmo", "R$ 19,90", "Guia de Aplicação de Guardanapos e Papel de Arroz", "Transforme potes de conserva e caixas de MDF em peças vintage com acabamento envernizado vitrificado.", "\"decoupage passo a passo guardanapo\"", "Coleção de Imagens Vintage em Alta Resolução por R$ 9,90"),
    ("Guirlandas de Natal e Porta-Maternidade em Feltro", "Artesanato & Faça Você Mesmo", "R$ 27,00", "Moldes Grandes em A4 de Papai Noel, Renas e Bichinhos", "O produto sazonal mais rentável do artesanato com moldes testados e fáceis de montar.", "\"guirlanda de natal em feltro moldes\"", "Alfabeto Completo para Nomes de Bebê por R$ 9,90"),
    ("Topos de Bolo em Camadas Prontos para Cortar", "Artesanato & Faça Você Mesmo", "R$ 24,90", "Mais de 100 Arquivos em PDF e SVG em Camadas 3D", "Aniversários, mesversários e datas comemorativas prontos para cortar e colar no canudo.", "\"topo de bolo em camadas arquivos\"", "Fontes Caligráficas para Nomes por R$ 9,90"),
    ("Bijuterias em Miçangas e Macramê Boho Chic", "Artesanato & Faça Você Mesmo", "R$ 19,90", "Gargantilhas, Pulseiras Ajustáveis e Phone Straps", "Acessórios de moda rápida com custo de centavos e venda garantida para jovens e adolescentes.", "\"bijuterias de micangas passo a passo\"", "Guia de Nós de Fecho Ajustável por R$ 7,90"),

    # Nicho 4: Crochê Moderno, Tricô, Macramê & Costura Criativa (20 ofertas)
    ("150 Gráficos de Crochê Exclusivos com Tradução de Pontos", "Costura & Fios Criativos", "R$ 27,00", "Apostila Digital Ilustrada + Vídeos de Pontos Raros", "Gráficos legíveis de pontos fantasia, flores, barrados e peças completas para nunca faltar ideias.", "\"graficos de croche para imprimir\"", "Dicionário Visual de Abreviações e Pontos por R$ 9,90"),
    ("Tapetes de Crochê Ovais e Redondos que Não Embabadam", "Costura & Fios Criativos", "R$ 22,90", "Receitas em Vídeo e Diagramas de Aumentos Certos", "Descubra o segredo dos aumentos perfeitos para o tapete ficar retinho no chão sem enrugar.", "\"tapete de croche que nao embabada\"", "Receita do Tapete Russo Espiral por R$ 12,90"),
    ("Sousplat de Crochê Elegantes para Mesa Posta", "Costura & Fios Criativos", "R$ 19,90", "20 Modelos Sofisticados com Porta-Copos Combinando", "Peças rápidas de fazer (1 hora por peça) de altíssima procura para jantares e mesas decoradas.", "\"sousplat de croche receitas\"", "Guia de Como Engomar e Endurecer Peças por R$ 9,90"),
    ("Bolsas em Fio de Malha: Modelos Estruturados com Fundo", "Costura & Fios Criativos", "R$ 27,00", "Bolsa Tote, Clutch de Festa e Sacola de Praia", "Como escolher o fio certo e fazer pontos firmes para a bolsa não ficar mole nem deformar com o peso.", "\"bolsa de fio de malha passo a passo\"", "Como Colocar Zíper e Forro em Bolsa de Crochê por R$ 12,90"),
    ("Amigurumis Fáceis de Bichinhos da Fazenda", "Costura & Fios Criativos", "R$ 24,90", "Vaca, Porquinho, Galinha e Carneirinho em Português", "Receitas sem costuras complicadas, ideais para iniciantes criarem presentes ou kits de berço.", "\"amigurumi bichinhos da fazenda\"", "Olhos com Trava de Segurança e Guia de Enchimento por R$ 9,90"),
    ("Costura Criativa: 20 Bolsas e Necessaires Fáceis de Vender", "Costura & Fios Criativos", "R$ 27,00", "Moldes em Tamanho Real com Margem de Costura", "Peças utilitárias de uso diário que usam poucos retalhos de tecido e tricoline e vendem o ano todo.", "\"necessaire facil costura criativa\"", "Guia de Instalação de Cursor e Zíper sem Erro por R$ 9,90"),
    ("Conserto e Ajuste de Roupas em Casa: Bainhas e Zíperes", "Costura & Fios Criativos", "R$ 24,90", "Manual Prático para Economizar e Ganhar Dinheiro", "Como fazer barra original de calça jeans, apertar cintura, trocar zíper de jaqueta e ajustar ombros.", "\"como ajustar roupas em casa\"", "Guia de Costura Invisível à Mão por R$ 9,90"),
    ("Modelagem Plana Feminina Sob Medida: Blusas e Saias", "Costura & Fios Criativos", "R$ 29,90", "Tabela de Medidas Industriais + Molde Base A4", "Aprenda a tirar medidas do próprio corpo e criar roupas sob medida que caem com caimento perfeito.", "\"modelagem feminina do zero moldes\"", "Adaptações de Decotes e Mangas por R$ 12,90"),
    ("Macramê para Parede e Suportes de Plantas (Hangers)", "Costura & Fios Criativos", "R$ 19,90", "Guia Passo a Passo dos 4 Nós Fundamentais", "Decoração boho contemporânea feita apenas com cordão de algodão cru e galhos naturais.", "\"macrame suporte de plantas passo a passo\"", "Calculadora de Metragem de Cordas por R$ 9,90"),
    ("Tricô Manual sem Agulha: Mantas Gigantes de Sofá", "Costura & Fios Criativos", "R$ 22,90", "Vídeo de Ponto de Braço com Lã Merino e Chenille", "Faça mantas grossas e fofas em menos de 2 horas usando apenas os braços e as mãos na mesa.", "\"manta de trico com os bracos\"", "Almofadas Nó Escandinavo Passo a Passo por R$ 9,90"),
    ("Vestuário em Crochê de Verão: Tops e Saídas de Praia", "Costura & Fios Criativos", "R$ 27,00", "Receitas Graduadas do P ao GG com Fio de Algodão", "Roupas leves que secam rápido e viram sensação nos litorais e piscinas na temporada de calor.", "\"top de croche receita passo a passo\"", "Gráficos de Saídas Longas Vazadas por R$ 14,90"),
    ("Cachepôs e Cestos Organizadores de Fio de Malha", "Costura & Fios Criativos", "R$ 19,90", "Bases de Madeira e Acrílico com Subida Reta", "Organize pincéis de maquiagem, fraldas e brinquedos com cestos firmes e laváveis.", "\"cesto organizador fio de malha\"", "Alças de Couro Sintético Caseiras por R$ 7,90"),
    ("Ponto Cruz Moderno: 80 Gráficos para Toalhas de Bebê", "Costura & Fios Criativos", "R$ 19,90", "Alfabetos Delicados, Animais e Ramos Florais", "Borde toalhas de banho e paninhos de boca com motivos elegantes que fogem do infantil antiquado.", "\"graficos de ponto cruz para toalhas\"", "Guia do Avesso Perfeito no Ponto Cruz por R$ 9,90"),
    ("Guia de Precificação Justa para Artesanato e Costura", "Costura & Fios Criativos", "R$ 17,90", "Planilha Automática de Horas Trabalhadas e Materiais", "Descubra quanto cobrar por cada peça sem tomar prejuízo e sem ter vergonha de cobrar o preço certo.", "\"como precificar artesanato planilha\"", "Roteiro de Atendimento no WhatsApp por R$ 9,90"),
    ("Roupas Pet em Tecido e Crochê com Moldes do PP ao GG", "Costura & Fios Criativos", "R$ 24,90", "Capinhas de Chuva, Suéteres Quentinhos e Bandanas", "Vista o cachorro ou gato da família com roupas confortáveis que não prendem os movimentos.", "\"moldes de roupas para cachorro imprimir\"", "Vestidinho com Saia Pregueada para Pet por R$ 9,90"),
    ("Barrados de Crochê Rápidos para Panos de Prato", "Costura & Fios Criativos", "R$ 17,90", "40 Bicos de 1 e 2 Carreiras Fáceis de Fazer", "Agregue valor aos panos de prato simples em 15 minutos com bicos delicados de corações e conchas.", "\"barrados de croche faceis para iniciantes\"", "Como Fazer Caseado Reto sem Puxar Fio por R$ 7,90"),
    ("Mantas de Bebê em Crochê: Pontos Fofos e Macios", "Costura & Fios Criativos", "R$ 22,90", "Ponto Pipoca, Ponto Waffle e Chevron em Tons Pastéis", "A manta que passa de geração em geração, feita com fios macios e antialérgicos.", "\"manta de bebe em croche grafico\"", "Gorro e Sapatinho Combinando por R$ 12,90"),
    ("Costura de Pijamas Femininos e Infantis em Viscolycra", "Costura & Fios Criativos", "R$ 24,90", "Moldes de Shorts, Calças Pantacourt e Camisetes", "A roupa mais confortável e fácil de costurar, ideal para presentear ou vender para a vizinhança.", "\"molde de pijama feminino imprimir\"", "Máscara de Dormir Acolchoada por R$ 7,90"),
    ("Tapetes de Barbante Geométricos e Chevron para Sala", "Costura & Fios Criativos", "R$ 19,90", "Gráficos de Linhas Retas em Barbante Número 6 e 8", "Design moderno escandinavo que combina com qualquer apartamento contemporâneo.", "\"tapete de barbante geometrico\"", "Como Fazer Franjas Alinhadas por R$ 7,90"),
    ("Flores de Crochê Realistas para Aplicação e Buquês", "Costura & Fios Criativos", "R$ 19,90", "Rosas com Pétalas Enroladas, Girassóis e Margaridas", "Use para enfeitar chapéus, bolsas, tiaras ou montar buquês duradouros que não murcham.", "\"flores de croche passo a passo\"", "Folhas e Ramos de Apoio por R$ 7,90"),

    # Nicho 5: Confeitaria Caseira, Pães Artesanais, Marmitas & Salgados (20 ofertas)
    ("Segredos do Pão de Queijo Mineiro Tradicional & Recheado", "Culinária & Panificação", "R$ 19,90", "Receitas de Polvilho Doce e Azedo + Dicas de Forno", "A casquinha crocante por fora e o miolo macio e elástico que não murcha depois de frio.", "\"pao de queijo mineiro receita original\"", "Variações Recheadas com Goiabada e Requeijão por R$ 9,90"),
    ("Bolos Caseiros da Vovó que Não Solam e Vendem Todo Dia", "Culinária & Panificação", "R$ 24,90", "Fubá com Goiabada, Cenoura com Chocolate Vulcão", "Massas fofinhas feitas no liquidificador com caldas brilhantes que atraem clientes pelo aroma.", "\"bolos caseiros simples para vender\"", "Guia de Conservação e Embalagens de Bolo por R$ 9,90"),
    ("Marmitas Saudáveis Congeladas para a Semana em 3 Horas", "Culinária & Panificação", "R$ 27,00", "Guia de Cozimento em Lote (Meal Prep) + Cardápios", "Alimente a família a semana inteira com comida saudável sem legumes empapados nem carnes secas.", "\"marmitas congeladas para a semana\"", "Planilha de Lista de Compras de Supermercado por R$ 9,90"),
    ("Pães de Fermentação Natural Sem Segredos (Levain Fácil)", "Culinária & Panificação", "R$ 29,90", "Manual da Isca Caseira + Farinha de Mercado", "Faça pães rústicos com casca dourada e alvéolos abertos no forno do seu fogão a gás convencional.", "\"pao com levain fermentacao natural em casa\"", "Pão de Forma com Levain 100% Macio por R$ 12,90"),
    ("Salgados de Festa que Podem ser Congelados sem Rachar", "Culinária & Panificação", "R$ 27,00", "Coxinha de Frango com Catupiry, Risoles e Bolinhas", "Massa coringa cozida no caldo do frango com empanamento super crocante que não estoura na fritura.", "\"massa de salgados para congelar\"", "Guia de Cálculo de Salgados por Convidado por R$ 9,90"),
    ("Copos da Felicidade e Sobremesas Lucrativas no Pote", "Culinária & Panificação", "R$ 22,90", "Camadas de Mousses Aeradas, Geleias e Brownie", "A sobremesa mais fotografada do Instagram, com alta margem de lucro e apresentação irresistível.", "\"copo da felicidade receitas lucrativas\"", "Como Calcular o Preço no Ifood por R$ 12,90"),
    ("Brigadeiros Gourmet de Ponto Perfeito que Não Cristalizam", "Culinária & Panificação", "R$ 19,90", "Técnicas de Fogo Baixo e Ingredientes que Duram 10 Dias", "Pistache, Belga, Ninho com Nutella e Maracujá que mantêm a maciez sem virar açúcar cristalizado.", "\"brigadeiro gourmet ponto correto\"", "Guia de Boleamento Rápido em Quantidade por R$ 9,90"),
    ("Pão de Mel Recheado com Casquinha Fina e Crocante", "Culinária & Panificação", "R$ 22,90", "Massa Úmida com Especiarias e Doce de Leite Cremoso", "Técnica de banho de chocolate fracionado ou nobre temperado que não derrete nas mãos.", "\"pao de mel recheado receitas\"", "Embalagens Decoradas para Lembrancinhas por R$ 9,90"),
    ("Geladinhos Gourmet Cremosos: 40 Receitas sem Gelo", "Culinária & Panificação", "R$ 19,90", "Base Coringa Ultra Cremosa com Liga Neutra", "Sabor de sorvete de massa no saquinho que vende no verão em condomínios, escolas e praças.", "\"geladinho gourmet receitas sem gelo\"", "Tags com Sabores Prontas para Imprimir por R$ 7,90"),
    ("Cookies Americanos Autênticos com Recheio Macio", "Culinária & Panificação", "R$ 22,90", "Bordas Douradas e Centro Puxa-Puxa com Gotas", "Segredo da manteiga noisette e repouso da massa na geladeira para cookies idênticos aos de Nova York.", "\"cookies americanos receita original\"", "Cookie Red Velvet com Brigadeiro Branco por R$ 9,90"),
    ("Empadas e Empadões com Massa Podre que Derrete na Boca", "Culinária & Panificação", "R$ 24,90", "Receitas de Palmito Cremoso, Frango com Queijo e Camarão", "Massa crocante e amanteigada que não esfarela antes da mordida e desmolda perfeitamente.", "\"empada massa podre que derrete na boca\"", "Empadas Doces de Leite Condensado por R$ 9,90"),
    ("Bolos no Pote Econômicos para Renda Extra Imediata", "Culinária & Panificação", "R$ 19,90", "Massas Chiffon que Não Ficam Secas com Recheios Suaves", "O produto de entrada mais fácil da confeitaria para começar com menos de 50 reais de insumos.", "\"bolo no pote para vender facil\"", "Planilha de Custo por Potinho por R$ 9,90"),
    ("Pizzas Artesanais com Fermentação Longa em Casa", "Culinária & Panificação", "R$ 24,90", "Massa Leve de Fácil Digestão com Borda Inflada", "Técnica de frigideira + grelha do forno para reproduzir o calor de um forno a lenha profissional.", "\"pizza artesanal fermentacao lenta\"", "Molho de Tomate San Marzano Caseiro por R$ 9,90"),
    ("Doces Finos para Casamentos e Formaturas Passo a Passo", "Culinária & Panificação", "R$ 29,90", "Camafeu de Nozes, Trouxinhas de Damasco e Copinhos", "O nicho mais valorizado da confeitaria com produtos que chegam a custar R$ 5 a unidade.", "\"doces finos para casamento receitas\"", "Guia de Degustação para Noivas por R$ 14,90"),
    ("Marmitas Fit Low Carb com Cálculo de Calorias e Macros", "Culinária & Panificação", "R$ 24,90", "Cardápios Ricos em Proteína e Fibras para Emagrecimento", "Refeições saborosas que saciam sem precisar de carboidratos pesados, congeláveis por 30 dias.", "\"marmitas low carb congeladas\"", "Tabela de Calorias por Porção por R$ 9,90"),
    ("Esfihas Abertas e Fechadas com Massa Macia de Esfiharia", "Culinária & Panificação", "R$ 22,90", "Receita com Fubá para Abrir e Recheio de Carne Sequinha", "O segredo do recheio de carne árabe com limão e cebola bem drenados que não encharcam a massa.", "\"esfiha aberta massa profissional\"", "Esfiha de Queijo com Zaatar por R$ 9,90"),
    ("Brownies com Casquinha Craquelada e Centro Denso", "Culinária & Panificação", "R$ 19,90", "Receita Exata com Cacau 100% e Manteiga Pura", "Como assar no ponto fudge sem ressecar e cortar em pedaços geométricos sem esmigalhar.", "\"brownie perfeito casquinha craquelada\"", "Brownie com Caramelo Salgado e Castanhas por R$ 9,90"),
    ("Conservas Artesanais, Geleias Naturais e Chutneys", "Culinária & Panificação", "R$ 22,90", "Técnicas de Pasteurização em Banho-Maria para 6 Meses", "Pimenta biquinho, palmito, antepastos de berinjela e geleias sem conservantes químicos.", "\"conservas artesanais como pasteurizar\"", "Etiquetas Rústicas com Data de Validade por R$ 9,90"),
    ("Tortas Salgadas e Quiches Rápidas de Liquidificador", "Culinária & Panificação", "R$ 19,90", "Massa Leve com Iogurte e Recheios Cremosos", "A refeição de domingo mais prática para aproveitar ingredientes da geladeira sem sujeira.", "\"torta salgada de liquidificador fofinha\"", "Quiche Lorraine Tradicional com Queijo e Bacon por R$ 9,90"),
    ("Guia de Fichas Técnicas e Precificação de Doces", "Culinária & Panificação", "R$ 17,90", "Planilha Automática de Gramatura, Gás e Mão de Obra", "Nunca mais cobre barato em doces e bolos por esquecer de embutir os custos invisíveis de produção.", "\"ficha tecnica confeitaria planilha\"", "Contrato Simples de Encomendas por R$ 9,90"),

    # Nicho 6: Horta Urbana, Orquídeas, Suculentas & Jardinagem em Casa (20 ofertas)
    ("Guia da Horta Orgânica em Apartamento e Vasos Pequenos", "Jardinagem & Vida Verde", "R$ 22,90", "Ebook Ilustrado com Guia de Sol, Terra e Drenagem", "Colha alface, tomate cereja, manjericão e couve frescos mesmo tendo apenas uma janela iluminada.", "\"horta em apartamento pequenos espacos\"", "Guia de Calendário de Plantio por R$ 9,90"),
    ("Manual do Cultivo de Orquídeas: Floração Todo Ano", "Jardinagem & Vida Verde", "R$ 27,00", "Phalaenopsis, Dendrobium e Cattleya Sem Mistério", "Descubra como regar pelas raízes, a luz correta e o adubo caseiro que faz brotar hastes florais seguidas.", "\"como cuidar de orquideas para florir\"", "Guia de Transplante e Substrato de Casca de Pinus por R$ 12,90"),
    ("Segredos das Suculentas e Cactos: Rega e Solução de Pragas", "Jardinagem & Vida Verde", "R$ 19,90", "Como Evitar o Apodrecimento por Excesso de Água", "A fórmula do substrato aerado com areia e perlita que mantém suas gordinhas coloridas e compactas.", "\"como cuidar de suculentas sem apodrecer\"", "Guia Visual de Suculentas Raras por R$ 9,90"),
    ("Adubos Caseiros Orgânicos Sem Gastar Dinheiro", "Jardinagem & Vida Verde", "R$ 17,90", "Casca de Ovo, Borra de Café, Casca de Banana e Cinzas", "Aporte de cálcio, potássio, fósforo e nitrogênio natural para folhas verdes e frutos grandes sem químicos.", "\"adubo caseiro para plantas\"", "Chá de Casca de Cebola Contra Pragas por R$ 7,90"),
    ("Horta de Temperos e Ervas Medicinais na Janela", "Jardinagem & Vida Verde", "R$ 19,90", "Alecrim, Hortelã, Tomilho, Sálvia e Capim-Santo", "Como plantar em floreiras de peitoril e manter temperos frescos sempre prontos para o almoço.", "\"temperos em vasos pequenos\"", "Guia de Secagem e Desidratação de Ervas por R$ 9,90"),
    ("Guia Definitivo contra Pulgões, Cochonilhas e Fungos", "Jardinagem & Vida Verde", "R$ 19,90", "Receitas Naturais com Óleo de Neem, Sabão e Bicarbonato", "Elimine manchas brancas, pulgões e mosquinhas do vaso sem prejudicar abelhas nem envenenar a casa.", "\"combater cochonilha e pulgao receitas naturais\"", "Guia de Identificação de Pragas por Foto por R$ 9,90"),
    ("Jardinagem para Iniciantes: Guia Visual de Rega", "Jardinagem & Vida Verde", "R$ 22,90", "Como Saber se a Terra Precisa de Água Apenas com o Dedo", "Acabe com a frustração de plantas morrendo por excesso ou falta de água com regras simples e claras.", "\"jardinagem para iniciantes guia\"", "Manual de Podas de Limpeza e Renovação por R$ 9,90"),
    ("Minhocário e Compostagem Doméstica sem Mau Cheiro", "Jardinagem & Vida Verde", "R$ 19,90", "Monte em 3 Caixas Plásticas Empilháveis de R$ 15", "Transforme restos de cascas de cozinha em húmus escuro fértil e biofertilizante líquido líquido para o jardim.", "\"compostagem em apartamento sem cheiro\"", "O Que Pode e Não Pode Ir na Caixa de Compostagem por R$ 7,90"),
    ("Propagação de Mudas por Estacas e Folhas", "Jardinagem & Vida Verde", "R$ 19,90", "Multiplique Suas Plantas com Água e Enraizadores Naturais", "Como cortar galhos e enraizar monsteras, jiboias, ficus e suculentas para ter centenas de plantas grátis.", "\"como fazer mudas de plantas\"", "Enraizador Caseiro à Base de Lentilha por R$ 9,90"),
    ("Cultivo de Morangos e Frutas Vermelhas em Vasos", "Jardinagem & Vida Verde", "R$ 24,90", "Guia de Mudas por Estolões e Polinização Manual", "Tenha morangos doces pendurados na varanda sem contato com a terra molhada para evitar fungos.", "\"cultivo de morango em vasos\"", "Adubação Especial para Frutíferas por R$ 9,90"),
    ("Bonsai Passo a Passo: Podas, Aramação e Cuidados", "Jardinagem & Vida Verde", "R$ 27,00", "Transforme Mudas Comuns de Fícus e Jabuticaba em Miniaturas", "A arte milenar de podar raízes e modelar troncos explicada de forma ocidental simples e didática.", "\"bonsai para iniciantes passo a passo\"", "Guia de Ferramentas Alternativas Caseiras por R$ 12,90"),
    ("Paisagismo Prático para Pequenos Jardins e Varandas", "Jardinagem & Vida Verde", "R$ 24,90", "Combinações de Altura, Textura e Cores de Folhagens", "Crie um cantinho de relaxamento estilo spa em casa combinando vasos de barro, pedras e plantas tropicais.", "\"paisagismo para varanda pequena\"", "Projetos em Planta Baixa com Medidas por R$ 12,90"),
    ("Plantas Purificadoras de Ar para Ter Dentro do Quarto", "Jardinagem & Vida Verde", "R$ 17,90", "Espada de São Jorge, Lírio da Paz e Zamioculca", "Espécies resistentes a ar condicionado e pouca luz que filtram toxinas do ar enquanto você dorme.", "\"plantas que purificam o ar dentro de casa\"", "Dicas de Umidificação do Ambiente por R$ 7,90"),
    ("Guia de Rosas e Flores de Época: Podas e Adubação", "Jardinagem & Vida Verde", "R$ 22,90", "Como Fazer Roseiras Florescerem com Botões Grandes", "A poda anual no inverno e a adubação com farinha de ossos que previne ferrugem e manchas pretas.", "\"como podar roseiras e adubar\"", "Guia de Rosas do Deserto por R$ 12,90"),
    ("Vasos Autoirrigáveis Feitos com Garrafa PET", "Jardinagem & Vida Verde", "R$ 17,90", "Sistema de Pavio que Alimenta as Plantas por 15 Dias", "Viaje de férias tranquilo sem vizinho precisando regar suas plantas com vasos reciclados inteligentes.", "\"como fazer vaso autoirrigavel\"", "Gabarito de Furação de Garrafas por R$ 7,90"),
    ("Cultivo de Microverdes em Casa: Colheita em 10 Dias", "Jardinagem & Vida Verde", "R$ 22,90", "Rúcula, Beterraba, Mostarda e Rabanete Concentrados", "Cultive superalimentos cheios de vitaminas em bandejas rasas dentro da cozinha sem agrotóxicos.", "\"como cultivar microverdes em casa\"", "Guia Culinário de Uso dos Brotos por R$ 9,90"),
    ("Plantas Tóxicas para Pets: Guia Completo de Segurança", "Jardinagem & Vida Verde", "R$ 17,90", "Comigo-Ninguém-Pode, Costela de Adão, Espada e Azaleia", "Identifique quais plantas da sua casa podem intoxicar cães e gatos e conheça alternativas 100% seguras.", "\"plantas venenosas para cachorros e gatos\"", "Manual de Primeiros Socorros por Intoxicação por R$ 9,90"),
    ("Germinação de Sementes e Produção de Mudas do Zero", "Jardinagem & Vida Verde", "R$ 19,90", "Bandejas de Células, Substrato Fino e Umidade Correta", "Aprenda a germinar até as sementes mais delicadas de flores e hortaliças sem perder a sementeira.", "\"germinacao de sementes dicas\"", "Guia de Quebra de Dormência de Sementes Duras por R$ 9,90"),
    ("Terrários Fechados de Musgo e Mini Plantas: Montagem", "Jardinagem & Vida Verde", "R$ 24,90", "Ecossistema Autossustentável em Vidro Fechado", "Como equilibrar camadas de carvão ativado, pedrinhas e fitônias que vivem anos com uma única rega.", "\"como fazer terrario fechado passo a passo\"", "Guia de Seleção de Vidros e Potes por R$ 9,90"),
    ("Jardim Vertical em Palets e Grades de Parede", "Jardinagem & Vida Verde", "R$ 19,90", "Aproveite Muros e Paredes Vagas com Vasos Meia-Lua", "A melhor forma de ter mais de 30 plantas ocupando zero metros quadrados de chão na sua casa.", "\"jardim vertical com paletes simples\"", "Tratamento da Madeira Contra Umidade por R$ 9,90"),

    # Nicho 7: Espiritualidade Cristã, Devocionais da Mulher, Memorização Bíblica (20 ofertas)
    ("Devocional da Mulher Sábia: 365 Dias de Provérbios", "Espiritualidade & Fé Cristã", "R$ 27,00", "PDF Ilustrado com Espaço para Anotações Diárias", "Reflexões de 5 minutos focadas no coração feminino, gestão do lar, maternidade, casamento e oração.", "\"devocional da mulher sabia\"", "Diário das Orações Respondidas por R$ 12,90"),
    ("Leitura Bíblica em 1 Ano com Checklists Cronológicos", "Espiritualidade & Fé Cristã", "R$ 24,90", "Plano com Livros Organizados pela Ordem dos Fatos", "Entenda a história bíblica como ela aconteceu, do Éden ao Apocalipse, com mapas da época.", "\"plano de leitura biblica cronologica\"", "Linha do Tempo Ilustrada dos Reis e Profetas por R$ 12,90"),
    ("Guia de Memorização Bíblica Visual: Versículos-Chave", "Espiritualidade & Fé Cristã", "R$ 19,90", "Cards Visuais com Mnemônicos e Desenhos Temáticos", "Grave no coração mais de 100 versículos de força, proteção, fé e consolo com facilidade.", "\"memorizacao biblica para imprimir\"", "Fichas de Bolso para Bolsa e Carro por R$ 9,90"),
    ("Caderno de Oração da Esposa e Mãe Intercessora", "Espiritualidade & Fé Cristã", "R$ 22,90", "Roteiros de Clamor Diário pela Família e Filhos", "Orações embasadas nas Escrituras para proteger seu lar contra contendas, esfriamento e ataques espirituais.", "\"oracoes pela familia e filhos\"", "30 Dias de Oração pelo Marido por R$ 12,90"),
    ("Mapa das Parábolas de Jesus em Esquemas Visuais", "Espiritualidade & Fé Cristã", "R$ 24,90", "Contexto Histórico, Personagens e Aplicação Prática", "Compreenda o significado profundo do Bom Samaritano, Filho Pródigo, Semeador e Talentos.", "\"parabolas de jesus explicadas\"", "Guia de Costumes da Época de Jesus por R$ 9,90"),
    ("Livro de Orações para Superar Crises e Ansiedade", "Espiritualidade & Fé Cristã", "R$ 19,90", "Palavras de Firmeza e Salmos Comentados para Calma", "O que orar quando o peito aperta e os pensamentos não calam, encontrando a paz que excede o entendimento.", "\"oracoes contra ansiedade biblia\"", "Áudios de Salmos Sussurrados para Dormir por R$ 12,90"),
    ("Harpa Cristã e Hinos Históricos: Reflexões e Histórias", "Espiritualidade & Fé Cristã", "R$ 19,90", "As Histórias Emocionantes por Trás dos Hinos Clássicos", "Conheça quem compôs 'Foi na Cruz', 'Grandioso És Tu' e 'Sossegai' em meio a naufrágios e tragédias.", "\"historias dos hinos da harpa crista\"", "Partituras e Cifras Simplificadas por R$ 12,90"),
    ("Journaling Bíblico: Como Anotar e Ilustrar as Escrituras", "Espiritualidade & Fé Cristã", "R$ 22,90", "Código de Cores para Marca-Textos e Letras Criativas", "Aprenda a fazer anotações ricas na margem da sua Bíblia, facilitando a revisão de temas espirituais.", "\"bible journaling para iniciantes\"", "Adesivos e Carimbos Digitais para Imprimir por R$ 9,90"),
    ("O Tabernáculo e o Templo em Infográficos 3D", "Espiritualidade & Fé Cristã", "R$ 27,00", "Cortes Ilustrados da Arca, Candelabro e Altar", "Entenda toda a tipologia de Cristo oculta nos rituais, tecidos e utensílios do Antigo Testamento.", "\"o tabernaculo ilustrado estudo\"", "Significado das Roupas do Sumo Sacerdote por R$ 9,90"),
    ("Cartões de Promessas de Deus para Ter na Bolsa", "Espiritualidade & Fé Cristã", "R$ 17,90", "60 Promessas Categorizadas por Situações de Vida", "Para momentos de medo financeiro, doença, solidão e decisões difíceis, com versículos em destaque.", "\"cartoes de promessas biblicas\"", "Caixinha Montável de Papel para os Cartões por R$ 7,90"),
    ("Estudo das Epístolas Paulinas em Linhas do Tempo", "Espiritualidade & Fé Cristã", "R$ 27,00", "Mapas das Viagens Missionárias e Propósito das Cartas", "Romanos, Coríntios e Gálatas contextualizados para o cristão comum entender a teologia da graça.", "\"cartas de paulo resumo estudo\"", "Guia de Romanos Versículo por Versículo por R$ 14,90"),
    ("O Método Neemias: Princípios Bíblicos de Gestão e Fé", "Espiritualidade & Fé Cristã", "R$ 24,90", "Como Reconstruir Muros Emocionais e Financeiros", "Lições de estratégia, oração em ação e liderança tiradas da reconstrução dos muros de Jerusalém.", "\"livro de neemias licoes de lideranca\"", "Planejador de Metas à Luz da Bíblia por R$ 9,90"),
    ("Jejum Bíblico com Propósito: Guia Espiritual e Físico", "Espiritualidade & Fé Cristã", "R$ 19,90", "Jejum de Daniel, Parcial e Completo com Seguridade", "Como preparar a mente e o corpo para momentos de consagração e quebra de cadeias espirituais.", "\"jejum biblico como fazer\"", "Cardápio do Jejum de Daniel por R$ 9,90"),
    ("Manual de Aconselhamento Bíblico Familiar", "Espiritualidade & Fé Cristã", "R$ 29,90", "Princípios das Escrituras para Resolução de Conflitos", "Como lidar com desavenças de parentes, herança, mágoas antigas e restauração de laços pelo perdão.", "\"aconselhamento biblico familia\"", "Estudo dos Provérbios sobre a Língua por R$ 9,90"),
    ("As Mulheres da Bíblia e Suas Lições de Coragem e Fé", "Espiritualidade & Fé Cristã", "R$ 22,90", "Ester, Rute, Débora, Ana, Maria e Priscila", "Exemplos práticos de ousadia, fidelidade e paciência para mulheres do século XXI.", "\"mulheres da biblia estudo devocional\"", "Roteiro de Encontro de Mulheres na Igreja por R$ 12,90"),
    ("Oração dos Salmos para Dormir em Paz", "Espiritualidade & Fé Cristã", "R$ 19,90", "Comentários dos Salmos 91, 23, 121, 3 e 4 com Áudio", "Deite a cabeça no travesseiro com a certeza da proteção angelical e descanso prometido nas Escrituras.", "\"salmos para dormir em paz\"", "Devocional Noturno de 30 Dias por R$ 9,90"),
    ("Estudo do Apocalipse Sem Mistério em Diagramas", "Espiritualidade & Fé Cristã", "R$ 29,90", "As 7 Igrejas, Selos, Trombetas e a Nova Jerusalém", "Um estudo equilibrado, livre de sensacionalismo barato, focando na esperança da vitória final de Cristo.", "\"estudo de apocalipse facil de entender\"", "Quadro Comparativo das Linhas Escatológicas por R$ 14,90"),
    ("Caderno de Gratidão Diária Cristã para Renovação", "Espiritualidade & Fé Cristã", "R$ 17,90", "Espaço Diário de Louvor e Contagem de Bênçãos", "Reconfigure seu olhar para enxergar a fidelidade de Deus mesmo nos dias mais nublados e difíceis.", "\"diario de gratidao cristo\"", "Versículos de Esperança para Colar na Agenda por R$ 7,90"),
    ("Doutrinas Bíblicas Fundamentais em Esquemas Simples", "Espiritualidade & Fé Cristã", "R$ 24,90", "Trindade, Salvação, Justificação e Dons do Espírito", "O que todo crente precisa saber para não ser levado por ventos de doutrina e ensinamentos confusos.", "\"teologia basica ilustrada para leigos\"", "Resumo da História da Igreja em 10 Fases por R$ 12,90"),
    ("Atividades Bíblicas para o Culto Doméstico com Filhos", "Espiritualidade & Fé Cristã", "R$ 22,90", "Historinhas com Perguntas, Dinâmicas e Desenhos", "Conduza o culto em família aos domingos com material que prende a atenção de crianças e adolescentes.", "\"culto domestico infantil atividades\"", "Caça ao Tesouro Bíblico pela Casa por R$ 9,90"),

    # Nicho 8: Fáscia, Postura, Mobilidade 50+ & Alívio na Cadeira (20 ofertas)
    ("Liberação da Fáscia e Rigidez Matinal em 10 Minutos", "Saúde Postural & Bem-Estar", "R$ 27,00", "Alongamentos Leves para Fazer na Própria Cama", "Acorde sem sentir o corpo enferrujado: solte a fáscia dos pés, quadris e coluna antes de pisar no chão.", "\"liberacao miofascial em casa na cama\"", "Guia de Automassagem para os Pés por R$ 9,90"),
    ("Mobilidade de Joelhos e Quadris para Pessoas 50+", "Saúde Postural & Bem-Estar", "R$ 29,90", "Exercícios sem Impacto para Destravar as Juntas", "Recupere a confiança para subir escadas, sentar e levantar do sofá sem estalos dolorosos.", "\"exercicios para joelho rigido idosos\"", "Guia de Fortalecimento com Faixa Elástica por R$ 12,90"),
    ("Pilates na Cadeira para Terceira Idade e Equilíbrio", "Saúde Postural & Bem-Estar", "R$ 24,90", "Rotinas Sentadas com Segurança Total contra Quedas", "Mantenha a força nas pernas, coluna ereta e estabilidade sem precisar deitar nem rolar no chão.", "\"pilates na cadeira para idosos\"", "Série de Exercícios para os Tornozelos por R$ 9,90"),
    ("Alívio Mecânico do Nervo Ciático na Parede", "Saúde Postural & Bem-Estar", "R$ 27,00", "Descompressão Suave do Músculo Piriforme", "Posições milenares de alívio rápido para a dor que corre pela perna e queima a nádega.", "\"alivio do nervo ciatico na parede\"", "Guia Postural de Como Dirigir sem Dor por R$ 9,90"),
    ("Respiração Diafragmática e Estímulo do Nervo Vago", "Saúde Postural & Bem-Estar", "R$ 19,90", "Técnicas 4-7-8 e Respiração em Caixa para Calma", "Abaixe a frequência cardíaca e relaxe a tensão dos ombros em 3 minutos ativando o sistema parassimpático.", "\"respiracao diafragmatica nervo vago\"", "Áudios com Ritmo Sonoro de Respiração por R$ 9,90"),
    ("Postura Alinhada para Quem Trabalha no Computador", "Saúde Postural & Bem-Estar", "R$ 22,90", "Pausas de 2 Minutos para Corrigir Ombros Caídos e Pescoço", "Elimine a corcunda de tela e a dor de cabeça tensional no final do expediente de trabalho.", "\"correcao postural escritorio\"", "Checklist de Ajuste de Monitor e Cadeira por R$ 9,90"),
    ("Pés Sem Dor: Fascite Plantar e Esporão de Calcâneo", "Saúde Postural & Bem-Estar", "R$ 24,90", "Alongamentos com Garrafa D'Água Congelada e Toalha", "Elimine aquela pontada aguda na sola do pé ao dar o primeiro passo da manhã.", "\"exercicios para fascite plantar caseiro\"", "Guia de Como Escolher Tênis e Palmilhas por R$ 9,90"),
    ("Descompressão Cervical e Alívio de Ombros Tensos", "Saúde Postural & Bem-Estar", "R$ 19,90", "Movimentos Milimétricos com Toalha Enrolada no Pescoço", "Solte os nós do trapézio e alivie a sensação de peso nas costas de forma suave e sem trancos.", "\"descompressao cervical em casa\"", "Guia do Travesseiro Ideal por R$ 9,90"),
    ("Exercícios Suaves para Mãos e Dedos: Articulações", "Saúde Postural & Bem-Estar", "R$ 19,90", "Prevenção de Rigidez e Fortalecimento de Pinça", "Ideal para artesãs, costureiras e pessoas com artrite leve recuperarem a destreza manual.", "\"exercicios para maos com artrite\"", "Compressas Mornas Caseiras de Camomila por R$ 7,90"),
    ("Fortalecimento do Assoalho Pélvico para Mulheres", "Saúde Postural & Bem-Estar", "R$ 24,90", "Kegel Descomplicado sem Aparelhos Estranhos", "Controle perdas de urina ao tossir ou rir e recupere o tônus muscular íntimo com segurança.", "\"exercicios de kegel fortalecimento\"", "Diário de Micção e Hábitos por R$ 9,90"),
    ("Caminhada Suave em Casa: 2.000 Passos na Sala", "Saúde Postural & Bem-Estar", "R$ 19,90", "Vídeo de Passadas Rítmicas sem Impacto", "Queime calorias, movimente a circulação e libere endorfina mesmo em dias de chuva sem sair de casa.", "\"caminhada em casa 15 minutos\"", "Cronômetro Musical com Ritmo de Passada por R$ 9,90"),
    ("Alongamentos para a Coluna Lombar antes de Dormir", "Saúde Postural & Bem-Estar", "R$ 19,90", "A Posição da Criança e Joelhos no Peito Guiados", "Zere a tensão acumulada na lombar para dormir em linha reta sem acordar no meio da noite com dor.", "\"alongamento lombar antes de dormir\"", "Guia de Posições Corretas de Sono por R$ 9,90"),
    ("Rotina de Flexibilidade e Equilíbrio Contra Quedas", "Saúde Postural & Bem-Estar", "R$ 24,90", "Apoio Unipodal e Caminhada no Fio Imaginário", "Treine o labirinto e a musculatura estabilizadora para andar na rua e em calçadas irregulares com segurança.", "\"treino de equilibrio idosos\"", "Checklist de Segurança Doméstica por R$ 9,90"),
    ("Exercícios com Cabo de Vassoura para Abrir o Peito", "Saúde Postural & Bem-Estar", "R$ 17,90", "Alavanca Suave que Expande a Caixa Torácica", "Corrija o encurtamento do peitoral e respire com mais capacidade pulmonar usando um cabo comum.", "\"exercicios postura cabo de vassoura\"", "Série para Escápulas Aladas por R$ 7,90"),
    ("Guia de Massagem com Bolinha de Tênis", "Saúde Postural & Bem-Estar", "R$ 19,90", "Como Soltar Pontos-Gatilho na Parede Sozinho", "Substitua o massoterapeuta: use o peso do próprio corpo para desatar nós doloridos nas costas.", "\"automassagem com bolinha de tenis\"", "Mapa dos Pontos de Tensão por R$ 9,90"),
    ("Movimentos Somáticos para Fibromialgia e Fadiga", "Saúde Postural & Bem-Estar", "R$ 27,00", "Micro-movimentos Quase Parados que Calmam o Cérebro", "Ressensibilize os receptores de dor sem exigir esforço muscular pesado em dias de crise.", "\"exercicios somaticos fibromialgia\"", "Guia de Banho com Sais e Sulfato de Magnésio por R$ 9,90"),
    ("Drenagem Linfática Facial Caseira com as Mãos", "Saúde Postural & Bem-Estar", "R$ 19,90", "Massagem de 5 Minutos para Desinchar o Rosto", "Melhore o contorno do maxilar, diminua bolsas nos olhos e estimule a circulação pela manhã.", "\"drenagem linfatica facial passo a passo\"", "Guia de Óleos Vegetais para Deslize por R$ 9,90"),
    ("Exercícios para Circulação e Inchaço nas Pernas", "Saúde Postural & Bem-Estar", "R$ 22,90", "Bombeamento da Panturrilha e Elevação na Parede", "Alivie a sensação de pernas pesadas e cansaço de quem passa o dia em pé ou sentado.", "\"exercicios circulacao pernas inchadas\"", "Guia de Chás Naturais Diuréticos por R$ 9,90"),
    ("Guia de Ergonomia Doméstica: Como Arrumar a Casa sem Dor", "Saúde Postural & Bem-Estar", "R$ 17,90", "Altura da Pia, Maneira Certa de Varrer e Pegar Baldes", "Evite travar a coluna nas tarefas domésticas diárias protegendo os discos da coluna.", "\"como varrer sem dor na coluna\"", "Checklist de Cuidados com o Tanque de Lavar por R$ 7,90"),
    ("Meditação Guiada para Sono Profundo e Relaxamento", "Saúde Postural & Bem-Estar", "R$ 19,90", "Varredura Corporal (Body Scan) da Cabeça aos Pés", "Desligue as preocupações do dia guiando a atenção para soltar cada músculo até adormecer leve.", "\"meditacao body scan relaxamento sono\"", "Áudios com Som de Chuva na Mata por R$ 9,90"),

    # Nicho 9: Pets & Adestramento Positivo em Casa (20 ofertas)
    ("Xixi e Cocô no Tapete Higiênico em 7 Dias", "Pets & Cuidado Animal", "R$ 27,00", "Método do Reforço Positivo e Temporizador", "Ensine filhotes e cães adultos a fazerem as necessidades no local certo sem esfregar o focinho nem broncas.", "\"xixi e coco no lugar certo adestramento\"", "Receita de Neutralizador de Odores Caseiro por R$ 9,90"),
    ("Ansiedade de Separação Canina: Como Acabar com Uivos", "Pets & Cuidado Animal", "R$ 29,90", "Dessensibilização dos Gatilhos de Saída de Casa", "Saia para o trabalho sem que o cachorro chore, uive, lamba as patas ou destrua a porta de entrada.", "\"ansiedade de separacao caes adestramento\"", "Guia de Brinquedos Recheáveis por R$ 12,90"),
    ("Guia da Alimentação Natural Segura para Cães", "Pets & Cuidado Animal", "R$ 24,90", "Cardápios Balanceados Cozidos com Carnes e Legumes", "Melhore a pelagem, reduza fezes volumosas e aumente a longevidade do pet sem conservantes industriais.", "\"alimentacao natural para caes cardapio\"", "Tabela de Alimentos Proibidos para Cães por R$ 9,90"),
    ("Biscoitos e Petiscos Saudáveis com Forno Convencional", "Pets & Cuidado Animal", "R$ 19,90", "Fórmulas com Aveia, Fígado, Maçã e Pasta de Amendoim", "Petiscos de treinamento crocantes e baratos sem corantes nem gordura hidrogenada.", "\"receitas de biscoito caseiro para cachorro\"", "Bolo de Aniversário Pet Saudável por R$ 9,90"),
    ("Como Fazer o Cão Parar de Pular nas Visitas", "Pets & Cuidado Animal", "R$ 19,90", "Treino dos 4 Pés no Chão e Redirecionamento de Foco", "Receba amigos e familiares em casa sem o constrangimento do cachorro arranhar roupas ou pular no colo.", "\"como fazer cachorro parar de pular\"", "Comando Senta e Espera Firme por R$ 9,90"),
    ("Passeio Perfeito: Cão Andando Sem Puxar a Guia", "Pets & Cuidado Animal", "R$ 24,90", "Técnica da Árvore e Recompensa no Calcanhar", "Transforme o pesadelo do passeio com o braço esticado em uma caminhada tranquila e prazerosa ao seu lado.", "\"passeio perfeito cachorro nao puxar guia\"", "Guia de Coleiras e Peitorais Antipuxão por R$ 12,90"),
    ("Enriquecimento Ambiental Caseiro para Pets", "Pets & Cuidado Animal", "R$ 19,90", "Garrafas PET, Rolos de Papelão e Tapetes de Fuçar", "Gaste a energia mental do cachorro dentro do apartamento para evitar que ele roa móveis e sapatos.", "\"enriquecimento ambiental caes e gatos\"", "Picolés Gelados de Frango para Dias Quentes por R$ 9,90"),
    ("Socialização Correta de Filhotes: Evite Medos Futuros", "Pets & Cuidado Animal", "R$ 22,90", "Checklist dos 100 Sons, Superfícies e Pessoas", "Apresente o mundo ao filhote de 2 a 4 meses com segurança para formar um cão confiante e sem traumas.", "\"como socializar filhote de cachorro\"", "Guia de Adaptação com Barulhos de Trovão e Fogos por R$ 12,90"),
    ("Guia do Gato de Apartamento: Adaptação e Arranhadores", "Pets & Cuidado Animal", "R$ 22,90", "Gatificação Simples de Ambientes e Caixa de Areia", "Como evitar que o gato arranhe o sofá novo e crie hábitos de beber água fresca sem problemas renais.", "\"como cuidar de gato em apartamento\"", "Guia de Areias Higiênicas Caseiras e Econômicas por R$ 9,90"),
    ("Primeiros Socorros para Cães e Gatos em Emergências", "Pets & Cuidado Animal", "R$ 27,00", "Intoxicações, Picadas de Inseto, Cortes e Queimaduras", "Saiba o que fazer nos primeiros minutos antes de chegar à clínica veterinária para salvar a vida do animal.", "\"primeiros socorros animais domesticos\"", "Cartão de Geladeira com Telefones de Emergência por R$ 9,90"),
    ("Truques Divertidos e Obediência Básica em Casa", "Pets & Cuidado Animal", "R$ 19,90", "Dar a Pata, Rolar, Ficar e Buscar a Bolinha", "Fortaleça a conexão com seu amigo de quatro patas ensinando comandos que impressionam a família.", "\"truques para cachorro adestramento\"", "Guia do Clicker de Treino por R$ 7,90"),
    ("Como Cortar as Unhas e Limpar Ouvidos do Pet Sem Medo", "Pets & Cuidado Animal", "R$ 17,90", "Dessensibilização ao Toque das Patas com Petiscos", "Nunca mais pague para tosar ou cortar unhas com o cão tremendo de medo de ser machucado.", "\"como cortar unha de cachorro em casa\"", "Solução Caseira Suave para Limpeza de Ouvido por R$ 7,90"),
    ("Adaptação entre Cão e Bebê / Novo Pet na Família", "Pets & Cuidado Animal", "R$ 22,90", "Apresentação Gradual pelo Cheiro e Limites Claros", "Como preparar o cachorro para a chegada do recém-nascido ou de um novo gatinho sem ciúmes.", "\"como apresentar bebe para cachorro\"", "Regras de Convivência Harmoniosa por R$ 9,90"),
    ("Como Evitar Latidos Excessivos no Portão e Campainha", "Pets & Cuidado Animal", "R$ 24,90", "Treino de Desconexão ao Interfone e Sons da Rua", "Tenha paz no condomínio ensinando o cão a ir para a caminha ao ouvir a campainha em vez de latir descontrolado.", "\"como parar latido de cachorro\"", "Comando 'Fica na Cama' Passo a Passo por R$ 12,90"),
    ("Higiene Bucal e Prevenção de Tártaro Canino", "Pets & Cuidado Animal", "R$ 17,90", "Pastas Caseiras de Coco e Enzimas sem Flúor", "Mantenha o hálito fresco e as gengivas sadias evitando cirurgias caras de raspagem de tártaro sob anestesia.", "\"como escovar dente de cachorro\"", "Mordedores Naturais que Limpam os Dentes por R$ 9,90"),
    ("Cuidados Essenciais com o Cão Idoso: Conforto", "Pets & Cuidado Animal", "R$ 22,90", "Adaptações de Piso Antiderrapante, Rampas e Dieta", "Como dar conforto, aliviar a artrose e cuidar da visão e cognição do seu companheiro na velhice.", "\"cuidados com cachorro idoso\"", "Massagem Suave para Articulações Idosas por R$ 9,90"),
    ("Alimentação Úmida e Sachês Naturais para Gatos", "Pets & Cuidado Animal", "R$ 19,90", "Caldos de Carne sem Sódio que Previnem Doenças Renais", "Faça sachês deliciosos em potinhos de vidro gastando um terço do preço das latinhas de pet shop.", "\"sache caseiro natural para gatos\"", "Guia de Estimulação Hídrica com Fontes por R$ 9,90"),
    ("Brincadeiras de Faro e Rastreio para Cães Hiperativos", "Pets & Cuidado Animal", "R$ 19,90", "Caça ao Petisco Escondido e Caixas de Papelão", "15 minutos de farejamento canino cansam mais o cérebro do que 1 hora correndo na esteira.", "\"jogos de faro para caes\"", "Guia de Como Montar Trilhas de Cheiro por R$ 9,90"),
    ("Elimine Cheiro de Xixi de Sofás e Tapetes", "Pets & Cuidado Animal", "R$ 17,90", "Fórmula Enzimática com Vinagre Branco e Álcool", "Destrua as moléculas de ureia para que o cachorro não sinta o cheiro e volte a marcar o mesmo local.", "\"como tirar cheiro de xixi de cachorro\"", "Impermeabilização Caseira Simples por R$ 9,90"),
    ("Diário de Saúde e Vacinas do Pet Imprimível", "Pets & Cuidado Animal", "R$ 14,90", "Histórico Veterinário, Pesagem, Vermífugos e Banho", "Tenha todas as informações médicas do seu pet organizadas em um único caderno elegante.", "\"caderneta de vacinacao pet imprimir\"", "Quadro de Medicamentos e Horários por R$ 7,90"),

    # Nicho 10: Organização Doméstica, Limpeza Rápida & Finanças Pessoais (20 ofertas)
    ("Método Casa Limpa em 30 Minutos: Cronograma Diário", "Organização & Gestão do Lar", "R$ 22,90", "Tabela de Limpeza por Cômodos e Zonas da Casa", "Mantenha a casa arrumada e cheirosa todos os dias sem perder o sábado inteiro fazendo faxina pesada.", "\"metodo casa limpa em 30 minutos\"", "Checklist de Manutenção Noturna de 10 min por R$ 9,90"),
    ("Planilha Inteligente de Finanças e Gastos Invisíveis", "Organização & Gestão do Lar", "R$ 24,90", "Excel e Google Sheets com Gráficos Automáticos", "Descubra para onde vai o seu dinheiro e estanque os pequenos vazamentos de delivery, assinaturas e taxas.", "\"planilha de controle financeiro familiar\"", "Calculadora de Reserva de Emergência por R$ 9,90"),
    ("Guia da Limpeza Natural com Vinagre e Bicarbonato", "Organização & Gestão do Lar", "R$ 17,90", "100 Fórmulas Não Tóxicas que Substituem Produtos Caros", "Limpe vidros, desengordure o fogão, limpe rejuntes e lave roupas gastando uma fração do supermercado.", "\"produtos de limpeza caseiros naturais\"", "Guia de Aromatizadores Cítricos Caseiros por R$ 7,90"),
    ("Organização de Guarda-Roupas e Desapego Consciente", "Organização & Gestão do Lar", "R$ 19,90", "Método das Dobras em Arquivo e Cabides Uniformes", "Dobre camisetas e roupas íntimas de forma vertical para enxergar tudo na gaveta sem bagunçar.", "\"como organizar guarda roupa pequeno\"", "Guia do Guarda-Roupa Cápsula Funcional por R$ 9,90"),
    ("Planejamento de Refeições Semanais que Economiza", "Organização & Gestão do Lar", "R$ 22,90", "Cardápio Inteligente de Almoço e Jantar em 4 Semanas", "Vá ao supermercado com a lista exata do que vai cozinhar e zere o desperdício de comida estragando na geladeira.", "\"planejamento de refeicoes semanais\"", "Inventário da Despensa e Freezer por R$ 9,90"),
    ("Roteiro para Quitar Dívidas e Organizar o Orçamento", "Organização & Gestão do Lar", "R$ 27,00", "Método Bola de Neve para Negociação com Bancos", "Como organizar as contas em atraso, priorizar juros e negociar descontos de até 80% nos feirões limpa-nome.", "\"como sair das dividas passo a passo\"", "Modelo de Carta de Renegociação de Juros por R$ 12,90"),
    ("Desafio 52 Semanas de Poupança com Tabelas Visuais", "Organização & Gestão do Lar", "R$ 17,90", "Poupe de R$ 1 a R$ 100 por Semana e Junte R$ 6.890", "Tabelas coloridas para marcar com caneta que transformam a economia de dinheiro em um jogo viciante.", "\"desafio 52 semanas tabela imprimir\"", "Envelope Financeiro das Metas do Ano por R$ 7,90"),
    ("Como Tirar Manchas Difíceis de Roupas Brancas e Cores", "Organização & Gestão do Lar", "R$ 17,90", "Manual contra Vinho, Graxa, Molho de Tomate e Suor", "Salve suas roupas preferidas sem estragar o tecido nem usar cloro agressivo que amarela peças brancas.", "\"como tirar manchas de roupas truques\"", "Guia dos Símbolos de Lavagem na Etiqueta por R$ 7,90"),
    ("Organização da Despensa e Cozinha: Potes e Validades", "Organização & Gestão do Lar", "R$ 19,90", "Sistema Primeiro que Vence, Primeiro que Sai (PVPS)", "Armazene grãos, farinhas e temperos em potes herméticos padronizados sem carunchos nem bichinhos.", "\"como organizar despensa de alimentos\"", "Etiquetas Minimalistas Prontas para Imprimir por R$ 9,90"),
    ("Planner da Vida Adulta em PDF: Finanças e Rotinas", "Organização & Gestão do Lar", "R$ 24,90", "Visão Mensal, Semanal e Diária Permanente (A4 e A5)", "Planeje consultas médicas, manutenção do carro, aniversários e metas de vida em um layout limpo.", "\"planner permanente em pdf para imprimir\"", "Rastreador de Hábitos Saudáveis por R$ 9,90"),
    ("Manual do Consumo Consciente: Reduza a Conta de Luz", "Organização & Gestão do Lar", "R$ 17,90", "Ajustes Simples em Chuveiro, Geladeira e Stand-by", "Como baixar até 30% da conta de energia elétrica com pequenos hábitos e sem passar desconforto no calor.", "\"como economizar energia eletrica em casa\"", "Guia de Lâmpadas LED e Eficiência por R$ 7,90"),
    ("Organização de Documentos e Papéis Importantes", "Organização & Gestão do Lar", "R$ 17,90", "Sistema de Pastas por Cores: O Que Guardar e Descartar", "Saiba exatamente por quantos anos guardar comprovantes de água, luz, cartões e imposto de renda.", "\"como organizar documentos pessoais em pastas\"", "Fichário Médico e Escolar por R$ 7,90"),
    ("Roteiro de Faxina Pesada em 4 Etapas Sem Cansaço", "Organização & Gestão do Lar", "R$ 19,90", "Como Limpar Janelas, Azulejos e Forno Sem Ficar Moída", "A ordem correta de limpeza de cima para baixo e do fundo para a porta que poupa esforço físico desnecessário.", "\"faxina pesada sem cansaco roteiro\"", "Playlist de Faxina Animada por R$ 7,90"),
    ("Checklist de Mudança de Casa Sem Estresse", "Organização & Gestão do Lar", "R$ 19,90", "Cronograma de 30 Dias Anteriores com Caixas Numeradas", "Embale louças, identifique caixas por cômodos e faça a transição para a casa nova sem nada quebrado.", "\"checklist de mudanca de casa\"", "Etiquetas Coloridas por Cômodo para Caixas por R$ 9,90"),
    ("Guia de Manutenção Preventiva do Lar contra Mofo", "Organização & Gestão do Lar", "R$ 22,90", "Soluções contra Umidade de Parede e Condensação", "Receitas com giz, cloreto de cálcio e ventilação cruzada para eliminar o cheiro de mofo dos armários.", "\"como acabar com mofo nas paredes\"", "Guia de Pequenos Reparos Hidráulicos por R$ 9,90"),
    ("Controle de Cartão de Crédito e Parcelamentos Futuros", "Organização & Gestão do Lar", "R$ 19,90", "Planilha de Impacto das Faturas nos Próximos 6 Meses", "Nunca mais seja pega de surpresa com a fatura do cartão estourada por causa de pequenas compras parceladas.", "\"controle de compras parceladas cartao\"", "Roteiro de Limite Seguro por Salário por R$ 9,90"),
    ("Método Malas Inteligentes para Viagem de 7 Dias", "Organização & Gestão do Lar", "R$ 19,90", "Leve Apenas Mala de Bordo com Roupas que Combinam", "Evite pagar despacho de bagagem com a seleção de 10 peças curingas que rendem mais de 20 looks diferentes.", "\"como arrumar mala de viagem de mao\"", "Necessaire de Líquidos para Avião (100ml) por R$ 7,90"),
    ("Gestão Financeira para Autônomos e MEI em Planilha", "Organização & Gestão do Lar", "R$ 27,00", "Separação de Conta Física e Jurídica + Lucro Real", "Descubra quanto você realmente ganha após pagar os boletos do DAS e os custos dos seus serviços.", "\"planilha financeira simples para mei\"", "Modelo de Orçamento e Recibo para Clientes por R$ 12,90"),
    ("Manual da Lavanderia Perfeita: Sabão Caseiro e Secagem", "Organização & Gestão do Lar", "R$ 17,90", "Receita de Sabão Líquido Rendado de 20 Litros por R$ 15", "Roupas limpas, macias e perfumadas gastando quase nada, com dicas de como secar rápido em dias frios.", "\"sabao liquido caseiro rende muito\"", "Guia do Vinagre como Amaciante Natural por R$ 7,90"),
    ("Calendário Doméstico Perpétuo para Geladeira", "Organização & Gestão do Lar", "R$ 14,90", "Tabela Plastificável para Anotar Recados com Caneta", "O centro de comando da família: cardápio do dia, consultas, provas dos filhos e avisos importantes à vista.", "\"calendario semanal para geladeira imprimir\"", "Conjunto de Ícones Magnéticos para Crianças por R$ 7,90")
]

br_offers = []
for idx, item in enumerate(br_raw, start=1):
    nome, nicho, ticket, formato, gancho, dork, bump = item
    br_offers.append({
        "id": f"BR-{idx:03d}",
        "num": idx,
        "nome": nome,
        "nicho": nicho,
        "ticket": ticket,
        "formato": formato,
        "descricao": gancho,
        "dork": dork,
        "order_bump": bump,
        "idioma": "PT-BR",
        "tipo": "Nova Oferta Brasil",
        "top10_es": False,
        "top10_br": False
    })

print(f"Total novas ofertas BR geradas: {len(br_offers)}")

# 3. Definição minuciosa dos Top 10 com dados de validação e escala
# Top 10 Espanhol (ES) selecionadas do catálogo internacional
top10_es_ids = [1, 2, 4, 16, 31, 41, 51, 62, 17, 43]
top10_es_details = {
    1: {
        "rank": 1,
        "motivo": "Nicho místico oracular com demanda reprimida massiva no México, Espanha, Argentina e Colômbia. CPMs na América Latina variam entre $1.50 e $3.00, permitindo CPA de aquisição na faixa de $2.00 a $4.00 com ticket de $9.90. Taxa de reembolso inferior a 1%.",
        "funil": "Front-end: $9.90 (Mapas das 36 Cartas) | Order Bump: $4.90 (Modelos de Tiradas) | Upsell 1: $19.90 (Curso Completo em Áudio e Vídeo das Combinações) | Downsell: $9.90 (Guia de Perguntas Poderosas)",
        "hook": "«¿Estudias la baraja gitana pero te cuesta memorizar las combinaciones en una tirada real? Descubre el método visual en mapas mentales que se graba para siempre en tu mente desde el primer día.»"
    },
    2: {
        "rank": 2,
        "motivo": "O público cristão na América Latina é um dos maiores do mundo. Produto 100% visual de Gênesis a Apocalipse não gera atritos de denominação (aceito por católicos e evangélicos). Conversão acima de 4% em tráfego frio.",
        "funil": "Front-end: $14.90 (Bíblia Visual em Mapas) | Order Bump: $7.90 (Linha do Tempo dos Reis e Profetas) | Upsell: $24.90 (Guia Ilustrado das Parábolas de Jesus)",
        "hook": "«La Biblia completa explicada libro por libro en diagramas y esquemas visuales. Comprende la historia sagrada de Génesis a Apocalipsis sin perderte en lecturas confusas.»"
    },
    4: {
        "rank": 3,
        "motivo": "Salmos de proteção e alívio do sofrimento emocional tocam na maior dor humana (ansiedade e medo do futuro). Audioguia de salmos narrados com música suave gera valor imediato.",
        "funil": "Front-end: $9.90 (Salmos Comentados + Áudios) | Order Bump: $5.90 (30 Dias de Oraciones Matutinas) | Upsell: $17.00 (El Libro de las Promesas de Dios para Tiempos Difíciles)",
        "hook": "«Cuando la mente se llena de preocupaciones, el Salmo 91 y el Salmo 23 no solo se leen: se sienten. Escucha y medita estas oraciones que devuelven la paz a tu hogar esta misma noche.»"
    },
    16: {
        "rank": 4,
        "motivo": "Artesanato terapêutico com forte apelo de renda extra ou passatempo antiestresse para mulheres 35-65 anos. Padrões imprimíveis têm custo zero de entrega e valor percebido altíssimo.",
        "funil": "Front-end: $9.90 (100 Patrones Amigurumi) | Order Bump: $4.90 (Guía de Puntos Raros y Acabados) | Upsell: $19.90 (Colección Personajes Navideños y Sagrada Familia)",
        "hook": "«Crea muñecos de amigurumi que encantan a todos, incluso si nunca has sostenido una aguja de crochet. 100 patrones en español paso a paso listos para imprimir.»"
    },
    31: {
        "rank": 5,
        "motivo": "Mães hispanas procuram desesperadamente alternativas lúdicas para desmame de telas de crianças de 2 a 5 anos. Produto rápido de baixar, imprimir e colocar na mesa.",
        "funil": "Front-end: $12.00 (Cuaderno Montessori 150 Páginas) | Order Bump: $6.00 (Tarjetas de Estimulación del Lenguaje) | Upsell: $19.90 (Kit Completo de Juegos Sensoriales para Imprimir)",
        "hook": "«Dile adiós a las rabietas por el celular. Más de 120 actividades prácticas que desarrollan la concentración, motricidad y paciencia de tu hijo mientras juega en casa.»"
    },
    41: {
        "rank": 6,
        "motivo": "Dor física mecânica (costas travadas e ciático). Sem remédios ou promessas ilegais: apenas biomecânica suave para fazer deitado na cama por 10 minutos. Aprovação instantânea no Facebook Ads.",
        "funil": "Front-end: $14.90 (Protocolo Espalda Sin Dolor) | Order Bump: $7.90 (Descompresión de Cuello y Hombros) | Upsell: $27.00 (Rutina de Movilidad y Alivio Articular para 50+)",
        "hook": "«10 minutos por la mañana en tu propia cama antes de poner un pie en el suelo para liberar la tensión acumulada de las vértebras lumbares sin ejercicios pesados.»"
    },
    51: {
        "rank": 7,
        "motivo": "Pães de fermentação natural viraram paixão na Espanha, Chile, México e Colômbia. O público gourmet gasta com prazer em guias didáticos que evitam pães duros e azedos.",
        "funil": "Front-end: $12.90 (Guía Pan de Masa Madre Fácil) | Order Bump: $6.90 (Recetario de Pizzas y Focaccias) | Upsell: $24.90 (Secretos de la Repostería Artesanal con Fermentos)",
        "hook": "«El pan de masa madre no tiene por qué ser complicado ni requerir harinas carísimas. Aprende la técnica exacta para lograr una corteza crujiente y miga aireada en tu horno de casa.»"
    },
    62: {
        "rank": 8,
        "motivo": "A humanização de cães e gatos no mundo hispânico cresce a taxas recordes. Mães de pets querem cozinhar petiscos saudáveis e biscoitos sem aditivos químicos para comemorar aniversários.",
        "funil": "Front-end: $9.90 (Repostería Canina y Snacks) | Order Bump: $5.90 (Guía de Alimentos Peligrosos para Mascotas) | Upsell: $17.00 (Alimentación Natural Cocida para Perros)",
        "hook": "«Prepara premios deliciosos, galletas crujientes y pasteles de cumpleaños que a tu perro le fascinarán, hechos con ingredientes naturales que ya tienes en tu cocina.»"
    },
    17: {
        "rank": 9,
        "motivo": "Costura prática de consertos e moldes prontos para imprimir em folha A4. Nicho tradicional que nunca morre, excelente para mulheres que querem economizar ajustando roupas em casa.",
        "funil": "Front-end: $12.00 (Moldes de Costura Fáciles en A4) | Order Bump: $5.90 (Guía de Arreglo de Cremalleras y Dobladillos) | Upsell: $19.90 (Patrones de Ropa Infantil y Pijamas)",
        "hook": "«Imprime los moldes en tu impresora común, une las hojas y corta tu propia ropa con medidas exactas y costura fácil, sin necesidad de cursos caros ni máquinas industriales.»"
    },
    43: {
        "rank": 10,
        "motivo": "Pilates na parede é a tendência número 1 no tráfego pago feminino de bem-estar. Criativos em vídeo de demonstração têm altíssima retenção e cliques baratíssimos.",
        "funil": "Front-end: $14.90 (Guía Pilates en la Pared para Mujeres) | Order Bump: $7.90 (Postura Aliniada y Abdomen Firme) | Upsell: $27.00 (Programa de Movilidad y Tonificación de 28 Días)",
        "hook": "«Solo necesitas una pared limpia y 15 minutos al día. El método suave que descomprime caderas, alivia la espalda y tonifica el cuerpo sin impacto en las articulaciones.»"
    }
}

# Top 10 Brasil (PT-BR) selecionadas das 200 novas ofertas BR
top10_br_ids = [1, 2, 21, 22, 61, 81, 141, 142, 161, 181]
top10_br_details = {
    1: {
        "rank": 1,
        "motivo": "Maternidade / Desfralde sem Traumas é uma das maiores dores das mães no Brasil. Nenhuma mãe quer brigar com a criança ou limpar sofá sujo todo dia. Ticket de R$ 27,00 tem conversão instantânea no Pix acima de 6% em tráfego Meta Ads.",
        "funil": "Front-end: R$ 27,00 (Método Desfralde em 7 Dias) | Order Bump 1: R$ 12,90 (Tabelas de Recompensas e Historinhas) | Order Bump 2: R$ 9,90 (Guia do Desfralde Noturno) | Upsell: R$ 37,00 (Manual Completo de Rotinas Infantis)",
        "hook": "«Cansada de brigar com seu filho pelo penico ou gastar fortunas em fraldas? Conheça o método lúdico em 7 dias que faz a criança pedir para ir ao banheiro por vontade própria.»"
    },
    2: {
        "rank": 2,
        "motivo": "Mães desesperadas por noites de sono contínuas. O sono do bebê é um nicho perene com baixo reembolso e alta recomendação em grupos de mães e WhatsApp.",
        "funil": "Front-end: R$ 29,90 (Manual do Sono sem Choro) | Order Bump: R$ 14,90 (Guia dos Saltos de Desenvolvimento) | Upsell: R$ 37,00 (Coleção de Áudios Relaxantes de Ruído Branco e Ninar)",
        "hook": "«Ajuste a janela de sono do seu bebê sem deixar ele chorando sozinho no berço. Noites inteiras de sono restaurador para você e seu pequeno acordarem dispostos.»"
    },
    21: {
        "rank": 3,
        "motivo": "Mães e professoras brasileiras compram cadernos de alfabetização por impulso no Pix. Material pronto para imprimir em folha A4 com 120 páginas de atividades coloridas.",
        "funil": "Front-end: R$ 27,00 (Caderno de Alfabetização Fônica) | Order Bump: R$ 12,90 (Jogos de Rimas e Consciência Fonológica) | Upsell: R$ 37,00 (Mega Pacote de 300 Atividades Pedagógicas)",
        "hook": "«Seu filho está com dificuldade de juntar as sílabas na escola? O método visual fônico que transforma a leitura em brincadeira e acelera o aprendizado em poucas semanas.»"
    },
    22: {
        "rank": 4,
        "motivo": "Aumento exponencial de diagnósticos de TDAH e queixas de falta de concentração por excesso de telas. Pais compram imediatamente para ver o filho calmo e focado nas tarefas.",
        "funil": "Front-end: R$ 29,90 (Kit Estimulação Cognitiva TDAH) | Order Bump: R$ 12,90 (Pranchas de Pausa e Autorregulação) | Upsell: R$ 37,00 (Rotina Visual e Fichas de Tarefas Descomplicadas)",
        "hook": "«Atividades práticas desenvolvidas para prender a atenção de crianças com mente acelerada e TDAH. Menos tempo no celular e mais foco, concentração e notas melhores.»"
    },
    61: {
        "rank": 5,
        "motivo": "O nicho de crochê no Brasil é uma potência no Facebook. Mulheres de 40 a 65 anos compram coleções de gráficos e receitas prontas diariamente via Pix.",
        "funil": "Front-end: R$ 27,00 (150 Gráficos de Crochê com Tradução) | Order Bump: R$ 9,90 (Dicionário de Abreviações e Pontos) | Upsell: R$ 37,00 (Coleção Tapetes Ovais e Sousplats que Não Embabadam)",
        "hook": "«150 gráficos de crochê detalhados e fáceis de ler, sem pontos misteriosos. Descubra como criar peças perfeitas para sua casa ou para vender com lucro alto na vizinhança.»"
    },
    81: {
        "rank": 6,
        "motivo": "Pão de queijo mineiro é paixão nacional. Apelo duplo: fazer para a família no lanche da tarde ou vender congelado como renda extra rápida em condomínios e escolas.",
        "funil": "Front-end: R$ 19,90 (Segredos do Pão de Queijo Mineiro) | Order Bump: R$ 9,90 (Receitas Recheadas Doces e Salgadas) | Upsell: R$ 29,90 (Manual das Massas Congeladas para Renda Extra)",
        "hook": "«A receita tradicional mineira que fica com a casquinha crocante por fora e o queijo puxando por dentro, sem murchar depois de frio. Perfeito para lanches e congelamento.»"
    },
    141: {
        "rank": 7,
        "motivo": "Mulheres 45+ sofrem com rigidez articular ao acordar. O alongamento leve de fáscia na cama sem precisar ir para academia resolve a dor sem risco de lesão.",
        "funil": "Front-end: R$ 27,00 (Liberação da Fáscia em 10 Minutos) | Order Bump: R$ 9,90 (Guia de Automassagem para Pés e Pernas) | Upsell: R$ 37,00 (Mobilidade de Joelhos e Coluna 50+)",
        "hook": "«Acorda com o corpo pesado e as juntas travadas? Conheça os 5 movimentos suaves para fazer na cama antes de levantar e comece o dia leve e sem dores musculares.»"
    },
    142: {
        "rank": 8,
        "motivo": "Dor nos joelhos e desgaste de cartilagem atingem mais de 30 milhões de brasileiros. Exercícios mecânicos sem impacto são a solução mais segura e de maior aceitação médica.",
        "funil": "Front-end: R$ 29,90 (Mobilidade de Joelhos e Quadris 50+) | Order Bump: R$ 12,90 (Fortalecimento com Faixa Elástica) | Upsell: R$ 37,00 (Pilates na Cadeira para Equilíbrio)",
        "hook": "«Subir escadas ou agachar não precisa ser um martírio. Exercícios sentados sem impacto que lubrificam as articulações e fortalecem os ligamentos com segurança.»"
    },
    161: {
        "rank": 9,
        "motivo": "Cães fazendo xixi no tapete da sala ou no sofá tiram qualquer dono do sério. Promessa clara de 7 dias com adestramento positivo vende em volume violento no Meta Ads.",
        "funil": "Front-end: R$ 27,00 (Xixi e Cocô no Lugar Certo em 7 Dias) | Order Bump: R$ 9,90 (Receita de Neutralizador de Odores) | Upsell: R$ 37,00 (Manual do Cão Educado: Passeio sem Puxar e Latidos)",
        "hook": "«Chega de limpar poças de xixi e estragar tapetes caros. Ensine seu cão a usar o tapete higiênico em apenas uma semana com técnicas simples de reforço positivo.»"
    },
    181: {
        "rank": 10,
        "motivo": "Mulheres que trabalham fora e cuidam da casa não aguentam passar o fim de semana esfregando chão. O método de 30 minutos por dia organiza a casa em etapas simples.",
        "funil": "Front-end: R$ 22,90 (Método Casa Limpa em 30 Minutos) | Order Bump: R$ 9,90 (Checklist de Limpeza Noturna de 10 min) | Upsell: R$ 27,00 (Guia da Limpeza Natural com Vinagre e Bicarbonato)",
        "hook": "«Sua casa limpa, perfumada e organizada todos os dias gastando apenas 30 minutos diários. Liberte seus sábados e domingos para descansar e curtir sua família.»"
    }
}

# Marcar flags nos arrays
for off in international_offers:
    if off["num"] in top10_es_ids:
        off["top10_es"] = True
        off["top10_details"] = top10_es_details[off["num"]]

for off in br_offers:
    if off["num"] in top10_br_ids:
        off["top10_br"] = True
        off["top10_details"] = top10_br_details[off["num"]]

print("Top 10 vinculados com sucesso!")

# 4. Salvar base de dados JSON unificada
all_offers = international_offers + br_offers
catalog_json_path = 'catalogo/ofertas.json'
os.makedirs('catalogo', exist_ok=True)
with open(catalog_json_path, 'w', encoding='utf-8') as f:
    json.dump({
        "total": len(all_offers),
        "total_internacionais": len(international_offers),
        "total_br": len(br_offers),
        "top10_es": [top10_es_details[x] for x in top10_es_ids],
        "top10_br": [top10_br_details[x] for x in top10_br_ids],
        "ofertas": all_offers
    }, f, ensure_ascii=False, indent=2)

print(f"Base de dados salva em {catalog_json_path} com {len(all_offers)} ofertas no total.")
