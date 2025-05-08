import json
import os
import yaml

firestore_backup_file_path="/home/thebault/projects/dml-backup/backup.json"
danses_output_dir = "src/content/danses"
cours_output_dir = "src/content/cours"

def sanitize_dance_name(name: str) -> str:
    sanitized_name = name.strip().replace(" ", "-").replace("\"", "").replace("'", "").replace("’", "").lower()
    if (sanitized_name[0].isdigit()):
         sanitized_name = "0." + sanitized_name
    return sanitized_name

def generate_dance_yaml_files():
  with open(firestore_backup_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

  os.makedirs(danses_output_dir, exist_ok=True)

  # Accès aux données
  dances:dict = data["__collections__"]["dances"] 

  for dance_id, dance_data in list(dances.items()):
      name: str = dance_data.get("name", "")
      name = name.strip()
      song_link: str = dance_data.get("songLink", "")
      video_link: str = dance_data.get("choreographyVideo", "")
      pdf_link: str = dance_data.get("choreographyPdf", "")

      yaml_data = {
          "nom": name,
          "lien_musique": song_link,
          "lien_video_choregraphie": video_link if video_link != None and video_link.startswith("http") else None,
          "lien_pdf_choregraphie": pdf_link
      }
      sanitized_name = sanitize_dance_name(name)
      file_name = f"{sanitized_name}.yml"

      output_path = os.path.join(danses_output_dir, file_name)
      with open(output_path, "w", encoding="utf-8") as out_file:
          yaml.dump(yaml_data, out_file, allow_unicode=True, default_flow_style=False,)

      print(f"✅ Fichier généré : {output_path}")


niveau_map = {
    "BEGINNER": "Débutant",
    "NOVICE": "Novice",
    "INTERMEDIATE": "Intermédiaire",
}

def generate_cours_yaml_files():
  with open(firestore_backup_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

  os.makedirs(danses_output_dir, exist_ok=True)

  # Accès aux données
  dances:dict = data["__collections__"]["dances"]
  dance_name_by_dance_id = {}
  classes:dict = data["__collections__"]["classes"]

  for dance_id, dance_data in list(dances.items()):
      name: str = dance_data.get("name", "")
      sanitized_name = sanitize_dance_name(name)
      dance_name_by_dance_id[dance_id] = sanitized_name
  
  for course_id, cours in list(classes.items()):
    print(course_id)
    niveau = niveau_map.get(cours.get("level", ""), cours.get("level"))
    reviewed = cours.get("reviewedDances", [])
    learned = [cours.get("learnedDance")]
    doneOn = cours.get("doneOn")

    danses_apprises = [f"danses/{dance_name_by_dance_id.get(dance_id)}" for dance_id in learned]
    danses_revisees = [f"danses/{dance_name_by_dance_id.get(dance_id)}" for dance_id in reviewed]

    yaml_data = {
        "niveau": niveau,
        "danses_apprises": danses_apprises,
        "danses_revisees": danses_revisees,
        "date_realisation": doneOn
    }

    file_name = f"{doneOn}-{sanitize_dance_name(niveau)}.yml"

    output_path = os.path.join(cours_output_dir, file_name)
    with open(output_path, "w", encoding="utf-8") as out_file:
        yaml.dump(yaml_data, out_file, allow_unicode=True, default_flow_style=False,)

    print(f"✅ Fichier généré : {output_path}")

generate_dance_yaml_files()
generate_cours_yaml_files()

