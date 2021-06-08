import sys
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QListView, QMainWindow, QApplication
from PyQt5.QtCore import Qt

class TableModel(QSqlTableModel):
    def __init__(self, *args, **kwargs):
        QSqlTableModel.__init__(self, *args, **kwargs)
        self.checkeable_data = {}

    def flags(self, index):
        fl = QSqlTableModel.flags(self, index)
        if index.column() == 1:
            fl |= Qt.ItemIsUserCheckable
        return fl

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.CheckStateRole and (
            self.flags(index) & Qt.ItemIsUserCheckable != Qt.NoItemFlags
        ):
            if index.row() not in self.checkeable_data.keys():
                self.setData(index, Qt.Unchecked, Qt.CheckStateRole)
            return self.checkeable_data[index.row()]
        else:
            return QSqlTableModel.data(self, index, role)

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.CheckStateRole and (
            self.flags(index) & Qt.ItemIsUserCheckable != Qt.NoItemFlags
        ):
            self.checkeable_data[index.row()] = value
            self.dataChanged.emit(index, index, (role,))
            return True
        return QSqlTableModel.setData(self, index, value, role)

def createConnection():
    db = QSqlDatabase.addDatabase("QSQLITE");
    db.setDatabaseName("data.db");
    if not db.open():
        print("Cannot open database"),
        print("Unable to establish a database connection.\n"
                        "This example needs SQLite support. Please read "
                        "the Qt SQL driver documentation for information how "
                        "to build it.\n\n"
                        "Click Cancel to exit.")
        return False
    return True

class Widget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        lv = QListView(self)
        self.setCentralWidget(lv)
        model = TableModel(self)
        model.setTable("Personne")
        model.select()
        lv.setModel(model)
        lv.setModelColumn(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(-1)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())