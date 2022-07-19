#Import libraries
import os
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = "s3cr3t"
app.debug = False
app._static_folder = os.path.abspath("templates/static/")

#Funcion controladora para mostrar la página principal
#Definicion de la ruta por defecto
@app.route("/", methods=["GET"])
#Llamar a index
def index():
    """
        Creates the index page with all of its attributes.

        Parameters
        ----------
        None

        Returns
        -------
        The index page rendered
    """
    # Creates the input image
    return render_template("/layouts/index.html")

#Funcion main del programa
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)