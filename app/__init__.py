#  IMPORTS  #
from flask import Flask
from flask_cors import CORS

#  DECLARATIONS  #
app = Flask(__name__)
CORS(app)

def create_app():
    
    # CONFIGURACIONES
    # app.config['SESSION_COOKIE_HTTPONLY']=True
    # app.config['SESSION_COOKIE_SECURE']=True
    # app.config['SESSION_COOKIE_SAMESITE']='None'

    # ROUTES
    from .routes import Songs , Artists, Albums , Lyrics
    
    # BLUEPRINTS
    app.register_blueprint(Songs.app)
    app.register_blueprint(Artists.app)
    app.register_blueprint(Albums.app)
    app.register_blueprint(Lyrics.app)

    return app