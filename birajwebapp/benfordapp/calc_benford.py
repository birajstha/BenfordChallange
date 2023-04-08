import numpy as np
from matplotlib.figure import Figure
from flask import flash
from birajwebapp.config import Config

def get_first_digit(num):
    while num >= 10:
        num //= 10
    return num

def benfords_law():
    expected = np.array([np.log10(1 + 1./i) for i in range(1, 10)])
    return expected

def calculate_benfords_law_distribution(data):
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
    return all(observed_data == sorted(observed_data, reverse=True))


def calculate_and_plot_benford(path, data_index, f_name):
    try:
        with open(path, 'r') as f:
            raw_data = f.readlines()
        data = [lines[1].split("\t")[data_index] for lines in enumerate(raw_data)]
        expected, observed = calculate_benfords_law_distribution(data)
        if not validate_benford(observed):
            flash("The data does not follow Benford's Law")
        return plot_benfords_law(expected, observed, f_name)
    
    except FileNotFoundError:
        flash("File not found, Try uploading again!")
        return None
    
    except Exception:
        flash("Sorry, But data don't look right ! Please check again")
        return None
    
    
