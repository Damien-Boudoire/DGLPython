from job02_718 import Livre, Auteur, AUTEURS, TITRES
from job01 import Personne

import random

class Client(Personne):
    def __init__(self, prenom = "", nom = ""):
        super().__init__(prenom, nom)
        self.collection = []

    def ajout_livre(self, livre : Livre):
        for element in self.collection:
            if element.getTitre() == livre.getTitre():
                return
        self.collection.append(livre)

    def retrait_livre(self, titre : str):
        for livre in self.collection:
            if livre.getTitre() == titre:
                self.collection.remove(livre)
                return livre

    def possedes(self):
        titres = []
        for livre in self.collection:
            titres.append(livre.getTitre())
        return titres

    def inventaire(self):
        for livre in self.collection:
            livre.print()


class Bibliotheque:
    def __init__(self, nom = ""):
        self.nom = nom
        self.catalogue = []

    def getNom(self):
        return self.nom

    def setNom(self, nom : str):
        self.nom = nom

    def acheterLivre(self, titre : str, auteur : Auteur, quantite : int):
        if not auteur.estIlLAuteur(titre):
            return
        if quantite <= 0:
            return

        for oeuvre in self.catalogue:
            if oeuvre["livre"].getTitre() == titre:
                oeuvre["stock"] += quantite
                return
        self.catalogue.append({"livre" : Livre(titre, auteur), "stock" : quantite})

    def inventaire(self):
        for entree in self.catalogue:
            print(entree["livre"].getTitre(), entree["stock"])

    def louer(self, client : Client, titre : str):
        for entree in self.catalogue:
            if entree["livre"].getTitre() == titre:
                if entree["stock"] == 1:
                    self.catalogue.remove(entree)
                else:
                    entree["stock"] -= 1
                client.ajout_livre(entree["livre"])

    def rendreLivres(self, client : Client):
        for titre in client.possedes():
            livre = client.retrait_livre(titre)
            self.acheterLivre(livre.getTitre(), livre.getAuteur(), 1)

def test():
    bonnevaine = Bibliotheque("Médiathèque Bonneveine")
    pabloNeruda = Bibliotheque("Médiathèque Pablo Neruda")
    alcazar = Bibliotheque("Bibliothèque de l'Alcazar")

    for titre in TITRES:
        for auteur in AUTEURS:
            if auteur.estIlLAuteur(titre):
                bonnevaine.acheterLivre(titre, auteur, random.randint(0,10))
                pabloNeruda.acheterLivre(titre, auteur, random.randint(0,10))
                alcazar.acheterLivre(titre, auteur, random.randint(0,10))

    print("inventaire " + bonnevaine.getNom())
    bonnevaine.inventaire()
    print("inventaire " + pabloNeruda.getNom())
    pabloNeruda.inventaire()
    print("inventaire " + alcazar.getNom())
    alcazar.inventaire()

    print("---------------")

    print("les clients viennent chercher des livres")

    clients = []
    for i in range(0, 20):
        clients.append(Client(chr(random.randint(97, 97 + 26 - 1)),
                              chr(random.randint(97, 97 + 26 - 1))))



    for client in clients:
        client.SePresenter()
        for titre in TITRES:
            for auteur in AUTEURS:
                if auteur.estIlLAuteur(titre):
                    if(random.randint(0,99) >= 10):
                        randBibli = random.randint(0,99)
                        if randBibli < 33:
                            bonnevaine.louer(client, titre)
                        elif randBibli < 66:
                            pabloNeruda.louer(client, titre)
                        else:
                            alcazar.louer(client, titre)

    print("---------------")


    print("inventaire " + bonnevaine.getNom())
    bonnevaine.inventaire()
    print("inventaire " + pabloNeruda.getNom())
    pabloNeruda.inventaire()
    print("inventaire " + alcazar.getNom())
    alcazar.inventaire()

    print("---------------")
    print("livres possédé par chaque client:")

    for client in clients:
        client.SePresenter()
        client.inventaire()
        print("###")
        randBibli = random.randint(0, 99)
        if randBibli < 33:
            bonnevaine.rendreLivres(client)
        elif randBibli < 66:
            pabloNeruda.rendreLivres(client)
        else:
            alcazar.rendreLivres(client)

    print("inventaire " + bonnevaine.getNom())
    bonnevaine.inventaire()
    print("inventaire " + pabloNeruda.getNom())
    pabloNeruda.inventaire()
    print("inventaire " + alcazar.getNom())
    alcazar.inventaire()


test()