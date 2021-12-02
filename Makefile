run: install database.db
	flask run --host 0.0.0.0

install: raml
	sudo pip install -r requirements.txt

raml:
	npm i -g raml2html
	raml2html api.raml > app/templates/api/doc.html

database.db: clean
	cat db/db.sql | sqlite3 db/database.db

clean:
	rm -rf app/static/*.xml || true
	rm -rf app/static/*.csv || true
	rm -rf db/database.db || true

.PHONY: run
.PHONY: install
.PHONY: raml
.PHONY: clean