class Mouvement:
    def __init__(self, name, description, muscle,type):
        self.name = name
        self.description = description
        self.muscle = muscle
        self.type = type

    def __str__(self):
        return f"Mouvement: {self.name}, Type: {self.type}, Muscles: {', '.join(self.muscle)}"