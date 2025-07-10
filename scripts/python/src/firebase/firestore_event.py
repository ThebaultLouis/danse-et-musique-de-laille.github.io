from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class FirestoreEvent:
    is_at_home: bool
    city: str
    zipcode: str
    poster_pdf: str
    done_on: date
    club: str
    id: str
    playlist_pdf: Optional[str]

    @staticmethod
    def from_dict(data: dict) -> "FirestoreEvent":
        return FirestoreEvent(
            is_at_home=data.get("isAtHome", False),
            city=data.get("city", None),
            zipcode=data.get("zipcode", None),
            poster_pdf=data.get("posterPdf", None),
            done_on=data.get("doneOn", None),
            club=data.get("club", None),
            id=data.get("id", None),
            playlist_pdf=data.get("playlistPdf", None)
        )
    
    @property
    def s3_prefix_key(self):
        return f"{self.done_on}/{self.club}"
    
    @property
    def poster_s3_key(self):
        if self.poster_pdf is None:
            return None
            
        extension = "jpeg"
        if "poster.png" in self.poster_pdf:
          extension = "png"
        return f"Agenda/{self.s3_prefix_key}/Poster.{extension}"

    @property
    def playlist_s3_key(self):
        return f"Agenda/{self.s3_prefix_key}/Playlist.pdf"

