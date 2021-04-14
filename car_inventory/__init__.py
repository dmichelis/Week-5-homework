from flask import Flask
from config import Config

from .main_site.routes import main_site
from .authentication.routes import auth

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(main_site)
app.register_blueprint(auth)