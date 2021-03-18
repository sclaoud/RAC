"""

Fichier des opérations entre les class et l'interface

"""

# Importation des modules
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog

from Acteurs import Ui_Acteurs
from CartedeCredits import Ui_UI_CC
from TabGUI import Ui_Application
from classes import *

    # Fenêtre de gestions des cartes de crédits
class WindowCC(Ui_UI_CC, QDialog):
    def __init__(self):
        QDialog.__init__((self))
        self.setupUi(self)

        #bouton pour cacher la fenêtre
        self.btnCloseCC.clicked.connect(self.hide)

    # Fenêtre de gestions des personnages des acteurs
class WindowActeurs(Ui_Acteurs, QDialog):
    def __init__(self):
        QDialog.__init__((self))
        self.setupUi(self)

        #bouton pour cacher la fenêtre
        self.btnCloseActeur.clicked.connect(self.hide)


    # Fenêtre principale
class Window(Ui_Application, QDialog):
    def __init__(self):
        QDialog.__init__((self))
        self.setupUi(self)

        # Bouton pour modifier les cartes de crédits
        self.btnGestionCC.clicked.connect(self.ouvrirCC)
        # Bouton pour modifier les personnages des acteurs
        self.btnGestionPers.clicked.connect(self.ouvrirActeurs)

        # Désactiver tant que la cb de la section désiré n'est pas coché
        self.linePwdClient.setDisabled(True)
        self.dateInsc.setDisabled(True)
        self.lineCourriel.setDisabled(True)
        self.dateEmb.setDisabled(True)
        self.lineUsername.setDisabled(True)
        self.linePwdEmp.setDisabled(True)
        self.comboAcces.setDisabled(True)
        self.listCharView.setDisabled(True)
        self.listCCview.setDisabled(True)
        self.btnGestionCC.setDisabled(True)
        self.btnGestionPers.setDisabled(True)

        # Echomode pour les Password
        self.linePwdClient.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.linePwdEmp.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)

        # Checkbox si la personne est artiste, active la section Artiste si coché
        self.cbActeur.toggled.connect(self.listCharView.setEnabled)
        self.cbActeur.toggled.connect(self.btnGestionPers.setEnabled)
        # Checkbox si la personne est Client, active la section client si coché
        self.cbClient.toggled.connect(self.listCCview.setEnabled)
        self.cbClient.toggled.connect(self.dateInsc.setEnabled)
        self.cbClient.toggled.connect(self.lineCourriel.setEnabled)
        self.cbClient.toggled.connect(self.linePwdClient.setEnabled)
        self.cbClient.toggled.connect(self.btnGestionCC.setEnabled)
        # Checkbox si la personne est employé, active la section employé si coché
        self.cbEmploye.toggled.connect(self.dateEmb.setEnabled)
        self.cbEmploye.toggled.connect(self.lineUsername.setEnabled)
        self.cbEmploye.toggled.connect(self.linePwdEmp.setEnabled)
        self.cbEmploye.toggled.connect(self.comboAcces.setEnabled)

        # Fonction de fermeture 'closeEvent' lorsque l'on appui sur le bouton
        self.btnFermer.clicked.connect(self.closeEvent)
        # Entré un nouveau film
        self.btnNvFilm.clicked.connect(self.newFilm)
        # Bouton précédent de la tab Films
        self.btnPrecedentFilm.clicked.connect(self.precedentFilm)
        # Bouton Suivant de la tab Films
        self.btnSuivantFilm.clicked.connect(self.suivantFilm)
        # Entré une nouvelle personne
        self.btnNvPers.clicked.connect(self.NewEntrie)
        # Bouton Précédent de la tab Personne
        self.btnPrecedent.clicked.connect(self.precedentPers)
        # Bouton Suivant de la tab Personne
        self.btnSuivant.clicked.connect(self.suivantPers)

        # Maximum de 40 Caracteres pour le nom et prenom
        self.linePrenom.setMaxLength(40)
        self.lineNom.setMaxLength(40)

        # Liste des choix du combobox comboAcces pour les employés
        self.listedesAcces = {"Consultant", "employé", "sécurité", "administrateur", "Direction"}
        self.comboAcces.addItems(self.listedesAcces)

        # QlisteView de la liste des catégories de films
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
        self.TitreFilm.setText("Titre du film")
        # Remplissage du champ Synopsis
        self.textDescFilm.setText('Inscrire la synopsie du film')
        # Bouton de sauvegarde des données
        self.btnSauvegarder.clicked.connect(self.sauvegarder)
        # Bouton de chargement des données
        self.btnCharger.clicked.connect(self.charger)


    #### Fonctions ####

    ### Enregistrement de l'entré et remise à zero des films ###  à retravailler
    def newFilm(self):
        Film.nomFilm = self.TitreFilm.text()
        Film.dureeFilm = self.dureeFilm.time()
        Film.descFilm = self.textDescFilm.toPlainText()

        model = self.listCatFilm.model()
        cat_film_list = []
        for i, v in enumerate(self.cbListCatFilm):
            item = model.item(i)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                print(i, v)
                cat_film_list.append(i)
        Film.catFilm = cat_film_list

        # Efface les champs #
        self.TitreFilm.setText("")
        self.dureeFilm.setTime(QtCore.QTime(00, 00))
        self.textDescFilm.setText("")
        # Efface les checkbox #
        model = self.listCatFilm.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)

        film_dict = {
            'Titre': Film.nomFilm,
            'duree': Film.dureeFilm,
            'description': Film.descFilm,
            'categories': Film.catFilm
        }

        Film.listeFilm.append(film_dict)

        self.UpdateFilm()
        print(Film.listeFilm)

    #        print (film.catFilm)
    #        print (film.nomFilm)
    #        print (film.dureeFilm)
    #        print (film.descFilm)

    ###Film suivant dans la liste de Film ### À retravailler
    def suivantFilm(self):
        print(Film.positionFilm)
        print(Film.listeFilm)
        self.TitreFilm.setText(Film.listeFilm[Film.positionFilm]['Titre'])
        self.textDescFilm.setText(Film.listeFilm[Film.positionFilm]['description'])
        self.dureeFilm.setTime(Film.listeFilm[Film.positionFilm]['duree'])
        self.cat_film_list = (Film.listeFilm[Film.positionFilm]['categories'])
        i = 0
        while self.model.item(i):
            item = self.model.item(i)
            if i in self.cat_film_list:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)
            i += 1

        Film.positionFilm += 1

        if Film.positionFilm == len(Film.listeFilm):
            Film.positionFilm = 0
        self.UpdateFilm()

    ###Film précédent dans la liste de film ### À retravailler

    def precedentFilm(self):
        print(Film.positionFilm)
        self.TitreFilm.setText(Film.listeFilm[Film.positionFilm]['Titre'])
        self.textDescFilm.setText(Film.listeFilm[Film.positionFilm]['description'])
        self.dureeFilm.setTime(Film.listeFilm[Film.positionFilm]['duree'])
        self.cat_film_list = (Film.listeFilm[Film.positionFilm]['categories'])
        i = 0
        while self.model.item(i):
            item = self.model.item(i)
            if i in self.cat_film_list:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)
            i += 1

        Film.positionFilm -= 1

        if Film.positionFilm < 0:
            Film.positionFilm = len(Film.listeFilm) - 1
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
        self.tabMain.setTabText(1, "Film ({})".format(len(Film.listeFilm)))

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
        self.dateInsc.setDate(QtCore.QDate(2021, 1, 1))
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
        if Personne.listePersonne[Personne.positionPers]['sexe'] == -2:
            self.rbtnH.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['sexe'] == -3:
            self.rbtnF.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['sexe'] == -4:
            self.rbtnNA.setChecked(True)

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
        if Personne.listePersonne[Personne.positionPers]['sexe'] == -2:
            self.rbtnH.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['sexe'] == -3:
            self.rbtnF.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['sexe'] == -4:
            self.rbtnNA.setChecked(True)

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
        name, filter = QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)")
        file = open(name, 'w')
        text = Personne.listePersonne.toPlainText()
        file.write(text)
        file.close()

    ### Chargement à retravailler ###
    def charger(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, "r")
        self.listdePersonne = file.load(file)
        file.close()
        self.PersonneUpdate()

    ### ouvrir la fenêtre de modification des cartes de crédits
    def ouvrirCC(self):
        FenetreCC = WindowCC()
        FenetreCC.exec_()

    ### ouvrir la fenêtre de modification des cartes de crédits
    def ouvrirActeurs(self):
        FenetreActeurs = WindowActeurs()
        FenetreActeurs.exec_()

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
