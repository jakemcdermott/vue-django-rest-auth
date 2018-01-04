# server development

``` bash
# install dependencies
pip install -r requirements-dev.txt

# setup development database
./manage.py makemigrations api --noinput
./manage.py migrate --noinput

# load data
./manage.py createsuperuser --username=root --email=root@example.com --noinput
./manage.py create_fixtures

# run development server
./manage.py runserver --settings=server.settings
```

**Note:** You should setup and activate a [virtualenv](https://virtualenv.pypa.io/en/stable/) before installing any python dependencies.
