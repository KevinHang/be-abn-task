from flask import Flask
from flask_restful import Api
from config import Config
from app.extensions import db
from app.resources import TVShowResource, TVShowListResource, TVShowSearchResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    api = Api(app)
    api.add_resource(TVShowResource, '/tvshows/<int:id>')
    api.add_resource(TVShowListResource, '/tvshows')
    api.add_resource(TVShowSearchResource, '/tvshows/search/<string:genre>')

    return app
