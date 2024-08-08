"""
La méthode __str__ en Python est une méthode spéciale utilisée pour définir la
représentation en chaîne de caractères d'une instance d'une classe.
Cette méthode est appelée par les fonctions intégrées str() et
print() pour obtenir une version lisible et conviviale de l'objet.

"""


class Voiture:
    def __init__(self, marque, vitesse):
        self.marque = marque
        self.vitesse = vitesse

    def __str__(self):
        return f"Voiture de marque {self.marque} avec vitesse maximale de {self.vitesse}"


porsche = Voiture("Porsche", 200)
print(porsche)
