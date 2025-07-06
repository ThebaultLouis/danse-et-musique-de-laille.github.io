import json
import os
from dotenv import load_dotenv
from dataclasses import dataclass
import urllib.parse

load_dotenv()

FIRESTORE_BACKUP_FILE_PATH = os.getenv("FIRESTORE_BACKUP_FILE_PATH")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

from dataclasses import dataclass


@dataclass
class FirestoreDance:
    name: str
    song_link: str
    video_link: str
    pdf_link: str

    @classmethod
    def from_dict(cls, dance: dict) -> "FirestoreDance":
        name = dance.get("name", "").strip()
        song_link = dance.get("songLink", "")
        video_link = dance.get("choreographyVideo", "")
        pdf_link = dance.get("choreographyPdf", "")
        return cls(name, song_link, video_link, pdf_link)

    @property
    def s3_key(self):
        return f"Danses/{self.name}/Chorégraphie.pdf"

    @property
    def s3_file_url(self):
        return f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{urllib.parse.quote(self.s3_key)}"


def read_firestore_backup():
    with open(FIRESTORE_BACKUP_FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def firestore_dances():
    data = read_firestore_backup()
    dances: dict = data["__collections__"]["dances"]
    return [FirestoreDance.from_dict(dance) for dance in dances.values()]
