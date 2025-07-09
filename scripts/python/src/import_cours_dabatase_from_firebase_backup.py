import time

from firebase import firebase_collections
from notion import notion_service
from notion.notion_cours import NotionCours


def get_firestore_dance_id_to_notion_danse_id():
    firestore_dances = firebase_collections.firestore_dances()
    notion_danses = notion_service.danses()
    notion_danses_by_nom = {
        notion_danse.nom: notion_danse for notion_danse in notion_danses
    }
    firestore_dance_id_to_notion_danse_id = {
        firestore_dance.id: notion_danses_by_nom[firestore_dance.name].id
        for firestore_dance in firestore_dances
    }
    return firestore_dance_id_to_notion_danse_id


def import_danse_dabatase_from_firebase_backup():
    firestore_dance_id_to_notion_danse_id = get_firestore_dance_id_to_notion_danse_id()

    for classe in firebase_collections.firestore_classes():
        notion_cours = NotionCours.from_firestore_classe(
            firestore_classe=classe,
            danses_apprises=[
                firestore_dance_id_to_notion_danse_id[classe.learnedDance]
            ],
            danses_revisees=[
                firestore_dance_id_to_notion_danse_id[reviewedDanceId]
                for reviewedDanceId in classe.reviewedDances
            ],
        )
        notion_service.create_cours(notion_cours)
        print("✅ Added:", notion_cours.date, notion_cours.niveau)
        time.sleep(0.4)  # Notion API rate limit: ~3 requests/sec
        return


if __name__ == "__main__":
    import_danse_dabatase_from_firebase_backup()
