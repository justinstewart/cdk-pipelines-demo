from flask import Flask

from .routes.index import blueprint as index_blueprint
from .routes.owners import blueprint as owners_blueprint
from .routes.pets import blueprint as pets_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(index_blueprint)
    app.register_blueprint(owners_blueprint)
    app.register_blueprint(pets_blueprint)
    return app
