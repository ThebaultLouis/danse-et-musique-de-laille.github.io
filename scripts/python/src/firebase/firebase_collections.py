import json
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

FIRESTORE_BACKUP_FILE_PATH = os.getenv("FIRESTORE_BACKUP_FILE_PATH")

from dataclasses import dataclass

@dataclass
class FirestoreDance:
    name: str
    song_link: str
    video_link: str
    pdf_link: str

    @classmethod
    def from_dict(cls, dance: dict) -> 'FirestoreDance':
        name = dance.get("name", "").strip()
        song_link = dance.get("songLink", "")
        video_link = dance.get("choreographyVideo", "")
        pdf_link = dance.get("choreographyPdf", "")
        return cls(name, song_link, video_link, pdf_link)


def read_firestore_backup():
    with open(FIRESTORE_BACKUP_FILE_PATH, 'r', encoding='utf-8') as f:
      data = json.load(f)

    return data

def firestore_dances():
    data = read_firestore_backup()
    dances : dict = data["__collections__"]["dances"]
    return [FirestoreDance.from_dict(dance) for dance in dances.values()]

