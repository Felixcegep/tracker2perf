from enum import Enum


class Genre(Enum):  # Héritage correct de Enum
    HOMME = "homme"
    FEMME = "femme"
genre = "homme"
if genre in [g.value for g in Genre]:           
    print("oui")
