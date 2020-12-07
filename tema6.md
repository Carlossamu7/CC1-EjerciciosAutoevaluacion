# TEMA 6: Microservicios
## Ejercicios de autoevaluación

**1.Instalar `etcd3`, averiguar qué bibliotecas funcionan bien con el lenguaje que estemos escribiendo el proyecto (u otro lenguaje), y hacer un pequeño ejemplo de almacenamiento y recuperación de una clave; hacer el almacenamiento desde la línea de órdenes (con `etcdctl`) y la recuperación desde el mini-programa que hagáis.**

Sol.

**2. Realizar una aplicación básica que use `express` para devolver alguna estructura de datos del modelo que se viene usando en el curso.**

He elegido el modelo de las apuestas. A continuación se muestra el código, cuyo fichero está [aquí](./docs/tema6/express/app.js).

```
var express = require('express');
var app = express();
const PORT = process.env.PORT || 8000;

app.set('port', PORT);

app.use('/apuestas', (req, res) => {
    let songs = [
        {
            local: 'Real Madrid CF',
            visitante: 'Granada CF',
            resultado: '2-1'
        },
				{
            local: 'Getafe CF',
            visitante: 'Real Betis Balompié',
            resultado: '1-3'
        },
				{
            local: 'SD Eibar',
            visitante: 'Sevilla FC',
            resultado: '0-0'
        }
    ];
    res.send(JSON.stringify(songs, null, 3));
})

app.get('',
	function(req,res){
		res.send("Ejercicio 2 de Cloud Computing - Pruebas con express");
	}
);

app.listen(PORT,
	function() {
		console.log("La aplicación se está ejecutando en localhost:" + app.get('port'));
	}
);
```

Al acceder a http://localhost:2000/:

![](./images/tema6/get.png)

Al acceder a http://localhost:2000/apuestas:

![](./images/tema6/apuestas.png)

**3. Programar un microservicio en express (o el lenguaje y marco elegido) que incluya variables como en el caso anterior.**

Sol.

**4. Crear pruebas para las diferentes rutas de la aplicación.**

Sol.

**5. Experimentar con diferentes gestores de procesos y servidores web front-end para un microservicio que se haya hecho con antelación, por ejemplo en la sección anterior.**

Sol.

**6. Usar rake, invoke o la herramienta equivalente en tu lenguaje de programación para programar diferentes tareas que se puedan lanzar fácilmente desde la línea de órdenes.**

Sol.
