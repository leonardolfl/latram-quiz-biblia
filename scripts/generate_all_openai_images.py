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

TASKS = [
    {
        "name": "bonus-01",
        "input_path": "ciganavisual/assets/images_backup_pt/bonus-01.webp",
        "output_path": "ciganavisual/assets/images/bonus-01.webp",
        "target_size": (480, 600),
        "prompt": "Translate all Portuguese text on this bonus cover to Spanish: change 'BÔNUS 01' to 'BONO 01', 'GUIA DE COMBINAÇÕES' to 'GUÍA DE COMBINACIONES', and on the 3D book cover change 'Guia de Combinações' to 'Guía de Combinaciones'. Keep the exact 3D book perspective, metallic gold embossing, lighting, shadows, colors and background perfectly identical."
    },
    {
        "name": "bonus-02",
        "input_path": "ciganavisual/assets/images_backup_pt/bonus-02.webp",
        "output_path": "ciganavisual/assets/images/bonus-02.webp",
        "target_size": (480, 600),
        "prompt": "Translate all Portuguese text on this bonus cover to Spanish: change 'BÔNUS 02' to 'BONO 02', 'MODELOS DE TIRAGENS' to 'MODELOS DE TIRADAS', and on the angled 3D book cover change 'Modelos de Tiragens' to 'Modelos de Tiradas'. Maintain the exact 3D book angle, perspective distortion, gold metallic gradient, lighting, and composition unchanged."
    },
    {
        "name": "bonus-03",
        "input_path": "ciganavisual/assets/images_backup_pt/bonus-03.webp",
        "output_path": "ciganavisual/assets/images/bonus-03.webp",
        "target_size": (480, 600),
        "prompt": "Translate all Portuguese text on this bonus cover to Spanish: change 'BÔNUS 03' to 'BONO 03', 'GUIA DE POLARIDADES DAS CARTAS' to 'GUÍA DE LAS POLARIDADES DE LAS CARTAS', and on the 3D book cover change 'Guia de Polaridades das Cartas' to 'Guía de las Polaridades de las Cartas'. Keep the 3D perspective, gold embossing on the spine and cover, lighting and background exactly identical."
    },
    {
        "name": "bonus-04",
        "input_path": "ciganavisual/assets/images_backup_pt/bonus-04.webp",
        "output_path": "ciganavisual/assets/images/bonus-04.webp",
        "target_size": (480, 600),
        "prompt": "Translate all Portuguese text on this bonus cover to Spanish: change 'BÔNUS 04' to 'BONO 04', 'GUIA DE PERGUNTAS PODEROSAS' to 'GUÍA DE LAS PREGUNTAS PODEROSAS', and on the 3D book cover change 'Guia de Perguntas Poderosas' to 'Guía de las Preguntas Poderosas'. Preserve the exact 3D book perspective, gold gradient lettering, lighting, and shadows perfectly."
    },
    {
        "name": "hero-mockup",
        "input_path": "ciganavisual/assets/images_backup_pt/hero-mockup.webp",
        "output_path": "ciganavisual/assets/images/hero-mockup.webp",
        "target_size": (480, 320),
        "prompt": "Translate the Portuguese text on this product bundle mockup into Spanish: on the central 3D book cover translate '36 CARTAS DO BARALHO CIGANO EM MAPAS MENTAIS' to '36 CARTAS DE LA BARAJA GITANA EN MAPAS MENTALES' and subtitle 'UM GUIA VISUAL...' to 'UNA GUÍA VISUAL PARA COMPRENDER SIGNIFICADOS, POLARIDADES E INTERPRETACIONES'. On the laptop screen change 'O CAVALEIRO' to 'EL JINETE'. On the tablet screen change 'COMBINAÇÕES' to 'COMBINACIONES'. On the open notebook change 'O CORAÇÃO' to 'EL CORAZÓN'. On spiral notebooks behind change 'TIRAGENS' to 'TIRADAS'. Keep all 3D curves, device screens, perspective angles, lighting, reflections, and composition exactly identical."
    },
    {
        "name": "bundle-mockup",
        "input_path": "ciganavisual/assets/images_backup_pt/bundle-mockup.webp",
        "output_path": "ciganavisual/assets/images/bundle-mockup.webp",
        "target_size": (480, 360),
        "prompt": "Translate Portuguese text into Spanish on this mockup: on the iMac screen translate '36 Cartas do Baralho Cigano em Mapas Mentais' to '36 Cartas de la Baraja Gitana en Mapas Mentales'. On tablet screen change 'O CAVALEIRO' to 'EL JINETE'. On mobile screen change 'O SOL' to 'EL SOL'. On book spines change '36 CARTAS DO BARALHO CIGANO' to '36 CARTAS DE LA BARAJA GITANA'. Keep all 3D screen perspectives, reflections, book spines, shadows and background identical."
    },
    {
        "name": "premium-mockup",
        "input_path": "ciganavisual/assets/images_backup_pt/premium-mockup.webp",
        "output_path": "ciganavisual/assets/images/premium-mockup.webp",
        "target_size": (420, 280),
        "prompt": "Translate Portuguese text into Spanish on this 3D product mockup: translate central book cover and spines to '36 CARTAS DE LA BARAJA GITANA EN MAPAS MENTALES', laptop to 'EL JINETE', tablet to 'COMBINACIONES', notebook to 'EL CORAZÓN'. Preserve all 3D device angles, shadows, textures and composition exactly."
    }
]

def process_task(task):
    name = task["name"]
    print(f"\n==========================================")
    print(f"Starting {name}...")
    
    # Check if we already have test_bonus_01.webp for bonus-01
    if name == "bonus-01" and os.path.exists("/tmp/test_bonus_01.webp"):
        print("Using existing generated image for bonus-01...")
        im = Image.open("/tmp/test_bonus_01.webp")
        im_opt = im.resize(task["target_size"], Image.Resampling.LANCZOS)
        im_opt.save(task["output_path"], "WEBP", quality=85, method=6)
        print(f"Saved {task['output_path']} ({os.path.getsize(task['output_path'])/1024:.1f} KB)")
        return True

    with open(task['input_path'], 'rb') as f:
        img_bytes = f.read()
    b64_img = base64.b64encode(img_bytes).decode()

    url = "https://api.openai.com/v1/images/edits"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-image-2.5-flare",
        "prompt": task["prompt"],
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
            print(f"API call completed in {dur:.1f}s. Usage: {usage}")
            
            raw_bytes = None
            if "data" in data and len(data["data"]) > 0:
                item = data["data"][0]
                if "b64_json" in item:
                    raw_bytes = base64.b64decode(item["b64_json"])
                elif "url" in item:
                    with urllib.request.urlopen(urllib.request.Request(item["url"]), context=ctx) as img_resp:
                        raw_bytes = img_resp.read()
            
            if not raw_bytes:
                print(f"Error: No image bytes received for {name}")
                return False
                
            im = Image.open(io.BytesIO(raw_bytes))
            im_resized = im.resize(task["target_size"], Image.Resampling.LANCZOS)
            im_resized.save(task["output_path"], "WEBP", quality=85, method=6)
            size_kb = os.path.getsize(task["output_path"]) / 1024
            print(f"Success! {task['output_path']} saved at {task['target_size']} ({size_kb:.1f} KB)")
            return True
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode()}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("Beginning generation of all 7 3D/mockup images with gpt-image-2.5-flare...")
    success_count = 0
    for t in TASKS:
        ok = process_task(t)
        if ok:
            success_count += 1
        else:
            print(f"\nFailed on {t['name']}. Stopping execution.")
            break
        time.sleep(1) # Gentle interval
        
    print(f"\nCompleted {success_count}/{len(TASKS)} images successfully!")

if __name__ == '__main__':
    main()
