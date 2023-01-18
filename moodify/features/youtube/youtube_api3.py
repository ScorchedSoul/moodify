# Youtube Time Traveller : Enter country, search keyword and date and returns top 10 trending videos of that time
from .build import youtube
import pycountry
from datetime import datetime
from google.api_core.datetime_helpers import to_rfc3339

def youtube_time_traveller(country,search,date):

    # country = "India"
    # search = "cricket"
    # date = "06/19/2010"

    iso_code = "IN"
    for country in pycountry.countries:
        try:
            if country.name == country:
                iso_code = country.alpha_2 
        except KeyError:
                iso_code = "IN"


    datetime_str = f'{date} 23:59:59'
    datetime_object = datetime.strptime(datetime_str, '%m/%d/%Y %H:%M:%S')
    rfc3339_str = to_rfc3339(datetime_object)

    search_date = rfc3339_str
    videos = []
    vid_ids = []

    pl_request = youtube.search().list(
        part = 'snippet',
        q = search,
        maxResults = 50,
        publishedBefore = search_date
    )

    pl_response = pl_request.execute()

    for item in pl_response['items']:
        id = item["id"]["videoId"]
        vid_ids.append(id)


    vid_request = youtube.videos().list(
            part = ["statistics","snippet"],
            id= ','.join(vid_ids),
            regionCode = iso_code
        )

    vid_response = vid_request.execute()

    for item in vid_response['items']:
        vid_views = item['statistics']['viewCount']
        vid_id = item['id']
        vid_title = item["snippet"]["title"]
        yt_link = f"https://youtu.be/{vid_id}"

        videos.append(
            {
                "views" : int(vid_views),
                "url" : yt_link,
                "title": vid_title,
                "id": vid_id
            }
        )

    videos.sort(key=lambda vid: vid['views'],reverse=True)
    return videos
