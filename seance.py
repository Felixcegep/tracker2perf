class Seance:
    nbseancetotal = 0
    def __init__(self, nom):
        self.nom = nom
        self.exercice_seaces = []
        Seance.nbseancetotal += 1

    def afficher_exercices(self):
        for exercice in self.exercice_seaces:
            print(exercice.nomexercice)

    def ajouterExercice(self, exercice):
        self.exercice_seaces.append(exercice)






