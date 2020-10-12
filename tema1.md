# TEMA 1: Arquitecturas software para la nube
## Ejercicios de autoevaluación

**1. Buscar una aplicación de ejemplo, preferiblemente propia, y deducir qué patrón es el que usa. ¿Qué habría que hacer para evolucionar a un patrón tipo microservicios?**

En el curso 2019/2020 realicé un asistente conversacional para la asignatura *Nuevos Paradigmas de Interacción* el cual se puede consultar [aquí](https://github.com/Carlossamu7/NPI_UGR/tree/master/P3-Voz). Mi equipo de trabajo sólo llevo a cabo la implementación del bot.

La aplicación general tiene una arquitectura cliente-servidor con las siguientes capas:

- Capa de presentación: se comunica con el usuario.

- Capa de acceso a datos: almacena, accede y modifica los datos del sistema.

- Capa de aplicación: gestiona el funcionamiento del sistema y coordina las capas.

Para evolucionar dicho sistema a una arquitectura basada en microservicios habría que separar las funcionalidades en los siguientes microservicios: uno para el bot, otro de acceso a los datos y otro encargado del sistema.

**2. En la aplicación que se ha usado como ejemplo en el ejercicio anterior, ¿podría usar diferentes lenguajes? ¿Qué almacenes de datos serían los más convenientes?**


Efectivamente para cada microservicio se puede usar un lenguaje diferente mejorando posiblemente el rendimiento del sistema. Esta es una de las ventajas de una arquitectura en microservicios.

El asistente conversacional consistía en dar información acerca de las entradas para visitar la Alhambra así como poder sacarlas. Por tanto como los datos a anotar son estáticos se podría usar una base de datos relacional, usando por ejemplo `SQL`.
