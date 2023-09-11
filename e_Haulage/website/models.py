# Import necessary modules and libraries.
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Define the 'Order' class for database modeling.
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='f_user1'))
    user2_id = db.Column(db.Integer, db.ForeignKey('user2.id', name='f_user2'))

# Define the 'User' class for database modeling, including UserMixin for user management.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    phone_no = db.Column(db.String(50), nullable=True)
    contact = db.Column(db.String(50), nullable=True)
    orders = db.relationship('Order')

# Define the 'User2' class for database modeling, including UserMixin for user management.
class User2(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    phone_no = db.Column(db.String(50), nullable=True)
    house_addr = db.Column(db.String(50), nullable=True)
    orders = db.relationship('Order')
