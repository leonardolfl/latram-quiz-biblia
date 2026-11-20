#!/usr/bin/env python3
"""
Minerador e Inspetor de VSLs VTurb / ConverteAI
Extrai player ID, link do vídeo, tempo de delay do botão de compra e metadados.
"""

import sys
import re
import json
import urllib.request
import ssl

ctx = ssl._create_unverified_context()

def inspect_vturb_page(url):
    print(f"\n[+] Analisando URL: {url}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"[-] Erro ao carregar página: {e}")
        return

    # 1. Procurar scripts do VTurb / ConverteAI
    # Exemplo: https://scripts.converteai.net/ACCOUNT_ID/players/PLAYER_ID/player.js
    vturb_scripts = re.findall(r'https?://(?:scripts|cdn)\.converteai\.net/([a-zA-Z0-9_-]+)/players/([a-zA-Z0-9_-]+)/(?:embed\.html|player\.js)', html)
    
    if not vturb_scripts:
        # Tentar regex mais flexível
        vturb_scripts = re.findall(r'converteai\.net/([a-zA-Z0-9_-]+)/players/([a-zA-Z0-9_-]+)', html)

    if vturb_scripts:
        account_id, player_id = vturb_scripts[0]
        print(f"\n[✓] VTURB / CONVERTE DETECTADO!")
        print(f"    - Account ID : {account_id}")
        print(f"    - Player ID  : {player_id}")
        print(f"    - Embed URL  : https://scripts.converteai.net/{account_id}/players/{player_id}/embed.html")
    else:
        print("[-] Nenhum script converteai.net explícito encontrado no HTML estático.")

    # 2. Procurar tempo de Delay do Botão (pitch time)
    # Comum em scripts de VSL: SECONDS_TO_DISPLAY = 1200 ou delay = ...
    delays = re.findall(r'(?:SEC_TO_DISPLAY|delay|timer|seconds_to_display|sec_to_show)\s*[:=]\s*([0-9]{2,5})', html, re.IGNORECASE)
    if delays:
        sec = int(delays[0])
        m = sec // 60
        s = sec % 60
        print(f"[✓] DELAY DO BOTÃO DETECTADO:")
        print(f"    - Pitch aos: {m}m {s}s ({sec} segundos)")

    # 3. Procurar links de checkout
    checkouts = re.findall(r'https?://(?:pay\.[a-zA-Z0-9.-]+|checkout\.[a-zA-Z0-9.-]+|hotmart\.com|digistore24\.com|kiwify\.com\.br|buygoods\.com)[^\s"\'<>]+', html)
    if checkouts:
        print(f"[✓] CHECKOUTS ENCONTRADOS ({len(checkouts)}):")
        for c in set(checkouts[:5]):
            print(f"    - {c}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = "https://cigana.wisefull.online/ciganavisual"
    inspect_vturb_page(target)
