from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret key haha lololol'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    # register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # import db schemas to make sure we run models.py before the db is created
    from .models import User, Event

    # call the create database function before the app is returned
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app



# initialize the database, if its already created, do not override
def create_database(app):
    if not path.exists('website/instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database! YURRRRRR \n ps AJ thinks you are super duper cool')