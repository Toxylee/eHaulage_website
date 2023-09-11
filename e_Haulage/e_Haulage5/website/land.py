# Import necessary modules and libraries.
from flask import Blueprint, render_template

# Create a Blueprint for the landing page route.
land = Blueprint('land', __name__)

# Route for the landing page.
@land.route('/')
def landing():
    return render_template("index.html")
