from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import Q

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        password = PasswordEdit()
        self.setCentralWidget(password)


app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()