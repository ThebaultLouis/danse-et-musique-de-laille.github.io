import time

from firebase import firebase_collections
from scripts.python.src.notion import notion_service


def import_danse_dabatase_from_firebase_backup():
    for dance in firebase_collections.firestore_dances():
        notion_service.create_danse(dance)
        print("✅ Added:", dance.name)
        time.sleep(0.4)  # Notion API rate limit: ~3 requests/sec
        return


if __name__ == "__main__":
    import_danse_dabatase_from_firebase_backup()
