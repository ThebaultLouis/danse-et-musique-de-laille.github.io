import json
import os
import yaml

firestore_backup_file_path="/home/thebault/projects/dml-backup/backup.json"
output_dir = "src/content/danses"

def generate_dance_yaml_files():
  with open(firestore_backup_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

  os.makedirs(output_dir, exist_ok=True)

  # Accès aux données
  dances:dict = data["__collections__"]["dances"] 

  for dance_id, dance_data in list(dances.items()):
      name: str = dance_data.get("name", "")
      song_link: str = dance_data.get("songLink", "")
      video_link: str = dance_data.get("choreographyVideo", "")
      pdf_link: str = dance_data.get("choreographyPdf", "")

      yaml_data = {
          "nom": name,
          "lien_musique": song_link,
          "lien_video_choregraphie": video_link if video_link != None and video_link.startswith("http") else None,
          "lien_pdf_choregraphie": pdf_link
      }

      sanitized_name = name.replace(" ", "-").replace("\"", "").replace("'", "").replace("’", "").lower()
      if (sanitized_name[0].isdigit()):
         sanitized_name = "0." + sanitized_name
      file_name = f"{sanitized_name}.yml"

      output_path = os.path.join(output_dir, file_name)
      with open(output_path, "w", encoding="utf-8") as out_file:
          yaml.dump(yaml_data, out_file, allow_unicode=True, default_flow_style=False,)

      print(f"✅ Fichier généré : {output_path}")

generate_dance_yaml_files()

