"""

Fichier des opérations entre les class et l'interface

"""

# Importation des modules
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog
import pandas as pd

from Acteurs import Ui_Acteurs
from cartedecredits import Ui_UI_CC
from TabGUI import Ui_Application
from classes import *


# Fenêtre de gestions des cartes de crédits
class WindowCC(Ui_UI_CC, QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        # bouton pour cacher la fenêtre
        self.btnCloseCC.clicked.connect(self.hide)
        # Sauvegardes des informations de cartes de crédit et affichage dans la fenêtre principale
        self.btnSaveCC.clicked.connect(self.newCC)


    # Fonction de sauvegarde des informations de cartes de crédit
    def newCC (self):
        cartedeCredits.numeroCC = self.NumeroCC.text()
        cartedeCredits.dateCC = self.expCC.text()
        cartedeCredits.codeCC = self.codesecretCC.text()

        #Sauvegarde des informations dans un dict

        CC_dict = {
            'Numero': cartedeCredits.numeroCC,
            'date': cartedeCredits.dateCC,
            'Codesecret': cartedeCredits.codeCC,
        }
        cartedeCredits.listCC.append(CC_dict)
#        Window.QtableCC = pd.DataFrame(data=cartedeCredits.listCC)
        self.dataCC = pd.DataFrame(cartedeCredits.listCC)# columns = ['Numero', 'Date d\'expiration', 'Code Secret'])
        self.modelCC = TableModelCC(self.dataCC) # changer le tableModel si besoin


        print (cartedeCredits.listCC)

    # Fenêtre de gestions des personnages des acteurs
class WindowActeurs(Ui_Acteurs, QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # bouton pour cacher la fenêtre
        self.btnCloseActeur.clicked.connect(self.hide)
        # Sauvegardes des informations des personnages joués et affichage dans la fenêtre principale
        self.btnSaveActeur.clicked.connect(self.newPers)

    # Fonction de sauvegarde des informations des personnages joués
    def newPers(self):
        acteurs.titreFilm = self.TitreduFilm.text()
        acteurs.personnage = self.NomPers.text()
        acteurs.debutEmploi = self.dateDebut.time()
        acteurs.finEmploi = self.DateFin.time()
        acteurs.cachet = self.cachet.text()

        # Sauvegarde des informations dans un dict
        Acteurs_dict = {
            'TitreFilm': acteurs.titreFilm,
            'Personnage' : acteurs.personnage,
            'dateDebut' : acteurs.debutEmploi,
            'dateFin': acteurs.finEmploi,
            'cachet': acteurs.cachet,
            }
        # Transfert du dictionnaire dans la listeActeurs
        acteurs.listeActeurs.append(Acteurs_dict)
        # Affichage des informations dans QtableActeurs

        print(acteurs.listeActeurs)


    # Fenêtre principale
class Window(Ui_Application, QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # Bouton pour modifier les personnages des acteurs
        self.btnGestionPers.clicked.connect(self.ouvrirActeurs)

        # Désactiver tant que la cb de la section client
        self.linePwdClient.setDisabled(True)
        self.dateInsc.setDisabled(True)
        self.lineCourriel.setDisabled(True)
        self.QtableCC.setDisabled(True)
        self.btnGestionCC.setDisabled(True)
        # Checkbox si la personne est Client, active la section client si coché
        self.cbClient.toggled.connect(self.QtableCC.setEnabled)
        self.cbClient.toggled.connect(self.dateInsc.setEnabled)
        self.cbClient.toggled.connect(self.lineCourriel.setEnabled)
        self.cbClient.toggled.connect(self.linePwdClient.setEnabled)
        self.cbClient.toggled.connect(self.btnGestionCC.setEnabled)
        # Bouton pour modifier les cartes de crédits
        self.btnGestionCC.clicked.connect(self.ouvrirCC)


        # Désactiver tant que la cb de la section désiré n'est pas coché
        self.dateEmb.setDisabled(True)
        self.lineUsername.setDisabled(True)
        self.linePwdEmp.setDisabled(True)
        self.comboAcces.setDisabled(True)
        self.QtableChar.setDisabled(True)
        self.btnGestionPers.setDisabled(True)

        # Echomode pour les Password
        self.linePwdClient.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.linePwdEmp.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)

        # Checkbox si la personne est artiste, active la section Artiste si coché
        self.cbActeur.toggled.connect(self.QtableChar.setEnabled)
        self.cbActeur.toggled.connect(self.btnGestionPers.setEnabled)
        # Checkbox si la personne est Client, active la section client si coché
        self.cbClient.toggled.connect(self.QtableCC.setEnabled)
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

        # Affichage des informations dans QtableCC
        self.dataCC = pd.DataFrame(cartedeCredits.listCC)# columns = ['Numero', 'Date d\'expiration', 'Code Secret'])
        self.modelCC = TableModelCC(self.dataCC)
        self.QtableCC.setModel(self.modelCC)

        # Affichage des informations dans QtableActeurs
        self.dataActeurs = pd.DataFrame (acteurs.listeActeurs)# columns = ['Numero', 'Date d\'expiration', 'Code Secret'])
        self.modelActeurs = TableModelCC(self.dataActeurs) # changer le tableModel si besoin
        self.QtableChar.setModel(self.modelActeurs)


    #### Fonctions ####

    # Enregistrement de l'entré et remise à zero des films TODO : à valider
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
        self.tabMain.setTabText(0, "Personne ({})".format(len(Personne.listePersonne)))

    # Update de la liste des films
    def UpdateFilm(self):
        self.tabMain.setTabText(1, "Film ({})".format(len(Film.listeFilm)))

    ### Enregistrement de l'entré et remise à zero ### à retravailler
    def NewEntrie(self):
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

        Personne_dict = {
            'prenom': Personne.prenom,
            'nom': Personne.nom,
            'sexe': Personne.sexe,
            'dateInsc': client.dateInsc,
            'courriel': client.courriel,
            'clientPwd' : client.clientPwd,
            'dateEmb' : employe.dateEmb,
            'username' : employe.username,
            'empPwD' : employe.empPWD,
            'acces' : employe.acces,
            'cbClient' : self.cbClient.checkState(),
            'cbActeur' : self.cbActeur.checkState(),
            'cbEmploye' : self.cbEmploye.checkState()
        }

        Personne.listePersonne.append(Personne_dict)
#        Personne.listePersonne.extend(cartedeCredits.listCC)
#        Personne.listePersonne.extend(acteurs.listeActeurs)

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
        print(Personne.listePersonne)
        self.PersonneUpdate()

    ### Personne suivante dans la liste de Personne ### TODO : à retravailler
    def suivantPers(self):
        print(Personne.positionPers)
#        print(Personne.listePersonne[Personne.positionPers]['sexe'])
        self.linePrenom.setText(Personne.listePersonne[Personne.positionPers]['prenom'])
        self.lineNom.setText(Personne.listePersonne[Personne.positionPers]['nom'])
        if Personne.listePersonne[Personne.positionPers]['sexe'] == -2:
            self.rbtnH.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['sexe'] == -3:
            self.rbtnF.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['sexe'] == -4:
            self.rbtnNA.setChecked(True)
        #Section client
        if Personne.listePersonne[Personne.positionPers]['cbClient'] == 2:
            self.cbClient.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['cbClient'] == 0:
            self.cbClient.setChecked(False)
        self.dateInsc.setDate(Personne.listePersonne[Personne.positionPers]['dateInsc'])
        self.lineCourriel.setText(Personne.listePersonne[Personne.positionPers]['courriel'])
        self.linePwdClient.setText(Personne.listePersonne[Personne.positionPers]['clientPwd'])
        #Section Acteurs
        if Personne.listePersonne[Personne.positionPers]['cbActeur'] == 2:
            self.cbActeur.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['cbActeur'] == 0:
            self.cbActeur.setChecked(False)
        #Section employé
        if Personne.listePersonne[Personne.positionPers]['cbEmploye'] == 2:
            self.cbEmploye.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['cbEmploye'] == 0:
            self.cbEmploye.setChecked(False)
        self.dateEmb.setDate(Personne.listePersonne[Personne.positionPers]['dateEmb']),
        self.lineUsername.setText(Personne.listePersonne[Personne.positionPers]['username']),
        self.linePwdEmp.setText(Personne.listePersonne[Personne.positionPers]['empPwD']),
        self.comboAcces.setCurrentIndex(Personne.listePersonne[Personne.positionPers]['acces'])

        # Affichage des informations dans QtableCC
        self.dataCC = pd.DataFrame (cartedeCredits.listCC)# columns = ['Numero', 'Date d\'expiration', 'Code Secret'])
        self.modelCC = TableModelCC(self.dataCC) # TODO : changer le tableModel si besoin
        self.QtableCC.setModel(self.modelCC)

        Personne.positionPers += 1

        if Personne.positionPers == len(Personne.listePersonne):
            Personne.positionPers = 0
        self.PersonneUpdate()

    ###Personne précédente dans la liste de Personne ### TODO : à retravailler
    def precedentPers(self):
        print(Personne.positionPers)
        #        print(Personne.listePersonne[Personne.positionPers]['sexe'])
        self.linePrenom.setText(Personne.listePersonne[Personne.positionPers]['prenom'])
        self.lineNom.setText(Personne.listePersonne[Personne.positionPers]['nom'])
        if Personne.listePersonne[Personne.positionPers]['sexe'] == -2:
            self.rbtnH.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['sexe'] == -3:
            self.rbtnF.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['sexe'] == -4:
            self.rbtnNA.setChecked(True)
        # Section client
        if Personne.listePersonne[Personne.positionPers]['cbClient'] == 2:
            self.cbClient.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['cbClient'] == 0:
            self.cbClient.setChecked(False)
        self.dateInsc.setDate(Personne.listePersonne[Personne.positionPers]['dateInsc'])
        self.lineCourriel.setText(Personne.listePersonne[Personne.positionPers]['courriel'])
        self.linePwdClient.setText(Personne.listePersonne[Personne.positionPers]['clientPwd'])
        #Section Acteurs
        if Personne.listePersonne[Personne.positionPers]['cbActeur'] == 2:
            self.cbActeur.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['cbActeur'] == 0:
            self.cbActeur.setChecked(False)
        #Section employé
        if Personne.listePersonne[Personne.positionPers]['cbEmploye'] == 2:
            self.cbEmploye.setChecked(True)
        if Personne.listePersonne[Personne.positionPers]['cbEmploye'] == 0:
            self.cbEmploye.setChecked(False)
        self.dateEmb.setDate(Personne.listePersonne[Personne.positionPers]['dateEmb']),
        self.lineUsername.setText(Personne.listePersonne[Personne.positionPers]['username']),
        self.linePwdEmp.setText(Personne.listePersonne[Personne.positionPers]['empPwD']),
        self.comboAcces.setCurrentIndex(Personne.listePersonne[Personne.positionPers]['acces'])

        # Affichage des informations dans QtableCC
        self.dataCC = pd.DataFrame (cartedeCredits.listCC)# columns = ['Numero', 'Date d\'expiration', 'Code Secret'])
        self.modelCC = TableModelCC(self.dataCC) # TODO :  changer le tableModel si besoin
        self.QtableCC.setModel(self.modelCC)

        Personne.positionPers -= 1

        if Personne.positionPers < 0:
            Personne.positionPers = len(Personne.listePersonne) - 1
        self.PersonneUpdate()

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

    # Sauvegarde des données en CSV avec pandas TODO : à revoir
    def sauvegarder(self):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Sauvegarder", "%username%/Documents/Data.csv",
                                                            "Fichiers csv (*.csv)")
        if fileName:
            df = pd.DataFrame(Film.listeFilm, Personne.listePersonne)
            df.to_csv('data.csv')
            print(fileName)

    ### Chargement des données CSV TODO : à revoir
    def charger(self):
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "", "Fichiers CSV (*.csv)")
        if files:
            df = pd.read_csv('data.csv', index_col='Personne', parse_dates='', header=0, names=['Prenom', 'Nom', 'Sexe'])
#            Film.listeFilm, Personne.listePersonne = df
            print(files)
        self.UpdateFilm()
        self.PersonneUpdate()

    ### ouvrir la fenêtre de modification des cartes de crédits
    def ouvrirCC(self):
        FenetreCC = WindowCC()
        FenetreCC.exec_()

    ### ouvrir la fenêtre de modification des cartes des acteurs
    def ouvrirActeurs(self):
        FenetreActeurs = WindowActeurs()
        FenetreActeurs.exec_()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Application = QtWidgets.QDialog()
    win = Window()
    win.show()
    sys.exit(app.exec())
