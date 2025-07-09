import time

from firebase import firebase_collections
from notion import notion_service
from notion.notion_danse import NotionDanse


def import_danse_dabatase_from_firebase_backup():
    notion_danses = notion_service.danses()
    notion_danse_noms = [notion_danse.nom for notion_danse in notion_danses]
    for firestore_dance in firebase_collections.firestore_dances():
        notion_danse = NotionDanse.from_firestore_dance(firestore_dance)
        if notion_danse.nom in notion_danse_noms:
            continue
        notion_service.create_danse(notion_danse)
        print("✅ Added:", notion_danse.name)
        time.sleep(0.4)  # Notion API rate limit: ~3 requests/sec
        # return


if __name__ == "__main__":
    import_danse_dabatase_from_firebase_backup()
