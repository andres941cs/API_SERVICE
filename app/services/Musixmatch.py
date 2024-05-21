import requests

class MusixmatchAPI:
  
  def __init__(self, api_key):
    self.api_key = "dfb4eead38c96405d196e1cde02976db"
    self.base_url = "https://api.musixmatch.com/ws/1.1/"

  def buscar_cancion_por_titulo(self, titulo):
    params = {
      "q_track": titulo,
      "f_lyrics_id": 1,
      "apikey": self.api_key
    }
    url = self.base_url + "track.search"
    response = requests.get(url, params=params)
    if response.status_code == 200:
      data = response.json()
      if data["message"]["header"]["status_code"] == 200:
        canciones = data["message"]["body"]["track_list"]
        for cancion in canciones:
          if cancion["track"]["has_lyrics"] == 1:
            return cancion
      else:
        return None
    else:
      raise Exception("Error al buscar la canción: {}".format(response.status_code))

  def searchArtist(self, artist):
    params = {
      "q_artist": artist,
      "apikey": self.api_key
    }
    url = self.base_url + "artist.search"
    response = requests.get(url, params=params)
    if response.status_code == 200:
      data = response.json()
      if data["message"]["header"]["status_code"] == 200:
        artists = data["message"]["body"]["artist_list"]
        data = []
        for artist in artists:
          data.append({
                    "id": artist["artist"]["artist_id"],
                    "name": artist["artist"]["artist_name"],
                    "country": artist["artist"]["artist_country"],
                })
        return data
      else:
        return {"data": "Artist not available"}
    else:
      raise Exception("Error al buscar la canción: {}".format(response.status_code))

  def getLyricSong(self, nameSong, nameArtist):
    params = {
      "apikey": self.api_key,
      "q_track": nameSong,
      "q_artist": nameArtist,
    }
    url = self.base_url + "matcher.lyrics.get"
    response = requests.get(url, params=params)
    if response.status_code == 200:
      data = response.json()
      if data["message"]["header"]["status_code"] == 200:
        lyric = data["message"]["body"]["lyrics"]
        return {
          "lyrics": lyric["lyrics_body"],
          # "language": lyric["lyrics_language"]
        }
      else:
        return {"lyrics": "Lyrics not available"}
    else:
      raise Exception("Error al obtener la letra de la canción: {}".format(response.status_code))

# Ejemplo de uso
api_key = "dfb4eead38c96405d196e1cde02976db"  # Reemplázalo con tu API key

musixmatch = MusixmatchAPI(api_key)

# Buscar canción por título
# titulo_cancion = "Yo te esperare"
# cancion = musixmatch.buscar_cancion_por_titulo(titulo_cancion)
# print(cancion)

# Buscar artista por nombre
# artista = "Daddy Yankee"
# artistas = musixmatch.searchArtist(artista)
# print(artistas)

# Obtener letra de una canción
# nombre_cancion = "Flowers"
# nombre_artista = "Miley Cyrus"
nombre_cancion = "Ghost"
nombre_artista = "Suisei Hoshimachi"
letra = musixmatch.getLyricSong(nombre_cancion, nombre_artista)
# print(letra)
