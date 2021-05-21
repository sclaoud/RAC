import sys
from PyQt5 import QtCore, QtWidgets
from pymysql import Error
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlError
rowNo = 1

try:
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("data.db")
    print("Database created")

except:
    print("failed to create database")
finally:
    cursor = QSqlDatabase.cursor()
    sql = "SELECT id, nome, email, senha, data_cadastro, niveis_acesso_id, validacao, ativo, como_chegou FROM usuarios ORDER BY nome ASC"
    cursor.execute(sql)
    con.close()

if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit()




class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(448, 300)

        self.lineEdit_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name.setGeometry(QtCore.QRect(130, 50, 241, 21))
        self.lineEdit_name.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.lineEdit_name.setObjectName("lineEdit_name")

        self.lineEdit_email = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_email.setGeometry(QtCore.QRect(130, 90, 191, 21))
        self.lineEdit_email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.lineEdit_email.setObjectName("lineEdit_email")

        self.lineEdit_pwd = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(130, 130, 131, 21))
        self.lineEdit_pwd.setInputMethodHints(QtCore.Qt.ImhSensitiveData | QtCore.Qt.ImhUppercaseOnly)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")

        self.lineEdit_market = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_market.setGeometry(QtCore.QRect(130, 170, 131, 21))
        self.lineEdit_market.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.lineEdit_market.setObjectName("lineEdit_market")

        self.pushButton_first = QtWidgets.QPushButton(Dialog)
        self.pushButton_first.setGeometry(QtCore.QRect(70, 240, 61, 28))
        self.pushButton_first.setObjectName("pushButton_first")
        self.pushButton_first.clicked.connect(ShowFirst)

        self.pushButton_previous = QtWidgets.QPushButton(Dialog)
        self.pushButton_previous.setGeometry(QtCore.QRect(150, 240, 61, 28))
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.pushButton_previous.clicked.connect(ShowPrevious)

        self.pushButton_next = QtWidgets.QPushButton(Dialog)
        self.pushButton_next.setGeometry(QtCore.QRect(230, 240, 61, 28))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_next.clicked.connect(ShowNext)

        self.pushButton_last = QtWidgets.QPushButton(Dialog)
        self.pushButton_last.setGeometry(QtCore.QRect(310, 240, 61, 28))
        self.pushButton_last.setObjectName("pushButton_last")
        self.pushButton_last.clicked.connect(ShowLast)

        self.retranslateUi(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_first.setText(_translate("Dialog", "<<"))
        self.pushButton_previous.setText(_translate("Dialog", "<"))
        self.pushButton_next.setText(_translate("Dialog", ">"))
        self.pushButton_last.setText(_translate("Dialog", ">>"))

        ShowFirst(self)


def ShowFirst(self):
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            ui.lineEdit_name.setText(row[1])
            ui.lineEdit_email.setText(row[2])
            ui.lineEdit_pwd.setText(row[3])
            ui.lineEdit_market.setText(row[8])
    except Error as e:
        print("Error in accessing table")


def ShowPrevious(self):
    global rowNo
    rowNo -= 1
    sql = "SELECT id, nome, email, senha, data_cadastro, niveis_acesso_id, validacao, ativo, como_chegou FROM usuarios WHERE id=" + str(
        rowNo) + " ORDER BY nome ASC"
    cursor.execute(sql)
    row = cursor.fetchone()

    if row:
        ui.lineEdit_name.setText(row[1])
        ui.lineEdit_email.setText(row[2])
        ui.lineEdit_pwd.setText(row[3])
        ui.lineEdit_market.setText(row[8])
    else:
        rowNo += 1


def ShowNext(self):
    global rowNo
    rowNo += 1
    sql = "SELECT id, nome, email, senha, data_cadastro, niveis_acesso_id, validacao, ativo, como_chegou FROM usuarios WHERE id=" + str(
        rowNo) + " ORDER BY nome ASC"
    cursor.execute(sql)
    row = cursor.fetchone()

    if row:
        ui.lineEdit_name.setText(row[1])
        ui.lineEdit_email.setText(row[2])
        ui.lineEdit_pwd.setText(row[3])
        ui.lineEdit_market.setText(row[8])
    else:
        rowNo -= 1


def ShowLast(self):
    cursor.execute(sql)
    for row in cursor.fetchall():
        ui.lineEdit_name.setText(row[1])
        ui.lineEdit_email.setText(row[2])
        ui.lineEdit_pwd.setText(row[3])
        ui.lineEdit_market.setText(row[8])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())