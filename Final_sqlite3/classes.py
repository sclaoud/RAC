
"""
Emplacement des classes

"""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

# Info de l'usager qui se connecte à la BD
class user(object):

    def __init__(self, login, pwd, acces):
        self._login = login
        self._pwd = pwd
        self._acces = acces

    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, login):
        self._login = login

    @property
    def pwd(self):
        return self._pwd
    @pwd.setter
    def pwd(self, pwd):
        self._pwd = pwd

    @property
    def acces(self):
        return self._acces
    @acces.setter
    def acces(self, acces):
        self._acces = acces


# class personne avec informations de bases
class Personne(object):

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


# class comprenant les informations des clients
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


# class pour les informations des employes, enfant de Personne
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

    categories = []

    def __init__(self, nomFilm, dureeFilm, descFilm, categories):
        self._nomFilm = nomFilm
        self._dureeFilm = dureeFilm
        self._descFilm = descFilm
        self._categories = categories
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