TTTrueSkill - minimal Django TrueSkill ranking for table tennis (prototype)
=======================================================================

Quick start (locally, without Docker):
1. python -m venv venv
2. source venv/bin/activate  (Linux/Mac) or venv\Scripts\activate (Windows)
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser  # optional - for admin
6. python manage.py runserver

Docker:
1. docker-compose build
2. docker-compose up

Notes:
- This is a minimal prototype for club use; edit settings.py for production settings.
- The TrueSkill update runs automatically when a Match object is created.

http://raspberrypi:6060/
