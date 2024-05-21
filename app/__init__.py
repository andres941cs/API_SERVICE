#  IMPORTS  #

# from pymongo import MongoClient

# Flask libraries
from flask import Flask
# from flask_restful import Api
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy


#  DECLARATIONS  #
# Api required variables

# db=SQLAlchemy()
app = Flask(__name__)
CORS(app)
# mongo = MongoClient("mongodb://"+s.MONGO_USER +":"+s.MONGO_PASS+"@"+s.MONGO_HOST+":"+s.MONGO_PORT+"",connect=False)

def create_app():
    
    #pip install Flask-RESTful Para error customs
    # api = Api(app)
    # CONFIGURACIONES
    # app.config['SESSION_COOKIE_HTTPONLY']=True

    # db.init_app(app)
     # Routes
    # from app.Songs import song
    from .routes import Songs , Artists, Albums
     # BLUEPRINTS
    app.register_blueprint(Songs.app)
    app.register_blueprint(Artists.app)
    app.register_blueprint(Albums.app)

    return app