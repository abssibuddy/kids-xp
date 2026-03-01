#!/usr/bin/env bash
set -euo pipefail

# Replit-friendly Django startup script

if [ ! -d ".venv" ]; then
  python -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

# Replit sometimes forces pip to use `--user` via env/config, which breaks inside venv.
# Ignore user config and any forced user installs.
unset PIP_USER || true
unset PYTHONUSERBASE || true
export PIP_CONFIG_FILE=/dev/null

pip -q install --upgrade pip
pip -q install -r requirements.txt

python manage.py migrate --noinput

PORT="${PORT:-8000}"
python manage.py runserver 0.0.0.0:"$PORT"
