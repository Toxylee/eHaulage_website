# Import necessary modules and libraries.
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, User2
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


# Create a Blueprint for the authentication routes.
auth = Blueprint('auth', __name__)

# Route for user login.
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)


# Route for user login 2.
@auth.route('/login2', methods=['GET', 'POST'])
def login2():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')


        user2 = User2.query.filter_by(email=email).first()
        if user2:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user2, remember=True)
                return redirect(url_for('views.home4'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user2=current_user)

# Route for user logout.
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("login.html")

# Route for user registration.
@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template("sign_up.html", user=current_user)
    else:
        if request.method == 'POST':
            email = request.form.get('email')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            contact = request.form.get('contact')
            phone_no = request.form.get('phone_no')
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')

            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email already exists.', category='error')
            elif len(email) < 4:
                flash('Email must be greater than 3 characters.', category='error')
            elif len(first_name) < 2:
                flash('First name must be greater than 1 character.', category='error')
            elif len(last_name) < 2:
                flash('Last name must be greater than 1 character.', category='error')
            elif len(contact) < 10:
                flash('Please write detailed contact address.', category='error')
            elif len(phone_no) < 10:
                flash('Please write correct phone no.', category='error')
            elif password1 != password2:
                flash('Passwords don\'t match.', category='error')
            elif len(password1) < 7:
                flash('Password must be at least 7 characters.', category='error')
            else:
                new_user = User(email=email, first_name=first_name, last_name=last_name, contact=contact, phone_no=phone_no, password=generate_password_hash(password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account created!', category='success')
                return redirect(url_for('views.home2'))
        return render_template("sign_up.html", user=current_user)


# Route for user registration 2.
@auth.route('/sign_up2', methods=['GET', 'POST'])
def sign_up2():
    if request.method == 'GET':
        return render_template("sign_up2.html", user=current_user)
    else:
        if request.method == 'POST':
            email = request.form.get('email')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            house_addr = request.form.get('house_address')
            phone_no = request.form.get('phone_no')
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')

            user2 = User2.query.filter_by(email=email).first()
            if user2:
                flash('Email already exists.', category='error')
            elif len(email) < 4:
                flash('Email must be greater than 3 characters.', category='error')
            elif len(first_name) < 2:
                flash('First name must be greater than 1 character.', category='error')
            elif len(last_name) < 2:
                flash('Last name must be greater than 1 character.', category='error')
            elif len(house_addr) < 10:
                flash('Please write detailed Permanent House address.', category='error')
            elif len(phone_no) < 10:
                flash('Please write correct phone no.', category='error')
            elif password1 != password2:
                flash('Passwords don\'t match.', category='error')
            elif len(password1) < 7:
                flash('Password must be at least 7 characters.', category='error')
            else:
                new_user = User(email=email, first_name=first_name, last_name=last_name, house_addr=house_addr, phone_no=phone_no, password=generate_password_hash(password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account created!', category='success')
                return redirect(url_for('views.home3'))

        return render_template("sign_up2.html", user2=current_user)
