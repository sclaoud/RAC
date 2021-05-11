import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt


class TableView(QTableWidget):
    def __init__(self, z, *args):
        super(TableView, self).__init__(*args)
        self.z = z
        self.setz()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setz(self):
        horHeaders = []
        for j, (key, values) in enumerate(sorted(self.z.items())):
            horHeaders.append(key)
            for i, value in enumerate(values):
                newitem = QTableWidgetItem()
                newitem.setData(Qt.EditRole, value)
                self.setItem(i, j, newitem)
        self.setHorizontalHeaderLabels(horHeaders)


def main(args):

    z = {
        "LEVEL 6 S1": [24.4999999999989, 5.00000000000394, 1.5],
        "LEVEL 5 S1": [25.4999999999992, 4.99999999999996, 1.5],
        "LEVEL 4 S1": [25.4999999999992, 4.99999999999996, 1.5],
        "LEVEL 3 S1": [25.4999999999992, 3.41666666666662, 1.5],
        "LEVEL 2 S1": [25.4999999999992, 3.91666666666663, 3.0],
        "LEVEL 1 S1": [25.4999999999992, 4.99999999999996, 1.33333333333333],
    }

    app = QApplication(args)
    table = TableView(z, 3, 6)
    table.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)