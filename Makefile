PYTHON_BIN = $(shell cd server && pipenv --venv)/bin/python

python_bin:
	pushd server; pipenv install --dev; popd;

database: python_bin
	$(PYTHON_BIN) ./server/manage.py makemigrations api --noinput
	$(PYTHON_BIN) ./server/manage.py migrate --noinput

fixtures: python_bin
	$(PYTHON_BIN) ./server/manage.py createsuperuser --username=root --email=root@example.com --noinput
	$(PYTHON_BIN) ./server/manage.py create_fixtures

server-dev: python_bin
	$(PYTHON_BIN) ./server/manage.py runserver --settings=server.settings

client/node_modules:
	yarn --cwd=./client install

client-dist: client/node_modules
	yarn --cwd=./client run build

clean:
	find . -name \*.pyc -o -name -delete
	find . -name \*.pyo -o -name -delete
	find . -name __pycache__ -o -name -delete
	find . -path "./server/server/api/migrations/*.py" -not -name "__init__.py" -o -name -delete
	rm -f server/db.sqlite3

all: clean database fixtures client-dist server-dev
