release: python manage.py collectstatic --noinput

web: gunicorn HarborageAtAshleyMarina.wsgi:application --log-file - --workers 3 --threads 2 --timeout 60
