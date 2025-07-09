from typing import List
from dataclasses import dataclass
from dataclasses import dataclass
from enum import Enum


class FirestoreClasseLevel(str, Enum):
    UNDEFINED = "UNDEFINED"
    BEGINNER = "BEGINNER"
    NOVICE = "NOVICE"
    INTERMEDIATE = "INTERMEDIATE"


@dataclass
class FirestoreClasse:
    level: FirestoreClasseLevel
    reviewedDances: List[str]
    learnedDance: str
    doneOn: str
    id: str

    @classmethod
    def from_dict(cls, classe: dict) -> "FirestoreClasse":
        level = FirestoreClasseLevel(
            classe.get("level", FirestoreClasseLevel.UNDEFINED)
        )
        reviewedDances = classe.get("reviewedDances", None)
        learnedDance = classe.get("learnedDance", None)
        doneOn = classe.get("doneOn", None)

        return cls(level, reviewedDances, learnedDance, doneOn)
