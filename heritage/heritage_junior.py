import heritage_utilisateur


class Junior(heritage_utilisateur.Utilisateur):
    def __init__(self, nom, prenom):
        heritage_utilisateur.Utilisateur.__init__(self, nom, prenom)


glecia = Junior("Glecia", "MAINDRON")
print(glecia)
