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

    # Getters and Setters
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

    def set_sexe(self, sexe):
        self._sexe = sexe