from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
    

db = SQLAlchemy() 
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__) ##Creates the app and database
    app.config['SECRET_KEY'] = 'Obliviate'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')   ##Blueprints the URLs
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view= 'auth.login'  ##A library that allows the login and user functionality
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))     ##Loads user

    return app

def create_database(app):
    if not path.exists('ReqBase/' + DB_NAME):   ##Creates database unless one already exists
        with app.app_context():
            db.create_all()
