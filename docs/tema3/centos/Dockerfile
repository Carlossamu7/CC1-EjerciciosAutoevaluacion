FROM centos:latest

WORKDIR /home/carlos/Documentos/CC1-EjerciciosAutoevaluacion/docs/tema3/centos

COPY hola_mundo.py ./

RUN dnf install python3 -y

RUN python3 -V

CMD python3 hola_mundo.py
