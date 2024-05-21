
from flask import request, Blueprint
from ..services.Spotify import SpotifyAPI
# MAPPING AND PREFIX
app = Blueprint('artist', __name__, url_prefix='/v1/artist')
# 
spotify = SpotifyAPI()
#_________________________________ Album _________________________________

# RUTA PARA BUSCAR ALBUNES
@app.route('/search/<name>', methods= ['GET'] )
def searchArtist(name):
    result = spotify.search_artist(name)
    return result

# RUTA PARA OBTENER ALBUM POR ID
@app.route('<id>', methods= ['GET'] )
def getSong(id):
    result = spotify.get_artist(id)
    return result
