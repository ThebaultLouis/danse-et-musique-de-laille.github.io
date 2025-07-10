import json
import os
from dotenv import load_dotenv
from .firestore_album import FirestoreAlbum
from .firestore_dance import FirestoreDance
from .firestore_classe import FirestoreClasse
from .firestore_event import FirestoreEvent

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


def firestore_events():
    data = read_firestore_backup()
    events: dict = data["__collections__"]["events"]
    return [FirestoreEvent.from_dict(event) for event in events.values()]


def firestore_albums():
    data = read_firestore_backup()
    albums: dict = data["__collections__"]["albums"]
    return [FirestoreAlbum.from_dict(album) for album in albums.values()]
