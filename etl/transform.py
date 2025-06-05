import pandas as pd


def transform_data(df, query_used="AI Jobs"):
    """
    Transforms the raw YouTube data:
    - Renames columns for clarity
    - Converts publish date to datetime
    - Adds a column for the search query

    Args:
        df (pd.DataFrame): Raw DataFrame from YouTube API
        query_used (str): Search query used for metadata

    Returns:
        pd.DataFrame: Cleaned and enriched DataFrame
    """

    # Convert 'published_at' to datetime format
    df["published_at"] = pd.to_datetime(df["published_at"])

    # Rename columns for better readability (optional)
    df.rename(columns={
        "video_id": "VideoID",
        "title": "Title",
        "published_at": "PublishedDate",
        "channel_title": "Channel"
    }, inplace=True)

    # Add a new column to track what search term was used
    df["SearchQuery"] = query_used

    return df


# Example test run
if __name__ == "__main__":
    from extract import get_video_data

    raw_df = get_video_data("AI Jobs", max_results=5)
    clean_df = transform_data(raw_df, "AI Jobs")
    print(clean_df)
