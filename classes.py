class Personne:
    "Personne"
    def __init__(self, nom, prenom, sexe):
        self._nom = nom
        self._prenom = prenom
        self._sexe = sexe
        self._carteCredits = []

#Getters and Setters
    def get_CarteCredits(self):
        return self._carteCredits
    def get_nom(self):
        return self._nom
    def get_prenom(self):
        return self._prenom
    def get_sexe(self):
        return self._sexe
    def set_nom(self, nom):
        self._nom = nom
    def set_prenom(self, prenom):
        self._prenom = prenom
#Méthodes
    def ajouterCarteCredit(self, carteCredit):
        self._carteCredits.append(carteCredit)
    def __str__(self):
        return "Le prénom est {}, le nom est {}, le sexe est {}".format(self._prenom, self._nom, self._sexe)


class Client(Personne):
    "client"
    def __init__(self, dateInsc, courriel, pwdClient):
        self._dateInsc = dateInsc
        self._courriel = courriel
        self._pwdClient = pwdClient
        return

#getter setter
    def getdateInsc(self):
        return self._dateInsc
    def getcourriel(self):
        return self._courriel
    def getpwdClient(self):
        return self._pwdClient

    def set_dateInscr(self):
        return self._dateInsc
    def set_courriel(self):
        return self._courriel
    def set_pwdClient(self):
        return self._pwdClient

class acteur(Personne):
    "acteur"
    def __init__(self, nomChar, debutJob, finJob, cachet):
        self._nomchar = nomChar
        self._debutJob = debutJob
        self._finJob = finJob
        self._cachet = cachet
        return

#getter setter
    def get_nomChar(self):
        return self._nomchar
    def get_debutJob(self):
        return self._debutJob
    def get_finJob(self):
        return self._finJob
    def get_cachet(self):
        return self._cachet

    def set_nomchar(self):
        return self._nomchar
    def set_debutJob(self):
        return self._debutJob
    def set_finJob(self):
        return self._finJob
    def set_cachet(self):
        return self._cachet

class employe(Personne):
    "Employés"
    def __init__(self, dateEmb, username, pwdEmp, access):
        self._dateEmb = dateEmb
        self._username = username
        self._pwdEmp = pwdEmp
        self._access = access
        return

#getter setter
    def get_dateEmp(self):
        return self._dateEmb
    def get_username(self):
        return self._username
    def get_pwdEmp(self):
        return self._pwdEmp
    def get_access(self):
        return self._access

    def set_dateEmb(self):
        return self._dateEmb
    def set_username(self):
        return self._username
    def set_pwdEmp(self):
        return self._pwdEmp
    def set_access(self):
        return self._access

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


class film:
    "Films"
    def __init__(self,nomFilm, dureeFilm, descFilm):
        self._nomFilm = nomFilm
        self._dureeFilm = dureeFilm
        self._descFilm = descFilm
        return

#getter setter
    def get_nomFilm(self):
        return
