docker-compose run backend python3 manage.py migrate
docker-compose run backend python3 manage.py loaddata apps/api/fixtures/restaurants.json
