# TEMA 7: Composición de contenedores
## Ejercicios de autoevaluación

**1. Crear un pod con dos o más contenedores, de forma que se pueda usar uno desde el otro. Uno de los contenedores contendrá la aplicación que queramos desplegar.**

He [instalado podman](https://podman.io/getting-started/installation) y consultado este [enlace](https://www.vultr.com/docs/how-to-install-and-use-podman-on-ubuntu-20-04).

Algunas órdenes básicas a tener en cuenta:
```
podman images
podman run hello-world
podman ps -a
podman stop --latest
podman start --latest
podman rm --latest
```

Para guardar los cambios de un contenedor:
```
podman commit \
       --message "Statement of changes" \
       --author "Author Name <example@example.com>" \
       <cntnr_id> repository/new_name
```

Para pushear los cambios:
```
podman login docker.io
podman push <image_id> <docker-registry-username>/<docker-image-name>
```


**2. Usar un miniframework REST para crear un servicio web y introducirlo en un contenedor, y componerlo con un cliente REST que sea el que finalmente se ejecuta y sirve como "frontend".**
