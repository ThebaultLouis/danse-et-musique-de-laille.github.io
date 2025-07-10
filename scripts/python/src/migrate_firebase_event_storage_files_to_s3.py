from firebase import firebase_collections
from s3_migration_client.client import S3MigrationClient

s3MigrationCLient = S3MigrationClient()


def migrate_firebase_event_storage_files_to_s3():
    object_keys = s3MigrationCLient.list_object_keys_in_folder("Agenda")
    for event in firebase_collections.firestore_events():
        if event.poster_s3_key not in object_keys:
            s3MigrationCLient.migrate_file(event.poster_pdf, event.poster_s3_key)
        if event.playlist_s3_key not in object_keys:
            s3MigrationCLient.migrate_file(event.playlist_pdf, event.playlist_s3_key)
        
if __name__ == "__main__":
    migrate_firebase_event_storage_files_to_s3()
