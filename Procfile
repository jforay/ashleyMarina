release: python manage.py collectstatic --noinput

web: gunicorn HarborageAtAshleyMarina.wsgi:application --log-file -
