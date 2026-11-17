import os
import json
import base64
import urllib.request
import ssl

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

TASKS = [
    {
        "name": "bonus-01",
        "input_path": "ciganavisual/assets/images_backup_pt/bonus-01.webp",
        "output_path": "ciganavisual/assets/images/bonus-01.webp",
        "prompt": "Translate all Portuguese text on this bonus cover to Spanish: change 'BÔNUS 01' to 'BONO 01', 'GUIA DE COMBINAÇÕES' to 'GUÍA DE COMBINACIONES', and on the 3D book cover change 'Guia de Combinações' to 'Guía de Combinaciones'. Keep the exact 3D book perspective, metallic gold embossing, lighting, shadows, colors and background perfectly identical."
    },
    {
        "name": "bonus-02",
        "input_path": "ciganavisual/assets/images_backup_pt/bonus-02.webp",
        "output_path": "ciganavisual/assets/images/bonus-02.webp",
        "prompt": "Translate all Portuguese text on this bonus cover to Spanish: change 'BÔNUS 02' to 'BONO 02', 'MODELOS DE TIRAGENS' to 'MODELOS DE TIRADAS', and on the angled 3D book cover change 'Modelos de Tiragens' to 'Modelos de Tiradas'. Maintain the exact 3D book angle, perspective distortion, gold metallic gradient, lighting, and composition unchanged."
    },
    {
        "name": "bonus-03",
        "input_path": "ciganavisual/assets/images_backup_pt/bonus-03.webp",
        "output_path": "ciganavisual/assets/images/bonus-03.webp",
        "prompt": "Translate all Portuguese text on this bonus cover to Spanish: change 'BÔNUS 03' to 'BONO 03', 'GUIA DE POLARIDADES DAS CARTAS' to 'GUÍA DE LAS POLARIDADES DE LAS CARTAS', and on the 3D book cover change 'Guia de Polaridades das Cartas' to 'Guía de las Polaridades de las Cartas'. Keep the 3D perspective, gold embossing on the spine and cover, lighting and background exactly identical."
    },
    {
        "name": "bonus-04",
        "input_path": "ciganavisual/assets/images_backup_pt/bonus-04.webp",
        "output_path": "ciganavisual/assets/images/bonus-04.webp",
        "prompt": "Translate all Portuguese text on this bonus cover to Spanish: change 'BÔNUS 04' to 'BONO 04', 'GUIA DE PERGUNTAS PODEROSAS' to 'GUÍA DE LAS PREGUNTAS PODEROSAS', and on the 3D book cover change 'Guia de Perguntas Poderosas' to 'Guía de las Preguntas Poderosas'. Preserve the exact 3D book perspective, gold gradient lettering, lighting, and shadows perfectly."
    },
    {
        "name": "hero-mockup",
        "input_path": "ciganavisual/assets/images_backup_pt/hero-mockup.webp",
        "output_path": "ciganavisual/assets/images/hero-mockup.webp",
        "prompt": "Translate the Portuguese text across the devices and 3D books into Spanish: on the central 3D book cover translate '36 CARTAS DO BARALHO CIGANO EM MAPAS MENTAIS' to '36 CARTAS DE LA BARAJA GITANA EN MAPAS MENTAIS' and subtitle 'UM GUIA VISUAL...' to 'UNA GUÍA VISUAL...'. On the laptop screen change 'O CAVALEIRO' to 'EL JINETE'. On the tablet change 'COMBINAÇÕES' to 'COMBINACIONES'. On the open notebook change 'O CORAÇÃO' to 'EL CORAZÓN'. Maintain all 3D curves, device screens, perspective angles, lighting, reflections, and shadow detail exactly identical."
    },
    {
        "name": "bundle-mockup",
        "input_path": "ciganavisual/assets/images_backup_pt/bundle-mockup.webp",
        "output_path": "ciganavisual/assets/images/bundle-mockup.webp",
        "prompt": "Translate Portuguese text into Spanish on the mockup: on the iMac screen '36 Cartas do Baralho Cigano em Mapas Mentais' -> '36 Cartas de la Baraja Gitana en Mapas Mentales'. On tablet 'O CAVALEIRO' -> 'EL JINETE'. On mobile phone 'O SOL' -> 'EL SOL'. On book spines '36 CARTAS DO BARALHO CIGANO' -> '36 CARTAS DE LA BARAJA GITANA'. Keep all 3D screen perspectives, reflections, book spines and shadows identical."
    },
    {
        "name": "premium-mockup",
        "input_path": "ciganavisual/assets/images_backup_pt/premium-mockup.webp",
        "output_path": "ciganavisual/assets/images/premium-mockup.webp",
        "prompt": "Translate Portuguese text into Spanish on the 3D mockup: translate central book cover and spines to '36 CARTAS DE LA BARAJA GITANA EN MAPAS MENTALES', laptop to 'EL JINETE', tablet to 'COMBINACIONES', notebook to 'EL CORAZÓN'. Preserve all 3D device angles, shadows and textures exactly."
    }
]

def edit_image(task):
    print(f"\nProcessing {task['name']}...")
    with open(task['input_path'], 'rb') as f:
        img_bytes = f.read()
    b64_img = base64.b64encode(img_bytes).decode()

    url = "https://api.openai.com/v1/images/edits"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Model: gpt-image-2.5-flare (lowest cost, fastest, token-efficient)
    payload = {
        "model": "gpt-image-2.5-flare",
        "prompt": task["prompt"],
        "images": [{"image_url": f"data:image/webp;base64,{b64_img}"}],
        "quality": "low",
        "output_format": "webp"
    }

    req = urllib.request.Request(url, headers=headers, data=json.dumps(payload).encode())
    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = json.loads(resp.read().decode())
            if "data" in data and len(data["data"]) > 0:
                item = data["data"][0]
                if "b64_json" in item:
                    out_bytes = base64.b64decode(item["b64_json"])
                elif "url" in item:
                    img_req = urllib.request.Request(item["url"])
                    with urllib.request.urlopen(img_req, context=ctx) as img_resp:
                        out_bytes = img_resp.read()
                
                with open(task["output_path"], "wb") as out_f:
                    out_f.write(out_bytes)
                print(f"Successfully generated and saved {task['output_path']} ({len(out_bytes)/1024:.1f} KB)")
                return True
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode()
        print(f"Error {e.code}: {err_msg}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == '__main__':
    print("Testing OpenAI Image Edit Pipeline...")
    for t in TASKS:
        success = edit_image(t)
        if not success:
            print("\nStopped due to error (e.g. credit limit). Recharge credits to proceed.")
            break
