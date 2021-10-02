from flask import Flask #aqui se importa flask
app = Flask(__name__) # instanciar, flask recibe como parametro la constante __name__, 
					  #indica el archivo a ejecutar en este caso flask_hello

@app.route("/") 

#se tiene que indicar a que ruta el cliente puede acceder pa esto se uliza un wrap o decorador, 
#inicia con @, route recibe como parametro un string en este caso un  /

def hello():
	return "Hola compañeros de 5 semestre, como estan?"

@app.route("/hola")
def hola():
    return "otro hola"

if __name__ == "__main__": #main idica es el codigo global del archivo principal
	app.run()# se encarga de ejecutar el servidor
 
 