class Utilisateur:
    nombre_utilisateur = 0
    def __init__(self, nom : str,taille: int, age: int, poid:float):
        self.nom = nom
        self.taille = taille
        self.age = age
        self.poid = poid
        self.pr = {

        }
        Utilisateur.nombre_utilisateur += 1




    @classmethod
    def afficher_total_utilisateur(cls):
        print(cls.nombre_utilisateur)

    def __str__(self):
        return f"Nom : {self.nom}\ntaille : {self.taille}\nage:  {self.age} \npoid: {self.poid} lbs"

if __name__ == '__main__':
    test = Utilisateur("test", 199, 99, 1000)
    test1 = Utilisateur("test", 199, 99, 1000)