from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Portée pour lecture seule de Drive
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


def connect_to_drive():
    flow = InstalledAppFlow.from_client_secrets_file(
        "/home/thebault/projects/danse-et-musique-de-laille.github.io/scripts/credentials.json",
        SCOPES,
    )
    creds = flow.run_local_server(port=0)
    return build("drive", "v3", credentials=creds)


def get_public_urls(service, folder_id):
    query = (
        f"'{folder_id}' in parents and trashed = false and mimeType contains 'image/'"
    )
    results = (
        service.files()
        .list(q=query, fields="files(id, name, webViewLink, webContentLink)")
        .execute()
    )
    files = results.get("files", [])

    urls = []
    for file in files:
        # webContentLink = lien direct vers le fichier
        # webViewLink = lien vers l'interface Google Drive
        url = f"https://drive.google.com/uc?export=view&id={file['id']}"
        urls.append((file["name"], url))
    return urls


# Exemple d'utilisation
if __name__ == "__main__":
    folder_id = "1oFaRmhBUYtsAtsIo4N_bN73bRua3jDb4"
    service = connect_to_drive()
    image_urls = get_public_urls(service, folder_id)

    for name, url in image_urls:
        print(f"{name} : {url}")
