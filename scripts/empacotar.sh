#!/usr/bin/env sh
# Gera dist/orquestrar-skill.zip (a skill pronta para enviar ao app do Claude ou do ChatGPT)
# e copia para docs/download/, de onde o site oferece o download.
set -eu
cd "$(dirname "$0")/.."
mkdir -p dist
rm -f dist/orquestrar-skill.zip
cd plugins/orquestrar/skills
zip -qr ../../../dist/orquestrar-skill.zip orquestrar
cd ../../..
mkdir -p docs/download
cp dist/orquestrar-skill.zip docs/download/orquestrar-skill.zip
echo "dist/orquestrar-skill.zip e docs/download/orquestrar-skill.zip"
