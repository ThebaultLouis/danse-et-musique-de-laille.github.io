import os
from typing import List
from dotenv import load_dotenv
from firebase.firebase_dance import FirestoreDance
from firebase.firestore_classe import FirestoreClasse
from notion_client import Client
from notion.notion_danse import NotionDanse
from notion.notion_cours import NotionCours

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")

notion = Client(auth=NOTION_API_KEY)


def create_danse(firestore_dance: FirestoreDance):
    return notion.pages.create(
        **NotionDanse.from_firestore_dance(
            firestore_dance
        ).to_notion_client_create_page_body()
    )


def create_cours(notion_cours: NotionCours):
    return notion.pages.create(**notion_cours.to_notion_client_create_page_body())


def fetch_all_database_items(database_id):
    results = []
    has_more = True
    next_cursor = None

    while has_more:
        query = (
            {"database_id": database_id, "start_cursor": next_cursor}
            if next_cursor
            else {"database_id": database_id}
        )

        response = notion.databases.query(**query)
        results.extend(response["results"])
        has_more = response["has_more"]
        next_cursor = response.get("next_cursor")

    return results


def danses() -> List[NotionDanse]:
    fetch_all_database_items(NotionDanse.database_id())


def cours() -> List[NotionCours]:
    fetch_all_database_items(NotionCours.database_id())
