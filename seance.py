from idlelib.colorizer import prog_group_name_to_tag

from exercice import Exercice


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


if __name__ == '__main__':
    Exercice1 = Exercice("bench", 5,5,50 )
    Exercice2 = Exercice("dips", 5, 5, 50)
    seance1 = Seance("push")
    seance1.ajouterExercice(Exercice1)
    seance1.ajouterExercice(Exercice2)
    seance1.afficher_exercices()



