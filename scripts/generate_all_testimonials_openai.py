import os
import json
import base64
import urllib.request
import ssl
import time
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_api_key():
    with open('.env') as f:
        for line in f:
            if line.startswith('OPENAI_API_KEY='):
                return line.strip().split('=', 1)[1].strip('\"\'')
    return os.environ.get('OPENAI_API_KEY')

API_KEY = get_api_key()

TESTIMONIALS = [
    {
        "id": 1,
        "input_path": "ciganavisual/assets/images_backup_pt/depoimento-1.webp",
        "output_path": "ciganavisual/assets/images/depoimento-1.webp",
        "prompt": (
            "Translate all Portuguese text in this WhatsApp chat screenshot into natural Spanish: "
            "Chat messages: 'Recebi o material 36 Cartas do Baralho Cigano em Mapas Mentais e é simplesmente incrível!' -> '¡Recibí el material 36 Cartas de la Baraja Gitana en Mapas Mentales y es simplemente increíble!', "
            "'Muito lindo, prático e super claro.' -> 'Muy lindo, práctico y súper claro.', "
            "'Está me ajudando demais a interpretar as cartas com confiança!' -> '¡Me está ayudando muchísimo a interpretar las cartas con total seguridad!', "
            "'Que coisa linda! Fico muito feliz que está gostando e que está fazendo sentido pra você!' -> '¡Qué alegría tan linda! Me alegra muchísimo que te esté gustando y sirviendo tanto!'. "
            "Header status: 'online' -> 'en línea'. Bottom placeholder: 'Mensagem' -> 'Mensaje'. "
            "Also inside the printed book photo on the desk: translate 'O CAVALEIRO' to 'EL JINETE', 'MOVIMENTO' to 'MOVIMIENTO', 'PALAVRAS-CHAVE' to 'PALABRAS CLAVE', 'POTENCIAL POSITIVO' to 'POTENCIAL POSITIVO', 'SIGNIFICADO GERAL' to 'SIGNIFICADO GENERAL'. "
            "Keep the customer profile photo, the photo of the book on the wooden desk, WhatsApp bubbles, colors, timestamps, checkmarks and layout completely identical."
        )
    },
    {
        "id": 2,
        "input_path": "ciganavisual/assets/images_backup_pt/depoimento-2.webp",
        "output_path": "ciganavisual/assets/images/depoimento-2.webp",
        "prompt": (
            "Translate all Portuguese text in this dark mode WhatsApp chat screenshot into natural Spanish: "
            "Messages: 'Recebi meu material!' -> '¡Recibí mi material!', "
            "'As 36 Cartas do Baralho Cigano em Mapas Mentais é completo e muito bem feito.' -> '36 Cartas de la Baraja Gitana en Mapas Mentales es completo y muy bien hecho.', "
            "'As combinações de amor e vínculos finalmente fizeram sentido pra mim.' -> 'Las combinaciones de amor y vínculos finalmente tuvieron sentido para mí.', "
            "'Já estou usando e me ajudou muito nas leituras!' -> '¡Ya lo estoy usando y me ayudó mucho en las lecturas!'. "
            "Inside the photo of the printed book page: 'COMBINAÇÕES — AMOR & VÍNCULOS' -> 'COMBINACIONES — AMOR & VÍNCULOS', 'AFETO + COMPROMISSO' -> 'AFECTO + COMPROMISO', 'AFETO + CLAREZA' -> 'AFECTO + CLARIDAD', 'AFETO + INCERTEZA' -> 'AFECTO + INCERTIDUMBRE'. "
            "Reply message: 'Que bom saber! Fico feliz em fazer parte da sua jornada!' -> '¡Qué bueno saberlo! ¡Me alegra ser parte de tu camino!'. "
            "Header: 'online' -> 'en línea'. Bottom: 'Mensagem' -> 'Mensaje'. "
            "Keep dark mode background, user photo, desk photo, timestamps, double blue checkmarks and layout exactly identical."
        )
    },
    {
        "id": 3,
        "input_path": "ciganavisual/assets/images_backup_pt/depoimento-3.webp",
        "output_path": "ciganavisual/assets/images/depoimento-3.webp",
        "prompt": (
            "Translate all Portuguese text in this WhatsApp chat screenshot into natural Spanish: "
            "Messages: 'Recebi meu material e já estou encantada! ✨' -> '¡Recibí mi material y ya estoy encantada! ✨', "
            "'Muito organizado e prático, as explicações em mapas mentais fazem toda a diferença.' -> 'Muy organizado y práctico, las explicaciones en mapas mentales hacen toda la diferencia.', "
            "'As combinações ficaram muito mais fáceis de entender agora!' -> '¡Las combinaciones quedaron mucho más fáciles de entender ahora!'. "
            "Inside the photo of the open spiral book: 'COMBINAÇÕES — AMOR & VÍNCULOS' -> 'COMBINACIONES — AMOR & VÍNCULOS'. "
            "Reply: 'Que alegria saber disso! ✨ O objetivo é exatamente facilitar sua jornada com clareza e prática. Conte comigo! 🌹' -> '¡Qué alegría saberlo! ✨ El objetivo es exactamente facilitar tu camino con claridad y práctica. ¡Cuenta conmigo! 🌹'. "
            "Header: 'online' -> 'en línea'. Bottom: 'Mensagem' -> 'Mensaje'. "
            "Keep the photo of the customer, the photo of the book on table, WhatsApp bubbles, timestamps and checkmarks identical."
        )
    },
    {
        "id": 4,
        "input_path": "ciganavisual/assets/images_backup_pt/depoimento-4.webp",
        "output_path": "ciganavisual/assets/images/depoimento-4.webp",
        "prompt": (
            "Translate all Portuguese text in this dark mode WhatsApp chat screenshot into natural Spanish: "
            "Header name: 'Juliana Cliente' -> 'Juliana', 'online' -> 'en línea'. "
            "Messages: 'Gente, que página linda da A Raposa! 🦊 As explicações estão super claras!' -> '¡Chicas, qué hermosa la página de La Raposa! 🦊 ¡Las explicaciones están súper claras!', "
            "'O design está maravilhoso, ficou muito a cara do baralho.' -> 'El diseño está maravilloso, quedó perfecto para estudiar.', "
            "'Li as cartas hoje e entendi muito mais fácil. Parabéns pelo trabalho!' -> 'Leí las cartas hoy y entendí todo mucho más fácil. ¡Felicitaciones por el trabalho!'. "
            "Inside the printed book photo on the desk: 'A RAPOSA' -> 'LA RAPOSA', 'ESTRATÉGIA' -> 'ESTRATEGIA', 'PALAVRAS-CHAVE' -> 'PALABRAS CLAVE', 'SIGNIFICADO GERAL' -> 'SIGNIFICADO GENERAL'. "
            "Reply: 'Fico feliz demais em saber! Obrigado pelo carinho e confiança! 🦊✨' -> '¡Me alegra muchísimo saberlo! ¡Muchas gracias por el cariño y la confianza! 🦊✨'. "
            "Keep dark mode WhatsApp, customer photo, photo of book on table, timestamps and layout identical."
        )
    },
    {
        "id": 5,
        "input_path": "ciganavisual/assets/images_backup_pt/depoimento-5.webp",
        "output_path": "ciganavisual/assets/images/depoimento-5.webp",
        "prompt": (
            "Translate all Portuguese text in this WhatsApp chat screenshot into natural Spanish: "
            "Header: 'online' -> 'en línea'. "
            "Messages: 'As explicações são diretas e objetivas 👏' -> 'Las explicaciones son directas y objetivas 👏', "
            "'O material deixou meus estudos mais leves e organizados ✨' -> 'El material hizo mis estudios más livianos y organizados ✨', "
            "'Amei a didática e os significados claros das cartas!' -> '¡Amé la didáctica y los significados claros de las cartas!'. "
            "Inside the iPad photo on table: 'A LUA' -> 'LA LUNA', 'INTUIÇÃO' -> 'INTUICIÓN', 'PALAVRAS-CHAVE' -> 'PALABRAS CLAVE'. "
            "Reply: 'Que ótimo saber! Fico muito feliz que tenha ajudado nos seus estudos! ✨' -> '¡Qué genial saberlo! ¡Me alegra mucho que te haya ayudado en tus estudios! ✨'. "
            "Keep customer photo, iPad photo, WhatsApp bubbles, timestamps and layout identical."
        )
    },
    {
        "id": 6,
        "input_path": "ciganavisual/assets/images_backup_pt/depoimento-6.webp",
        "output_path": "ciganavisual/assets/images/depoimento-6.webp",
        "prompt": (
            "Translate all Portuguese text in this dark mode WhatsApp chat screenshot into natural Spanish: "
            "Header: 'Juliana Cliente' -> 'Juliana', 'online' -> 'en línea'. "
            "Messages: 'Já usei o modelo Tiragem de 3 Cartas numa consulta hoje 💖' -> 'Ya usé el modelo Tirada de 3 Cartas en una consulta hoy 💖', "
            "'Achei super prático' -> 'Me pareció súper práctico', "
            "'Deu clareza pra cliente entender passado, presente e futuro' -> 'Le dio total claridad a la consultante para entender pasado, presente y futuro', "
            "'Material muito profissional!' -> '¡Material muy profesional!'. "
            "Inside the MacBook screen photo: 'TIRAGEM DE 3 CARTAS — PASSADO • PRESENTE • FUTURO' -> 'TIRADA DE 3 CARTAS — PASADO • PRESENTE • FUTURO', 'QUANDO USAR' -> 'CUÁNDO USAR', 'COMO MONTAR' -> 'CÓMO ARMAR'. "
            "Reply: 'Que bom que ajudou! ✨' -> '¡Qué bueno que te sirvió! ✨'. "
            "Keep dark mode WhatsApp, customer photo, laptop photo, timestamps and layout identical."
        )
    },
    {
        "id": 7,
        "input_path": "ciganavisual/assets/images_backup_pt/depoimento-7.webp",
        "output_path": "ciganavisual/assets/images/depoimento-7.webp",
        "prompt": (
            "Translate all Portuguese text in this dark mode WhatsApp chat screenshot into natural Spanish: "
            "Header: 'Bianca Cliente' -> 'Bianca', 'online' -> 'en línea'. "
            "Messages: 'Oi! Chegou meu material e está simplesmente lindo e muito bem feito. 😍' -> '¡Hola! Ya me llegó el material y está simplemente hermoso y muy bien hecho. 😍', "
            "'O cuidado em cada detalhe é visível, parabéns pelo capricho!' -> 'El cuidado en cada detalle es visible, ¡felicitaciones por la dedicación!', "
            "'Estou animada para usar nas minhas leituras e estudos, vai fazer toda a diferença.' -> 'Estoy muy emocionada de usarlo en mis lecturas y estudios, va a hacer toda la diferencia.'. "
            "Inside the photo on the desk: on book box 'BARALHO CIGANO EM MAPAS MENTAIS' -> 'BARAJA GITANA EN MAPAS MENTALES', on iPad 'O CAVALEIRO' -> 'EL JINETE', 'MOVIMENTO' -> 'MOVIMIENTO'. "
            "Reply: 'Que alegria saber disso! ✨ Aproveite muito seu material e conte comigo sempre que precisar!' -> '¡Qué alegría saberlo! ✨ ¡Disfruta mucho tu material y cuenta conmigo siempre que lo necesites!'. "
            "Keep dark mode WhatsApp, user photo, desk setup photo, timestamps and layout identical."
        )
    },
    {
        "id": 8,
        "input_path": "ciganavisual/assets/images_backup_pt/depoimento-8.webp",
        "output_path": "ciganavisual/assets/images/depoimento-8.webp",
        "prompt": (
            "Translate all Portuguese text in this WhatsApp chat screenshot into natural Spanish: "
            "Header: 'Juliana Cliente' -> 'Juliana', 'online' -> 'en línea'. "
            "Messages: 'Gente, a qualidade é maravilhosa!' -> '¡Chicas, la calidad es maravillosa!', "
            "'O conteúdo é super prático pro estudo do dia a dia.' -> 'El contenido es súper práctico para el estudio del día a día.', "
            "'As cartas estão fazendo total sentido pra mim!' -> '¡Las cartas están teniendo total sentido para mí!'. "
            "Inside the MacBook photo: 'COMBINAÇÕES — AMOR & VÍNCULOS' -> 'COMBINACIONES — AMOR & VÍNCULOS'. "
            "Reply: 'Que bom saber! ✨' -> '¡Qué bueno saberlo! ✨'. "
            "Keep customer photo, laptop photo, WhatsApp bubbles, timestamps and layout identical."
        )
    },
    {
        "id": 9,
        "input_path": "ciganavisual/assets/images_backup_pt/depoimento-9.webp",
        "output_path": "ciganavisual/assets/images/depoimento-9.webp",
        "prompt": (
            "Translate all Portuguese text in this dark mode WhatsApp chat screenshot into natural Spanish: "
            "Header: 'Juliana Cliente' -> 'Juliana', 'online' -> 'en línea'. "
            "Messages: 'Genteee, amei o material! 😍' -> '¡Chicaas, amé el material! 😍', "
            "'As explicações nos mapas mentais ajudam demais a memorizar os significados rapidinho.' -> 'Las explicaciones en mapas mentales ayudan muchísimo a memorizar los significados rapidísimo.', "
            "'Já tô sentindo diferença nas minhas leituras.' -> 'Ya estoy sintiendo la diferencia en mis lecturas.'. "
            "Inside the photo of spiral notebook and book box: '15 O URSO - FORÇA' -> '15 EL OSO - FUERZA', on box 'CARTAS DO BARALHO CIGANO EM MAPAS MENTAIS' -> 'CARTAS DE LA BARAJA GITANA EN MAPAS MENTALES'. "
            "Reply: 'Queeee bom saber! 😍📚 Continue assim!' -> '¡Quééé bueno saberlo! 😍📚 ¡Sigue así!'. "
            "Keep dark mode WhatsApp, customer photo, desk photo, timestamps and layout identical."
        )
    }
]

def process_item(item):
    num = item["id"]
    out_path = item["output_path"]
    print(f"\n==========================================")
    print(f"Starting Depoimento {num}...")

    # If depoimento 1 already generated in test
    if num == 1 and os.path.exists("/tmp/test_depoimento_1_opt.webp"):
        print("Using existing generated image for depoimento-1...")
        im = Image.open("/tmp/test_depoimento_1_opt.webp")
        im.save(out_path, "WEBP", quality=85, method=6)
        print(f"Saved {out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")
        return True

    with open(item['input_path'], 'rb') as f:
        img_bytes = f.read()
    b64_img = base64.b64encode(img_bytes).decode()

    url = "https://api.openai.com/v1/images/edits"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-image-2.5-flare",
        "prompt": item["prompt"],
        "images": [{"image_url": f"data:image/webp;base64,{b64_img}"}],
        "quality": "low",
        "output_format": "webp"
    }

    req = urllib.request.Request(url, headers=headers, data=json.dumps(payload).encode())
    try:
        t0 = time.time()
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = json.loads(resp.read().decode())
            dur = time.time() - t0
            usage = data.get("usage", {})
            print(f"Depoimento {num} API completed in {dur:.1f}s. Usage: {usage}")

            raw_bytes = None
            if "data" in data and len(data["data"]) > 0:
                it = data["data"][0]
                if "b64_json" in it:
                    raw_bytes = base64.b64decode(it["b64_json"])
                elif "url" in it:
                    with urllib.request.urlopen(urllib.request.Request(it["url"]), context=ctx) as img_resp:
                        raw_bytes = img_resp.read()

            if not raw_bytes:
                print(f"Error: No image bytes received for depoimento {num}")
                return False

            im = Image.open(io.BytesIO(raw_bytes))
            im_resized = im.resize((420, 746), Image.Resampling.LANCZOS)
            im_resized.save(out_path, "WEBP", quality=85, method=6)
            size_kb = os.path.getsize(out_path) / 1024
            print(f"Success! {out_path} saved at (420, 746) ({size_kb:.1f} KB)")
            return True
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode()}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("Beginning generation of all 9 WhatsApp Real Social Proofs with gpt-image-2.5-flare...")
    success = 0
    for it in TESTIMONIALS:
        ok = process_item(it)
        if ok:
            success += 1
        else:
            print(f"Failed at depoimento {it['id']}. Halting.")
            break
        time.sleep(1)

    print(f"\nCompleted {success}/{len(TESTIMONIALS)} testimonials successfully!")

if __name__ == '__main__':
    main()
