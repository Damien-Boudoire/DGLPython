class Personne :
    def __init__(self, prenom="", nom=""):
        self.prenom = prenom
        self.nom = nom

    def SePresenter(self):
        print(self.prenom+" "+self.nom)

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom



def test():
    persos = [ ("Jonathan", "Joestar"),
      ("Joseph", "Joestar"),
      ("Jotaro", "Kujo"),
      ("Dio", "Brando"),
      ("Robert","Speedwagon"),
      ("Jean-Pierre", "Polnareff")
      ]

    personnes = []

    for perso in persos:
        personnes.append(Personne(perso[0], perso[1]))

    for personne in personnes:
        personne.SePresenter()

#test()