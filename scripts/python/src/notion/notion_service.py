import os
from typing import List
from dotenv import load_dotenv
from notion_client import Client
from notion_client.helpers import collect_paginated_api
from firebase.firestore_dance import FirestoreDance
from .notion_danse import NotionDanse
from .notion_cours import NotionCours

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")

notion = Client(auth=NOTION_API_KEY)


def create_danse(firestore_dance: FirestoreDance):
    notion_danse = NotionDanse.from_firestore_dance(firestore_dance)
    return notion.pages.create(
        parent={"database_id": notion_danse.database_id()},
        properties=notion_danse.to_notion_client_create_page_body(),
    )


def create_cours(notion_cours: NotionCours):
    return notion.pages.create(
        parent={"database_id": notion_cours.database_id()},
        properties=notion_cours.to_notion_client_create_page_body(),
    )


def danses() -> List[NotionDanse]:
    return [
        NotionDanse.from_notion_page(page)
        for page in collect_paginated_api(
            notion.databases.query, database_id=NotionDanse.database_id()
        )
    ]


def cours() -> List[NotionCours]:
    return collect_paginated_api(
        notion.databases.query, database_id=NotionCours.database_id()
    )
