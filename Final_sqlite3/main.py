"""

Fichier des opérations entre les class et l'interface

"""

# Importation des modules
import sqlite3
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlError
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QRegExpValidator, QStandardItemModel, QStandardItem
from PyQt5.QtCore import QRegExp, QDir
from PyQt5.Qt   import QColor
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QFileDialog, QTableWidgetItem, QAbstractItemView
import re
import pandas as pd


from TABUI import Ui_Application
from classes import *
from sql    import *


    # Fenêtre principale
class Window(Ui_Application, QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        con.open()

        #validation des lignes avec limitations textes/chiffres uniquements
        regexText = QRegExpValidator(QRegExp(r'^[a-zA-Z]*$'))
        self.lineNom.setValidator(regexText)
        self.linePrenom.setValidator(regexText)


        # Bouton pour ajouter une ranger dans la QtableCC
        self.btnAjoutCC.clicked.connect(self.AjoutCC)
        # Bouton pour supprimer une ranger dans la QtableCC
        self.btnSuppCC.clicked.connect(self.SuppCC)
        # Bouton pour ajouter une ranger dans la QtableChar
        self.btnAjoutPers.clicked.connect(self.AjoutPers)
        # Bouton pour supprimer une ranger dans la QtableChar
        self.btnSuppPers.clicked.connect(self.SuppPers)

        #test avec bouton modifier de film
        self.btnModFilm.clicked.connect(self.ModifFilm)

        #test avec le bouton modifier de personne
        self.btnModPers.clicked.connect(self.ModifPers)


        # Désactiver tant que la cb de la section désiré n'est pas coché
        self.dateEmb.setDisabled(True)
        self.lineUsername.setDisabled(True)
        self.linePwdEmp.setDisabled(True)
        self.comboAcces.setDisabled(True)
        self.QtableChar.setDisabled(True)
        self.btnAjoutCC.setDisabled(True)
        self.btnSuppCC.setDisabled(True)
        self.linePwdClient.setDisabled(True)
        self.dateInsc.setDisabled(True)
        self.lineCourriel.setDisabled(True)
        self.QtableCC.setDisabled(True)
        self.btnAjoutPers.setDisabled(True)
        self.btnSuppPers.setDisabled(True)


        # Echomode pour les Password
        self.linePwdClient.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.linePwdEmp.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)

        # Checkbox si la personne est artiste, active la section Artiste si coché
        self.cbActeur.toggled.connect(self.QtableChar.setEnabled)
        self.cbActeur.toggled.connect(self.btnSuppPers.setEnabled)
        self.cbActeur.toggled.connect(self.btnAjoutPers.setEnabled)
        # Checkbox si la personne est Client, active la section client si coché
        self.cbClient.toggled.connect(self.QtableCC.setEnabled)
        self.cbClient.toggled.connect(self.dateInsc.setEnabled)
        self.cbClient.toggled.connect(self.lineCourriel.setEnabled)
        self.cbClient.toggled.connect(self.linePwdClient.setEnabled)
        self.cbClient.toggled.connect(self.btnAjoutCC.setEnabled)
        self.cbClient.toggled.connect(self.btnSuppCC.setEnabled)
        # Checkbox si la personne est employé, active la section employé si coché
        self.cbEmploye.toggled.connect(self.dateEmb.setEnabled)
        self.cbEmploye.toggled.connect(self.lineUsername.setEnabled)
        self.cbEmploye.toggled.connect(self.linePwdEmp.setEnabled)
        self.cbEmploye.toggled.connect(self.comboAcces.setEnabled)

        # Ajustement de la fenêtre QtableCC
        header = self.QtableCC.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        # Ajustement de la fenêtre QtableChar
        header = self.QtableChar.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        #Liste temporaires des changements dans la fenêtre QtableCC
        self.changed_CC = []
        #Vérification des cellules dans QtableCC suite à l'écriture
        self.QtableCC.itemChanged.connect(self.log_changeCC)

        # Fonction de fermeture 'closeEvent' lorsque l'on appui sur le bouton
        self.btnFermer.clicked.connect(self.closeEvent)
        # Entré un nouveau film
        self.btnNvFilm.clicked.connect(self.newFilm)
        # Bouton précédent de la tab Films
        self.btnPrecedentFilm.clicked.connect(self.precedentFilm)
        # Bouton Suivant de la tab Films
        self.btnSuivantFilm.clicked.connect(self.suivantFilm)
        # Entré une nouvelle personne
        self.btnNvPers.clicked.connect(self.Validation)
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
        self.model = QStandardItemModel()
        # Liste des catégories de films (n'est pas iterable)
        self.cbListCatFilm = {"Animation", "Fantaisie", "Science-Fiction", "Horreur", "Drame",
                              "Thriller", "Documentaire", "Comédie"}
        for list in self.cbListCatFilm:
            item = QStandardItem(list)
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

        self.PersonneUpdate()

    #### Fonctions ####

    # Enregistrement de l'entré et remise à zero des films
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



    # Film suivant dans la liste de Film
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

    # Film précédent dans la liste de film

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


    # choix bouton radio sexe
    def radio_button_clicked(self):
        Personne.sexe = self.sexeBtnG.checkedButton().text()

        print(Personne.sexe)

    # Met à jour le nombre de personne dans le système
    def PersonneUpdate(self):
        position = QSqlQuery()
        position.exec_("select * from Personne")
        index = position.record().indexOf('id')
        self.tabMain.setTabText(0, "Personne ({})".format(position.value(index)))
        print(position.value(index))
        print (position.lastError().text())

    # Update de la liste des films
    def UpdateFilm(self):
        self.tabMain.setTabText(1, "Film ({})".format(len(Film.listeFilm)))

    # Bouton pour mettre à jour une personne (Présentement en test)
    def ModifPers(self):
        query = QSqlQuery()
        print (query.lastError().text())

    ### Enregistrement de l'entré et remise à zero ### à retravailler
    def Validation(self):
        Personne.prenom = self.linePrenom.text()
        Personne.nom = self.lineNom.text()
        Personne.sexe = self.sexeBtnG.checkedId()
        client.dateInsc = self.dateInsc.date()
        client.courriel = self.lineCourriel.text()
        client.clientPwd = self.linePwdClient.text()
        employe.dateEmb = self.dateEmb.date()
        employe.username = self.lineUsername.text()
        employe.empPWD = self.linePwdEmp.text()
        employe.acces = self.comboAcces.currentIndex()

        idq = QSqlQuery()
        idq.prepare(
            """
            INSERT INTO Personne (
                Prenom,
                Nom,
                Sexe
            )
            VALUES (?, ?, ?)
            """
        )
        idq.prepare(
            """
            INSERT INTO Client (
                DateInsc,
                Courriel,
                ClientPwd
            )
            VALUES (?, ?, ?)
            """
        )

        idq.addBindValue(Personne.prenom)
        idq.addBindValue(Personne.nom)
        idq.addBindValue(Personne.sexe)
        idq.addBindValue(client.dateInsc)
        idq.addBindValue(client.courriel)
        idq.addBindValue(client.clientPwd)
        idq.exec()



    ### Personne suivante dans la liste de Personne ###
    def suivantPers(self):
#        query = QSqlQuery('SELECT id, Prenom, Nom, Sexe FROM Personne')
#        query.next()
        query = QSqlQuery()
        query.exec_("select * from Personne")
        index = query.record().indexOf('id')
        query.next()
        print(query.value(index))
        Personne.prenom = query.value('Prenom')
        Personne.nom = query.value('Nom')
        Personne.sexe = query.value('Sexe')
        self.linePrenom.setText(Personne.prenom)
        self.lineNom.setText(Personne.nom)
        if Personne.sexe == -2:
            self.rbtnH.setChecked(True)
        if Personne.sexe == -3:
            self.rbtnF.setChecked(True)
        if Personne.sexe == -4:
            self.rbtnNA.setChecked(True)

        self.PersonneUpdate()

#        print(query.lastError().text())


    ###Personne précédente dans la liste de Personne ###
    def precedentPers(self):
        query = QSqlQuery()
        query.exec_("select * from Personne")
        index = query.record().indexOf('id')
        while query.previous():
            print(query.value(index))

    # Fenêtre de confirmation de la fermeture de l'application TODO : Message d'erreur à fix
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

    # Sauvegarde des données en excel avec Pandas
    def sauvegarder(self):
        print ("save")

    ### Chargement des données CSV TODO : à revoir
    def charger(self):
        print ("load")

    # Ajout d'une nouvelle rangée pour inscrire une nouvelle carte de crédit
    def AjoutCC(self):
        rowPosition = self.QtableCC.rowCount()
        self.QtableCC.insertRow(rowPosition)

    # Supprimer la rangée d'une carte de crédit
    def SuppCC(self):
        row = self.QtableCC.currentRow()
        self.QtableCC.removeRow(row)

    # Ajout d'une nouvelle rangée pour inscrire un nouveau personnage d'acteur
    def AjoutPers(self):
        rowPosition = self.QtableChar.rowCount()
        self.QtableChar.insertRow(rowPosition)

    # Supprimer la rangée d'un personnage d'acteur
    def SuppPers(self):
        row = self.QtableChar.currentRow()
        self.QtableChar.removeRow(row)

    def ModifFilm(self):
        print (Film.listeFilm.loc[Film.positionFilm])

#Inutilisé pour le moment
    def PopulateCC(self):
        spisok = cartedeCredits.listCC
        if spisok:
            row_count = (len(spisok))
            column_count = (len(spisok[0]))
            self.QtableCC.setColumnCount(column_count)
            self.QtableCC.setRowCount(row_count)
            self.QtableCC.setHorizontalHeaderLabels((list(spisok[0].keys())))
            for row in range(row_count):  # add items from array to QTableWidget
                for column in range(column_count):
                    item = (list(spisok[row].values())[column])
                    self.QtableCC.setItem(row, column, QTableWidgetItem(item))


    def log_changeCC(self, item):
        print("CC")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Application = QtWidgets.QDialog()
    win = Window()
    win.show()
    sys.exit(app.exec())
