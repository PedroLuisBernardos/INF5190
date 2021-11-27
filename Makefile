all: run

install:
	sudo pip install -r requirements.txt

run: install
	flask run --host 0.0.0.0

raml:
	npm i -g raml2html
	raml2html api.raml > app/templates/api/doc.html

clean:
	rm app/static/*.xml
	rm app/static/*.csv