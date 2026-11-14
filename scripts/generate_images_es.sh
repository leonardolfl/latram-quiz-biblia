#!/bin/bash
set -e
echo "Gerando todas as imagens em Espanhol (Depoimentos, Capas de Bônus e Mapas Mentais)..."
python3 scripts/generate_testimonials.py
python3 scripts/generate_bonuses.py
python3 scripts/generate_cards.py
echo "Todas as imagens em Espanhol geradas e otimizadas com sucesso!"
