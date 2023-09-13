# Import necessary modules and libraries.
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Order
from . import db
import json

# Create a Blueprint named 'views'.
views = Blueprint('views', __name__)


# Define a route for the home page that requires user authentication.
@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        order = request.form.get('order')#Gets the note from the HTML 

        if len(order) < 1:
            flash('Order request is too short!', category='error') 
        else:
            new_order = Order(data=order, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_order) #adding the note to the database
            db.session.commit()
            flash('Order added!', category='success')

    return render_template("Request.html", user=current_user)

@views.route('/home4', methods=['GET', 'POST'])
@login_required
def home4():
    if request.method == 'POST':
        order = request.form.get('order')#Gets the note from the HTML

        if len(order) < 1:
            flash('Order request is too short!', category='error')
        else:
            new_order = Order(data=order, user2_id=current_user2.id)  #providing the schema for the note
            db.session.add(new_order) #adding the note to the database
            db.session.commit()
            flash('Order added!', category='success')

    return render_template("Request.html", user2=current_user)

# Define a route for the home page that requires user authentication.
@views.route('/home2', methods=['GET', 'POST'])
@login_required
def home2():
    if request.method == 'POST':
        order = request.form.get('order')#Gets the note from the HTML

        if len(order) < 1:
            flash('Order request is too short!', category='error')
        else:
            new_order = Order(data=order, user_id=current_user.id)  #providing the schema for the note
            db.session.add(new_order) #adding the note to the database
            db.session.commit()
            flash('Order added!', category='success')

    return render_template("Receive.html", user=current_user)


# Define a route for the home page that requires user authentication.
@views.route('/home3', methods=['GET', 'POST'])
@login_required
def home3():
    if request.method == 'POST':
        order = request.form.get('order')#Gets the note from the HTML

        if len(order) < 1:
            flash('Order request is too short!', category='error')
        else:
            new_order = Order(data=order, user2_id=current_user2.id)  #providing the schema for the note
            db.session.add(new_order) #adding the note to the database
            db.session.commit()
            flash('Order added!', category='success')

    return render_template("Receive.html", user2=current_user)


# Define a route to delete a note.
@views.route('/delete-note', methods=['POST'])
def delete_note():  
    order = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    orderId = order['orderId']
    order = Order.query.get(orderId)
    if order:
        if order.user_id == current_user.id:
            db.session.delete(order)
            db.session.commit()

    return jsonify({})
