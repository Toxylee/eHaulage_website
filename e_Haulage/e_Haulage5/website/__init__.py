# Import necessary modules and libraries.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate

# Create a SQLAlchemy database instance.
db = SQLAlchemy()
DB_NAME = "database.db"

# Function to create and configure the Flask application.
def create_app():
    # Create a Flask application instance.
    app = Flask(__name__)

    # Configure the Flask application with a secret key.
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    # Configure the SQLAlchemy database URI to use SQLite.
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Initialize the database with the Flask application.
    db.init_app(app)

    # Initialize Flask-Migrate with the Flask application and the database instance.
    migrate = Migrate(app, db)

    # Import and register blueprints from different parts of the application.
    from .land import land
    from .views import views
    from .auth import auth

    app.register_blueprint(land, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import models and create database tables.
    from .models import User, User2, Order
    
    with app.app_context():
        db.create_all()
    
    # Initialize Flask-Login's LoginManager.
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    # Define a user loader function for Flask-Login.
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    # Return the configured Flask application.
    return app

    @login_manager.user_loader
    def load_user(id):
        return User2.query.get(int(id))

    return app

# Function to create the database if it doesn't exist.
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
