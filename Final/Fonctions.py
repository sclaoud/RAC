"""

Fichier des opérations entre les class et l'interface

"""

# Importation des modules

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

#   QMessageBox n'était pas importer depuis QtWidgets et doit être forcer ainsi que filedialog
from PyQt5.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl
from PyQt5 import QtCore, QtGui, QtWidgets
from classes import *
from TabGUI import *



class GUI(QtWidgets.QMainWindow, Ui_Application):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.lineFilm(self)


#### Fonctions ####
class operation:
    ### Enregistrement de l'entré et remise à zero des films ###  à retravailler
    def newFilm(self):
        film.nomFilm = GUI.lineFilm.text()
        film.dureeFilm = GUI.timeEdit.time()
        film.descFilm = ui.textDescFilm_2.toPlainText()

        model = ui.listCatFilm.model()
        cat_film_list = []
        for i, v in enumerate(ui.cbListCatFilm):
            item = model.item(i)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                print(i, v)
                cat_film_list.append(i)
        film.catFilm = cat_film_list

        # Efface les champs #
        ui.lineFilm_2.setText("")
        ui.dureeFilm.setTime(QtCore.QTime(00, 00))
        ui.textDescFilm_2.setText("")
        # Efface les checkbox #
        model = ui.listCatFilm.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)

        film_dict = {
            'Titre': film.nomFilm,
            'duree': film.dureeFilm,
            'description': film.descFilm,
            'categories': film.catFilm
        }

        film.listeFilm.append(film_dict)

        self.UpdateFilm()
        print(film.listeFilm)

    #        print (film.catFilm)
    #        print (film.nomFilm)
    #        print (film.dureeFilm)
    #        print (film.descFilm)

    ###Film suivant dans la liste de Film ### À retravailler
    def suivantFilm(self):
        print(self.positionFilm)
        print(self.listeFilm)
        ui.lineFilm_2.setText(self.listeFilm[self.positionFilm]['Titre'])
        ui.textDescFilm_2.setText(self.listeFilm[self.positionFilm]['description'])
        ui.dureeFilm.setTime(self.listeFilm[self.positionFilm]['duree'])
        self.cat_film_list = (self.listeFilm[self.positionFilm]['categories'])
        i = 0
        while self.model.item(i):
            item = self.model.item(i)
            if i in self.cat_film_list:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)
            i += 1

        self.positionFilm += 1

        if self.positionFilm == len(self.listeFilm):
            self.positionFilm = 0
        self.UpdateFilm()

        ###Film précédent dans la liste de film ### À retravailler

    def precedentFilm(self):
        print(self.positionFilm)
        ui.lineFilm_2.setText(self.listeFilm[self.positionFilm]['Titre'])
        ui.textDescFilm_2.setText(self.listeFilm[self.positionFilm]['description'])
        ui.dureeFilm.setTime(self.listeFilm[self.positionFilm]['duree'])
        self.cat_film_list = (self.listeFilm[self.positionFilm]['categories'])
        i = 0
        while self.model.item(i):
            item = self.model.item(i)
            if i in self.cat_film_list:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)
            i += 1

        self.positionFilm -= 1

        if self.positionFilm < 0:
            self.positionFilm = len(self.listeFilm) - 1
        self.UpdateFilm()

    ### choix bouton radio sexe
    def radio_button_clicked(self):
        Personne.sexe = ui.sexeBtnG.checkedButton().text()

        print(Personne.sexe)

    ### Met à jour le nombre de personne dans le système ### À retravailler
    def PersonneUpdate(self):
        ui.tabMain.setTabText(0, "Personne ({})".format(len(self.listePersonne)))

    ### Update de la liste des films
    def UpdateFilm(self):
        ui.tabMain.setTabText(1, "Film ({})".format(len(self.listeFilm)))

    ### Enregistrement de l'entré et remise à zero ### à retravailler
    def NewEntrie(self):
        Personne.prenom = self.linePrenom.text()
        Personne.nom = self.lineNom.text()
        Personne.sexe = self.mood_button_group.checkedId()
        Personne_test = {
            'prenom': Personne.prenom,
            'nom': Personne.nom,
            'sexe': Personne.sexe
        }

        self.listePersonne.append(Personne_test)

        ui.linePrenom.setText("")
        ui.lineNom.setText("")
        #        self.cbClient.setChecked(False)
        #       self.cbEmploye.setChecked(False)
        #        self.cbActeur.setChecked(False)
        ui.lineDateInsc.setText("")
        ui.lineCourriel.setText("")
        ui.linePwdClient.setText("")
        print(self.listePersonne)
        self.PersonneUpdate()

    ### Personne suivante dans la liste de Personne ### à retravailler
    def suivantPers(self):
        #        print(self.positionPers)
        print(self.listePersonne[self.positionPers]['sexe'])
        ui.linePrenom.setText(self.listePersonne[self.positionPers]['prenom'])
        ui.lineNom.setText(self.listePersonne[self.positionPers]['nom'])
        if self.listePersonne[self.positionPers]['sexe'] == 0:
            ui.sexeBtnG(0).setChecked(True)
        if self.listePersonne[self.positionPers]['sexe'] == 1:
            ui.sexeBtnG(1).setChecked(True)
        if self.listePersonne[self.positionPers]['sexe'] == 2:
            ui.sexeBtnG(2).setChecked(True)

        self.positionPers += 1

        if self.positionPers == len(self.listePersonne):
            self.positionPers = 0
        self.PersonneUpdate()

    ###Personne précédente dans la liste de Personne ### À retravailler
    def precedentPers(self):
        #        print(self.positionPers)
        print(self.listePersonne[self.positionPers]['prenom'])
        ui.linePrenom.setText(self.listePersonne[self.positionPers]['prenom'])
        ui.lineNom.setText(self.listePersonne[self.positionPers]['nom'])
        if self.listePersonne[self.positionPers]['sexe'] == 0:
            ui.sexeBtnG(0).setChecked(True)
        if self.listePersonne[self.positionPers]['sexe'] == 1:
            ui.sexeBtnG(1).setChecked(True)
        if self.listePersonne[self.positionPers]['sexe'] == 2:
            ui.sexeBtnG(2).setChecked(True)

        self.positionPers -= 1

        if self.positionPers < 0:
            self.positionPers = len(self.listePersonne) - 1
        self.PersonneUpdate()

    # Fenêtre de confirmation de la fermeture de l'application
    def closeEvent(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Êtes-vous sure de quitter?")
        msgBox.setWindowTitle("Message de fermeture")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #   Choix du message de fermeture
        res = msgBox.exec_()
        if res == QMessageBox.Ok:
            ui.sys.exit()
        if res == QMessageBox.Cancel:
            return True
        return False

    ### Sauvegarde à retravailler ###
    def sauvegarder(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    ### Chargement à retravailler ###
    def charger(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, "r")
        self.listdePersonne = file.load(file)
        file.close()
        self.Personne()
