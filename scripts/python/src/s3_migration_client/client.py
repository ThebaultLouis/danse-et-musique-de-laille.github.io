import mimetypes
import os
import requests
import urllib
import boto3
from dotenv import load_dotenv
import requests
import boto3

load_dotenv()

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")


class S3MigrationClient:
    def __init__(self):
        self.s3 = boto3.client("s3")

    def get_s3_public_file_url(s3_key: str):
        if s3_key == None:
            return None
        return f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{urllib.parse.quote(s3_key)}"
    
    def list_object_keys_in_folder(self, folder_prefix: str) -> list:
      paginator = self.s3.get_paginator("list_objects_v2")
      result = []
      for page in paginator.paginate(Bucket=S3_BUCKET_NAME, Prefix=folder_prefix):
          contents = page.get("Contents", [])
          for obj in contents:
              result.append(obj["Key"])
      return result

    def migrate_file(self, url: str, s3_key: str):
        if not url:
            return
        if not url.startswith("https://"):
            return

        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to download {url}")
            return

        file_data = response.content
        content_type=response.headers.get("Content-Type")
        if content_type is not None:
            file_extension = mimetypes.guess_extension(content_type)
            if file_extension is not None:
                 file_base = os.path.splitext(s3_key)[0]
                 s3_key = file_base + file_extension

        try:
            self.s3.put_object(
                Bucket=S3_BUCKET_NAME,
                Key=s3_key,
                Body=file_data,
                ContentType=content_type,
            )
            print(f"Migrated {s3_key}")
        except Exception as e:
            print(f"Error uploading {url} to S3: {e}")
