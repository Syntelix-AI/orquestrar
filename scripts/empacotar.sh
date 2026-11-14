#!/usr/bin/env sh
# Gera dist/orquestrar-skill.zip: a skill pronta para enviar ao app do Claude ou do ChatGPT.
set -eu
cd "$(dirname "$0")/.."
mkdir -p dist
rm -f dist/orquestrar-skill.zip
cd plugins/orquestrar/skills
zip -qr ../../../dist/orquestrar-skill.zip orquestrar
echo "dist/orquestrar-skill.zip"
