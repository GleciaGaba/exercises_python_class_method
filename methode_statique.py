class Voiture:
    voiture_crees = 0

    def __init__(self, marque, vitesse, prix):
        Voiture.voiture_crees += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    @classmethod
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=250, prix=200000)

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=300, prix=180000)

    @staticmethod
    def afficher_nombre_voitures():
        print(f"Vous avez {Voiture.voiture_crees} voitures dans votre garage.")
        """
        Le décorateur @staticmethod en Python est utilisé pour définir des méthodes statiques 
        dans une classe. Contrairement aux méthodes d'instance et aux méthodes de classe, 
        une méthode statique n'a pas accès à l'instance (self) ni à la classe (cls). 
        Cela en fait une méthode utile pour regrouper une fonction utilitaire avec une classe, 
        même si cette fonction ne nécessite ni l'instance ni la classe.
        """


lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
