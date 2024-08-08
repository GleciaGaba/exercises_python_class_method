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


paul = Utilisateur("Paul", "Durand")
paul.afficher_projets()
print(paul)
