# kids-xp

Fortnite-style XP + Season Pass web app to motivate reading and English practice for kids.

## MVP
- Kids submit XP activities (Pending)
- Parent approves/rejects every submission
- XP transactions
- Rewards unlock by level

## Stack
- Django
- SQLite (dev/Replit)

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```
