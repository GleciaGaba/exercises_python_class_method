
projets = ["pr_GameOfThrones", "HarryPotter", "pr_Avengers"]


class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"

    def afficher_projets(self):
        for projet in projets:
            print(projet)


class Junior(Utilisateur):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)

"""

super() -> 

La fonction super() en Python est utilisée pour appeler une méthode de la classe parente
(ou superclasse) dans une classe dérivée (ou sous-classe). Cela est particulièrement utile
dans le contexte de l'héritage, où une classe enfant souhaite étendre ou modifier le
comportement d'une méthode héritée de sa classe parent.

"""

paul = Junior("Paul", "Durand")
paul.afficher_projets()
