from django.shortcuts import render
from .features.spotify.filter import happy_songs,sad_songs,high_energy_songs,calm_songs,cheerful_songs
# Create your views here.

emotion = "sad"


emotion_to_songs = {
    "happy" : happy_songs,
    "sad" : sad_songs,
    "angry" : calm_songs,
    "fear" : cheerful_songs,
    "party" : high_energy_songs
}

def home(request):
    return render(request , "moodify/home.html",{
        "emotion" : emotion
    }) 

def recommended_songs(request):
    return render(request, "moodify/recommended_songs.html",{
        "songs_list" : emotion_to_songs[emotion], 
        "emotion" : emotion
    })

def recommended_videos(request):
    return None