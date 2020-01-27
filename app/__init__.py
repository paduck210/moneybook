from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
app.static_folder = 'static'
login = LoginManager(app)
login.login_view = 'login' # @login_required
csrf = CSRFProtect()
csrf.init_app(app)


from app import routes, models


