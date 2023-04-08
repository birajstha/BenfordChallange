import numpy as np
from matplotlib.figure import Figure
from flask import flash, redirect, url_for
from birajwebapp.config import Config
from birajwebapp.entity.utils import db

def get_first_digit(num):
    """
    Returns the first digit of a given number.

    Parameters:
    num (int/float): Number whose first digit is to be determined.

    Returns:
    int: The first digit of the given number.
    """
    while num >= 10:
        num //= 10
    return num


def benfords_law():
    """
    Returns the expected distribution of first digits according to Benford's law.

    Returns:
    numpy.ndarray: An array containing the expected distribution of first digits according to Benford's law.
    """
    expected = np.array([np.log10(1 + 1./i) for i in range(1, 10)])
    return expected


def calculate_benfords_law_distribution(data):
    """
    Calculates the observed and expected distributions of first digits of the given data.

    Parameters:
    data (list): A list of numeric data.

    Returns:
    tuple: A tuple containing two arrays. The first array is the expected distribution of first digits, and the second array is the observed distribution of first digits.
    """
    data = [float(i) for i in data]
    try:
        first_digits = [get_first_digit(num) for num in data]
        counts = np.bincount(first_digits)[1:]
        total_counts = sum(counts)
        observed = counts / total_counts
        expected = benfords_law()
        return expected, observed

    except Exception as e:
        flash("Invalid Data. Try again! ")
        return None, None


def plot_benfords_law(expected, observed, f_name):
    """
    Plots the observed and expected distributions of first digits of the data and saves it to the plot directory.

    Parameters:
    expected (numpy.ndarray): The expected distribution of first digits.
    observed (numpy.ndarray): The observed distribution of first digits.
    f_name (str): The name of the file to be saved.

    Returns:
    matplotlib.figure.Figure: The plot of the expected and observed distributions of first digits.
    """
    fig = Figure(figsize=(10, 5), dpi=100)
    ax = fig.add_subplot()
    ax.plot(range(1, 10), expected, 'bo', ms=8, label='Benford\'s Law (Expected)')
    ax.plot(range(1, 10), observed, 'ro', ms=8, label='Observed')
    ax.set_xlabel('First Digit')
    ax.set_ylabel('Frequency')
    ax.set_title('Benford\'s Law')
    ax.legend()
    fig.savefig(f"{Config.PLOTS_DIR}/{f_name}.png")
    return fig


def validate_benford(observed_data):
    """
    Validates if the data follows Benford's law or not.

    Parameters:
    observed_data (numpy.ndarray): The observed distribution of first digits.

    Returns:
    bool: True if the data follows Benford's law, False otherwise.
    """
    return all(observed_data == sorted(observed_data, reverse=True))



def calculate_and_plot_benford(data_dao, path, data_index, f_name):
    """
    This function calculates and plots the Benford's law distribution of the data, validates if the data follows Benford's law or not,
    and saves the data to the database.

    Parameters:

        data_dao (object): Data Access Object for the data to be saved in the database.
        path (str): Path to the file containing the data to be analyzed.
        data_index (int): The index of the data column to be analyzed.
        f_name (str): The name of the output plot file.

    Returns:

        None if there is an error or the file is not found.
        A plot of the Benford's Law distribution if the data follows Benford's Law.
        Redirect to /benford without plot if benford is not validated

    """
    try:
        with open(path, 'r') as f:
            raw_data = f.readlines()
        data = [lines[1].split("\t")[data_index] for lines in enumerate(raw_data)]
        expected, observed = calculate_benfords_law_distribution(data)
        if not validate_benford(observed):
            flash("The data does not follow Benford's Law")
            return redirect(url_for('benfordapp.benford'))
        db.session.add(data_dao)
        db.session.commit()
        flash("Data Saved on Database")
        return plot_benfords_law(expected, observed, f_name)
    
    except FileNotFoundError:
        flash("File not found, Try uploading again!")
        return None
    
    except Exception:
        flash("Sorry, But data don't look right ! Please check again")
        return None
    
    
