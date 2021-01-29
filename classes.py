class Personne:
    "Personne"
    def __init__(self, nom, prenom, nas):
        self._nom = nom
        self._prenom = prenom
        self._nas = nas
        self._carteCredits = []

#Getters and Setters
    def getCarteCredits(self):
        return self._carteCredits
    def getNom(self):
        return self._nom
    def getPrenom(self):
        return self._prenom
    def getNas(self):
        return self._nas
    def setNom(self, nom):
        self._nom = nom
    def setPrenom(self, prenom):
        self._prenom = prenom
#Méthodes
    def ajouterCarteCredit(self, carteCredit):
        self._carteCredits.append(carteCredit)
    def __str__(self):
        return "Le prénom est {}, le nom est {}, le nas est {}".format(self._prenom, self._nom, self._nas)


class CarteCredit:
    def __init__(self, numero, compagnie):
        self._numero = numero
        self._compagnie = compagnie
    #Getters and Setters
    def getNumero(self):
        return self._numero
    def getCompagnie(self):
        return self._compagnie
    def setNumero(self, numero):
        if len(numero == 16):
            self._numero = numero
    def __str__(self):
        return "Le numero est {} et la compagnie est {}".format(self._numero, self._compagnie)


