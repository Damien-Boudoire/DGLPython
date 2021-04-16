from job01 import Personne

class Auteur(Personne):

    def __init__(self, prenom="", nom=""):
        super().__init__(prenom, nom)
        self.oeuvre = []

    def listerOeuvre(self):
        for livre in self.oeuvre:
            livre.print()

    def ecrireUnLivre(self, titre):
        if not self.estIlLAuteur(titre):
            self.oeuvre.append(Livre(titre, self))

    def estIlLAuteur(self, titre):
        for livre in self.oeuvre:
            if livre.titre == titre:
                return True
        return False

class Livre:

    def __init__(self, titre="", auteur=Auteur()):
        self.titre = titre
        self.auteur = auteur

    def getTitre(self):
        return self.titre

    def setTitre(self, titre):
        self.titre = titre

    def getAuteur(self):
        return self.auteur

    def setAuteur(self, auteur):
        self.auteur = auteur

    def print(self):
        print(self.titre)


pkDick = Auteur("Philip K.", "Dick")
pkDick.ecrireUnLivre("Le maître du haut château")
pkDick.ecrireUnLivre("Ubik")
pkDick.ecrireUnLivre("Blade Runner")

iAsimov = Auteur("Isaac", "Asimov")
iAsimov.ecrireUnLivre("Fondation")
iAsimov.ecrireUnLivre("Le cycle des robots")

rBradburry = Auteur("Ray", "Bradbury")
rBradburry.ecrireUnLivre("Chroniques martiennes")
rBradburry.ecrireUnLivre("Fahrenheit 451")

AUTEURS = [pkDick, iAsimov, rBradburry]
TITRES =["Le maître du haut château", "Ubik",
         "Blade Runner", "Fondation", "Le cycle des robots",
         "Chroniques martiennes", "Fahrenheit 451"]


def test1():
    for auteur in AUTEURS:
        auteur.SePresenter()
        auteur.listerOeuvre()
        print("")

#test1()