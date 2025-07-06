import json
import os
import requests
import sys
import time
from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DANSES_DATABASE_ID = os.getenv("NOTION_DANSES_DATABASE_ID")
NOTION_COURS_DATABASE_ID = os.getenv("NOTION_COURS_DATABASE_ID")
FIRESTORE_BACKUP_FILE_PATH=os.getenv("FIRESTORE_BACKUP_FILE_PATH")

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

def build_properties(dance: dict):
      name: str = dance.get("name", "")
      name = name.strip()
      song_link: str = dance.get("songLink", "")
      video_link: str = dance.get("choreographyVideo", "")
      pdf_link: str = dance.get("choreographyPdf", "")
      return {
          "Nom": {
              "title": [{"text": {"content": name}}]
          },
          "Lien de la musique": {
              "url": song_link
          },
          "Lien de la chorégraphie": {
              "url": video_link
          },
          "Pdf de la chorégraphie": {
              "files": [
                 {
                    "name": "Chorégraphie PDF",
                    "external": {
                        "url": pdf_link
                    }
                 }
              ]
          }
      }

def import_danse_dabatase_from_firebase_backup():
    with open(FIRESTORE_BACKUP_FILE_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    dances : dict = data["__collections__"]["dances"] 

    for dance in list(dances.values())[:1]:
        payload = {
            "parent": {"database_id": NOTION_DANSES_DATABASE_ID},
            "properties": build_properties(dance)
        }
        result = create_page(payload)
        print("✅ Added:", dance.get("name"))
        time.sleep(0.4)  # Notion API rate limit: ~3 requests/sec

if __name__ == "__main__":
    import_danse_dabatase_from_firebase_backup()