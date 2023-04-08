from flask import Blueprint, request, redirect, url_for, render_template, flash
from birajwebapp.entity.forms import UploadForm
from birajwebapp.entity.utils import save_data
from birajwebapp.benfordapp.calc_benford import calculate_and_plot_benford
from birajwebapp.models import Data
from os import path


main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
def home():
    form = UploadForm()
    if request.method == 'POST' and form.validate_on_submit():
        data_uploaded = form.file.data
        f_name, f_ext = path.splitext(data_uploaded.filename)
        data_column = form.data_column.data
        data_dao = Data(f_name, data_column)

       # check for correct file (extension)
        # Only Flat files supported - with no extension
        if f_ext != "":
            flash("Only Flat files supported")
            return render_template('home.html', title='Home', form=form)

        else:
            # check for data column
            data_path = save_data(data_dao, data_uploaded)
            if data_path != None:
                try:
                    with open(data_path, 'r') as f:
                        raw_data = f.readlines()
                except FileNotFoundError:
                    flash("File not found, Try uploading again!")
                
                headers = raw_data[0].split("\t")
                headers = [header.strip() for header in headers]
                
                if data_column in headers:   
                    try:         
                        check_None = calculate_and_plot_benford(data_dao, data_path, headers.index(data_column), f_name)
                        if check_None != None:
                            return redirect(url_for('benfordapp.benford', filename=f_name))
                    except Exception as e:
                        flash("Sorry, Looks like Data is not valid.")
                        check_None = calculate_and_plot_benford(data_dao, data_path, headers.index(data_column), f_name)
                        if check_None != None:
                            return redirect(url_for('benfordapp.benford', filename=f_name))
                        return render_template('home.html', title='Home', form=form)
                    
                else:
                    flash(f"Data Column doesn't exist. Please select from {headers}")
                    return render_template('home.html', title='Home', form=form)

    return render_template('home.html', title='Home', form=form)


@main.route("/about")
def about():
    return render_template('about.html')


@main.route("/login")
@main.route("/register")
def login():
    return render_template('errors/under_construction.html')
