# Instala las dependencias
install: requirements.txt
	pipenv install --three
	pipenv install -r requirements.txt

# Comprueba sintaxis
sintaxis:
	pipenv run python3.8 app.py

# Ejecuta los tests
test:
	# Tests unitarios e informe a través de report -m
	pipenv run coverage run test_app.py -v
	#pipenv run coverage report -m

# Borra ficheros creados
clean:
	#rm -r ./docs/tema6/__pycache__
	rm .coverage
	rm Pipfile*
