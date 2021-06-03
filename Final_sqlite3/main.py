"""

Fichier des opérations entre les class et l'interface

"""

# Importation des modules
import sqlite3
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlError
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QRegExpValidator, QStandardItemModel, QStandardItem
from PyQt5.QtCore import QRegExp, QDir, Qt, QDate
from PyQt5.QtWidgets import QListView
from PyQt5.Qt   import QColor
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QFileDialog, QTableWidgetItem, QAbstractItemView, QTableView
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

        # Bouton pour ajouter une ranger dans la QtableAct
        self.btnAjoutPers.clicked.connect(self.AjoutPers)
        # Bouton pour supprimer une ranger dans la QtableAct
        self.btnSuppPers.clicked.connect(self.SuppPers)

        #test avec bouton modifier de film
        self.btnModFilm.clicked.connect(self.ModifFilm)

        #test avec le bouton modifier de personne
        self.btnModPers.clicked.connect(self.ModifPers)


        # Désactiver tant que la cb de la section désiré n'est pas coché
        self.dateEmb.setDisabled(True)
        self.QtableCC.setDisabled(True)
        self.lineUsername.setDisabled(True)
        self.linePwdEmp.setDisabled(True)
        self.comboAcces.setDisabled(True)
        self.QtableAct.setDisabled(True)
        self.btnAjoutCC.setDisabled(True)
        self.btnSuppCC.setDisabled(True)
        self.linePwdClient.setDisabled(True)
        self.dateInsc.setDisabled(True)
        self.lineCourriel.setDisabled(True)
        self.btnAjoutPers.setDisabled(True)
        self.btnSuppPers.setDisabled(True)


        # Echomode pour les Password
        self.linePwdClient.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.linePwdEmp.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)

        # Checkbox si la personne est artiste, active la section Artiste si coché
        self.cbActeur.toggled.connect(self.QtableAct.setEnabled)
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



        # Fonction de fermeture 'closeEvent' lorsque l'on appui sur le bouton
        self.btnFermer.clicked.connect(self.closeEvent)
        # Entré un nouveau film
        self.btnNvFilm.clicked.connect(self.newFilm)
        # Entré une nouvelle personne
        self.btnNvPers.clicked.connect(self.Validation)

        # Maximum de 40 Caracteres pour le nom et prenom
        self.linePrenom.setMaxLength(40)
        self.lineNom.setMaxLength(40)

        # Liste des choix du combobox comboAcces pour les employés
        self.listedesAcces = {"Consultant", "employé", "sécurité", "administrateur", "Direction"}
        self.comboAcces.addItems(self.listedesAcces)

        # QlisteView de la liste des catégories de films
        self.model = QStandardItemModel()
        listquery = QSqlQuery("SELECT name FROM PRAGMA_TABLE_INFO('CatFilm')")
#        query.exec_("PRAGMA table_info('CatFilm')")
#        list = query.value('name')
#        list = listquery.value()
#        print (listquery.value(0))
        self.cbListCatFilm = {"bob"}
        # Liste des catégories de films (n'est pas iterable)
        for list in self.cbListCatFilm:
            item = QStandardItem(list)
            item.setCheckable(True)
            self.model.appendRow(item)
        self.listCatFilm.setModel(self.model)

        # Model pour La table CartedeCredit
        self.modelcc = QSqlTableModel(self)
        self.modelcc.setTable("CartedeCredits")
        self.modelcc.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.modelcc.select()
        # Set up the view
        self.QtableCC.setModel(self.modelcc)
        self.QtableCC.resizeColumnsToContents()

        # Model pour La table Acteurs
        self.modelact = QSqlTableModel(self)
        self.modelact.setTable("Acteurs")
        self.modelact.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.modelact.select()
        # Set up the view
        self.QtableAct.setModel(self.modelact)
        self.QtableAct.resizeColumnsToContents()

        # Remplir la liste des ID et des champs au besoin
        self.comboboxID()
        #Si sélection d'un contenu de la comboboxID
        self.comboID.currentIndexChanged.connect(self.PersonneUpdate)

        self.UpdateFilm()

    #### Fonctions ####

    def comboboxID(self):
        listid = []
        self.comboID.clear() #Supprimer les items présent et éviter la duplication
        idquery = QSqlQuery("SELECT id  FROM Personne")
        while idquery.next():
            listid.append(str(idquery.value('id')))
        self.comboID.addItems(listid)
        self.PersonneUpdate()


    # Enregistrement de l'entré et remise à zero des films
    def newFilm(self):
        Film.nomFilm = self.TitreFilm.text()
        Film.dureeFilm = self.dureeFilm.time()
        Film.descFilm = self.textDescFilm.toPlainText()

        # Enregistrement des checkbox de catégories cochés
        model = self.listCatFilm.model()
        cat_film_list = []
        for i, v in enumerate(self.cbListCatFilm):
            item = model.item(i)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
#                print(i, v)
                #Sauvegarde des int en str
                cat_film_list.append(str(v))
        Film.catFilm = cat_film_list
        print (Film.catFilm)

        #enregistrement du nouveau film dans la BD SQL
        nf = QSqlQuery()
        nf.prepare(
           """
            INSERT INTO Film (
                NomFilm,
                DureeFilm,
                DescFilm,
                CatFilm
            )
            VALUES (?, ?, ?, ?)
            """
        )
        nf.addBindValue(Film.nomFilm)
        nf.addBindValue(Film.dureeFilm)
        nf.addBindValue(Film.descFilm)
        nf.addBindValue(Film.catFilm)
        nf.exec()
        print (nf.lastError().text())
        self.UpdateFilm()

    # choix bouton radio sexe
    def radio_button_clicked(self):
        Personne.sexe = self.sexeBtnG.checkedButton().text()
        print(Personne.sexe)

    # Met à jour les données selon le ID
    def PersonneUpdate(self):
        #Affiche le nombre de personne à coté de la TAB
        pp = QSqlQuery("SELECT * FROM Personne")
        pp.last()
        rec = pp.value('id')
        self.tabMain.setTabText(0, "Personne ({})".format(rec))
#        print (pp.lastError().text()

        # récupérer le ID sélectionné dans comboboxID
        ppid = self.comboID.currentText()

        #Prepare le query en filtrant la var PPID (ID selectionner dans comboID)
        query = QSqlQuery()
        query.prepare('SELECT * FROM Personne CROSS JOIN Client, employe ON Personne.id = Client.id WHERE Personne.id is :id')
        query.bindValue(':id', ppid) #Pointe la variable :1 vers ppid
        query.exec()
        while query.next():
#            print (ppid)
            Personne.sexe = query.value('Sexe')
            self.linePrenom.setText(query.value('Prenom'))
            self.lineNom.setText(query.value('Nom'))
            # Coche le bon radioButton selon la var Personne.Sexe
            if Personne.sexe == -2:
                self.rbtnH.setChecked(True)
            if Personne.sexe == -3:
                self.rbtnF.setChecked(True)
            if Personne.sexe == -4:
                self.rbtnNA.setChecked(True)
            # Active les sections selon ce qui est coché dans la BD
            if query.value('cbc') == 2:
                self.cbClient.setChecked(True)
                #Filtre du model de la table Carte de crédits pour n'afficher que les cartes ayant un lien avec la personne
                self.modelcc.setFilter("id = '%s'" % ppid)
                self.modelcc.select()
                #convertion de la date d'inscription de string en date
                clientdate = QDate.fromString(query.value('DateInsc'), "yyyy-MM-dd")
                self.dateInsc.setDate(clientdate)
                self.lineCourriel.setText(query.value('Courriel'))
                self.linePwdClient.setText(query.value('ClientPwd'))
            if query.value('cba') == 2:
                self.cbActeur.setChecked(True)
                #Filtre du model de la table Acteur pour n'afficher que les personnages ayant un lien avec la personne
                self.modelact.setFilter("id = '%s'" % ppid)
                self.modelact.select()
            if query.value('cbe') == 2:
                self.cbEmploye.setChecked(True)
                # convertion de la date d'embauche de string en date
                embdate = QDate.fromString(query.value('DateEmb'), "yyyy-MM-dd")
                self.dateInsc.setDate(embdate)
                self.lineUsername.setText(query.value('Username'))
                self.linePwdEmp.setText(query.value('empPwd'))
                acces = query.value('acces')
                print (acces)
#                self.comboAcces.setCurrentIndex(acces)


    # Update de la liste des films
    def UpdateFilm(self):
        pf = QSqlQuery("SELECT idf FROM Film")
        pf.last()
        rec = pf.value('idf')
        self.tabMain.setTabText(1, "Film ({})".format(rec))
#        print (pf.lastError().text())

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

        #query principale pour la personne
        db = QSqlQuery()
        db.prepare( #Préparation d'insertion des données dans la table Personne
           """
            INSERT INTO Personne (
                Prenom,
                Nom,
                Sexe,
                cbc,
                cba,
                cbe
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """
        )
        db.addBindValue(Personne.prenom)
        db.addBindValue(Personne.nom)
        db.addBindValue(Personne.sexe)
        db.addBindValue(self.cbClient.checkState())
        db.addBindValue(self.cbActeur.checkState())
        db.addBindValue(self.cbEmploye.checkState())
        db.exec()

        id = db.lastInsertId()  # Recupérer le dernier ID utiliser pour lié les infos
        print(id)
        # Si la Checkbox section Client est checked
        if self.cbClient.isChecked():
            db.prepare( #préparation d'insertion des données dans la table client
                """INSERT INTO Client (id, DateInsc, Courriel, ClientPwd)
                VALUES (?, ?, ?, ?)
                """ )
            db.addBindValue(id)
            db.addBindValue(client.dateInsc)
            db.addBindValue(client.courriel)
            db.addBindValue(client.clientPwd)
            db.exec()
            print(db.lastError().text())
        if self.cbEmploye.isChecked():
            db.prepare( #préparation d'insertion des données dans la table employe
                """
                INSERT INTO employe (
                    id,
                    DateEmb,
                    Username,
                    empPwd,
                    acces
                )
                VALUES (?, ?, ?, ?, ?)
                """
            )
            db.addBindValue(id)
            db.addBindValue(employe.dateEmb)
            db.addBindValue(employe.username)
            db.addBindValue(employe.empPWD)
            db.addBindValue(employe.acces)
            db.exec()
            print(db.lastError().text())
        self.cleanupPers() # clean up

    #Cleanup des champs une fois l'enregistrement
    def cleanupPers(self):
        # Reset des champs pour une nouvelle entrée
        self.linePrenom.setText("")
        self.lineNom.setText("")
        self.cbClient.setChecked(False)
        self.cbEmploye.setChecked(False)
        self.cbActeur.setChecked(False)
        self.dateInsc.setDate(QtCore.QDate(2021, 1, 1))
        self.lineCourriel.setText("")
        self.linePwdClient.setText("")
        self.dateEmb.setDate(QtCore.QDate(2021, 1, 1))
        self.lineUsername.setText("")
        self.linePwdEmp.setText("")
        self.comboAcces.setCurrentIndex(1)

        self.comboboxID()

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

    # Ajout d'une nouvelle rangée pour inscrire une nouvelle carte de crédit
    def AjoutCC(self):
        rowPosition = self.modelcc.rowCount()
        self.modelcc.insertRow(rowPosition)

    # Supprimer la rangée d'une carte de crédit
    def SuppCC(self):
        self.modelcc.removeRow(self.QtableCC.currentIndex().row())
        self.modelcc.submit()
        self.modelcc.select()

    # Ajout d'une nouvelle rangée pour inscrire un nouveau personnage d'acteur
    def AjoutPers(self):
        rowPosition = self.modelact.rowCount()
        self.modelact.insertRow(rowPosition)

    # Supprimer la rangée d'un personnage d'acteur
    def SuppPers(self):
        self.modelact.removeRow(self.QtableAct.currentIndex().row())
        self.modelact.submit()
        self.modelact.select()

    def ModifFilm(self):
        print (Film.listeFilm.loc[Film.positionFilm])


    def log_change(self, item):
        print("CC")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Application = QtWidgets.QDialog()
    win = Window()
    win.show()
    sys.exit(app.exec())
