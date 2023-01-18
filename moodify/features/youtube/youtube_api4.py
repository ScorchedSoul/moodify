# Youtube Current Trending : Enter country and returns top 10 current trending videos
from .build import youtube
import pycountry

def youtube_current_trending(country):

    # country = "India"
    
    iso_code = "IN"
    for country in pycountry.countries:
        try:
            if country.name == country:
                iso_code = country.alpha_2 
        except KeyError:
                iso_code = "IN"


    videos=[]

    vd_request = youtube.videos().list(
            part = ["snippet","statistics"],
            chart = "mostPopular",
            regionCode = iso_code
        )

    vd_response = vd_request.execute()

    for item in vd_response["items"]:
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

    # for video in videos[:10]:
    #     print(video['url'],video['views'],video['title'])
