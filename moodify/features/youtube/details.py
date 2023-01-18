from .youtube_api import youtube_duration_finder
from .youtube_api2 import youtube_trending_playlist
from .youtube_api3 import youtube_time_traveller
from .youtube_api4 import youtube_current_trending

yt_app_details = [
    {
        "key":"first",
        "value":
        {
            "title" : "Youtube Duration Calculator ",
            "description" : "Enter playlist link and returns the total duration of the playlist",
            "function" : youtube_duration_finder,
            "required_params" : ["pl_link"],
            "feature_no": 1
        }
    },
    {
        "key":"second",
        "value":
        {
            "title" : "Youtube Trending in Playlist",
            "description" : "Enter playlist link and returns the top videos of that playlist",
            "function" : youtube_trending_playlist,
            "required_params" : ["pl_link"],
            "feature_no": 2
        }
    },
    {
        "key":"third",
        "value":
        {
            "title" : "Youtube Time Traveller",
            "description" : "Enter country, search keyword and date and returns top 10 trending videos of that time",
            "function" : youtube_time_traveller,
            "required_params" : ["country","search","date"],
            "feature_no": 3
        }
    },
    {
        "key":"fourth",
        "value":
        {
            "title" : "Youtube Current Trending",
            "description" : "Enter country and returns top 10 current trending videos",
            "function" : youtube_current_trending,
            "required_params" : ["country"],
            "feature_no": 4
        }
    }
]

