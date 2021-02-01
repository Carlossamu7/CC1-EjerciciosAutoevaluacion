# Instala las dependencias
install: requirements.txt
	pip3 install -r requirements.txt

# Comprueba sintaxis
check:
	python3 src/Alumno.py
	python3 src/AsignaturaConcepto.py
	python3 src/Asignatura.py
	python3 src/Conservatorio.py

# Ejecuta los tests
test:
	# Tests unitarios e informe a través de report -m
	##########################  Test de Alumno  ##########################
	python3 tests/testAlumno.py
	####################  Test de AsignaturaConcepto  ####################
	python3 tests/testAsignaturaConcepto.py
	########################  Test de Asignatura  ########################
	python3 tests/testAsignatura.py
	#######################  Test de Conservatorio  ######################
	python3 tests/testConservatorio.py
	###########################  Test de la API  #########################
	python3 tests/testApp.py

# Construcción
build:
	echo 'No es necesario realizar build'

# Ejecuta la app
execute:
	python3 src/app.py

# Borra ficheros creados
clean:
	#rm -r ./src/__pycache__
	rm .coverage
	rm Pipfile*
