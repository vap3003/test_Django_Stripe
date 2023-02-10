gunicorn djangostripe.wsgi
heroku ps:scale web=1
release: python djangostripe/manage.py migrate