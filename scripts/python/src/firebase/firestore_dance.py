import os
from dotenv import load_dotenv
from dataclasses import dataclass
import urllib.parse
from dataclasses import dataclass

load_dotenv()

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")


@dataclass
class FirestoreDance:
    id: str
    name: str
    song_link: str
    video_link: str
    pdf_link: str

    @classmethod
    def from_dict(cls, dance: dict) -> "FirestoreDance":
        id = dance.get("id", None)
        name = dance.get("name", None).strip()
        song_link = dance.get("songLink", None)
        video_link = dance.get("choreographyVideo", None)
        pdf_link = dance.get("choreographyPdf", None)

        if song_link != None and len(song_link) == 0:
            song_link = None
        if video_link != None and len(video_link) == 0:
            video_link = None
        if pdf_link != None and len(pdf_link) == 0:
            pdf_link = None
        return cls(id, name, song_link, video_link, pdf_link)

    @property
    def s3_key(self):
        return f"Danses/{self.name}/Chorégraphie.pdf"

    @property
    def s3_file_url(self):
        if self.pdf_link == None:
            return None
        return f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{urllib.parse.quote(self.s3_key)}"
