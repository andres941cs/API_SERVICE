
from flask import request, Blueprint
from ..services.Spotify import SpotifyAPI
# MAPPING AND PREFIX
app = Blueprint('album', __name__, url_prefix='/v1/album')
# 
spotify = SpotifyAPI()
#_________________________________ Album _________________________________

# RUTA PARA BUSCAR ALBUNES
@app.route('search/<name>', methods= ['GET'] )
def searchSong(name):
    result = spotify.search_album(name)
    return result

# RUTA PARA OBTENER ALBUM POR ID
@app.route('<id>', methods= ['GET'] )
def getSong(id):
    result = spotify.get_album(id)
    return result
