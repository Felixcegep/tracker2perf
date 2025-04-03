
class Aliment:
    def __init__(self,nom,calories,proteine):
        self.nom = nom
        self.calories = calories
        self.proteine = proteine

    @property
    def calories(self):
        return self._calories
    @calories.setter
    def calories(self, calories):
        if calories >= 0:

            self._calories = calories
        else:
            raise ValueError("les calories doivent être superieur a 0")
if __name__ == '__main__':
    Aliment("test", -99,30)