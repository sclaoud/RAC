import sys
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *



class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.cbListCatFilm = ["Animation", "Fantaisie", "Science-Fiction", "Horreur", "Drame",
                             "Thriller", "Documentaire", "Comédie"]
        self.listCatFilm    = ['', '', '', '', '', '', '', '', ]
        grid = QGridLayout()


        for i, v in enumerate(self.cbListCatFilm):
            self.cbListCatFilm[i] = QCheckBox(v)
            self.listCatFilm[i] = QLabel()
            grid.addWidget(self.cbListCatFilm[i], i, 0)
            grid.addWidget(self.listCatFilm[i],    i, 1)

        self.button = QPushButton("Check CheckBox")
        self.button.clicked.connect(self.checkboxChanged)
        self.labelResult = QLabel()

        grid.addWidget(self.button,     10, 0, 1,2)
        grid.addWidget(self.labelResult,11, 0, 1,2)
        self.setLayout(grid)

    def checkboxChanged(self):
        self.labelResult.setText("")
        for i, v in enumerate(self.cbListCatFilm):
            self.listCatFilm[i].setText("True" if v.checkState() else "False")
            self.labelResult.setText("{}, {}".format(self.labelResult.text(),
                                                     self.listCatFilm[i].text()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())