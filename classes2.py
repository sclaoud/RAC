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


class film(QObject):
    "Films"

    def __init__(self, _nomFilm, _dureeFilm, _descFilm, catFilm):
        self._nomFilm = nomFilm
        self._dureeFilm = pyqtProperty(int, self.dureeFilm, fset=self.get_dureeFilm)
        self._descFilm = pyqtProperty(str, self.descFilm)
        self._catFilm = catFilm.append



#    @property(fget=nomFilm, fset=set_nomFilm)
#    def nomFilm(self):
#        return self._nomFilm

    #nomFilm.setter
    def set_nomFilm(self, SnomFilm):
        self.nomFilm = SnomFilm

    #nomFilm.getter
    def get_nomFilm(self, nomFilm):
        self._nomFilm = nomFilm

    nomFilm = property(fget=get_nomFilm, fset=set_nomFilm)

    return

#    @pyqtProperty(str)
#    def nomFilm(self):
#        return self._nomFilm
#    @nomFilm.setter
#    def nomFilm(self, SnomFilm):
#        self._nomFilm = SnomFilm



    @property
    def dureeFilm(self):
        return self._dureeFilm

    @dureeFilm.setter
    def dureeFilm(self, dureeFilm):
        self._dureeFilm = dureeFilm

#    @dureeFilm.getter
#    def get_dureeFilm(self, dureeFilm):
#        self._dureeFilm = dureeFilm

    @property
    def descFilm(self):
        return self._descFilm

    @descFilm.setter
    def descFilm(self, descFilm):
        self._descFilm = descFilm

    @pyqtProperty(list)
    def catFilm(self):
        return self._catfilm

    @catFilm.setter
    def catfilm(self, catFilm):
        self._catFilm = catFilm



