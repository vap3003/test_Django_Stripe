web: gunicorn djangostripe.wsgi:application --log-file -
heroku ps:scale web=1
release: python djangostripe/manage.py migrate