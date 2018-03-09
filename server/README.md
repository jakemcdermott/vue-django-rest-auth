# server development

``` bash
# install dependencies
pipenv install --dev

# setup development database
./manage.py makemigrations api --noinput
./manage.py migrate --noinput

# load data
./manage.py createsuperuser --username=root --email=root@example.com --noinput
./manage.py create_fixtures

# run development server
./manage.py runserver --settings=server.settings
```

**Note:** You should install [pipenv](https://docs.pipenv.org/) before installing any python dependencies.
