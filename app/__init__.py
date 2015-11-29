from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.googlemaps import GoogleMaps

from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
googlemaps = GoogleMaps()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    config[config_name].init_db(db)

    bootstrap.init_app(app)
    googlemaps.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
