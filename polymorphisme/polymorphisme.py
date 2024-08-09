"""
Le polymorphisme est un concept fondamental de la programmation orientée objet (POO)
qui permet aux objets de différentes classes d'être traités de manière interchangeable,
à condition qu'ils partagent une interface commune. Le polymorphisme permet d'utiliser
une seule interface pour représenter différents types d'objets, ce qui rend le code plus
flexible et extensible.

"""


class Vehicule:
    def avance(self):
        print("Le véhicule démarre")


class Voiture(Vehicule):
    def avance(self):  # def roule(self): à la place de roule, on doit utiliser avance(self)
        super().avance()
        print("La voiture roule")


class Avion(Vehicule):
    def avance(self):  # def vol(self): à la place de vol, on doit utiliser avance(self)
        super().avance()
        print("L'avion vol")


v = Voiture()
a = Avion()

v.avance()
a.avance()
