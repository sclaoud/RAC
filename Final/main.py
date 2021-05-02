"""

Fichier des opérations entre les class et l'interface

"""

# Importation des modules
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp, QDir
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QFileDialog
import re
import csv

from TABGUI import Ui_Application
from classes import *

"""
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
"""

    # Fenêtre principale
class Window(Ui_Application, QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        #validation des lignes avec limitations textes/chiffres uniquements
        regexText = QRegExpValidator(QRegExp(r'^[a-zA-Z]*$'))
        regexnum = QRegExpValidator(QRegExp(r'[0-9]+'))
        self.lineNom.setValidator(regexText)
        self.linePrenom.setValidator(regexText)

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

        # Bouton pour ajouter d'une rangé dans Qtablechar
        self.btnAjoutPers.clicked.connect(self.AjoutPers)
        # Bouton pour supprimer la rangé Qtablechar
        self.btnSuppPers.clicked.connect(self.SuppPers)

        # Bouton pour ajouter une ranger dans la QtableCC
        self.btnAjoutCC.clicked.connect(self.AjoutCC)
        # Bouton pour supprimer une ranger dans la QtableCC
        self.btnSuppCC.clicked.connect(self.SuppCC)


        # Désactiver tant que la cb de la section désiré n'est pas coché
        self.dateEmb.setDisabled(True)
        self.lineUsername.setDisabled(True)
        self.linePwdEmp.setDisabled(True)
        self.comboAcces.setDisabled(True)
        self.QtableChar.setDisabled(True)
        self.btnAjoutPers.setDisabled(True)
        self.linePwdClient.setDisabled(True)
        self.dateInsc.setDisabled(True)
        self.lineCourriel.setDisabled(True)
        self.QtableCC.setDisabled(True)
        self.btnAjoutCC.setDisabled(True)
        self.btnSuppCC.setDisabled(True)
        self.btnSuppPers.setDisabled(True)

        # Echomode pour les Password
        self.linePwdClient.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.linePwdEmp.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)

        # Checkbox si la personne est artiste, active la section Artiste si coché
        self.cbActeur.toggled.connect(self.QtableChar.setEnabled)
        self.cbActeur.toggled.connect(self.btnAjoutPers.setEnabled)
        self.cbActeur.toggled.connect(self.btnSuppPers.setEnabled)
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
            'cbEmploye': self.cbEmploye.checkState()
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
        print(Personne.listePersonne)
        self.PersonneUpdate()

    ### Personne suivante dans la liste de Personne ### TODO : à retravailler
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

        # Affichage des informations dans QtableCC TODO: refaire l'affichage


        Personne.positionPers += 1

        if Personne.positionPers == len(Personne.listePersonne):
            Personne.positionPers = 0
        self.PersonneUpdate()

    ###Personne précédente dans la liste de Personne ### TODO : à retravailler
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

        # Affichage des informations dans QtableCC TODO: refaire l'affichage


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

    # Sauvegarde des données en CSV avec module CSV
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
            if fileSave:
                with open(fileSave, mode="w", encoding="utf-8", newline="") as file:
                    writer = csv.writer(file, dialect='excel')
                    writer.writerow(Personne.listePersonne)
                    writer.writerow(Film.listeFilm)
                file.close()


    ### Chargement des données CSV TODO : à revoir
    def charger(self):
        fileLoad, _ = QFileDialog.getOpenFileNames(self,"Chargement des données", (QDir.homePath()),"CSV Files (*.csv);;All Files (*)")

        file_path = Path.home() / "data.csv"
        file = file_path.open(mode="r", encoding="utf-8", newline="")
        reader = csv.reader(file)
        row1 = next(reader)
        Personne.listePersonne = row1
        print (Personne.listePersonne)
        row2 = next(reader)
        Film.listeFilm = row2
        print (Film.listeFilm)


        self.UpdateFilm()
        self.PersonneUpdate()

    # Ajout d'une nouvelle rangée pour inscrire une nouvelle carte de crédit
    def AjoutCC(self):
        rowPosition = self.QtableCC.rowCount()
        self.QtableCC.insertRow(rowPosition)

    # Supprimer la rangée d'une carte de crédit TODO: Non-fonctionnel
    def SuppCC(self):
        model = self.model
        indices = self.QtableCC.selectionModel().selectedRows()
        for index in sorted(indices):
            model.removeRow(index.row())


     #Ajout d'une nouvelle rangée pour inscrire un nouveau personnage d'acteur
    def AjoutPers(self):
        rowPosition = self.QtableChar.rowCount()
        self.QtableChar.insertRow(rowPosition)

    # Supprimer la rangée d'un personnage d'acteur TODO: Non-fonctionnel
    def SuppPers(self):
        model = self.model
        indices = self.QtableChar.selectionModel().selectedRows()
        for index in sorted(indices):
            model.removeRow(index.row())

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Application = QtWidgets.QDialog()
    win = Window()
    win.show()
    sys.exit(app.exec())
