from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
app.config['SECRET_KEY']='225a0dabbad8bf94f52e22de'
bcrypt= Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = 'info'
#engine = create_engine("mysql+pymysql://user:pw@host/db", pool_pre_ping=True)

from market import routes


