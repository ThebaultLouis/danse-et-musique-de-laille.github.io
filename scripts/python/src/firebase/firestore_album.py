from dataclasses import dataclass
from typing import List

@dataclass
class FirestoreAlbum:
    name: str
    done_on: str
    photos: List[str]
    id: str

    @staticmethod
    def from_dict(data: dict) -> "FirestoreAlbum":
        return FirestoreAlbum(
            name=data.get("name", None),
            done_on=data.get("doneOn", None),
            photos=data.get("photos", []),
            id=data.get("id", None)
        )
    
    @property
    def s3_key_prefix(self):
        return f"Albums photos/{self.done_on.replace('/', '-')} {self.name}"
