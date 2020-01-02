release: python manage.py db migrate
web: gunicorn --bind 0.0.0.0:$PORT run:app 
