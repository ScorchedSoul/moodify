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
top_tracks = sp.current_user_top_tracks(limit=50)
# genre = 
# user_id = sp.current_user()["id"]
# results = sp.current_user_saved_tracks()

for idx, item in enumerate(top_tracks['items']):
    # track = item['track']
    uri = item['uri']

    
    acousticness = sp.audio_features(uri)[0]['acousticness']
    energy = sp.audio_features(uri)[0]['energy']
    danceability = sp.audio_features(uri)[0]['danceability']
    valence = sp.audio_features(uri)[0]['valence']
    print(idx, item['uri'], item['name'], [a['name'] for a in item['artists']],danceability)
    
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


print("LIST OF HAPPY SONGS")
for item in happy_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]}")


print("LIST OF SAD SONGS")
for item in sad_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]}")


print("LIST OF HIGH ENERGY SONGS")
for item in high_energy_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]}")


print("LIST OF CALM SONGS")
for item in calm_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]}")


print("LIST OF CHEERFUL SONGS")
for item in cheerful_songs:
    print(f"Song: {item['name']}, Artists: {[a['name'] for a in item['artists']]}")




# sad happy neutral surprise angry disgust fear
