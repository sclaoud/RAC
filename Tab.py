# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#Importation des modules
from PyQt5.QtWidgets import QMessageBox
#   QMessageBox n'était pas importer depuis QtWidgets et doit être forcer ainsi que filedialog
from PyQt5 import QtCore, QtGui, QtWidgets

#from classes import Personne
from classes2 import *



class Ui_Application(object):
    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(1087, 627)
        Application.setSizeGripEnabled(True)
        self.tabMain = QtWidgets.QTabWidget(Application)
        self.tabMain.setGeometry(QtCore.QRect(30, 30, 991, 531))
        self.tabMain.setObjectName("tabMain")


#### DÉBUT DE LA TAB PERSONNE ####

        self.tabPersonne = QtWidgets.QWidget()
        self.tabPersonne.setObjectName("tabPersonne")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabPersonne)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 140, 871, 147))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

    #### Début de la section client ####
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)

    # Lineedit contenant la date d'inscription du client
        self.lineDateInsc = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineDateInsc.setObjectName("lineDateInsc")
        # Désactiver tant que la cb n'est pas coché
        self.lineDateInsc.setDisabled(True)
        self.verticalLayout_2.addWidget(self.lineDateInsc)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)

    # Lineedit contenant le courriel du client
        self.lineCourriel = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineCourriel.setObjectName("lineCourriel")
        # Désactiver tant que la cb n'est pas coché
        self.lineCourriel.setDisabled(True)
        self.verticalLayout_3.addWidget(self.lineCourriel)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)

    # LineEdit contenant le mot de passe du client
        self.linePwdClient = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.linePwdClient.setObjectName("linePwdClient")
        ### Display characters as they are entered while editing otherwise display characters as with Password. ### à tester
        self.linePwdClient.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        # Désactiver tant que la cb n'est pas coché
        self.linePwdClient.setDisabled(True)
        self.verticalLayout_4.addWidget(self.linePwdClient)

    #### Début de la section carte de crédits ####

        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_13.addWidget(self.label_15)

    # List contenant les numeros de carte de crédits des clients
        self.listCarteCredits = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listCarteCredits.setObjectName("listCarteCredits")
        # Désactiver tant que la cb n'est pas coché
        self.listCarteCredits.setDisabled(True)
        self.verticalLayout_13.addWidget(self.listCarteCredits)
        self.horizontalLayout_7.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_14.addWidget(self.label_16)

    # Lineedit contenant la date d'expiration de la carte de crédit
        self.lineDateExp = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineDateExp.setObjectName("lineDateExp")
        # Désactiver tant que la cb n'est pas coché
        self.lineDateExp.setDisabled(True)
        self.verticalLayout_14.addWidget(self.lineDateExp)
        self.horizontalLayout_7.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_15.addWidget(self.label_17)

    # Lineedit contenant le code secret de la carte de crédit
        self.lineCode = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineCode.setObjectName("lineCode")
        # Désactiver tant que la cb n'est pas coché
        self.lineCode.setDisabled(True)
        self.verticalLayout_15.addWidget(self.lineCode)
        self.horizontalLayout_7.addLayout(self.verticalLayout_15)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

    #### Section des informations de la personne dans le haut / classe Parent ####

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tabPersonne)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(330, 30, 621, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_16.addWidget(self.label_18)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_16.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_16.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")

    # Lineedit contenant le Prenom de la personne
        self.linePrenom = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.linePrenom.setObjectName("linePrenom")
        self.linePrenom.setText(str("Inscrire le prénom"))
        #Maximum de 40 Caractere
        self.linePrenom.setMaxLength(40)
        self.verticalLayout_17.addWidget(self.linePrenom)
        self.linePrenom = Personne.prenom(self)

    # Lineedit contenant le Nom de la personne
        self.lineNom = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineNom.setObjectName("lineNom")
        self.lineNom.setText('Inscrire le nom')
        #Maximum de 40 Caractere
        self.lineNom.setMaxLength(40)
        self.verticalLayout_17.addWidget(self.lineNom)
        self.lineNom = Personne.nom(self)

    # RadioButton du choix de sexe de la personne
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # Choix homme
        self.rdSexeHomme = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rdSexeHomme.setObjectName("rdSexeHomme")
        self.horizontalLayout_2.addWidget(self.rdSexeHomme)
        # choix Femme
        self.rdSexeFemme = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rdSexeFemme.setObjectName("rdSexeFemme")
        self.horizontalLayout_2.addWidget(self.rdSexeFemme)
        # Préfère ne pas répondre
        self.rdSexeAlien = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rdSexeAlien.setObjectName("rdSexeAlien")
        self.horizontalLayout_2.addWidget(self.rdSexeAlien)
        self.verticalLayout_17.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_17)


    #### Section des boutons Nouveau/Supprimer dans un vertical layout (suivant/precedent à part) ####

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tabPersonne)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(160, 20, 160, 112))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")

    # Bouton pour créer une nouvelle entrée
        self.btnNouveau = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnNouveau.setObjectName("btnNouveau")
        self.btnNouveau.clicked.connect(self.NewEntrie)
        self.verticalLayout_18.addWidget(self.btnNouveau)

    # Bouton pour supprimer une entrée
        self.btnSupprimer = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnSupprimer.setObjectName("btnSupprimer")
        self.verticalLayout_18.addWidget(self.btnSupprimer)

        #### Debut de la section Artiste ####

        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tabPersonne)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(80, 300, 871, 121))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)

    # Liste des personnages jouer par l'artiste
        self.listChar = QtWidgets.QListWidget(self.horizontalLayoutWidget_5)
        self.listChar.setObjectName("listChar")
        # Désactiver tant que la cb n'est pas coché
        self.listChar.setDisabled(True)
        self.verticalLayout_5.addWidget(self.listChar)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)

    # Lineedit du debut d'emploi de l'artiste
        self.lineDebutEmploi = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineDebutEmploi.setObjectName("lineDebutEmploi")
        # Désactiver tant que la cb n'est pas coché
        self.lineDebutEmploi.setDisabled(True)
        self.verticalLayout_6.addWidget(self.lineDebutEmploi)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)

    # Lineedit de la date de fin d'emploi de l'artiste
        self.lineFinEmploi = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineFinEmploi.setObjectName("lineFinEmploi")
        # Désactiver tant que la cb n'est pas coché
        self.lineFinEmploi.setDisabled(True)
        self.verticalLayout_7.addWidget(self.lineFinEmploi)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)

    # Lineedit du cachet de l'artiste
        self.lineCachet = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineCachet.setObjectName("lineCachet")
        # Désactiver tant que la cb n'est pas coché
        self.lineCachet.setDisabled(True)
        self.verticalLayout_8.addWidget(self.lineCachet)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        #### Debut de la section employé ####

        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tabPersonne)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(80, 440, 871, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)

    # Lineedit de la date d'embauche de l'employé
        self.lineDateEmb = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineDateEmb.setObjectName("lineDateEmb")
        # Désactiver tant que la cb n'est pas coché
        self.lineDateEmb.setDisabled(True)
        self.verticalLayout_9.addWidget(self.lineDateEmb)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)

    # Lineedit du username de l'employé
        self.lineUsername = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineUsername.setObjectName("lineUsername")
        # Désactiver tant que la cb n'est pas coché
        self.lineUsername.setDisabled(True)
        self.verticalLayout_10.addWidget(self.lineUsername)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_11.addWidget(self.label_13)

    # Lineedit du mot de passe de l'employé
        self.linePwdEmp = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.linePwdEmp.setObjectName("linePwdEmp")
        # Display characters as they are entered while editing otherwise display characters as with Password.
        self.linePwdEmp.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        # Désactiver tant que la cb n'est pas coché
        self.linePwdEmp.setDisabled(True)
        self.verticalLayout_11.addWidget(self.linePwdEmp)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_12.addWidget(self.label_14)

    # Lineedit des accès d'un employé
        self.lineAccess = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineAccess.setObjectName("lineAccess")
        # Désactiver tant que la cb n'est pas coché
        self.lineAccess.setDisabled(True)
        self.verticalLayout_12.addWidget(self.lineAccess)
        self.horizontalLayout_6.addLayout(self.verticalLayout_12)

    #### Section checkbox ####

    # Checkbox si la personne est artiste, active la section Artiste si coché
        self.cbActeur = QtWidgets.QCheckBox(self.tabPersonne)
        self.cbActeur.setGeometry(QtCore.QRect(10, 310, 55, 17))
        self.cbActeur.setObjectName("cbActeur")
        self.cbActeur.toggled.connect(self.listChar.setEnabled)
        self.cbActeur.toggled.connect(self.lineDebutEmploi.setEnabled)
        self.cbActeur.toggled.connect(self.lineFinEmploi.setEnabled)
        self.cbActeur.toggled.connect(self.lineCachet.setEnabled)

    # Checkbox si la personne est Client, active la section client si coché
        self.cbClient = QtWidgets.QCheckBox(self.tabPersonne)
        self.cbClient.setGeometry(QtCore.QRect(10, 140, 50, 17))
        self.cbClient.setObjectName("cbClient")
        self.cbClient.toggled.connect(self.listCarteCredits.setEnabled)
        self.cbClient.toggled.connect(self.lineDateInsc.setEnabled)
        self.cbClient.toggled.connect(self.lineCourriel.setEnabled)
        self.cbClient.toggled.connect(self.linePwdClient.setEnabled)
        self.cbClient.toggled.connect(self.lineDateExp.setEnabled)
        self.cbClient.toggled.connect(self.lineCode.setEnabled)

    # Checkbox si la personne est employé, active la section employé si coché
        self.cbEmploye = QtWidgets.QCheckBox(self.tabPersonne)
        self.cbEmploye.setGeometry(QtCore.QRect(10, 450, 63, 17))
        self.cbEmploye.setObjectName("cbEmploye")
        self.tabMain.addTab(self.tabPersonne, "")
        self.cbEmploye.toggled.connect(self.lineDateEmb.setEnabled)
        self.cbEmploye.toggled.connect(self.lineUsername.setEnabled)
        self.cbEmploye.toggled.connect(self.linePwdEmp.setEnabled)
        self.cbEmploye.toggled.connect(self.lineAccess.setEnabled)


    # Bouton Précédent de la tab Personne
        self.btnPrecedent = QtWidgets.QPushButton(self.tabPersonne)
        self.btnPrecedent.setGeometry(QtCore.QRect(60, 70, 31, 23))
        self.btnPrecedent.setObjectName("btnPrecedent")

    # Bouton Suivant de la tab Personne
        self.btnSuivant = QtWidgets.QPushButton(self.tabPersonne)
        self.btnSuivant.setGeometry(QtCore.QRect(110, 70, 31, 23))
        self.btnSuivant.setObjectName("btnSuivant")




#### DEBUT DE LA TAB FILMS ####
        self.tabFilms = QtWidgets.QWidget()
        self.tabFilms.setObjectName("tabFilms")

    # Bouton précédent de la tab Films
        self.btnPrecedent_2 = QtWidgets.QPushButton(self.tabFilms)
        self.btnPrecedent_2.setGeometry(QtCore.QRect(50, 140, 31, 23))
        self.btnPrecedent_2.setObjectName("btnPrecedent_2")

    # Bouton Suivant de la tab Films
        self.btnSuivant_2 = QtWidgets.QPushButton(self.tabFilms)
        self.btnSuivant_2.setGeometry(QtCore.QRect(110, 140, 31, 23))
        self.btnSuivant_2.setObjectName("btnSuivant_2")

    ## Layout vertical contenant les boutons nouveaux et supprimer
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tabFilms)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 160, 112))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")

    # Bouton pour enregistrer une nouvelle entrée Film
        self.btnNouveau_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnNouveau_3.setObjectName("btnNouveau_3")
        self.verticalLayout_21.addWidget(self.btnNouveau_3)
        self.btnNouveau_3.clicked.connect(self.newFilm)

    # Bouton pour supprimer l'entré film sélectionné
        self.btnSupprimer_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnSupprimer_3.setObjectName("btnSupprimer_3")
        self.verticalLayout_21.addWidget(self.btnSupprimer_3)

    ## Layout vertical contenant les informations du films
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tabFilms)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(220, 20, 211, 171))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")

    # Lineedit Contenant le titre du film
        self.lineFilm_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineFilm_2.setObjectName("lineFilm_2")
        self.lineFilm_2.setText('Inscrire le titre du film')
        self.verticalLayout_22.addWidget(self.lineFilm_2)
        self.lineFilm_2 = film.nomFilm(self)

    # Lineedit avec la durée du film
        self.dureeFilm = QtWidgets.QTimeEdit(self.verticalLayoutWidget_4)
        self.dureeFilm.setObjectName("dureeFilm")
        self.verticalLayout_22.addWidget(self.dureeFilm)
        self.dureeFilm = film.catFilm(self)

    # TextEdit contenant une description du film
        self.textDescFilm_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.textDescFilm_2.setObjectName("textDescFilm_2")
        self.textDescFilm_2.setText('Inscrire la synopsie du film')
        self.verticalLayout_22.addWidget(self.textDescFilm_2)
        self.textDescFilm_2 = film.descFilm(self)

    ## Grid layout contenant les checkbox des catégories de films
        self.label_2 = QtWidgets.QLabel(self.tabFilms)
        self.label_2.setGeometry(QtCore.QRect(520, 10, 111, 20))
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.tabFilms)
        self.widget.setGeometry(QtCore.QRect(470, 30, 211, 161))
        self.widget.setObjectName("widget")
        self.GLCatFilm = QtWidgets.QGridLayout(self.widget)
        self.GLCatFilm.setContentsMargins(0, 0, 0, 0)
        self.GLCatFilm.setObjectName("GLCatFilm")
    # checkbot catégorie de film animation
        self.cbCatAnim = QtWidgets.QCheckBox(self.widget)
        self.cbCatAnim.setObjectName("cbCatAnim")
        self.GLCatFilm.addWidget(self.cbCatAnim, 0, 0, 1, 1)
    # checkbot catégorie de film Fantastique
        self.cbCatFan = QtWidgets.QCheckBox(self.widget)
        self.cbCatFan.setObjectName("cbCatFan")
        self.GLCatFilm.addWidget(self.cbCatFan, 2, 0, 1, 1)
    # checkbot catégorie de film Science-Fiction
        self.cbCatSF = QtWidgets.QCheckBox(self.widget)
        self.cbCatSF.setObjectName("cbCatSF")
        self.GLCatFilm.addWidget(self.cbCatSF, 2, 1, 1, 1)
    # checkbot catégorie de film horreur
        self.cbCatHorreur = QtWidgets.QCheckBox(self.widget)
        self.cbCatHorreur.setObjectName("cbCatHorreur")
        self.GLCatFilm.addWidget(self.cbCatHorreur, 3, 0, 1, 1)
    # checkbot catégorie de film Drame
        self.cbCatDrame = QtWidgets.QCheckBox(self.widget)
        self.cbCatDrame.setObjectName("cbCatDrame")
        self.GLCatFilm.addWidget(self.cbCatDrame, 1, 1, 1, 1)
    # checkbot catégorie de film Thriller
        self.cbCatThriller = QtWidgets.QCheckBox(self.widget)
        self.cbCatThriller.setObjectName("cbCatThriller")
        self.GLCatFilm.addWidget(self.cbCatThriller, 3, 1, 1, 1)
        self.cbCatDoc = QtWidgets.QCheckBox(self.widget)
    # checkbot catégorie de film documentaire
        self.cbCatDoc.setObjectName("cbCatDoc")
        self.GLCatFilm.addWidget(self.cbCatDoc, 1, 0, 1, 1)
    # checkbot catégorie de film comédie
        self.cbCatCom = QtWidgets.QCheckBox(self.widget)
        self.cbCatCom.setObjectName("cbCatCom")
        self.GLCatFilm.addWidget(self.cbCatCom, 0, 1, 1, 1)

        self.tabMain.addTab(self.tabFilms, "")

    # Bouton de fermeture lancant un QMessageBox de confirmation
        self.btnFermer = QtWidgets.QPushButton(Application)
        self.btnFermer.setGeometry(QtCore.QRect(940, 570, 75, 23))
        self.btnFermer.setObjectName("btnFermer")
        self.btnFermer.clicked.connect(self.closeEvent)

     # Bouton de sauvegarde des données
        self.btnSauvegarder = QtWidgets.QPushButton(Application)
        self.btnSauvegarder.setGeometry(QtCore.QRect(540, 570, 158, 23))
        self.btnSauvegarder.setObjectName("btnSauvegarder")
        self.btnSauvegarder.clicked.connect(self.sauvegarder)

    # Bouton de chargement des données
        self.btnCharger = QtWidgets.QPushButton(Application)
        self.btnCharger.setGeometry(QtCore.QRect(700, 570, 158, 23))
        self.btnCharger.setObjectName("btnCharger")
        self.btnCharger.clicked.connect(self.charger)

        self.retranslateUi(Application)
        self.tabMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Application)

    def retranslateUi(self, Application):
        _translate = QtCore.QCoreApplication.translate
        Application.setWindowTitle(_translate("Application", "Dialog"))
        self.label_4.setText(_translate("Application", "Date d\'inscription"))
        self.label_5.setText(_translate("Application", "courriel"))
        self.label_6.setText(_translate("Application", "Mot de passe"))
        self.label_15.setText(_translate("Application", "Numero de carte"))
        self.label_16.setText(_translate("Application", "Date d\'expiration"))
        self.label_17.setText(_translate("Application", "Code secret"))
        self.label_18.setText(_translate("Application", "Prenom"))
        self.label.setText(_translate("Application", "Nom"))
        self.label_3.setText(_translate("Application", "Sexe"))
        self.rdSexeHomme.setText(_translate("Application", "Homme"))
        self.rdSexeFemme.setText(_translate("Application", "Femme"))
        self.rdSexeAlien.setText(_translate("Application", "Préfère ne pas répondre"))
        self.btnPrecedent.setText(_translate("Application", "<"))
        self.btnNouveau.setText(_translate("Application", "Nouveau"))
        self.btnSupprimer.setText(_translate("Application", "Supprimer"))
        self.label_7.setText(_translate("Application", "Personnages joués dans les films"))
        self.label_8.setText(_translate("Application", "Début d\'emploi"))
        self.label_9.setText(_translate("Application", "Fin d\'emploi"))
        self.label_10.setText(_translate("Application", "Cachet"))
        self.label_11.setText(_translate("Application", "Date d\'embauche"))
        self.label_12.setText(_translate("Application", "code utilisateur"))
        self.label_13.setText(_translate("Application", "Mot de passe"))
        self.label_14.setText(_translate("Application", "Type d\'accès"))
        self.cbActeur.setText(_translate("Application", "Artiste"))
        self.cbClient.setText(_translate("Application", "Client"))
        self.btnSuivant.setText(_translate("Application", ">"))
        self.cbEmploye.setText(_translate("Application", "Employé"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabPersonne), _translate("Application", "Personne"))
        self.btnPrecedent_2.setText(_translate("Application", "<"))
        self.btnSuivant_2.setText(_translate("Application", ">"))
        self.btnNouveau_3.setText(_translate("Application", "Nouveau"))
        self.btnSupprimer_3.setText(_translate("Application", "Supprimer"))
        self.label_2.setText(_translate("Application", "Catégories du film"))
        self.cbCatAnim.setText(_translate("Application", "Animation"))
        self.cbCatFan.setText(_translate("Application", "Fantaisie"))
        self.cbCatSF.setText(_translate("Application", "Science-Fiction"))
        self.cbCatHorreur.setText(_translate("Application", "Horreur"))
        self.cbCatDrame.setText(_translate("Application", "Drame"))
        self.cbCatThriller.setText(_translate("Application", "Thriller"))
        self.cbCatDoc.setText(_translate("Application", "Documentaire"))
        self.cbCatCom.setText(_translate("Application", "Comédie"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabFilms), _translate("Application", "Films"))
        self.btnFermer.setText(_translate("Application", "Fermer"))
        self.btnSauvegarder.setText(_translate("Application", "Sauvegarder"))
        self.btnCharger.setText(_translate("Application", "Charger"))

#### Fonctions des classes ####

 ### Enregistrement de l'entré et remise à zero des films ###
    def newFilm(self):
        self.Film.catFilm.setText("")



 ### Enregistrement de l'entré et remise à zero ### à retravailler
    def NewEntrie(self):
        Personne.set_sexe()
#        if self.rdSexeAlien.isChecked():
#            return rdValue = c
#        elif self.rdSexeFemme.isChecked():
#            return rdValue = b
#        elif self.rdSexeHomme.isChecked():
#            return rdValue = a

        self.linePrenom.setText("")
        self.lineNom.setText("")
        self.rdSexeHomme.setChecked(False)
        self.rdSexeFemme.setChecked(False)
        self.rdSexeAlien.setChecked(False)
        self.cbClient.setChecked(False)
        self.cbEmploye.setChecked(False)
        self.cbActeur.setChecked(False)
        self.lineDateInsc.setText("")
        self.lineCourriel.setText("")
        self.linePwdClient.setText("")
#        self.listCarteCredits.setText("")
        self.lineDateExp.setText("")
        self.lineCode.setText("")
#        self.listChar.setText("")
        self.lineDebutEmploi.setText("")
        self.lineFinEmploi.setText("")
        self.lineCachet.setText("")
        self.lineDateEmb.setText("")
        self.lineUsername.setText("")
        self.linePwdEmp.setText("")
        self.lineAccess.setText("")




 ### Personne suivante dans la liste de Personne ### à retravailler
    def suivantPers(self):
        # print(self.positionListe)
        self.prenomTxt.set(self.ListeDePersonnes[self.positionListe].prenom)
        self.nomTxt.set(self.ListeDePersonnes[self.positionListe].nom)
        self.positionListe += 1

        if self.positionListe == len(self.ListeDePersonnes):
            self.positionListe = 0
        self.contactsUpdate()

 ###Personne précédente dans la liste de Personne ### À retravailler
    def precedentPers(self):
        print(self.positionListe)
        self.prenomTxt.set(self.ListeDePersonnes[self.positionListe].prenom)
        self.nomTxt.set(self.ListeDePersonnes[self.positionListe].nom)
        self.positionListe -=1
        print(self.positionListe)
        if self.positionListe < 0:
            self.positionListe = len(self.ListeDePersonnes)-1
        self.contactsUpdate()

 ###Film suivant dans la liste de Film ### À retravailler
    def suivantFilm(self):
        # print(self.positionListe)
        self.prenomTxt.set(self.ListeDePersonnes[self.positionListe].prenom)
        self.nomTxt.set(self.ListeDePersonnes[self.positionListe].nom)
        self.positionListe += 1

        if self.positionListe == len(self.ListeDePersonnes):
            self.positionListe = 0
        self.filmUpdate()

 ###Film précédent dans la liste de film ### À retravailler
    def precedentFilm(self):
        print(self.positionListe)
        self.prenomTxt.set(self.ListeDePersonnes[self.positionListe].prenom)
        self.nomTxt.set(self.ListeDePersonnes[self.positionListe].nom)
        self.positionListe -=1
        print(self.positionListe)
        if self.positionListe < 0:
            self.positionListe = len(self.ListeDePersonnes)-1
        self.FilmUpdate()

 ### Met à jour le nombre de personne dans le système ### À retravailler
    def PersonneUpdate(self):
        self.tabPersonne = QtWidgets.QTabWidget.setTabText("Personne ({})".format(len(self.listPersonne)))


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
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

 ### Chargement à retravailler ###
    def charger(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, "r")
        self.ListeDePersonnes = file.load(file)
        file.close()
        self.contactsUpdate()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Application = QtWidgets.QDialog()
    ui = Ui_Application()
    ui.setupUi(Application)
    Application.show()
    sys.exit(app.exec_())
