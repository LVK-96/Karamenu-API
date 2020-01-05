# Karamenu API

Django rest framework powered API to unify the format of the data from different restaurant APIs (Sodexo and Fazer for now).

* Deployed to [heroku](https://karamenu-api.herokuapp.com/restaurants)

## Dev environment setup

Requires [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/).

> Start the db and backend containers
```bash
docker-compose up # API is running at localhost:8000
```

### Adding restaurants
Just run the script `migrate_and_load.sh`.

> If you wish to add some other restaurants you can create an admin account and add them through the admin panel.
```bash
python manage.py createsuperuser # create an admin account
```
Navigate to `localhost:8000/admin` in your browser.
