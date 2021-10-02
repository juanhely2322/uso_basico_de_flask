
from flask import Flask
from flask import render_template #permite redenrizar los templates

app = Flask(__name__)
@app.route("/") 
def index():
    	return render_template('index.html') #recibe como parametro el nombre del template 



if __name__ == "__main__":
	app.run(port=8000)