import os
import requests
from dotenv import load_dotenv
from firebase.firebase_collections import FirestoreDance

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DANSES_DATABASE_ID = os.getenv("NOTION_DANSES_DATABASE_ID")
NOTION_COURS_DATABASE_ID = os.getenv("NOTION_COURS_DATABASE_ID")

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}


def create_page(payload):
    url = "https://api.notion.com/v1/pages"
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code != 200:
        print("❌ Error:", response.status_code, response.text)
    return response.json()


def build_danse_properties(danse: FirestoreDance):
    return {
        "Nom": {"title": [{"text": {"content": danse.name}}]},
        "Lien de la musique": {"url": danse.song_link},
        "Lien de la chorégraphie": {"url": danse.video_link},
        "Pdf de la chorégraphie": {
            "files": [{"name": "Chorégraphie PDF", "external": {"url": danse.s3_file_url}}]
        },
    }


def create_danse(danse: FirestoreDance):
    payload = {
        "parent": {"database_id": NOTION_DANSES_DATABASE_ID},
        "properties": build_danse_properties(danse),
    }
    return create_page(payload)
