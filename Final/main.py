"""

Fichier des opérations entre les class et l'interface

"""

# Importation des modules
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QRegExpValidator, QStandardItemModel, QStandardItem
from PyQt5.QtCore import QRegExp, QDir
from PyQt5.Qt   import QColor
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QFileDialog, QTableWidgetItem, QAbstractItemView
import re
import pandas as pd

from TABUI import Ui_Application
from classes import *


    # Fenêtre principale
class Window(Ui_Application, QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)


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
        self.tabMain.setTabText(0, "Personne ({})".format(len(Personne.listePersonne)))

    # Update de la liste des films
    def UpdateFilm(self):
        self.tabMain.setTabText(1, "Film ({})".format(len(Film.listeFilm)))

    # Bouton pour mettre à jour une personne (Présentement en test)
    def ModifPers(self):
        # search for the item
        print (cartedeCredits.listCC)


    ### Enregistrement de l'entré et remise à zero ### à retravailler
    def Validation(self):
        # inscription des informations dans les class correspondantes
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



#        cartedeCredits.numeroCC =
#        cartedeCredits.dateCC =
#        cartedeCredits.codeCC =

        # Valide si au moins les premières informations sont entrés
        while self.linePrenom.text() and self.lineNom.text() and self.sexeBtnG.checkedButton():
            # Si une des sections est coché, valider que celle-ci est remplie
            if self.cbClient.isChecked() or self.cbActeur.isChecked() or self.cbEmploye.isChecked():
                # Si le checkbox de la section client est coché, validation que les champs sont remplies
                if self.cbClient.isChecked():
                    # validation du courriel si vide skip
                    if self.lineCourriel.text():
                        regexmail = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
                        if re.search(regexmail, client.courriel):
                            print("Courriel valide")
                        # Si courriel non valide
                        else:
                            courrielMsg = QMessageBox()
                            courrielMsg.setIcon(QMessageBox.Warning)
                            courrielMsg.setInformativeText("Courriel invalide")
                            courrielMsg.setWindowTitle("Courriel Invalide")
                            courrielMsg.exec()
                            break

                    # Validation su le mot de passe correspont au standard de sécurité si vide skip mais nécessite aussi la présence d'un courriel
                    if self.linePwdClient.text() and self.lineCourriel.text():
                        password = client.clientPwd
                        if len(password) < 8:

                            print("Le mot de passe du client doit contenir au moins 8 caractères")
                            break
                        elif re.search('[0-9]', password) is None:
                            print("Le mot de passe du client doit contenir au moins 1 chiffre")
                            break
                        elif re.search('[A-Z]', password) is None:
                            print("Le mot de passe du client doit contenir au 1 majuscule")
                            break
                        else:
                            print("Le mot de passe entré est fonctionnel")
                            self.enregistrement()
                            break

                    # Message si des informations sont manquantes dans la section client
                    else:
                        clientMsg = QMessageBox()
                        clientMsg.setIcon(QMessageBox.Warning)
                        clientMsg.setInformativeText("Des informations sont manquantes dans la section client")
                        clientMsg.setWindowTitle("Avertissement")
                        clientMsg.exec()
                        break

                # Si le checkbox de la section Acteur est coché, validation que les champs sont remplies
                if self.cbActeur.isChecked():
                    if self.cbActeur.isChecked():
                        print("A valider si des informations sont à inscrire")
                        self.enregistrement()
                        break
                    else:
                        clientMsg = QMessageBox()
                        clientMsg.setIcon(QMessageBox.Warning)
                        clientMsg.setInformativeText("Des informations sont manquantes dans la section acteur")
                        clientMsg.setWindowTitle("Avertissement")
                        clientMsg.exec()
                        break

                # Si le checkbox de la section employe est coché, validation que les champs sont remplies
                if self.cbEmploye.isChecked():
                    # validation du username de l'employé si vide skip
                    if self.lineUsername.text():
                        if len(self.lineUsername.text()) < 8:
                           userMsg = QMessageBox()
                           userMsg.setIcon(QMessageBox.Warning)
                           userMsg.setInformativeText("Le username de l'employé doit contenir au moins 8 caractères")
                           userMsg.setWindowTitle("Avertissement")
                           userMsg.exec()
                           break

                    # Validation du mot de passe employe si vide skip
                    if self.linePwdClient.text():
                        password = employe.empPWD
                        if len(password) < 8:
                            print("Le mot de passe du client doit contenir au moins 8 caractères")
                            break
                        elif re.search('[0-9]', password) is None:
                            print("Le mot de passe du client doit contenir au moins 1 chiffre")
                            break
                        elif re.search('[A-Z]', password) is None:
                            print("Le mot de passe du client doit contenir au 1 majuscule")
                            break
                        else:
                            print("Le mot de passe entrer est correct")
                            self.enregistrement()
                            break

                    else:
                        empMsg = QMessageBox()
                        empMsg.setIcon(QMessageBox.Warning)
                        empMsg.setInformativeText("Des informations sont manquantes dans la section employée")
                        empMsg.setWindowTitle("Avertissement")
                        empMsg.exec()
                        break

            else:
                self.enregistrement()
                break


        # Si des champs sont manquantes.
        else:
            videMsg = QMessageBox()
            videMsg.setIcon(QMessageBox.Warning)
            videMsg.setInformativeText("Des informations sont manquantes sur la personne")
            videMsg.setWindowTitle("Avertissement")
            videMsg.exec()



    def enregistrement(self):

        #Nettoyage des données
        for item in self.changed_CC:
            self.QtableCC.blockSignals(True)
            item.setBackground(QColor("white"))
            self.QtableCC.blockSignals(False)
             #= item.text(), item.column(), item.row()

        #Enregistrement des données de la personnes dans un dictionnaire indexé
        Personne_dict = {
            'prenom': Personne.prenom,
            'nom': Personne.nom,
            'sexe': Personne.sexe,
            'dateInsc': client.dateInsc,
            'courriel': client.courriel,
            'clientPwd': client.clientPwd,
            'dateEmb': employe.dateEmb,
            'username': employe.username,
            'empPwD': employe.empPWD,
            'acces': employe.acces,
            'cbClient': self.cbClient.checkState(),
            'cbActeur': self.cbActeur.checkState(),
            'cbEmploye': self.cbEmploye.checkState(),
            'listCC' : cartedeCredits.CC()
        }

        Personne.listePersonne.append(Personne_dict)


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
        self.QtableCC.setRowCount(0)
        self.QtableChar.setRowCount(0)
        print(Personne.listePersonne)
        self.PersonneUpdate()

    ### Personne suivante dans la liste de Personne ###
    def suivantPers(self):
        print(Personne.positionPers)
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

        print (Personne.listePersonne)
        Personne.positionPers += 1

        if Personne.positionPers == len(Personne.listePersonne):
            Personne.positionPers = 0
        self.PersonneUpdate()

    ###Personne précédente dans la liste de Personne ###
    def precedentPers(self):
        print(Personne.positionPers)
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

    # Sauvegarde des données en excel avec Pandas
    def sauvegarder(self):

        # si la liste est vide, envoi un message d'erreur
        if not Personne.listePersonne :
            userMsg = QMessageBox()
            userMsg.setIcon(QMessageBox.Warning)
            userMsg.setInformativeText("Il ni a pas de données à sauvegarder")
            userMsg.setWindowTitle("Avertissement")
            userMsg.exec()

        # sauvegarde en fichier csv des listes personnes et film.
        if Personne.listePersonne:
            fileSave, _ = QFileDialog.getSaveFileName(self, "Sauvegarde", QDir.homePath() + "/data.csv",
                                                     "CSV files(*.csv);;All Files (*)")

#            fileSave, _ = QFileDialog.getSaveFileName(self, "Sauvegarde", QDir.homePath() + "/data.xlsx",
#                                                     "XLSM files(*.xlsx);;All Files (*)")

        if fileSave:
            dfp = pd.DataFrame(Personne.listePersonne)
            dfp.to_csv(fileSave)

#            dfp = pd.DataFrame(Personne.listePersonne)
#            dff = pd.DataFrame(Film.listeFilm)
#            writer = pd.ExcelWriter(fileSave)
#            dfp.to_excel(writer, sheet_name='Info', index=False)
#            dff.to_excel(writer, sheet_name='Film', index=False)
#            writer.save()

    ### Chargement des données CSV TODO : à revoir
    def charger(self):
#        df = pd.DataFrame
#        filepath, _ = QFileDialog.getOpenFileName(self,"Chargement des données", (QDir.homePath()),"XLSX Files *.xlsx")
        filepath, _ = QFileDialog.getOpenFileName(self,"Chargement des données", (QDir.homePath()),"CSV Files *.csv")


        if filepath:
            df = pd.read_csv(filepath, header=1)
            Personne.listePersonne =df
            print (Personne.listePersonne)

#            df1 = pd.read_excel(filepath, engine='openpyxl', header=0,  na_filter= False, sheet_name='Info')
#            df2 = pd.read_excel(filepath, engine='openpyxl', sheet_name='Film')
#            Personne.listePersonne = df1
#            Film.listeFilm = df2
#            print(Personne.listePersonne)
#            print(Film.listeFilm)

        self.UpdateFilm()
        self.PersonneUpdate()

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
        self.QtableCC.blockSignals(True)
        item.setBackground(QColor('red'))
        self.QtableCC.blockSignals(False)
        print (item.text(), item.column(), item.row())
        row = self.QtableCC.rowCount()
        column = self.QtableCC.columnCount()
        CC = []
        for r in range(row):
            for c in range(column):
                it = self.QtableCC.item(r,c)
                if it:
                    text = it.text()
                    CC.append(text)
                    print( CC, len(CC))
        cartedeCredits.CC = (CC)
#        column = 0
        # rowCount() This property holds the number of rows in the table
#        for row in range(self.QtableCC.rowCount()):
#                if item.column() == 0:
#                    cartedeCredits.numeroCC = (str(item.text()))
#                if item.column() == 1:
#                    cartedeCredits.dateCC = (str(item.text()))
#                if item.column() == 2:
#                    cartedeCredits.codeCC = (str(item.text()))

#        print (cartedeCredits.numeroCC, cartedeCredits.dateCC, cartedeCredits.codeCC)
#        for item.row() in item:
#            cartedeCredits.CCposition = len(cartedeCredits.listCC)
#            cartedeCredits.numeroCC = item.text()
#
#        self.changed_CC.append(str(item.text()))
#        print (self.changed_CC)
#        print (item.text(), item.column(), item.row())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Application = QtWidgets.QDialog()
    win = Window()
    win.show()
    sys.exit(app.exec())
