docker-compose run karamenu_backend python3 manage.py migrate
docker-compose run karamenu_backend python3 manage.py loaddata apps/api/fixtures/restaurants.json
