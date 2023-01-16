import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

# print(os.environ['SPOTIPY_CLIENT_ID'])

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

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))


def retrieve_songs():
    top_tracks = sp.current_user_top_tracks(limit=10)

    for idx, item in enumerate(top_tracks['items']):
        uri = item['uri']
        acousticness = sp.audio_features(uri)[0]['acousticness']
        energy = sp.audio_features(uri)[0]['energy']
        danceability = sp.audio_features(uri)[0]['danceability']
        valence = sp.audio_features(uri)[0]['valence']
        print(idx, item['uri'], item['name'], [a['name'] for a in item['artists']],valence)
        
        if valence > 0.5:
            happy_songs.append(item)
           
        else:
            sad_songs.append(item)
        
        if energy>0.6:
            high_energy_songs.append(item)
        else:
            calm_songs.append(item)
        
        if danceability>0.7:
            cheerful_songs.append(item)



retrieve_songs()

print("LIST OF HAPPY SONGS")
happy_songs = sorted(happy_songs, key=lambda k: [sp.audio_features(k['uri'])[0]['valence']])
happy_songs.reverse()
for item in happy_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]} , {sp.audio_features(item['uri'])[0]['valence']}")



print("LIST OF SAD SONGS")
sad_songs = sorted(sad_songs, key=lambda k: [sp.audio_features(k['uri'])[0]['valence']])
for item in sad_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]} , {sp.audio_features(item['uri'])[0]['valence']}")


print("LIST OF HIGH ENERGY SONGS")
high_energy_songs = sorted(high_energy_songs, key=lambda k: [sp.audio_features(k['uri'])[0]['energy']])
high_energy_songs.reverse()
for item in high_energy_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]},{sp.audio_features(item['uri'])[0]['energy']}" )


print("LIST OF CALM SONGS")
calm_songs = sorted(calm_songs, key=lambda k: [sp.audio_features(k['uri'])[0]['energy']])
for item in calm_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]},{sp.audio_features(item['uri'])[0]['energy']}")


print("LIST OF CHEERFUL SONGS")
cheerful_songs = sorted(cheerful_songs, key=lambda k: [sp.audio_features(k['uri'])[0]['danceability']])
cheerful_songs.reverse()
for item in cheerful_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]},{sp.audio_features(item['uri'])[0]['danceability']}")




# sad happy neutral surprise angry disgust fear
