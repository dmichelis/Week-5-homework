from flask import Flask
from config import Config
from api.routes import api

from .main_site.routes import main_site
from .authentication.routes import auth
from .models import db as root_db, login_manager, ma

from flask_cors import CORS 

from .helpers import JSONEncoder

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(main_site)
app.register_blueprint(auth)
app.register_blueprint(api)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin'

ma.init_app(app)

CORS(app)

app.json_encoder = JSONEncoder