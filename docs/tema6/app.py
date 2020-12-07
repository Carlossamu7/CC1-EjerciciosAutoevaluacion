from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>¡Hola Mundo!</h1>'

@app.route('/<nombre>')
def hello_world_nombre(nombre):
    return '<h1>¡Hola {}!</h1>'.format(nombre)

if __name__ == "__main__":
    app.run()
