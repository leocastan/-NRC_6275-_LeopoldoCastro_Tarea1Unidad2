#Import libraries
import os
from flask import Flask, render_template
from pyquery import PyQuery as pq


app = Flask(__name__)
app.secret_key = "LC"
app.debug = False
app._static_folder = os.path.abspath("templates/static/")

#Function to show the main page
#DDefault path definition
@app.route("/", methods=["GET"])
#Call the index
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