from dataclasses import dataclass
from enum import Enum
import os
from typing import List
from dotenv import load_dotenv
from firebase.firestore_classe import FirestoreClasse, FirestoreClasseLevel
from firebase.firestore_dance import FirestoreDance
from notion.notion_danse import NotionDanse

load_dotenv()

NOTION_COURS_DATABASE_ID = os.getenv("NOTION_COURS_DATABASE_ID")


class NotionCoursNiveau(str, Enum):
    UNDEFINED = "UNDEFINED"
    DEBUTANT = "Débutant"
    NOVICE = "Novice"
    INTERMEDIAIRE = "Intermédiaire"


FirestoreClasseLevel_NotionCoursNiveau = {
    FirestoreClasseLevel.UNDEFINED: NotionCoursNiveau.UNDEFINED,
    FirestoreClasseLevel.BEGINNER: NotionCoursNiveau.DEBUTANT,
    FirestoreClasseLevel.NOVICE: NotionCoursNiveau.NOVICE,
    FirestoreClasseLevel.INTERMEDIATE: NotionCoursNiveau.INTERMEDIAIRE,
}


@dataclass
class NotionCours:
    date: str
    type: str
    niveau: NotionCoursNiveau
    danses_apprises: List[str]
    danses_revisees: List[str]

    @staticmethod
    def database_id():
        return NOTION_COURS_DATABASE_ID

    @staticmethod
    def from_firestore_classe(
        cls,
        firestore_classe: FirestoreClasse,
        danses_apprises: List[str],
        danses_revisees: List[str],
        niveau="Country",
    ) -> "NotionCours":
        cls(
            date=firestore_classe.doneOn,
            type=FirestoreClasseLevel_NotionCoursNiveau[firestore_classe.level],
            niveau=niveau,
            danses_apprises=danses_apprises,
            danses_revisees=danses_revisees,
        )

    @classmethod
    def to_notion_client_create_page_body(cls):
        return {
            "parent": {"database_id": NOTION_COURS_DATABASE_ID},
            "properties": {
                "date": {"title": [{"text": {"content": cls.date}}]},
                "id": {"rich_text": [{"text": {"content": cls.id}}]},
                "type": {"select": {"name": cls.type}},
                "niveau": {"select": {"name": cls.niveau}},
                "danses_apprises": {
                    "relation": [{"id": dance_id} for dance_id in cls.danses_apprises]
                },
                "danses_revisees": {
                    "relation": [{"id": dance_id} for dance_id in cls.danses_revisees]
                },
            },
        }
