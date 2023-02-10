web: gunicorn djangostripe.wsgi:application --log-file
release: python djangostripe/manage.py collectstatic --noinput
release: python djangostripe/manage.py migrate