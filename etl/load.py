import boto3
import pandas as pd
import os
from datetime import datetime


def upload_to_s3(df, bucket_name, object_name_prefix="youtube_data"):
    """
    Saves a DataFrame as CSV and uploads it to AWS S3.

    Args:
        df (pd.DataFrame): Cleaned DataFrame to upload
        bucket_name (str): Name of the S3 bucket
        object_name_prefix (str): Optional prefix for the file name in S3

    Returns:
        str: S3 object URL or file path
    """
    # Create a filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{object_name_prefix}_{timestamp}.csv"
    filepath = os.path.join("data", filename)

    # Save DataFrame as CSV locally
    df.to_csv(filepath, index=False)
    print(f"✅ CSV saved locally at {filepath}")

    # Connect to AWS S3
    s3 = boto3.client("s3")

    try:
        s3.upload_file(filepath, bucket_name, filename)
        print(f"✅ Uploaded to S3 bucket: {bucket_name}/{filename}")
        return f"s3://{bucket_name}/{filename}"
    except Exception as e:
        print("❌ Upload failed:", e)
        return None


# Example test
if __name__ == "__main__":
    from extract import get_video_data
    from transform import transform_data

    df_raw = get_video_data("AI Jobs", 5)
    df_clean = transform_data(df_raw, "AI Jobs")

    # Set your own S3 bucket name below
    BUCKET_NAME = "your-s3-bucket-name"
    upload_to_s3(df_clean, BUCKET_NAME)
