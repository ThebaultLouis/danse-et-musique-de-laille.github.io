from dataclasses import dataclass
import os
from dotenv import load_dotenv
from firebase.firestore_dance import FirestoreDance
from s3_migration_client.client import S3MigrationClient

load_dotenv()

NOTION_DANSES_DATABASE_ID = os.getenv("NOTION_DANSES_DATABASE_ID")


@dataclass
class NotionDanse:
    id: str
    nom: str
    lien_de_la_musique: str
    lien_de_la_choregraphie: str
    pdf_de_la_chorégrapgie: str

    @staticmethod
    def database_id():
        return NOTION_DANSES_DATABASE_ID

    @staticmethod
    def from_firestore_dance(firestore_dance: FirestoreDance) -> "NotionDanse":
        return NotionDanse(
            id=None,
            nom=firestore_dance.name,
            lien_de_la_musique=firestore_dance.song_link,
            lien_de_la_choregraphie=firestore_dance.video_link,
            pdf_de_la_chorégrapgie=firestore_dance.s3_file_url,
        )

    def to_notion_client_create_page_body(cls):
        return {
            "Nom": {"title": [{"text": {"content": cls.nom}}]},
            "Lien de la musique": {"url": cls.lien_de_la_musique},
            "Lien de la chorégraphie": {"url": cls.lien_de_la_choregraphie},
            "Pdf de la chorégraphie": {
                "files": [
                    {
                        "name": "Chorégraphie PDF",
                        "external": {"url": cls.pdf_de_la_chorégrapgie},
                    }
                ]
            },
        }

    @staticmethod
    def from_notion_page(page: dict) -> "NotionDanse":
        properties = page["properties"]
        return NotionDanse(
            id=page["id"],
            nom=(
                properties["Nom"]["title"][0]["text"]["content"]
                if properties["Nom"]["title"]
                else None
            ),
            lien_de_la_musique=properties["Lien de la musique"].get("url", None),
            lien_de_la_choregraphie=properties["Lien de la chorégraphie"].get(
                "url", None
            ),
            pdf_de_la_chorégrapgie=(
                properties["Pdf de la chorégraphie"]["files"][0]["external"]["url"]
                if properties["Pdf de la chorégraphie"]["files"]
                else None
            ),
        )
