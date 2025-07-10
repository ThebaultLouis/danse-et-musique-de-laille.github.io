from concurrent.futures import ThreadPoolExecutor
from firebase import firebase_collections
from s3_migration_client.client import S3MigrationClient

s3MigrationCLient = S3MigrationClient()


def migrate_firebase_album_storage_files_to_s3():
    photo_to_url = []
    object_keys = s3MigrationCLient.list_object_keys_in_folder("Albums photos")
    for album in firebase_collections.firestore_albums():
        for index, photo in enumerate(album.photos):
            s3_key = f"{album.s3_key_prefix}/{index:02}"
            if s3_key not in object_keys:
                photo_to_url.append((photo, s3_key))
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(lambda p: s3MigrationCLient.migrate_file(*p), photo_to_url)

if __name__ == "__main__":
    migrate_firebase_album_storage_files_to_s3()
