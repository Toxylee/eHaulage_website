from flask import Blueprint, render_template

land = Blueprint('land', __name__)

@land.route('/')
def landing():
    return render_template("index.html")
