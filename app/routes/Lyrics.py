from flask import request, Blueprint
from ..services.Musixmatch import MusixmatchAPI
# MAPPING AND PREFIX
app = Blueprint('lyric', __name__, url_prefix='/v1/lyric')
# 
musixmatch = MusixmatchAPI()
#_________________________________ SONGS _________________________________

# RUTA PARA BUSCAR CANCIONES
@app.route('/search/<song>/<artist>', methods= ['GET'] )
def searchSong(song, artist):
    # name tiene el formato "nombre de la cancion - nombre del artista"
    result = musixmatch.getLyricSong(nameSong=song, nameArtist=artist)
    return result