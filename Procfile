gunicorn djangostripe.wsgi
release: python djangostripe/manage.py migrate
heroku ps:scale web=1
release: python djangostripe/manage.py runserver