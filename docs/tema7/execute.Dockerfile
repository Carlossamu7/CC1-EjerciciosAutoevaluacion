# Imagen base
FROM python:3.8-slim

# Etiqueta que indica el mantenedor
LABEL maintainer="carlossamu7@gmail.com"

# Creación de un usuario sin permisos, carpeta y actualización de pip
RUN useradd -m -s /bin/bash nonrootuser \
    && python3 -m pip install --upgrade pip

# Directorio de trabajo
WORKDIR .

# Fichero con los paquetes necesarios
COPY ./ ./

# Instalación de paquetes
RUN pip install -r requirements.txt \
    && rm requirements.txt

# Usamos el usuario creado
USER nonrootuser

# Expongo el puerto 5000
EXPOSE 80

# Ejecutamos la API
CMD ["python3", "./src/app.py"]
