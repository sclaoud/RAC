"""

Fichier des opérations entre les class et l'interface

"""

# Importation des modules
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QRadioButton, QButtonGroup, QDialog

from TabGUI import Ui_Application
from classes import *


class Window(Ui_Application, QDialog):
    def __init__(self):
        QDialog.__init__((self))
        self.setupUi(self)

        # Désactiver tant que la cb de la bonne section n'est pas coché
        self.linePwdClient.setDisabled(True)
        self.dateEdit_2.setDisabled(True)
        self.lineCourriel.setDisabled(True)
        self.dateEdit.setDisabled(True)
        self.lineUsername.setDisabled(True)
        self.linePwdEmp.setDisabled(True)
        self.comboBox.setDisabled(True)
        self.listChar.setDisabled(True)
        self.tableView.setDisabled(True)
        self.btnGestionCC.setDisabled(True)
        self.btnGestionPers.setDisabled(True)

        # Display characters as they are entered while editing otherwise display characters as with Password.
        self.linePwdClient.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.linePwdEmp.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)

        # Checkbox si la personne est artiste, active la section Artiste si coché
        self.cbActeur.toggled.connect(self.listChar.setEnabled)
        self.cbActeur.toggled.connect(self.btnGestionPers.setEnabled)
        # Checkbox si la personne est Client, active la section client si coché
        self.cbClient.toggled.connect(self.tableView.setEnabled)
        self.cbClient.toggled.connect(self.dateEdit_2.setEnabled)
        self.cbClient.toggled.connect(self.lineCourriel.setEnabled)
        self.cbClient.toggled.connect(self.linePwdClient.setEnabled)
        self.cbClient.toggled.connect(self.btnGestionCC.setEnabled)
        # Checkbox si la personne est employé, active la section employé si coché
        self.cbEmploye.toggled.connect(self.dateEdit.setEnabled)
        self.cbEmploye.toggled.connect(self.lineUsername.setEnabled)
        self.cbEmploye.toggled.connect(self.linePwdEmp.setEnabled)
        self.cbEmploye.toggled.connect(self.comboBox.setEnabled)

        # Fonction de fermeture 'closeEvent' lorsque l'on appui sur le bouton
        self.btnFermer.clicked.connect(self.closeEvent)
        # Entré un nouveau film
        self.btnNouveau_3.clicked.connect(self.newFilm)
        # Bouton précédent de la tab Films
        self.btnPrecedent_2.clicked.connect(self.precedentFilm)
        # Bouton Suivant de la tab Films
        self.btnSuivant_2.clicked.connect(self.suivantFilm)
        # Entré une nouvelle personne
        self.btnNouveau.clicked.connect(self.NewEntrie)
        # Bouton Précédent de la tab Personne
        self.btnPrecedent.clicked.connect(self.precedentPers)
        # Bouton Suivant de la tab Personne
        self.btnSuivant.clicked.connect(self.suivantPers)

        # Maximum de 40 Caracteres pour le nom et prenom
        self.linePrenom.setMaxLength(40)
        self.lineNom.setMaxLength(40)

        # RadioButton du choix de sexe de la personne
        sexe = [QRadioButton("Homme"), QRadioButton("Femme"), QRadioButton("Préfère ne pas répondre")]
        # Création du groupe de boutton pour les Qradiobtn
        self.sexeBtnG = QButtonGroup(self.horizontalLayoutWidget)
        for i in range(len(sexe)):
            # Add each radio button to the button layout
            self.horizontalLayout_2.addWidget(sexe[i])
            # Add each radio button to the button group & give it an ID of i
            self.sexeBtnG.addButton(sexe[i], i)
            # Connect each radio button to a method to run when it's clicked
            self.sexeBtnG.buttonClicked.connect(self.radio_button_clicked)

        self.model = QtGui.QStandardItemModel()
        # Liste des catégories de films (n'est pas iterable)
        self.cbListCatFilm = {"Animation", "Fantaisie", "Science-Fiction", "Horreur", "Drame",
                              "Thriller", "Documentaire", "Comédie"}
        for list in self.cbListCatFilm:
            item = QtGui.QStandardItem(list)
            item.setCheckable(True)
            self.model.appendRow(item)
        self.listCatFilm.setModel(self.model)

        # Remplissage du champ Titre
        self.lineFilm_2.setText("Titre du film")
        # Remplissage du champ Synopsis
        self.textDescFilm_2.setText('Inscrire la synopsie du film')
        # Bouton de sauvegarde des données
        self.btnSauvegarder.clicked.connect(self.sauvegarder)
        # Bouton de chargement des données
        self.btnCharger_2.clicked.connect(self.charger)

    #### Fonctions ####

    ### Enregistrement de l'entré et remise à zero des films ###  à retravailler
    def newFilm(self):
        film.nomFilm = self.lineFilm_2.text()
        film.dureeFilm = self.timeEdit.time()
        film.descFilm = self.textDescFilm_2.toPlainText()

        model = self.listCatFilm.model()
        cat_film_list = []
        for i, v in enumerate(self.cbListCatFilm):
            item = model.item(i)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                print(i, v)
                cat_film_list.append(i)
        film.catFilm = cat_film_list

        # Efface les champs #
        self.lineFilm_2.setText("")
        self.timeEdit.setTime(QtCore.QTime(00, 00))
        self.textDescFilm_2.setText("")
        # Efface les checkbox #
        model = self.listCatFilm.model()
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
        print(film.positionFilm)
        print(film.listeFilm)
        self.lineFilm_2.setText(film.listeFilm[film.positionFilm]['Titre'])
        self.textDescFilm_2.setText(film.listeFilm[film.positionFilm]['description'])
        self.dureeFilm.setTime(film.listeFilm[film.positionFilm]['duree'])
        self.cat_film_list = (film.listeFilm[film.positionFilm]['categories'])
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
        print(film.positionFilm)
        self.lineFilm_2.setText(film.listeFilm[film.positionFilm]['Titre'])
        self.textDescFilm_2.setText(film.listeFilm[film.positionFilm]['description'])
        self.dureeFilm.setTime(film.listeFilm[film.positionFilm]['duree'])
        self.cat_film_list = (film.listeFilm[film.positionFilm]['categories'])
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
        Personne.sexe = self.sexeBtnG.checkedButton().text()

        print(Personne.sexe)

    ### Met à jour le nombre de personne dans le système ### À retravailler
    def PersonneUpdate(self):
        self.tabMain.setTabText(0, "Personne ({})".format(len(Personne.listePersonne)))

    ### Update de la liste des films
    def UpdateFilm(self):
        self.tabMain.setTabText(1, "Film ({})".format(len(self.listeFilm)))

    ### Enregistrement de l'entré et remise à zero ### à retravailler
    def NewEntrie(self):
        Personne.prenom = self.linePrenom.text()
        Personne.nom = self.lineNom.text()
        Personne.sexe = self.sexeBtnG.checkedId()
        Personne_test = {
            'prenom': Personne.prenom,
            'nom': Personne.nom,
            'sexe': Personne.sexe
        }

        Personne.listePersonne.append(Personne_test)

        self.linePrenom.setText("")
        self.lineNom.setText("")
        #        self.cbClient.setChecked(False)
        #       self.cbEmploye.setChecked(False)
        #        self.cbActeur.setChecked(False)
        self.dateEdit_2.setDate(QtCore.QDate(2021, 1, 1))
        self.lineCourriel.setText("")
        self.linePwdClient.setText("")
        print(Personne.listePersonne)
        self.PersonneUpdate()

    ### Personne suivante dans la liste de Personne ### à retravailler
    def suivantPers(self):
        #        print(self.positionPers)
        print(Personne.listePersonne[Personne.positionPers]['sexe'])
        self.linePrenom.setText(Personne.listePersonne[Personne.positionPers]['prenom'])
        self.lineNom.setText(Personne.listePersonne[Personne.positionPers]['nom'])
        if Personne.listePersonne[Personne.positionPers]['sexe'] == 0:
            self.sexeBtnG(0).setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['sexe'] == 1:
            self.sexeBtnG(1).setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['sexe'] == 2:
            self.sexeBtnG(2).setChecked(True)

        Personne.positionPers += 1

        if Personne.positionPers == len(Personne.listePersonne):
            Personne.positionPers = 0
        self.PersonneUpdate()

    ###Personne précédente dans la liste de Personne ### À retravailler
    def precedentPers(self):
        #        print(self.positionPers)
        print(Personne.listePersonne[Personne.positionPers]['prenom'])
        self.linePrenom.setText(Personne.listePersonne[Personne.positionPers]['prenom'])
        self.lineNom.setText(Personne.listePersonne[Personne.positionPers]['nom'])
        if Personne.listePersonne[Personne.positionPers]['sexe'] == 0:
            self.sexeBtnG(0).setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['sexe'] == 1:
            self.sexeBtnG(1).setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['sexe'] == 2:
            self.sexeBtnG(2).setChecked(True)

        Personne.positionPers -= 1

        if Personne.positionPers < 0:
            Personne.positionPers = len(Personne.listePersonne) - 1
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
            sys.exit()
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


# if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    Application = QtWidgets.QDialog()
#    ui = Ui_Application()
#    ui.setupUi(Application)
#    Application.show()
#    sys.exit(app.exec_())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Application = QtWidgets.QDialog()
    win = Window()
    win.show()
    sys.exit(app.exec())
