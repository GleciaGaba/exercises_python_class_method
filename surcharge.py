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

    def afficher_projets(self):
        for projet in projets:
            if not projet.startswith("pr_"):
                print(projet)
"""
La méthode afficher_projets dans la classe Junior va écraser celle qui a été créée 
dans la classe parente Utilisateur, car elle a été modifiée dans la classe Junior. 
En effet, la méthode dans la classe Junior a priorité sur celle dans la classe parente.


La surcharge est un concept courant dans la programmation orientée objet, 
où plusieurs méthodes dans la même classe (ou dans des classes parentes et enfants) 
portent le même nom mais diffèrent par leurs paramètres ou leur comportement. 
 
"""

paul = Junior("Paul", "Durand")
paul.afficher_projets()
