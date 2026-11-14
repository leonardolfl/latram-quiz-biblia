#!/bin/bash
set -e
echo "Revertendo imagens para a versão original em Português..."
cp -r ciganavisual/assets/images_backup_pt/* ciganavisual/assets/images/
echo "Imagens revertidas com sucesso para o Português!"
