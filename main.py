from ExerciceMusculation import ExerciceMusculation
from Seance import Seance
from datetime import datetime
from Journee import Journee
if __name__ == '__main__':
    datedeseance = datetime(2005, 2, 7)
    Journee("test", datedeseance)
    seance1 = Seance("test")
    exercice1 = ExerciceMusculation("test",1,1,1,5)
