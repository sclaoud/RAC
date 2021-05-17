from PyQt5.QtCore import Qt
import PyQt5
from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton, QTableWidgetItem, QTableWidget

class Dlg(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.layout = QGridLayout(self)
        self.label1 = QLabel('FERTILIZACION SUBSUELO')
        self.btn = QPushButton('RUN')
        self.btn.setFixedWidth(100)

        nb_row = 5
        nb_col = 2

        #creating empty table
        data = [ [] for i in range(nb_row) ]

        for i in range(nb_row):
            for j in range(nb_col):
                data[i].append('')

        self.table1 = QTableWidget()

        self.table1.setRowCount(nb_row)
        self.table1.setColumnCount(nb_col)
        self.table1.setHorizontalHeaderLabels(['LIMITE 1', 'LIMITE 2'])

        for row in range (nb_row):
            for col in range(nb_col):
                item = QTableWidgetItem(str(data[row][col]))
                self.table1.setItem(row, col, item)

        self.layout.addWidget(self.label1, 0, 0)
        self.layout.addWidget(self.table1, 1, 0)
        self.layout.addWidget(self.btn, 2, 0)

        self.btn.clicked.connect(self.print_table_values)

    def print_table_values(self, data):

        nb_row = 5
        nb_col = 2

        for row in range (nb_row):
            for col in range(nb_col):
                print(row, col, self.table1.item(row, col).text())

w = Dlg()
w.resize(350,300)
w.setWindowTitle('fertilizacion_abono')
w.setWindowFlags(Qt.WindowStaysOnTopHint)
w.show()