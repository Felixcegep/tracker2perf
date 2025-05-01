# pour 100 grams



#Todo : tu vas devoir faire un des super donc fait des calorie d'aliments
class TemplateAliment:
    def __init__(self,nom,calories,proteines):
        self.nom = nom
        self.calories = calories
        self.proteines = proteines

    @property
    def calories(self):
        return self._calories
    @calories.setter
    def calories(self, calories):
        if calories >= 0:
            self._calories = calories
        else:
            raise ValueError("Les calories doivent être superieur a 0")

    @property
    def proteines(self):
        return self._proteines
    @proteines.setter
    def proteines(self, proteines):
        if proteines >= 0:
            self._proteines = proteines
        else:
            raise ValueError("Les protéines doivent être superieures a 0")