class Exercice:

    exercicedisponible = ["bench", "squat", "deadlift"]
    def __init__(self, nomexercice,set : str , rep : str,poid: int,temps: int = None):
        self.nomexercice = nomexercice
        self.rep = rep
        self.set = set
        self.poid = poid
        self.temps = temps
    # TODO: FAIRE UNE CLASS SPÉCIAL POUR LES CLASSES CARDIO SPÉCIALISER POUR UTILISER SUPER()_INIT__





    def __str__(self):
        return f"{self.nomexercice} rep {self.rep} poid {self.poid} temps {self.temps}"

