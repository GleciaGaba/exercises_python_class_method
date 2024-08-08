"""
Les méthodes de classe en Python sont des méthodes qui sont liées à la classe elle-même,
plutôt qu'à une instance spécifique de la classe. Elles peuvent être utilisées pour accéder
ou modifier des propriétés de la classe, ou pour implémenter des fonctionnalités qui sont
globales à la classe et ne dépendent pas de l'état des instances individuelles.

Caractéristiques des méthodes de classe

Utilisation du décorateur @classmethod : Pour définir une méthode de classe, on utilise le décorateur @classmethod.

Premier paramètre cls : Le premier paramètre d'une méthode de classe est conventionnellement nommé cls.

Il fait référence à la classe elle-même et permet d'accéder aux propriétés et méthodes de classe.

Définir une méthode de classe
Voici un exemple de définition et d'utilisation d'une méthode de classe :

python
Copier le code
class MaClasse:
    compteur = 0  # Variable de classe

    def __init__(self):
        MaClasse.compteur += 1

    @classmethod
    def nombre_instances(cls):
        return cls.compteur

# Création d'instances
instance1 = MaClasse()
instance2 = MaClasse()
instance3 = MaClasse()

# Appel de la méthode de classe
print(MaClasse.nombre_instances())  # Affiche : 3
Utilisations courantes des méthodes de classe
Accès aux variables de classe : Les méthodes de classe peuvent être utilisées pour accéder ou
modifier les variables de classe.
Constructeurs alternatifs : Les méthodes de classe peuvent être utilisées pour définir des
constructeurs alternatifs. Par exemple, vous pourriez vouloir créer des instances de la classe de différentes manières.
Exemple de constructeur alternatif
python
Copier le code
class Date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    @classmethod
    def de_chaine(cls, date_chaine):
        jour, mois, annee = map(int, date_chaine.split('-'))
        return cls(jour, mois, annee)

# Création d'une instance en utilisant le constructeur alternatif
date = Date.de_chaine("31-12-2024")
print(date.jour, date.mois, date.annee)  # Affiche : 31 12 2024
Dans cet exemple, la méthode de classe de_chaine permet de créer une instance de Date à
partir d'une chaîne de caractères formatée.

Différence avec les méthodes statiques
Les méthodes de classe ne doivent pas être confondues avec les méthodes statiques (@staticmethod).
Les méthodes statiques ne prennent ni self ni cls comme premier paramètre. Elles sont utilisées lorsque vous
n'avez pas besoin d'accéder à l'état de la classe ou de l'instance.

Exemple de méthode statique :

python
Copier le code
class MaClasse:
    @staticmethod
    def methode_statique(param1, param2):
        return param1 + param2

# Appel de la méthode statique
print(MaClasse.methode_statique(5, 10))  # Affiche : 15
En résumé, les méthodes de classe sont des outils puissants pour travailler avec des propriétés et
des fonctionnalités liées à la classe dans son ensemble, tandis que les méthodes statiques sont des
fonctions utilitaires qui n'interagissent ni avec la classe ni avec ses instances.



"""


class MaClasse:
    compteur = 0  # variable de classe

    def __init__(self):
        MaClasse.compteur +=1

    @classmethod
    def nombre_instances(cls):
        return cls.compteur

# Création d'instances

"""
1. Accès aux variables de classe: Les méthodes de classe peuvent être utilisées pour 
accéder ou modifier les variables de classe.

2. Constructeurs alternatifs: les méthodes de classe peuvent être utilisées pour définir des construteurs alternatifs.
Les méthodes de classe peuvent être utilisées pour définir des constructeurs alternatifs. Par exemple, vous pourriez
vouloir créer des instances de la classe de différents manières.

"""

class Date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    @classmethod
    def de_chaine(cls, date_chaine):
        jour, mois, annee = map(int, date_chaine.split("-"))
        return cls(jour, mois, annee)

    #  Création d'une instance en utilisant le constructeur alternatif

date = Date.de_chaine("31-12-2024")
print(date.jour, date.mois, date.annee)
# Affiche : 31 12 2024





