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

    @property
    def notion_key(cls):
        return f"{cls.date}-{cls.niveau}"
    
    @staticmethod
    def database_id():
        return NOTION_COURS_DATABASE_ID

    @staticmethod
    def from_firestore_classe(
        firestore_classe: FirestoreClasse,
        danses_apprises: List[str],
        danses_revisees: List[str],
        type="Country",
    ) -> "NotionCours":
        return NotionCours(
            date=firestore_classe.doneOn,
            niveau=FirestoreClasseLevel_NotionCoursNiveau[firestore_classe.level],
            type=type,
            danses_apprises=danses_apprises,
            danses_revisees=danses_revisees,
        )

    def to_notion_client_create_page_body(cls):
        return {
            "Date": {"title": [{"text": {"content": cls.date}}]},
            "Type": {"select": {"name": cls.type}},
            "Niveau": {"select": {"name": cls.niveau}},
            "Danses apprises": {
                "relation": [{"id": dance_id} for dance_id in cls.danses_apprises]
            },
            "Danses révisées": {
                "relation": [{"id": dance_id} for dance_id in cls.danses_revisees]
            },
        }
    
    @staticmethod
    def from_notion_page(page: dict) -> "NotionCours":
        properties = page["properties"]
    
        date = properties["Date"]["title"][0]["text"]["content"]
        type_ = properties["Type"]["select"]["name"]
        niveau = NotionCoursNiveau(properties["Niveau"]["select"]["name"])

        danses_apprises = [rel["id"] for rel in properties["Danses apprises"]["relation"]]
        danses_revisees = [rel["id"] for rel in properties["Danses révisées"]["relation"]]

        return NotionCours(
            date=date,
            type=type_,
            niveau=niveau,
            danses_apprises=danses_apprises,
            danses_revisees=danses_revisees,
        )
