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
    notion_cours = notion_service.cours()
    notion_cours_keys = [cours.notion_key for cours in notion_cours]

    for classe in firebase_collections.firestore_classes():
        try:
            notion_cours = NotionCours.from_firestore_classe(
                firestore_classe=classe,
                danses_apprises=[
                    firestore_dance_id_to_notion_danse_id[classe.learnedDance]
                ] if classe.learnedDance != None else [],
                danses_revisees=[
                    firestore_dance_id_to_notion_danse_id[reviewedDanceId]
                    for reviewedDanceId in classe.reviewedDances
                ],
            )
            if notion_cours.notion_key in notion_cours_keys:
                continue
            notion_service.create_cours(notion_cours)
            print("✅ Added:", notion_cours.date, notion_cours.niveau)
            time.sleep(0.4)  # Notion API rate limit: ~3 requests/sec
            # return
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import_danse_dabatase_from_firebase_backup()
