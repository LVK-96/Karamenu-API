release: python manage.py migrate && python manage.py loaddata apps/api/fixtures/restaurants.json
web: gunicorn karamenu.wsgi --log-file -
