#!/usr/bin/env bash
set -euo pipefail

# Replit-friendly Django startup script

if [ ! -d ".venv" ]; then
  python -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

pip -q install --upgrade pip
pip -q install -r requirements.txt

python manage.py migrate --noinput

PORT="${PORT:-8000}"
python manage.py runserver 0.0.0.0:"$PORT"
