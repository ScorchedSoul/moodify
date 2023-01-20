import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()


scopes = ["user-library-read","user-top-read"]
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         client_id=SPOTIPY_CLIENT_ID,
#         client_secret=SPOTIPY_CLIENT_SECRET,
#         redirect_uri="http://example.com",
#         scope=scope,
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )


happy_songs = []
sad_songs = []
calm_songs = []
high_energy_songs = []
cheerful_songs = []
disgust_songs = []
neutral_songs = []

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))


def retrieve_songs():
    top_tracks = sp.current_user_top_tracks(limit=20)

    for idx, item in enumerate(top_tracks['items']):
        uri = item['uri']
        acousticness = sp.audio_features(uri)[0]['acousticness']
        energy = sp.audio_features(uri)[0]['energy']
        danceability = sp.audio_features(uri)[0]['danceability']
        valence = sp.audio_features(uri)[0]['valence']
        print(idx, item['uri'], item['name'], [a['name'] for a in item['artists']])
        
        neutral_songs.append(item)

        if valence > 0.5:
            happy_songs.append(item)
            item.update({"valence" : valence})
           
        else:
            sad_songs.append(item)
            item.update({"valence" : valence})
        
        if energy>0.6:
            high_energy_songs.append(item)
            item.update({"energy" : energy})
        else:
            calm_songs.append(item)
            item.update({"energy" : energy})

        
        if danceability>0.7:
            cheerful_songs.append(item)
            item.update({"danceability" : danceability})
        
        if danceability<0.3:
            cheerful_songs.append(item)
            item.update({"danceability" : danceability})
        
         

retrieve_songs()



print("LIST OF NEUTRAL SONGS")
for item in neutral_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]} , {item['valence']} ")


print("LIST OF HAPPY SONGS")
happy_songs = sorted(happy_songs, key=lambda k: k["valence"])
happy_songs.reverse()
for item in happy_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]} , {item['valence']} ")



print("LIST OF SAD SONGS")
sad_songs = sorted(sad_songs, key=lambda k: k["valence"])
for item in sad_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]} , {item['valence']} ")


print("LIST OF HIGH ENERGY SONGS")
high_energy_songs = sorted(high_energy_songs, key=lambda k: k["energy"])
high_energy_songs.reverse()
for item in high_energy_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]} , {item['energy']} " )


print("LIST OF CALM SONGS")
calm_songs = sorted(calm_songs, key=lambda k: k["energy"])
for item in calm_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]} , {item['energy']} ")


print("LIST OF CHEERFUL SONGS")
cheerful_songs = sorted(cheerful_songs, key=lambda k: k["danceability"])
cheerful_songs.reverse()
for item in cheerful_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]} , {item['danceability']} ")

print("LIST OF DISGUST SONGS")
cheerful_songs = sorted(cheerful_songs, key=lambda k: k["danceability"])
for item in disgust_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]} , {item['danceability']} ")




# sad happy neutral surprise angry disgust fear
