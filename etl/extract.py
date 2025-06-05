import requests
import pandas as pd
from config.config import YOUTUBE_API_KEY


def get_video_data(query, max_results=10):
    """
    Fetches video data from YouTube based on a search query.

    Args:
        query (str): The search keyword.
        max_results (int): Number of results to return.

    Returns:
        pd.DataFrame: A DataFrame containing video metadata.
    """

    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    # List to store extracted video info
    videos = []

    for item in data.get("items", []):
        video_info = {
            "video_id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "published_at": item["snippet"]["publishedAt"],
            "channel_title": item["snippet"]["channelTitle"]
        }
        videos.append(video_info)

    # Convert to DataFrame
    return pd.DataFrame(videos)


# Example test run
if __name__ == "__main__":
    df = get_video_data("AI Jobs", max_results=5)
    print(df)
