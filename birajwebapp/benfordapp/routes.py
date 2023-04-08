from flask import Blueprint, render_template, flash, redirect,url_for
from birajwebapp.models import Data

benfordapp = Blueprint('benfordapp', __name__)


@benfordapp.route("/benford/<filename>")
def benford(filename):
    return render_template('benford.html', filename=filename)

@benfordapp.route("/benford/alldata")
def alldata():
    try:
        all_uploaded_data = Data.query.all()
        return render_template('alldata.html', all_uploaded_data = all_uploaded_data)
    except Exception:
        flash("Can't find Data")
        return  redirect(url_for('main.home'))