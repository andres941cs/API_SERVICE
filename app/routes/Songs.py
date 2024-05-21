
from flask import request, Blueprint
from ..services.Spotify import SpotifyAPI
from ..services.Translate import Translate
# MAPPING AND PREFIX
app = Blueprint('song', __name__, url_prefix='/v1/song')
# 
spotify = SpotifyAPI()
tranlate = Translate()
#_________________________________ SONGS _________________________________

# RUTA PARA BUSCAR CANCIONES
@app.route('/search/<name>', methods= ['GET'] )
def searchSong(name):
    result = spotify.search_song(name)
    return result

# RUTA PARA OBTENER CANCION POR ID
@app.route('<id>', methods= ['GET'] )
def getSong(id):
    result = spotify.get_song(id)
    return result


@app.route('/upload', methods=['POST'])
def upload_file():
    # audio es el name de input del formalario
    if 'audio' not in request.files:
        return 'No se ha proporcionado ningún archivo'

    archivo = request.files['audio']

    # Puedes guardar el archivo en el servidor, procesarlo, etc.
    # Aquí solo se imprime el nombre del archivo
    if archivo.filename != '':
        filename = archivo.filename
        # la funcion .save(ruta donde se guarda y el nombre del archivo)
        # archivo.save(filename)
        # AQUI DEBERIA ESTAR EL SERVICIO DE OPEN AI QUE ME PASE DE AUDIO A TEXTO
        
        return 'El archivo {} ha sido subido correctamente'.format(filename)
    else:
        return 'No se ha seleccionado ningún archivo'
    
@app.route('/romanized', methods=['POST'])
def romanized():
    data = request.get_json()
    if 'lyric' not in data:
        return 'No se ha proporcionado ningún archivo'
    lyric = data['lyric']

    # DETECTAR IDIOMA
    language = tranlate.detect_language(lyric)

    # TRADUCIR A ROMANIZADO
    if language == "JAPONESE":
        romanized = tranlate.romanize_japanese(lyric)
        return {"data":romanized, "language":"Romaji"}
    elif language == "KOREAN":
        romanized = tranlate.romanize_korean(lyric)
        return {"data":romanized, "language":"RR"}
    return {"data":"NO_ROMANIZED"}
