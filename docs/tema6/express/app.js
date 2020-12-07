var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
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
    res.send(JSON.stringify(songs, null, 3),);
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
