import json
import os
from dotenv import load_dotenv

from firestore_dance import FirestoreDance, FirestoreClasse

load_dotenv()

FIRESTORE_BACKUP_FILE_PATH = os.getenv("FIRESTORE_BACKUP_FILE_PATH")


def read_firestore_backup():
    with open(FIRESTORE_BACKUP_FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def firestore_dances():
    data = read_firestore_backup()
    dances: dict = data["__collections__"]["dances"]
    return [FirestoreDance.from_dict(dance) for dance in dances.values()]


def firestore_classes():
    data = read_firestore_backup()
    classes: dict = data["__collections__"]["classes"]
    return [FirestoreClasse.from_dict(classe) for classe in classes.values()]
