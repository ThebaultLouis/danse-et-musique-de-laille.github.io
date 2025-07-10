from firebase import firebase_collections
from s3_migration_client.client import S3MigrationClient

s3MigrationCLient = S3MigrationClient()


def migrate_firebase_dance_storage_files_to_s3():
    object_keys = s3MigrationCLient.list_object_keys_in_folder("Danses")
    for dance in firebase_collections.firestore_dances():
        if dance.s3_key not in object_keys:
            s3MigrationCLient.migrate_file(dance.pdf_link, dance.s3_key)

if __name__ == "__main__":
    migrate_firebase_dance_storage_files_to_s3()
