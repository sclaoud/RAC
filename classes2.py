from PyQt5.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine

"""
Emplacement des classes

"""


class Personne(QObject):
    "Personne"

    def __init__(self, nom, prenom, sexe, parent=None):
        super().__init__(parent)
        self._nom = nom
        self._prenom = prenom
        self._sexe = sexe
        self._carteCredits = []

    @pyqtProperty(str)
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @pyqtProperty(str)
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, prenom):
        self._prenom = prenom

    @pyqtProperty(str)
    def sexe(self):
        return self._sexe

    @sexe.setter
    def sexe(self, sexe):
        self._sexe = sexe




class film (QObject):
    "Films"
    def __init__(self,nomFilm, dureeFilm, descFilm):
        self._nomFilm = nomFilm
        self._dureeFilm = dureeFilm
        self._descFilm = descFilm
        self._catFilm = []
        return

    @pyqtProperty(str)
    def nomFilm(self):
        return self._nomFilm

    @nomFilm.setter
    def nomFilm(self, nomFilm):
        self._nomFilm = nomFilm

    @pyqtProperty(int)
    def dureeFilm(self):
        return self._dureeFilm

    @dureeFilm.setter
    def dureeFilm(self, dureeFilm):
        self._dureeFilm = dureeFilm

    @pyqtProperty(str)
    def descFilm(self):
        return self._descFilm

    @descFilm.setter
    def descFilm(self, descFilm):
        self._descFilm = descFilm

    @pyqtProperty(str)
    def catFilm(self):
        return self._catFilm
    @catFilm.setter
    def catFilm(self,catFilm):
        self._catFilm = catFilm

