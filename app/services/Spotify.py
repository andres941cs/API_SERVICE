import requests
import base64

class SpotifyAPI:
    def __init__(self):
        self.url = "https://api.spotify.com/v1/"
        self.client_id = "c585723063d1410fbd32b278bfdfed80"
        self.client_secret = "b833e6d969934e79abd10726a44b2f8f"
        self.token = self.get_token(self.client_id, self.client_secret)

    # Get token
    def get_token(self, client_id, client_secret):
        url = "https://accounts.spotify.com/api/token"
        params = {
            "grant_type": "client_credentials"
        }
        auth = client_id + ":" + client_secret
        auth_base64 = base64.b64encode(auth.encode()).decode()
        headers = {
            'Authorization': 'Basic ' + auth_base64,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            token = data["access_token"]
            return token
        else:
            return response.status_code
    
    # _________________________ALBUMS_________________________
    # Search Album by name
    def search_album(self, name):
        url = self.url+"search"
        params = {
            "q": name,
            "type": "album"
        }
        headers = {
            'Authorization': 'Bearer ' + self.token
        }
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            array_albums = []
            for album in data["albums"]["items"]:
                array_albums.append({
                    "id": album["id"],
                    "name": album["name"],
                    "release_date": album["release_date"],
                    "artists": " ".join([artist["name"] for artist in album["artists"]]),
                    "image": album["images"][0]["url"] if len(album["images"]) > 0 else "",
                    "genres": album["genres"] if "genres" in album else "N/A"
                })
            return array_albums
        else:
            return response.status_code
        
    def get_album(self, album_id):
        url = self.url +"albums/" + album_id
        headers = {
            'Authorization': 'Bearer ' + self.token
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            arstists = [artist["name"] for artist in data["artists"]]
            songs = [song["name"] for song in data["tracks"]["items"]]

            album = {
                "id": data["id"],
                "name": data["name"],
                "release_date": data["release_date"],
                "total_tracks": data["total_tracks"],
                "image": data["images"][0]["url"] if "images" in data and len(data["images"]) > 0 else "",
                "genres": data["genres"],
                "artists": arstists,
                "tracks": songs
            }
            return album
        else:
            return None
    
    #_________________________ARTISTS_________________________
    # Get Artist
    def get_artist(self, id_artist):
        url = self.url+"artists/"+id_artist
        headers = {'Authorization': 'Bearer ' + self.token}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # FORMAT DATA
            if len(data["images"]) == 0:
                    data["images"] = [{"url": "https://placehold.co/640x640"}]
            else:
                data["images"] = data["images"][0]["url"]
            artist = {
                    "id": data["id"],
                    "name": data["name"],
                    "image": data["images"],
                    "country": "N/A"
                }
            return artist
        else:
            return None

    
    def search_artist(self, artist_name):
        url = self.url+"search"
        params = {
            "q": artist_name,
            "type": "artist"
        }
        headers = {
            'Authorization': 'Bearer ' + self.token
        }
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            array_artists = data["artists"]["items"]
            data = []
            for artist in array_artists:
                data.append({
                    "id": artist["id"],
                    "name": artist["name"],
                    "image":artist["images"][0]["url"] if len(artist["images"]) > 0 else "",
                    "country": "N/A"
                })
            return data

        else:
            return response.json()

    # _________________________SONGS_________________________
    # Get Song
    def get_song(self, track_id):
        url = self.url+"tracks/"+track_id
        headers = {
            'Authorization': 'Bearer ' + self.token
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # FORMAT DATA
            song = {
                "id": data["id"],
                "name": data["name"],
                "artists": [artist["name"] for artist in data["artists"]],
                "album": data["album"]["name"],
                "duration": int(data["duration_ms"]/1000),
                "preview_url": data["preview_url"],
                "image": data["album"]["images"][0]["url"]
            }
            return song
        else:
            return None
    
    # Search Song by name
    def search_song(self, name):
        url = self.url+"search"
        params = {"q": name,"type": "track"}
        headers = {
            'Authorization': 'Bearer ' + self.token
        }
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            # FORMAT DATA
            array_songs = data["tracks"]["items"]
            songs = []
            for song in array_songs:
                print(song)
                songs.append({
                    "id": song["id"],
                    "name": song["name"],
                    "duration": int(song["duration_ms"]/1000),
                    "preview_url": song["preview_url"],
                    "artists": " ".join([artist["name"] for artist in song["artists"]]),
                    "album": song["album"]["name"],
                    "image":song["album"]["images"][0]["url"],
                    "genres": song["artists"][0]["genres"][0] if "genres" in song["artists"][0] else "N/A"
                })
            return songs
        else:
            return response.status_code
    


# SPOTIFY
spotify = SpotifyAPI()
# __________________PRUEBAS_____________________
# result = spotify.search_artist("miley")

# result = spotify.get_artist("726WiFmWkohzodUxK3XjHX")

# result = spotify.search_song("Flowers")
# result = spotify.search_song("Rebellion")
# result = spotify.get_song("0K1xwwKZkuI7ixSgSem0Fv")

# result = spotify.search_album("Specter")
# result = spotify.get_album("5eQx95EHzDMcPurV2aByeh")
# print(result)

