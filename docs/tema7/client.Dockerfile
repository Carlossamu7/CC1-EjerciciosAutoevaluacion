# Imagen base
FROM python:3.8-slim

# Etiqueta que indica el mantenedor
LABEL maintainer="carlossamu7@gmail.com"

# Creación de un usuario sin permisos, carpeta y actualización de pip
RUN useradd -m -s /bin/bash nonrootuser \
    && python3 -m pip install --upgrade pip \
    && apt-get update

WORKDIR .

COPY ./src/client.py requirements_client.txt ./

# Instalación de paquetes
RUN pip install -r requirements_client.txt \
    && rm requirements_client.txt

# Usamos el usuario creado
USER nonrootuser

# Abrir puerto 4001
EXPOSE 4001

CMD ["python3", "client.py"]
