from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']
app.config["SECRET_KEY"] = "606f36256c1e65ac6075db285c0b4958"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db' #relative path from the current file
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_method_category = 'info'

from blog import routes
