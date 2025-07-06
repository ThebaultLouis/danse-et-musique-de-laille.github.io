import os
from firebase import firebase_collections
import requests
import boto3
from dotenv import load_dotenv

load_dotenv()

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

s3 = boto3.client("s3")


def migrate_firebase_storage_files_to_s3():
    for dance in firebase_collections.firestore_dances():
        if not dance.pdf_link:
            continue
        response = requests.get(dance.pdf_link)
        if response.status_code != 200:
            print(f"Failed to download {dance.pdf_link} for {dance.name}")
            continue

        file_data = response.content

        # Upload to S3
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=dance.s3_key,
            Body=file_data,
            ContentType="application/pdf",
        )

        print(f"Migrated {dance.name} to {dance.s3_file_url}")


if __name__ == "__main__":
    migrate_firebase_storage_files_to_s3()
