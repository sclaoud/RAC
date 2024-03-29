
"""
Emplacement des classes

"""

# class personne avec informations de bases
class Personne(object):

    listePersonne = []
    positionPers = 0
    pdict = {}

    def __init__(self, prenom, nom, sexe, parent=None):
        super().__init__(parent)
        self._prenom = prenom
        self._nom = nom
        self._sexe = sexe

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, prenom):
        self._prenom = prenom

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def sexe(self):
        return self._sexe

    @sexe.setter
    def sexe(self, sexe):
        self._sexe = sexe


class client (Personne):

    def __init__(self, dateInsc, courriel, clientPwd, prenom, nom, sexe):
        super().__init__(prenom, nom, sexe)
        self._dateInsc = dateInsc
        self._courriel = courriel
        self._clientPwd = clientPwd
        return

    @property
    def dateInsc(self):
        return self._dateInsc

    @dateInsc.setter
    def dateInsc(self, dateInsc):
        self._dateInsc = dateInsc

    @property
    def courriel(self):
        return self._courriel

    @courriel.setter
    def courriel(self, courriel):
        self._courriel = courriel

    @property
    def clientPwd(self):
        return self._clientPwd

    @clientPwd.setter
    def clientPwd(self, clientPwd):
        self._clientPwd = clientPwd


class cartedeCredits (client):

    listCC = []
    CCposition = 0
    CC = {}

    def __init__(self, numeroCC, dateCC, codeCC, dateInsc, courriel, clientPwd, prenom, nom, sexe):
        super().__init__(dateInsc, courriel, clientPwd, prenom, nom, sexe)
        self._numeroCC = numeroCC
        self._dateCC = dateCC
        self._codeCC = codeCC
        return

    @property
    def numeroCC(self):
        return self._numeroCC

    @numeroCC.setter
    def numeroCC(self, numeroCC):
        self._numeroCC = numeroCC

    @property
    def dateCC(self):
        return self._dateCC

    @dateCC.setter
    def dateCC(self, dateCC):
        self._dateCC = dateCC

    @property
    def codeCC(self):
        return self._codeCC

    @codeCC.setter
    def codeCC(self, codeCC):
        self._codeCC = codeCC


# class des acteurs, enfant de personne
class acteurs (Personne):

    listeActeurs = [{
            'TitreFilm': 'titreFilm',
            'Personnage': 'personnage',
            'dateDebut': 'debutEmploi',
            'dateFin': 'finEmploi',
            'cachet': 'cachet',
            }]

    def __init__(self, titreFilm, personnage, debutEmploi, finEmploi, cachet, prenom, nom, sexe):
        super().__init__(prenom, nom, sexe)
        self._titreFilm = titreFilm
        self._personnage = personnage
        self._debutEmploi = debutEmploi
        self._finEmploi = finEmploi
        self._cachet = cachet
        return

    @property
    def titreFilm(self):
        return self._titreFilm

    @titreFilm.setter
    def titreFilm(self, titreFilm):
        self._titreFilm = titreFilm

    @property
    def personnage(self):
        return self._personnage

    @personnage.setter
    def personnage(self, personnage):
        self._personnage = personnage

    @property
    def debutEmploi(self):
        return self._debutEmploi

    @debutEmploi.setter
    def debutEmploi(self, debutEmploi):
        self._debutEmploi = debutEmploi

    @property
    def finEmploi(self):
        return self._finEmploi

    @finEmploi.setter
    def finEmploi(self, finEmploi):
        self._finEmploi = finEmploi

    @property
    def cachet(self):
        return self._cachet

    @cachet.setter
    def cachet(self, cachet):
        self._cachet = cachet


class employe (Personne):

    def __init__(self, dateEmb, username, empPwd, acces, prenom, nom, sexe):
        super().__init__(prenom, nom, sexe)
        self._dateEmb = dateEmb
        self._username = username
        self._empPwd = empPwd
        self._acces = acces
        return

    @property
    def dateEmb(self):
        return self._dateEmb

    @dateEmb.setter
    def dateEmb(self, dateEmb):
        self._dateEmb = dateEmb

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def empPWD(self):
        return self._empPwd

    @empPWD.setter
    def empPWD(self, empPwd):
        self._empPwd = empPwd

    @property
    def acces(self):
        return self._acces

    @acces.setter
    def acces(self, acces):
        self._acces = acces


# class contenant les informations sur les films
class Film(object):

    positionFilm = 0
    listeFilm = []

    def __init__(self, nomFilm, dureeFilm, descFilm, catFilm):
        self._nomFilm = nomFilm
        self._dureeFilm = dureeFilm
        self._descFilm = descFilm
        self._catFilm = catFilm
        return

    @property
    def nomFilm(self):
        return self._nomFilm

    @nomFilm.setter
    def nomFilm(self, SnomFilm):
        self._nomFilm = SnomFilm

    @nomFilm.deleter
    def nomFilm(self):
        del self._nomFilm

    @property
    def dureeFilm(self):
        return self._dureeFilm

    @dureeFilm.setter
    def dureeFilm(self, dureeFilm):
        self._dureeFilm = dureeFilm

    @property
    def descFilm(self):
        return self._descFilm

    @descFilm.setter
    def descFilm(self, descFilm):
        self._descFilm = descFilm

    @property
    def catFilm(self):
        return self._catFilm

    @catFilm.setter
    def catFilm(self, catFilm):
        self._catFilm = catFilm
