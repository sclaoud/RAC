from PyQt5.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine

"""
Emplacement des classes

"""


class Personne(object):
    "Personne"

    def __init__(self,prenom, nom, sexe, parent=None):
        super().__init__(parent)
        self._prenom = prenom
        self._nom = nom
        self._sexe = sexe

#    nom = property(fget=nom.getter, fset=nomFilm.setter, fdel=nomFilm.deleter)
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


class film(object):
    "Films"

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

    @pyqtProperty(list)
    def catFilm(self):
        return self._catFilm

    @catFilm.setter
    def catFilm(self, catFilm):
        self._catFilm = catFilm



