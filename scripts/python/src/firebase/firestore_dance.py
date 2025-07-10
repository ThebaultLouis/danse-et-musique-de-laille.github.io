from dataclasses import dataclass
from dataclasses import dataclass
from s3_migration_client.client import S3MigrationClient

s3_migration_client = S3MigrationClient()

@dataclass
class FirestoreDance:
    id: str
    name: str
    song_link: str
    video_link: str
    pdf_link: str

    @staticmethod
    def from_dict(dance: dict) -> "FirestoreDance":
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
        return FirestoreDance(id, name, song_link, video_link, pdf_link)

    @property
    def s3_key(self):
        return f"Danses/{self.name}/Chorégraphie.pdf"

    @property
    def s3_file_url(self):
        return s3_migration_client.get_s3_public_file_url(self.s3_key)
