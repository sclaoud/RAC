# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#Importation des modules
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
#   QMessageBox n'était pas importer depuis QtWidgets et doit être forcer ainsi que filedialog
from classes import *


class Ui_Application(object):
    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(1087, 627)
        Application.setSizeGripEnabled(True)
        self.tabMain = QtWidgets.QTabWidget(Application)
        self.tabMain.setGeometry(QtCore.QRect(30, 30, 991, 531))
        self.tabMain.setObjectName("tabMain")
        self.tabPersonne = QtWidgets.QWidget()
        self.tabPersonne.setObjectName("tabPersonne")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabPersonne)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 140, 871, 147))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lineDateInsc = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineDateInsc.setObjectName("lineDateInsc")
        self.verticalLayout_2.addWidget(self.lineDateInsc)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.lineCourriel = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineCourriel.setObjectName("lineCourriel")
        self.verticalLayout_3.addWidget(self.lineCourriel)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.linePwdClient = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.linePwdClient.setObjectName("linePwdClient")
        self.verticalLayout_4.addWidget(self.linePwdClient)
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
        self.listCarteCredits = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listCarteCredits.setObjectName("listCarteCredits")
        self.verticalLayout_13.addWidget(self.listCarteCredits)
        self.horizontalLayout_7.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_14.addWidget(self.label_16)
        self.lineDateExp = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineDateExp.setObjectName("lineDateExp")
        self.verticalLayout_14.addWidget(self.lineDateExp)
        self.horizontalLayout_7.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_15.addWidget(self.label_17)
        self.lineCode = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineCode.setObjectName("lineCode")
        self.verticalLayout_15.addWidget(self.lineCode)
        self.horizontalLayout_7.addLayout(self.verticalLayout_15)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
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
        self.linePrenom = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.linePrenom.setObjectName("linePrenom")
        self.verticalLayout_17.addWidget(self.linePrenom)
        self.lineNom = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineNom.setObjectName("lineNom")
        self.verticalLayout_17.addWidget(self.lineNom)
        self.lineSexe = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineSexe.setObjectName("lineSexe")
        self.verticalLayout_17.addWidget(self.lineSexe)
        self.horizontalLayout.addLayout(self.verticalLayout_17)

    # Bouton Précédent de la tab Personne
        self.btnPrecedent = QtWidgets.QPushButton(self.tabPersonne)
        self.btnPrecedent.setGeometry(QtCore.QRect(60, 70, 31, 23))
        self.btnPrecedent.setObjectName("btnPrecedent")


        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tabPersonne)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(160, 20, 160, 112))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.btnNouveau = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnNouveau.setObjectName("btnNouveau")
        self.verticalLayout_18.addWidget(self.btnNouveau)
        self.btnSupprimer = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnSupprimer.setObjectName("btnSupprimer")
        self.verticalLayout_18.addWidget(self.btnSupprimer)
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
        self.listChar = QtWidgets.QListWidget(self.horizontalLayoutWidget_5)
        self.listChar.setObjectName("listChar")
        self.verticalLayout_5.addWidget(self.listChar)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.lineDebutEmploi = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineDebutEmploi.setObjectName("lineDebutEmploi")
        self.verticalLayout_6.addWidget(self.lineDebutEmploi)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.lineFinEmploi = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineFinEmploi.setObjectName("lineFinEmploi")
        self.verticalLayout_7.addWidget(self.lineFinEmploi)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.lineCachet = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineCachet.setObjectName("lineCachet")
        self.verticalLayout_8.addWidget(self.lineCachet)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
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
        self.lineDateEmb = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineDateEmb.setObjectName("lineDateEmb")
        self.verticalLayout_9.addWidget(self.lineDateEmb)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.lineUsername = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineUsername.setObjectName("lineUsername")
        self.verticalLayout_10.addWidget(self.lineUsername)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_11.addWidget(self.label_13)
        self.linePwdEmp = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.linePwdEmp.setObjectName("linePwdEmp")
        self.verticalLayout_11.addWidget(self.linePwdEmp)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_12.addWidget(self.label_14)
        self.lineAccess = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineAccess.setObjectName("lineAccess")
        self.verticalLayout_12.addWidget(self.lineAccess)
        self.horizontalLayout_6.addLayout(self.verticalLayout_12)
        self.cbActeur = QtWidgets.QCheckBox(self.tabPersonne)
        self.cbActeur.setGeometry(QtCore.QRect(10, 310, 55, 17))
        self.cbActeur.setObjectName("cbActeur")
        self.cbClient = QtWidgets.QCheckBox(self.tabPersonne)
        self.cbClient.setGeometry(QtCore.QRect(10, 140, 50, 17))
        self.cbClient.setObjectName("cbClient")

    # Bouton Suivant de la tab Personne
        self.btnSuivant = QtWidgets.QPushButton(self.tabPersonne)
        self.btnSuivant.setGeometry(QtCore.QRect(110, 70, 31, 23))
        self.btnSuivant.setObjectName("btnSuivant")
        self.cbEmploye = QtWidgets.QCheckBox(self.tabPersonne)
        self.cbEmploye.setGeometry(QtCore.QRect(10, 450, 63, 17))
        self.cbEmploye.setObjectName("cbEmploye")
        self.tabMain.addTab(self.tabPersonne, "")
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

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tabFilms)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 160, 112))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.btnNouveau_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnNouveau_3.setObjectName("btnNouveau_3")
        self.verticalLayout_21.addWidget(self.btnNouveau_3)
        self.btnSupprimer_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnSupprimer_3.setObjectName("btnSupprimer_3")
        self.verticalLayout_21.addWidget(self.btnSupprimer_3)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tabFilms)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(220, 20, 211, 171))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.lineFilm_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineFilm_2.setObjectName("lineFilm_2")
        self.verticalLayout_22.addWidget(self.lineFilm_2)
        self.textDescFilm_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.textDescFilm_2.setObjectName("textDescFilm_2")
        self.verticalLayout_22.addWidget(self.textDescFilm_2)
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
        self.cbActeur.setText(_translate("Application", "Acteur"))
        self.cbClient.setText(_translate("Application", "Client"))
        self.btnSuivant.setText(_translate("Application", ">"))
        self.cbEmploye.setText(_translate("Application", "Employé"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabPersonne), _translate("Application", "Personne"))
        self.btnPrecedent_2.setText(_translate("Application", "<"))
        self.btnSuivant_2.setText(_translate("Application", ">"))
        self.btnNouveau_3.setText(_translate("Application", "Nouveau"))
        self.btnSupprimer_3.setText(_translate("Application", "Supprimer"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabFilms), _translate("Application", "Films"))
        self.btnFermer.setText(_translate("Application", "Fermer"))
        self.btnSauvegarder.setText(_translate("Application", "Sauvegarder"))
        self.btnCharger.setText(_translate("Application", "Charger"))

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

 # Sauvegarde à retravailler
    def sauvegarder(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Open File')
        file = open(name, "w")
        text = self.ListeDePersonnes, file()
        file.close()

 # Chargement à retravailler
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
