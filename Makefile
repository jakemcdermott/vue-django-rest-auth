clean:
	find . -name \*.pyc -o -name -delete
	find . -name \*.pyo -o -name -delete
	find . -name __pycache__ -o -name -delete
	find . -path "./server/server/api/migrations/*.py" -not -name "__init__.py" -o -name -delete
	rm -f server/db.sqlite3

database:
	./server/manage.py makemigrations api --noinput
	./server/manage.py migrate --noinput

fixtures:
	./server/manage.py createsuperuser --username=root --email=root@example.com --noinput
	./server/manage.py create_fixtures

client/node_modules:
	npm --prefix=./client install

client-dist: client/node_modules
	npm --prefix=./client run build

server-dev:
	./server/manage.py runserver --settings=server.settings

all: clean database fixtures client-dist server-dev
