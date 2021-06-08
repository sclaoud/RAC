"""

Fichier des opérations entre les class et l'interface

"""

# Importation des modules
from datetime import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QRegExpValidator, QStandardItemModel, QStandardItem, QColor
from PyQt5.QtCore import QRegExp, QDir, Qt, QDate, QTime
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QFileDialog, QTableWidgetItem, QAbstractItemView, \
    QTableView, QPushButton, QListView

from TABUI import Ui_Application
from classes import *
from sql import *


# Fenêtre principale
class Window(Ui_Application, QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.ppid = str(self.comboID.currentText())

        # validation des lignes avec limitations textes/chiffres uniquements
        regexText = QRegExpValidator(QRegExp(r'^[a-zA-Z]*$'))
        self.lineNom.setValidator(regexText)
        self.linePrenom.setValidator(regexText)

        # Bouton pour ajouter une ranger dans la QtableCC
        self.btnAjoutCC.clicked.connect(self.AjoutCC)
        # Bouton pour supprimer une ranger dans la QtableCC
        self.btnSuppCC.clicked.connect(self.SuppCC)

        # Bouton pour ajouter une ranger dans la QtableAct
        self.btnAjoutPers.clicked.connect(self.AjoutAct)
        # Bouton pour supprimer une ranger dans la QtableAct
        self.btnSuppPers.clicked.connect(self.SuppAct)

        # test avec bouton modifier de film
        self.btnVF.clicked.connect(self.ViderFilm)

        # Vidange des champs de la TAB Personne pour permettre un nouvel enregistrement
        self.btnVP.clicked.connect(self.ViderPers)

        # Supression des tables comprenant le ID de la personne sélectionné
        self.btnSupPers.clicked.connect(self.SuppPers)

        # Supression des tables comprenant le ID de film sélectionné
        self.btnSupFilm.clicked.connect(self.SuppFilm)

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
        # Enregistrement d'un nouveau film
        self.btnEF.clicked.connect(self.newFilm)
        # Enregistrement d'une nouvelle personne
        self.btnEP.clicked.connect(self.ValidationP)

        # Maximum de 40 Caracteres pour le nom et prenom
        self.linePrenom.setMaxLength(40)
        self.lineNom.setMaxLength(40)

        # Model de la liste des catégories de films
        self.model = QStandardItemModel()
        self.cbListCatFilm = {"Animation", "Fantaisie", "Science-Fiction", "Horreur", "Drame",
                              "Thriller", "Documentaire", "Comédie"}
        # Liste des catégories de films (n'est pas iterable)
        for list in self.cbListCatFilm:
            item = QStandardItem(list)
            item.setCheckable(True)
            self.model.appendRow(item)
        self.listCatFilm.setModel(self.model)

        # Model pour La table CartedeCredit
        self.modelcc = QSqlRelationalTableModel(self)
        self.modelcc.setTable("CartedeCredits")
        self.modelcc.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.modelcc.select()
        # Set up the view
        self.QtableCC.setModel(self.modelcc)
        self.QtableCC.setColumnHidden(0, True)  # Cache la column ID
        self.QtableCC.resizeColumnsToContents()

        # Model pour La table Acteurs
        self.modelact = QSqlRelationalTableModel(self)
        self.modelact.setTable("Acteurs")
        self.modelact.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.modelact.select()
        # Set up the view
        self.QtableAct.setModel(self.modelact)
        self.QtableAct.setColumnHidden(0, True)  # Cache la column des ID
        self.QtableAct.resizeColumnsToContents()

        # Si sélection d'un contenu de la comboboxID
        self.comboID.currentIndexChanged.connect(self.PersonneUpdate)

        # Si sélection d'un contenu de la comboboxIDF dans les films
        self.comboIDF.currentIndexChanged.connect(self.UpdateFilm)

        # Remplir la combobox des Accès
        self.comboboxAcces()
        # Remplir la combobox des ID des personnes et des champs au besoin
        self.comboboxID()
        # Remplir la comboxbox des ID de Films et des champs associés
        self.comboF()

    #### Fonctions ####

    # Liste des ID Personne indexé dans la combobox de selection
    def comboF(self):
        listid = []
        self.comboIDF.clear()  # Supprimer les items présent et éviter la duplication
        idquery = QSqlQuery("SELECT idf  FROM Film")
        while idquery.next():
            listid.append(str(idquery.value('idf')))
        self.comboIDF.addItems(listid)  # Ajouter la liste de ID à la comboBox

        self.UpdateFilm()  # Populate la tab selon le ID

    def ValidationP(self):
        if self.cbVP.isChecked():
            self.Enregistrement()
        else:
            self.MAJP()

    # Liste des choix du combobox comboAcces pour les employés
    def comboboxAcces(self):
        la = []
        laquery = QSqlQuery("SELECT list FROM CatAcces")
        while laquery.next():
            la.append(str(laquery.value('list')))
        self.comboAcces.addItems(la)

    # Liste des ID Personne indexé dans la combobox de selection
    def comboboxID(self):
        listid = []
        self.comboID.clear()  # Supprimer les items présent et éviter la duplication
        idquery = QSqlQuery("SELECT id  FROM Personne")
        while idquery.next():
            listid.append(str(idquery.value('id')))
        self.comboID.addItems(listid)  # Ajouter la liste de ID à la comboBox

        self.PersonneUpdate()  # Populate la tab selon le ID

    # Enregistrement de l'entré et remise à zero des films
    def newFilm(self):
        Film.nomFilm = self.TitreFilm.text()
        Film.dureeFilm = self.dureeFilm.time()
        Film.descFilm = self.textDescFilm.toPlainText()

        # Enregistrement des checkbox de catégories cochés
        model = self.listCatFilm.model()
        cat_film_list = []
        cat_film_list.clear()
        for i, v in enumerate(self.cbListCatFilm):
            item = model.item(i)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                # Sauvegarde des int en str
                cat_film_list.append(str(v))
#        print(Film.catFilm)

        if 'Animation' in cat_film_list:
            animation = 2
        else:
            animation = 0
        if 'Fantaisie' in cat_film_list:
            fantaisie = 2
        else:
            fantaisie = 0
        if 'Science-Fiction' in cat_film_list:
            syfy = 2
        else:
            syfy = 0
        if 'Horreur' in cat_film_list:
            horreur = 2
        else:
            horreur = 0
        if 'Drame' in cat_film_list:
            drame = 2
        else:
            drame = 0
        if 'Thriller' in cat_film_list:
            thriller = 2
        else:
            thriller = 0
        if 'Documentaire' in cat_film_list:
            documentaire = 2
        else:
            documentaire = 0
        if 'Comédie' in cat_film_list:
            comedie = 2
        else:
            comedie = 0


        # enregistrement du nouveau film dans la BD SQL
        nf = QSqlQuery()
        nf.prepare(
            """
            INSERT INTO Film (
            NomFilm=:nf
            )
            """
        )
        nf.bindValue(':nf', Film.nomFilm)
#        nf.bindValue(':tf', Film.dureeFilm)
#        nf.bindValue(':df', Film.descFilm)
#        nf.bindValue(':ca', animation)
#        nf.bindValue(':cf', fantaisie)
#        nf.bindValue(':cs', syfy)
#        nf.bindValue(':ch', horreur)
#        nf.bindValue(':cd', drame)
#        nf.bindValue(':ct', thriller)
#        nf.bindValue(':cd', documentaire)
#        nf.bindValue(':cc', comedie)
        nf.exec()
        self.comboF()
        print(nf.lastError().text())

    # choix bouton radio sexe
    def radio_button_clicked(self):
        Personne.sexe = self.sexeBtnG.checkedButton().text()

    # Met à jour les données selon le ID
    def PersonneUpdate(self):
        query = QSqlQuery()

        self.ppid = str(self.comboID.currentText())

        # Prepare le query en filtrant la var PPID (ID selectionner dans comboID)
        query.prepare('SELECT * FROM Personne WHERE id is :id')
        query.bindValue(':id', self.ppid)  # Pointe la variable :1 vers ppid
        query.exec()
        while query.next():
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
            # Si la checkbox client est coché, lance la fonction loadclient sinon s'assure que les champs sont vide
            if query.value('cbc') == 2:
                self.loadclient()
            else:
                self.cbClient.setChecked(False)
                cdate = QDate.fromString("2021-01-01", "yyyy-MM-d")
                self.dateInsc.setDate(cdate)
                self.lineCourriel.setText("")
                self.linePwdClient.setText("")
                # Filtre du modelcc de la table CartedeCredtis pour apparaitre vide
                self.modelcc.setFilter("id = 0")
                self.modelcc.select()

            # Si la checkbox acteur est coché, load la table acteur sinon vide la fenetre
            if query.value('cba') == 2:
                self.cbActeur.setChecked(True)
                # Filtre du model de la table Acteur pour n'afficher que les personnages ayant un lien avec la personne
                self.modelact.setFilter("id = '%s'" % self.ppid)
                self.modelact.select()

            else:
                self.cbActeur.setChecked(False)
                # Filtre du model de la table Acteur pour n'afficher que les personnages ayant un lien avec la personne
                self.modelact.setFilter("id = 0")
                self.modelact.select()

            # Si la checkbox employe est coché, load la table employe
            if query.value('cbe') == 2:
                self.loademploye()
            else:
                self.cbEmploye.setChecked(False)
                self.lineUsername.setText("")
                self.linePwdEmp.setText("")
                self.comboAcces.setCurrentIndex(0)

    # charge la section client si cbc est coché
    def loadclient(self):
        cquery = QSqlQuery()
        self.cbClient.setChecked(True)
        cquery.prepare('SELECT * FROM Client WHERE id is :id')  # condition que le id est sélectionné
        cquery.bindValue(':id', self.ppid)  # Pointe la variable :1 vers ppid
        cquery.exec()
        # Filtre du model de la table Carte de crédits pour n'afficher que les cartes ayant un lien avec la personne
        self.modelcc.setFilter("id = '%s'" % self.ppid)
        self.modelcc.select()
        # convertion de la date d'inscription de string en date
        clientdate = QDate.fromString(cquery.value('DateInsc'), "yyyy-MM-d")
        while cquery.next():
            self.dateInsc.setDate(clientdate)
            self.lineCourriel.setText(cquery.value('Courriel'))
            self.linePwdClient.setText(cquery.value('ClientPwd'))

    # Charge les données de l'employé si la checkbox est coché
    def loademploye(self):
        equery = QSqlQuery()
        self.cbEmploye.setChecked(True)
        equery.prepare('SELECT * FROM employe WHERE id is :id')  # condition que le id est sélectionné
        equery.bindValue(':id', self.ppid)  # Pointe la variable :1 vers ppid
        equery.exec()
        while equery.next():
            # convertion de la date d'embauche de string en date
            embdate = QDate.fromString(equery.value('DateEmb'), "yyyy-MM-d")
            self.dateEmb.setDate(embdate)
            # Remplissage des champs selon les données recoltés
            self.lineUsername.setText(equery.value('Username'))
            self.linePwdEmp.setText(equery.value('empPwd'))
            acces = equery.value('acces')
            self.comboAcces.setCurrentIndex(acces)

    # Update la tab des films selon le ID sélectionné
    def UpdateFilm(self):
        query = QSqlQuery()
        self.idf = str(self.comboIDF.currentText())
        # Prepare le query en filtrant la var PPID (ID selectionner dans comboID)
        query.prepare('SELECT * FROM Film WHERE idf is :idf')
        query.bindValue(':idf', self.idf)  # Pointe la variable :idf vers idf
        query.exec()
        while query.next():
            ftime = QTime.fromString(query.value('DureeFilm'))
            self.TitreFilm.setText(query.value('NomFilm'))
            self.dureeFilm.setTime(ftime)
            self.textDescFilm.setText(query.value('DescFilm'))

    # Suppression des informations de la personne dans toute les tables si existantes
    def SuppPers(self):
        query = QSqlQuery()
        query.prepare("DELETE FROM Personne WHERE id is :id")  # condition que le id est sélectionné
        query.bindValue(':id', self.ppid)
        query.exec()
        query.prepare("DELETE FROM Client WHERE id is :id")  # condition que le id est sélectionné
        query.bindValue(':id', self.ppid)
        query.exec()
        query.prepare("DELETE FROM CartedeCredits WHERE id is :id")  # condition que le id est sélectionné
        query.bindValue(':id', self.ppid)
        query.exec()
        query.prepare("DELETE FROM Acteurs WHERE id is :id")  # condition que le id est sélectionné
        query.bindValue(':id', self.ppid)
        query.exec()
        query.prepare("DELETE FROM employe WHERE id is :id")  # condition que le id est sélectionné
        query.bindValue(':id', self.ppid)
        query.exec()
        self.comboboxID()  # Call comboboxID pour mettre à jour

    def SuppFilm(self):
        query = QSqlQuery()
        query.prepare("DELETE FROM Film WHERE idf is :idf")  # condition que le id est sélectionné
        query.bindValue(':idf', self.idf)
        query.exec()
        self.comboF()  # Call comboboxID pour mettre à jour

    # Mise-à-jour de l'index en cours si cbVP n'est pas coché
    def MAJP(self):
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

        # query principale pour la personne
        db = QSqlQuery()
        db.prepare(  # Préparation d'insertion des données dans la table Personne
            """
            UPDATE Personne SET 
                Prenom =:prenom,
                Nom =:nom,
                Sexe =:sexe,
                cbc =:cbc,
                cba =:cba,
                cbe =:cbe
                WHERE id is :id
            """
        )
        db.bindValue(':prenom', Personne.prenom)
        db.bindValue(':nom', Personne.nom)
        db.bindValue(':sexe', Personne.sexe)
        db.bindValue(':cbc', self.cbClient.checkState())
        db.bindValue(':cba', self.cbActeur.checkState())
        db.bindValue(':cbe', self.cbEmploye.checkState())
        db.bindValue(':id', self.ppid)
        db.exec()

        # Si la Checkbox section Client est checked
        if self.cbClient.isChecked():
            db.prepare(  # préparation d'insertion des données dans la table client
                """UPDATE Client SET DateInsc=:dateinsc, Courriel=:courriel, ClientPwd=:clientpwd WHERE id is :id""")
            db.bindValue(':id', self.ppid)
            db.bindValue(':dateinsc', client.dateInsc)
            db.bindValue(':courriel', client.courriel)
            db.bindValue(':clientpwd', client.clientPwd)
            db.exec()
            print(db.lastError().text())
        # Si la checkbox section employe est checked
        if self.cbEmploye.isChecked():
            db.prepare(  # préparation d'insertion des données dans la table employe
                """ UPDATE employe SET DateEmb=:dateemb, Username=:username, empPwd=:emppwd, acces=:acces
                    WHERE id is :id """)
            db.bindValue(':id', self.ppid)
            db.bindValue(':dateemb', employe.dateEmb)
            db.bindValue(':username', employe.username)
            db.bindValue(':emppwd', employe.empPWD)
            db.addBindValue(':acces', employe.acces)
            db.exec()

        # Met à jour la fenêtre
        self.comboboxID()

    # Enregistrement de l'entré
    def Enregistrement(self):
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

        # query principale pour la personne
        db = QSqlQuery()
        db.prepare(  # Préparation d'insertion des données dans la table Personne
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
        # Si la Checkbox section Client est checked
        if self.cbClient.isChecked():
            db.prepare(  # préparation d'insertion des données dans la table client
                """INSERT INTO Client (id, DateInsc, Courriel, ClientPwd)
                VALUES (?, ?, ?, ?)
                """)
            db.addBindValue(id)
            db.addBindValue(client.dateInsc)
            db.addBindValue(client.courriel)
            db.addBindValue(client.clientPwd)
            db.exec()
            print(db.lastError().text())
        # Si la checkbox section employe est checked
        if self.cbEmploye.isChecked():
            db.prepare(  # préparation d'insertion des données dans la table employe
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

        # Met à jour la fenêtre
        self.comboboxID()

    # Cleanup des champs une fois l'enregistrement
    def ViderPers(self):
        # Reset des champs pour une nouvelle entrée
        self.comboID.setCurrentIndex(00)
        self.linePrenom.setText("")
        self.lineNom.setText("")
        self.rbtnNA.setChecked(True)  # Radio Ne pas répondre activé car ne peut avoir aucune réponse par défaut
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
        # Filtre des model des tables Acteurs et CartedeCredtis pour apparaitre vide
        self.modelact.setFilter("id = 0")
        self.modelact.select()
        self.modelcc.setFilter("id = 0")
        self.modelcc.select()

    def ViderFilm(self):
        # Reset des champs pour une nouvelle entrée
        self.comboID.setCurrentIndex(00)
        self.TitreFilm.setText("")
        self.textDescFilm.setText("")
        qtime = time()
        self.dureeFilm.setTime(qtime)

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
        rec = self.modelcc.record()
        rec.setValue('id', self.ppid)
        self.modelcc.insertRecord(rowPosition, rec)

    # Supprimer la rangée d'une carte de crédit
    def SuppCC(self):
        self.modelcc.removeRow(self.QtableCC.currentIndex().row())
        self.modelcc.submit()
        self.modelcc.select()

    # Ajout d'une nouvelle rangée pour inscrire un nouveau personnage d'acteur
    def AjoutAct(self):
        rowPosition = self.modelact.rowCount()
        rec = self.modelact.record()
        rec.setValue('id', self.ppid)
        self.modelact.insertRecord(rowPosition, rec)

    # Supprimer la rangée d'un personnage d'acteur
    def SuppAct(self):
        self.modelact.removeRow(self.QtableAct.currentIndex().row())
        self.modelact.submit()
        self.modelact.select()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Application = QtWidgets.QDialog()
    win = Window()
    win.show()
    sys.exit(app.exec())
