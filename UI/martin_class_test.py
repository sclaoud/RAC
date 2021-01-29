# This Python file uses the following encoding: utf-8
import sys
from PySide.QtWidgets import *


class Personne(QWidget):
    def __init__(self):
        QWidget.__init__(self)



if __name__ == "__main__":
    app = QApplication([])


    window = Personne()
    layout = QFormLayout()

    okButton = QPushButton("Confirmer")
    cancelButton = QPushButton("Annuler")

    hbox = Qt
    hbox.addStretch(1)
    hbox.addWidget(okButton)
    hbox.addWidget(cancelButton)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())



