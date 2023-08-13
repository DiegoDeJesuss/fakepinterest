from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "8503fc386ee2ec838e11eb222471bce0"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
#login_view mesma coisa que @route, no caso na homepage
login_manager.login_view = "homepage"
from fakepinterest import routes