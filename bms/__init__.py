from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginmanager = LoginManager(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
loginmanager.login_view = 'main.login'
loginmanager.login_message = 'You need to login to access this page'
loginmanager.login_message_category = 'info'


from bms.owners.routes import owners
from bms.parents.routes import parents
from bms.main.routes import main
app.register_blueprint(owners)
app.register_blueprint(parents)
app.register_blueprint(main)