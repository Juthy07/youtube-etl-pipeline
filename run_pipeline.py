from etl.extract import get_video_data
from etl.transform import transform_data
from etl.load import upload_to_s3


def run_etl_pipeline(search_term, max_results, bucket_name):
    print("🔍 Starting ETL pipeline...")

    # Extract
    print("📥 Extracting data...")
    raw_df = get_video_data(search_term, max_results)

    # Transform
    print("🧹 Transforming data...")
    clean_df = transform_data(raw_df, search_term)

    # Load
    print("☁️ Uploading to AWS S3...")
    s3_path = upload_to_s3(clean_df, bucket_name)

    print(f"✅ Pipeline complete. Data available at: {s3_path}")


# Example run
if __name__ == "__main__":
    SEARCH_TERM = "AI Jobs"
    MAX_RESULTS = 10
    BUCKET_NAME = "juthy-youtube-etl"  # Change this to your actual bucket
    run_etl_pipeline(SEARCH_TERM, MAX_RESULTS, BUCKET_NAME)
