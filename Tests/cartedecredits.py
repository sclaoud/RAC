# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cartedecredits.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI_CC(object):
    def setupUi(self, UI_CC):
        UI_CC.setObjectName("UI_CC")
        UI_CC.resize(455, 145)
        self.btnSaveCC = QtWidgets.QPushButton(UI_CC)
        self.btnSaveCC.setGeometry(QtCore.QRect(250, 110, 75, 23))
        self.btnSaveCC.setObjectName("btnSaveCC")
        self.btnCloseCC = QtWidgets.QPushButton(UI_CC)
        self.btnCloseCC.setGeometry(QtCore.QRect(350, 110, 75, 23))
        self.btnCloseCC.setObjectName("btnCloseCC")
        self.btnPrecCC = QtWidgets.QPushButton(UI_CC)
        self.btnPrecCC.setGeometry(QtCore.QRect(30, 110, 31, 23))
        self.btnPrecCC.setObjectName("btnPrecCC")
        self.btnSvCC = QtWidgets.QPushButton(UI_CC)
        self.btnSvCC.setGeometry(QtCore.QRect(80, 110, 31, 23))
        self.btnSvCC.setObjectName("btnSvCC")
        self.horizontalLayoutWidget = QtWidgets.QWidget(UI_CC)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 401, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblNumCC = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblNumCC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNumCC.setObjectName("lblNumCC")
        self.verticalLayout_2.addWidget(self.lblNumCC)
        self.lbldateExp = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbldateExp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbldateExp.setObjectName("lbldateExp")
        self.verticalLayout_2.addWidget(self.lbldateExp)
        self.lblcodesecretCC = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblcodesecretCC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblcodesecretCC.setObjectName("lblcodesecretCC")
        self.verticalLayout_2.addWidget(self.lblcodesecretCC)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.NumeroCC = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.NumeroCC.setText("")
        self.NumeroCC.setMaxLength(16)
        self.NumeroCC.setObjectName("NumeroCC")
        self.verticalLayout.addWidget(self.NumeroCC)
        self.expCC = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.expCC.setObjectName("expCC")
        self.verticalLayout.addWidget(self.expCC)
        self.codesecretCC = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.codesecretCC.setObjectName("codesecretCC")
        self.verticalLayout.addWidget(self.codesecretCC)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(UI_CC)
        QtCore.QMetaObject.connectSlotsByName(UI_CC)

    def retranslateUi(self, UI_CC):
        _translate = QtCore.QCoreApplication.translate
        UI_CC.setWindowTitle(_translate("UI_CC", "CartedeCredits"))
        self.btnSaveCC.setText(_translate("UI_CC", "Sauvegarder"))
        self.btnCloseCC.setText(_translate("UI_CC", "Fermer"))
        self.btnPrecCC.setText(_translate("UI_CC", "<"))
        self.btnSvCC.setText(_translate("UI_CC", ">"))
        self.lblNumCC.setText(_translate("UI_CC", "Numéro de Carte de Crédits"))
        self.lbldateExp.setText(_translate("UI_CC", "Date d\'expiration"))
        self.lblcodesecretCC.setText(_translate("UI_CC", "Code secret"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UI_CC = QtWidgets.QDialog()
    ui = Ui_UI_CC()
    ui.setupUi(UI_CC)
    UI_CC.show()
    sys.exit(app.exec_())
