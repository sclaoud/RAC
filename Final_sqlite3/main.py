"""

Fichier des opérations entre les class et l'interface

"""

# Importation des modules
from datetime import time
from PyQt5 import QtCore
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp, QDate, QTime
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtSql import QSqlRelationalTableModel
from TABUI import Ui_Application
import re
from classes import *
from sql import *

# Fenêtre de login
class Login(QDialog):
    vquery = QSqlQuery()

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.login = QLineEdit(self)
        self.pwd = QLineEdit(self)
        self.pwd.setEchoMode(QLineEdit.Password)
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QVBoxLayout(self)
        layout.addWidget(self.login)
        layout.addWidget(self.pwd)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):

        user.login = self.login.text()
        user.pwd = self.pwd.text()

        self.vquery.prepare("""SELECT * FROM employe""")
        self.vquery.exec()
        while self.vquery.next():
            sqlun = self.vquery.value('employe.Username')
            sqlpwd = self.vquery.value('employe.empPwd')
            if (user.login == sqlun) and (user.pwd == sqlpwd):
                user.acces = self.vquery.value('employe.Acces')
                self.reussit()


    def reussit(self):
        if user.acces == 'Lecture':
            self.accept()
        if user.acces == 'Lecture/Ecriture':
            self.accept()


# Fenêtre principale si l'usager n'à accès qu'en lecture
class Window_readonly(Ui_Application, QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # Label pour aviser la personne de ses accès.
        self.label_acces.setText("Bonjour " + user.login + ", vous êtes en lecture seulement")

        # Désactive toute les section en lecture seulement
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
        self.cbVP.setDisabled(True)
        self.cbClient.setDisabled(True)
        self.cbActeur.setDisabled(True)
        self.cbEmploye.setDisabled(True)
        self.lineNom.setDisabled(True)
        self.linePrenom.setDisabled(True)
        self.rbtnNA.setDisabled(True)
        self.rbtnF.setDisabled(True)
        self.rbtnH.setDisabled(True)
        self.btnEP.setDisabled(True)
        self.btnVP.setDisabled(True)
        self.btnSupPers.setDisabled(True)
        self.btnVF.setDisabled(True)
        self.btnEF.setDisabled(True)
        self.btnSupFilm.setDisabled(True)
        self.cbVF.setDisabled(True)
        self.TitreFilm.setDisabled(True)
        self.dureeFilm.setDisabled(True)
        self.textDescFilm.setDisabled(True)
        self.listCatFilm.setDisabled(True)

        # Echomode pour les Password
        self.linePwdClient.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.linePwdEmp.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        # Fonction de fermeture 'closeEvent' lorsque l'on appui sur le bouton
        self.btnFermer.clicked.connect(self.closeEvent)

    # Model des catégories de Films pour la tab Film
        self.modelcf = QSqlTableModel()
        self.modelcf.setTable("Categories")
        self.modelcf.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.modelcf.select()
        self.listCatFilm.setModel(self.modelcf)
        self.listCatFilm.setSelectionMode(2)

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
        self.comboID.currentIndexChanged.connect(self.ROPersonne)

        # Si sélection d'un contenu de la comboboxIDF dans les films
        self.comboIDF.currentIndexChanged.connect(self.ROFilm)

        # Remplir la combobox des Accès
        self.ROcbA()
        # Remplir la combobox des ID des personnes et des champs au besoin
        self.ROcbP()
        # Remplir la comboxbox des ID de Films et des champs associés
        self.ROcbF()

    # Liste des choix du combobox comboAcces pour les employés
    def ROcbA(self):
        la = []
        laquery = QSqlQuery("SELECT list FROM CatAcces")
        while laquery.next():
            la.append(str(laquery.value('list')))
        self.comboAcces.addItems(la)

    # Fonctions de la fenêtre readonly
    # Liste des ID Personne indexé dans la combobox de selection
    def ROcbF(self):
        listid = []
        self.comboIDF.clear()  # Supprimer les items présent et éviter la duplication
        idquery = QSqlQuery("SELECT idf  FROM Film")
        while idquery.next():
            listid.append(str(idquery.value('idf')))
        self.comboIDF.addItems(listid)  # Ajouter la liste de ID à la comboBox
        self.ROFilm()

    # Liste des ID Personne indexé dans la combobox de selection
    def ROcbP(self):
        listid = []
        self.comboID.clear()  # Supprimer les items présent et éviter la duplication
        idquery = QSqlQuery("SELECT id FROM Personne")
        while idquery.next():
            listid.append(str(idquery.value('id')))
        self.comboID.addItems(listid)  # Ajouter la liste de ID à la comboBox

        self.ROPersonne()  # Populate la tab selon le ID

    # Met à jour les données selon le ID
    def ROPersonne(self):
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

        # Update la tab des films selon le ID sélectionné

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
            self.comboAcces.setCurrentText(acces)

    def ROFilm(self):
        query = QSqlQuery()
        # Définition de la var idf avec l'index de la liste déroulante Film
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
        # Remplie la liste des categorie selon la selection
        Film.categories.clear()  # clear de la liste précédente
        cquery = QSqlQuery()
        cquery.prepare('SELECT * FROM CatFilm WHERE idf is :idf')  # condition que le id est sélectionné
        cquery.bindValue(':idf', self.idf)  # Pointe la variable idf vers idf
        cquery.exec()
        # Selection les items dans la list selon la liste rapporter de la table catfilm
        while cquery.next():
            if cquery.value('Animation') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(0, 0))
            if cquery.value('Comedie') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(1, 0))
            if cquery.value('Documentaire') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(2, 0))
            if cquery.value('Drame') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(3, 0))
            if cquery.value('Fantaisie') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(4, 0))
            if cquery.value('Horreur') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(5, 0))
            if cquery.value('ScienceFiction') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(6, 0))
            if cquery.value('Thriller') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(7, 0))

# Fenêtre principale si l'usager à les droits d'écriture
class Window(Ui_Application, QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # Label pour aviser la personne de ses accès.
        self.label_acces.setText("Bonjour " + user.login + ", vous êtes en lecture/Écriture")

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
        self.linePwdClient.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.linePwdEmp.setEchoMode(QLineEdit.PasswordEchoOnEdit)

    # Désactive la table carte de crédit et la cbacteur si la personne n'a pas été créer pour raison de bug (le id doit exister)
        self.cbVP.toggled.connect(self.cbActeur.setDisabled)
        self.cbVP.toggled.connect(self.QtableCC.setDisabled)
        self.cbVP.toggled.connect(self.btnAjoutCC.setDisabled)
        self.cbVP.toggled.connect(self.btnSuppCC.setDisabled)

    # Checkbox si la personne est artiste, active la section Artiste
        self.cbActeur.toggled.connect(self.QtableAct.setEnabled)
        self.cbActeur.toggled.connect(self.btnSuppPers.setEnabled)
        self.cbActeur.toggled.connect(self.btnAjoutPers.setEnabled)
    # Checkbox si la personne est Client, active la section client
        self.cbClient.toggled.connect(self.dateInsc.setEnabled)
        self.cbClient.toggled.connect(self.lineCourriel.setEnabled)
        self.cbClient.toggled.connect(self.linePwdClient.setEnabled)
        self.cbClient.toggled.connect(self.QtableCC.setEnabled)
        self.cbClient.toggled.connect(self.btnAjoutCC.setEnabled)
        self.cbClient.toggled.connect(self.btnSuppCC.setEnabled)
        # Garde les fonctions désactivé si les entrés sont pas créer dans les tables en premiers
        if self.cbVP.isChecked() and self.cbClient.isChecked():
            self.cbVP.toggled.connect(self.QtableCC.setDisabled)
            self.cbVP.toggled.connect(self.btnAjoutCC.setDisabled)
            self.cbVP.toggled.connect(self.btnSuppCC.setDisabled)

        # Checkbox si la personne est employé, active la section employé si coché
        self.cbEmploye.toggled.connect(self.dateEmb.setEnabled)
        self.cbEmploye.toggled.connect(self.lineUsername.setEnabled)
        self.cbEmploye.toggled.connect(self.linePwdEmp.setEnabled)
        self.cbEmploye.toggled.connect(self.comboAcces.setEnabled)

        # Fonction de fermeture 'closeEvent' lorsque l'on appui sur le bouton
        self.btnFermer.clicked.connect(self.closeEvent)
        # Enregistrement d'un nouveau film
        self.btnEF.clicked.connect(self.ValidationF)
        # Enregistrement d'une nouvelle personne
        self.btnEP.clicked.connect(self.ValidationP)

        # Maximum de 40 Caracteres pour le nom et prenom
        self.linePrenom.setMaxLength(40)
        self.lineNom.setMaxLength(40)

    # Model des catégories de Films pour la tab Film
        self.modelcf = QSqlTableModel()
        self.modelcf.setTable("Categories")
        self.modelcf.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.modelcf.select()
        self.listCatFilm.setModel(self.modelcf)
        self.listCatFilm.setSelectionMode(2)
        # Sauvegarde les catégories selectionnés
        self.listCatFilm.selectionModel().selectionChanged.connect(self.Selectcat)

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

# Section de la TAB Film

    # Ajoute les catégories selectionnés de la liste des catégories de films dans une liste
    def Selectcat(self):
        cf = []
        for i in self.listCatFilm.selectedIndexes():
            cf.append(i.data())
        # transfert la list temporaire dans Film.categorie mais doit pouvoir oublier les elements non selectionné
        Film.categories = cf

    # Liste des ID Personne indexé dans la combobox de selection
    def comboF(self):
        listid = []
        self.comboIDF.clear()  # Supprimer les items présent et éviter la duplication
        idquery = QSqlQuery("SELECT idf  FROM Film")
        while idquery.next():
            listid.append(str(idquery.value('idf')))
        self.comboIDF.addItems(listid)  # Ajouter la liste de ID à la comboBox

    # Valide si la case de nouvel enregistrement de la tab Film est coché ou non
    def ValidationF(self):
        if self.cbVF.isChecked():
            self.newFilm()
        else:
            self.MAJF()

    # Enregistrement de l'entré et remise à zero des films
    def newFilm(self):
        Film.nomFilm = self.TitreFilm.text()
        Film.dureeFilm = self.dureeFilm.time()
        Film.descFilm = self.textDescFilm.toPlainText()


        # enregistrement du nouveau film dans la BD SQL
        nf = QSqlQuery()
        nf.prepare(
            """
            INSERT INTO Film (NomFilm, DureeFilm, DescFilm)
            values (?, ?, ?)
            """
        )
        nf.addBindValue(Film.nomFilm)
        nf.addBindValue(Film.dureeFilm)
        nf.addBindValue(Film.descFilm)
        nf.exec()

        idf = nf.lastInsertId()  # Recupérer le dernier ID utiliser pour lié les infos

        # Valide si chacune des valeurs existe dans la liste des catégories de film
        if 'Animation' in Film.categories:
            Animation = 2
        if 'Animation' not in Film.categories:
            Animation = 0
        if 'Comedie' in Film.categories:
            Comedie = 2
        if 'Comedie' not in Film.categories:
            Comedie = 0
        if 'Documentaire' in Film.categories:
            Documentaire = 2
        if 'Documentaire' not in Film.categories:
            Documentaire = 0
        if 'Drame' in Film.categories:
            Drame = 2
        if 'Drame' not in Film.categories:
            Drame = 0
        if 'Fantaisie' in Film.categories:
            Fantaisie = 2
        if 'Fantaisie' not in Film.categories:
            Fantaisie = 0
        if 'Horreur' in Film.categories:
            Horreur = 2
        if 'Horreur' not in Film.categories:
            Horreur = 0
        if 'ScienceFiction' in Film.categories:
            ScienceFiction = 2
        if 'ScienceFiction' not in Film.categories:
            ScienceFiction = 0
        if 'Thriller' in Film.categories:
            Thriller = 2
        if 'Thriller' not in Film.categories:
            Thriller = 0

        nf.prepare(  # préparation d'insertion des données dans la table client
            """INSERT INTO CatFilm (idf, Animation, Comedie, Documentaire, Drame,
             Fantaisie, Horreur, ScienceFiction, Thriller)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """)
        nf.addBindValue(idf)
        nf.addBindValue(Animation)
        nf.addBindValue(Comedie)
        nf.addBindValue(Documentaire)
        nf.addBindValue(Drame)
        nf.addBindValue(Fantaisie)
        nf.addBindValue(Horreur)
        nf.addBindValue(ScienceFiction)
        nf.addBindValue(Thriller)
        nf.exec()

        self.ViderFilm() # Vide les champs
        self.comboF()  # Reload de l'indexation et de la fenêtre.

    # Update du film sélectionné si la case Nouvelle entrée n'est pas coché
    def MAJF(self):
        Film.nomFilm = self.TitreFilm.text()
        Film.dureeFilm = self.dureeFilm.time()
        Film.descFilm = self.textDescFilm.toPlainText()

        uf = QSqlQuery()
        uf.prepare(
            """
        UPDATE Film SET 
            NomFilm=:nf, 
            DureeFilm=:nt, 
            DescFilm=:nd
        WHERE id is :idf
            """
        )
        uf.bindValue(':nf', Film.nomFilm)
        uf.bindValue(':nt', Film.dureeFilm)
        uf.bindValue(':nd', Film.descFilm)
        uf.bindValue(':idf', self.idf)
        uf.exec()

        # Valide si chacune des valeurs existe dans la liste des catégories de film
        if 'Animation' in Film.categories:
            Animation = 2
        if 'Animation' not in Film.categories:
            Animation = 0
        if 'Comedie' in Film.categories:
            Comedie = 2
        if 'Comedie' not in Film.categories:
            Comedie = 0
        if 'Documentaire' in Film.categories:
            Documentaire = 2
        if 'Documentaire' not in Film.categories:
            Documentaire = 0
        if 'Drame' in Film.categories:
            Drame = 2
        if 'Drame' not in Film.categories:
            Drame = 0
        if 'Fantaisie' in Film.categories:
            Fantaisie = 2
        if 'Fantaisie' not in Film.categories:
            Fantaisie = 0
        if 'Horreur' in Film.categories:
            Horreur = 2
        if 'Horreur' not in Film.categories:
            Horreur = 0
        if 'ScienceFiction' in Film.categories:
            ScienceFiction = 2
        if 'ScienceFiction' not in Film.categories:
            ScienceFiction = 0
        if 'Thriller' in Film.categories:
            Thriller = 2
        if 'Thriller' not in Film.categories:
            Thriller = 0

        uf.prepare(  # préparation d'insertion des données dans la table client
            """UPDATE CatFilm SET Animation=:ca, Comedie=:cc, Documentaire=:cd,
             Drame=:cdd, Fantaisie=:cf, Horreur=:ch, ScienceFiction=:cs, Thriller=:ct
            WHERE idf is :idf
            """)
        uf.bindValue(':idf', self.idf)
        uf.bindValue(':ca', Animation)
        uf.bindValue(':cc', Comedie)
        uf.bindValue(':cd', Documentaire)
        uf.bindValue(':cdd', Drame)
        uf.bindValue(':cf', Fantaisie)
        uf.bindValue(':ch', Horreur)
        uf.bindValue(':cs', ScienceFiction)
        uf.bindValue(':ct', Thriller)
        uf.exec()

        self.comboF()  # Reload de l'indexation et de la fenêtre.

    # Supression d'un film de la BD
    def SuppFilm(self):
        query = QSqlQuery()
        query.prepare("DELETE FROM Film WHERE idf is :idf")  # condition que le id est sélectionné
        query.bindValue(':idf', self.idf)
        query.exec()
        #Message de confirmation de suppression
        delmsg = QMessageBox
        delmsg.setIcon(QMessageBox.Information)
        delmsg.setInformativeText("Le film a été supprimer avec succès")
        delmsg.setWindowTitle("Confirmation")
        delmsg.exec()
        self.comboF()  # Call comboboxID pour mettre à jour

    # Cleanup des champs une fois l'enregistrement
    def ViderFilm(self):
        # Reset des champs pour une nouvelle entrée
        self.comboID.setCurrentIndex(00)
        self.TitreFilm.setText("")
        self.textDescFilm.setText("")
        qtime = time()
        self.dureeFilm.setTime(qtime)
        self.listCatFilm.clearSelection()

    # Update la tab des films selon le ID sélectionné
    def UpdateFilm(self):
        query = QSqlQuery()
        # Définition de la var idf avec l'index de la liste déroulante Film
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
        # Remplie la liste des categorie selon la selection
        Film.categories.clear()  # clear de la liste précédente
        cquery = QSqlQuery()
        cquery.prepare('SELECT * FROM CatFilm WHERE idf is :idf')  # condition que le id est sélectionné
        cquery.bindValue(':idf', self.idf)  # Pointe la variable idf vers idf
        cquery.exec()
        # Selection les items dans la list selon la liste rapporter de la table catfilm
        while cquery.next():
            if cquery.value('Animation') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(0, 0))
            if cquery.value('Comedie') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(1, 0))
            if cquery.value('Documentaire') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(2, 0))
            if cquery.value('Drame') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(3, 0))
            if cquery.value('Fantaisie') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(4, 0))
            if cquery.value('Horreur') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(5, 0))
            if cquery.value('ScienceFiction') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(6, 0))
            if cquery.value('Thriller') == 2:
                self.listCatFilm.setCurrentIndex(self.modelcf.index(7, 0))

#  Section de la TAB Personne

    # Liste des ID Personne indexé dans la combobox de selection
    def comboboxID(self):
        listid = []
        self.comboID.clear()  # Supprimer les items présent et éviter la duplication
        idquery = QSqlQuery("SELECT id  FROM Personne")
        while idquery.next():
            listid.append(str(idquery.value('id')))
        self.comboID.addItems(listid)  # Ajouter la liste de ID à la comboBox

        self.PersonneUpdate()  # Populate la tab selon le ID

    # Valide sur la case de nouvel enregistrement de la tab Personne est coché ou non
    def ValidationP(self):
        if self.cbVP.isChecked():
            self.ValP() # Validation nouvel enregistremnet
        else:
            self.MAJP()

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
            self.comboAcces.setCurrentText(acces)

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
        # Message de configuration de la suppression
        delmsg = QMessageBox()
        delmsg.setIcon(QMessageBox.Information)
        delmsg.setInformativeText("La personne a été supprimer avec succès")
        delmsg.setWindowTitle("Confirmation")
        delmsg.exec()

        self.comboboxID()  # Call comboboxID pour mettre à jour

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
        cl = [] # listing des courriels pour validation
        cquery = QSqlQuery() # Query pour le courriel
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
            # Validation du courriel
            regexmail = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
            if re.search(regexmail, client.courriel):
                # Valide si le courriel est unique ou non
                cquery.prepare("SELECT Courriel FROM Client")
                cquery.exec()
                while cquery.next():
                    cl.append(cquery.value('Courriel'))
                if client.courriel in cl:
                    courrielMsg = QMessageBox()
                    courrielMsg.setIcon(QMessageBox.Warning)
                    courrielMsg.setInformativeText("Le courriel doit être unique")
                    courrielMsg.setWindowTitle("Courriel")
                    courrielMsg.exec()
                else:
                    # Validation du mot de passe si le courriel est correct
                    if self.linePwdClient.text() and self.lineCourriel.text():
                        password = client.clientPwd
                        if len(password) < 8:
                            pwdMsg = QMessageBox()
                            pwdMsg.setIcon(QMessageBox.Warning)
                            pwdMsg.setInformativeText("Le mot de passe du client doit contenir au moins 8 caractères")
                            pwdMsg.setWindowTitle("Mot de passe")
                            pwdMsg.exec()
                        elif re.search('[0-9]', password) is None:
                            pwdMsg = QMessageBox()
                            pwdMsg.setIcon(QMessageBox.Warning)
                            pwdMsg.setInformativeText("Le mot de passe du client doit contenir au moins 1 chiffre")
                            pwdMsg.setWindowTitle("Mot de passe")
                            pwdMsg.exec()
                        elif re.search('[A-Z]', password) is None:
                            pwdMsg = QMessageBox()
                            pwdMsg.setIcon(QMessageBox.Warning)
                            pwdMsg.setInformativeText("Le mot de passe du client doit contenir au 1 majuscule")
                            pwdMsg.setWindowTitle("Mot de passe")
                            pwdMsg.exec()
                        else:
                            # Toute les informations clients sont correct et vont pasés à l'update
                            self.MAJP_client()
            else:
                cmsg = QMessageBox()
                cmsg.setIcon(QMessageBox.Warning)
                cmsg.setInformativeText("Le courriel est invalide")
                cmsg.setWindowTitle("Courriel")
                cmsg.exec()

        # Si la checkbox section employe est checked
        if self.cbEmploye.isChecked():
            self.MAJP_employe()

    # Met à jour les champs de la section client si les conditions sont réunis
    def MAJP_employe(self):
        db = QSqlQuery()
        db.prepare(  # préparation d'insertion des données dans la table employe
            """ UPDATE employe SET DateEmb=:dateemb, Username=:username, empPwd=:emppwd, acces=:acces
                WHERE id is :id """)
        db.bindValue(':id', self.ppid)
        db.bindValue(':dateemb', employe.dateEmb)
        db.bindValue(':username', employe.username)
        db.bindValue(':emppwd', employe.empPWD)
        db.bindValue(':acces', employe.acces)
        db.exec()
        # Met à jour la fenêtre
        self.comboboxID()

    # Met à jour les champs de la section client si les conditions sont réunis
    def MAJP_client(self):
        db = QSqlQuery()
        db.prepare(  # préparation d'insertion des données dans la table client
            """UPDATE Client SET DateInsc=:dateinsc, Courriel=:courriel, ClientPwd=:clientpwd WHERE id is :id""")
        db.bindValue(':id', self.ppid)
        db.bindValue(':dateinsc', client.dateInsc)
        db.bindValue(':courriel', client.courriel)
        db.bindValue(':clientpwd', client.clientPwd)
        db.exec()
        # Met à jour la fenêtre
        self.comboboxID()

    # Enregistrement de l'entré
    def ValP(self):
        cl = [] # listing des courriels pour validation
        cquery = QSqlQuery() # Query pour le courriel

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

        # Si la Checkbox section Client est checked
        while self.cbClient.isChecked():
            # Validation du courriel
            regexmail = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
            if re.search(regexmail, client.courriel):
                # Valide si le courriel est unique ou non
                cquery.prepare("SELECT Courriel FROM Client")
                cquery.exec()
                while cquery.next():
                    cl.append(cquery.value('Courriel'))
                if client.courriel in cl:
                    courrielMsg = QMessageBox()
                    courrielMsg.setIcon(QMessageBox.Warning)
                    courrielMsg.setInformativeText("Le courriel doit être unique")
                    courrielMsg.setWindowTitle("Courriel")
                    courrielMsg.exec()
                    break
                else:
                    # Validation du mot de passe si le courriel est correct
                    if self.linePwdClient.text() and self.lineCourriel.text():
                        password = client.clientPwd
                        if len(password) < 8:
                            pwdMsg = QMessageBox()
                            pwdMsg.setIcon(QMessageBox.Warning)
                            pwdMsg.setInformativeText("Le mot de passe du client doit contenir au moins 8 caractères")
                            pwdMsg.setWindowTitle("Mot de passe")
                            pwdMsg.exec()
                            break
                        elif re.search('[0-9]', password) is None:
                            pwdMsg = QMessageBox()
                            pwdMsg.setIcon(QMessageBox.Warning)
                            pwdMsg.setInformativeText("Le mot de passe du client doit contenir au moins 1 chiffre")
                            pwdMsg.setWindowTitle("Mot de passe")
                            pwdMsg.exec()
                            break
                        elif re.search('[A-Z]', password) is None:
                            pwdMsg = QMessageBox()
                            pwdMsg.setIcon(QMessageBox.Warning)
                            pwdMsg.setInformativeText("Le mot de passe du client doit contenir au 1 majuscule")
                            pwdMsg.setWindowTitle("Mot de passe")
                            pwdMsg.exec()
                            break
                        else:
                            # Toute les informations clients sont correct et vont pasés à l'update
                            print("Toutes les informations sont valides")
            else:
                cmsg = QMessageBox()
                cmsg.setIcon(QMessageBox.Warning)
                cmsg.setInformativeText("Le courriel est invalide")
                cmsg.setWindowTitle("Courriel")
                cmsg.exec()
                break

        # Si la checkbox section employe est checked
        if self.cbEmploye.isChecked():
            self.savePE()

        else:
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

            # Met à jour la fenêtre
            self.comboboxID()

    def Save_PC(self):
        db = QSqlQuery()
        id = db.lastInsertId()  # Recupérer le dernier ID utiliser pour lié les infos
        db.prepare(  # préparation d'insertion des données dans la table client
                """INSERT INTO Client (id, DateInsc, Courriel, ClientPwd)
                VALUES (?, ?, ?, ?)
                """)
        db.addBindValue(id)
        db.addBindValue(client.dateInsc)
        db.addBindValue(client.courriel)
        db.addBindValue(client.clientPwd)
        db.exec()
        # Met à jour la fenêtre
        self.comboboxID()

    # Si la checkbox section employe est checked
    def Save_employe(self):
        db = QSqlQuery()
        id = db.lastInsertId()  # Recupérer le dernier ID utiliser pour lié les infos
        db.prepare(  # préparation d'insertion des données dans la table employe
            """
            INSERT INTO employe (
                id,
                DateEmb,
                Username,
                empPwd,
                Acces
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

    # Liste des choix du combobox comboAcces pour les employés
    def comboboxAcces(self):
        la = []
        laquery = QSqlQuery("SELECT list FROM CatAcces")
        while laquery.next():
            la.append(str(laquery.value('list')))
        self.comboAcces.addItems(la)

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

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    login = Login()

    if login.exec_() == QDialog.Accepted and user.acces == 'Lecture/Ecriture':
        window = Window()
        window.show()
        sys.exit(app.exec_())
    if login.exec_() == QDialog.Accepted and user.acces == 'Lecture':
        window = Window_readonly()
        window.show()
        sys.exit(app.exec_())
