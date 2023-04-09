# Importing the required modules
from flask import Blueprint, render_template, flash, redirect, url_for
from birajwebapp.models import Data
from birajwebapp.config import Config
from os import path
from birajwebapp.logging.logger import log_error, log_debug

# Creating a blueprint named 'benfordapp'
benfordapp = Blueprint('benfordapp', __name__)

# Defining a route for the benford plot page that takes a filename as a parameter
@benfordapp.route("/benford/<filename>")
def benford(filename):
    # Checking if the plot file exists in the directory specified in the Config class
    if path.isfile(f"{Config.PLOTS_DIR}/{filename}.png"):
        # If the plot file exists, rendering the benford template with the filename
        return render_template('benford.html', filename=filename)
    # If the plot file does not exist, flashing a message and redirecting to the home page
    flash("Oops! Can't find the plot")
    log_error("File doesnt exist")
    return redirect(url_for('main.home'))

# Defining a route for the page that shows all uploaded data
@benfordapp.route("/benford/alldata")
def alldata():
    try:
        # Querying all the uploaded data from the database
        all_uploaded_data = Data.query.all()
        # Rendering the alldata template with the queried data
        return render_template('alldata.html', all_uploaded_data=all_uploaded_data)
    except Exception as e:
        # If there is an exception while querying the data, flashing a message and redirecting to the home page
        flash("Can't find Data")
        log_debug(e)
        return redirect(url_for('main.home'))
