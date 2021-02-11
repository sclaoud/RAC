import os, sys
from PyQt5 import QtWidgets, QtCore, QtGui

class ChecklistDialog(QtWidgets.QDialog):
    def __init__(self, name, stringlist=None, checked=False, icon=None, parent=None):
        super(ChecklistDialog, self).__init__(parent)

        self.name = name
        self.icon = icon
        self.model = QtGui.QStandardItemModel()
        self.listView = QtWidgets.QListView()

        if stringlist is not None:
            for i in range(len(stringlist)):
                item = QtGui.QStandardItem(stringlist[i])
                item.setCheckable(True)
                check = QtCore.Qt.Checked if checked else QtCore.Qt.Unchecked
                item.setCheckState(check)
                self.model.appendRow(item)

        self.listView.setModel(self.model)

        self.okButton = QtWidgets.QPushButton("OK")
        self.cancelButton = QtWidgets.QPushButton("Cancel")
        self.selectButton = QtWidgets.QPushButton("Select All")
        self.unselectButton = QtWidgets.QPushButton("Unselect All")

        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        hbox.addWidget(self.selectButton)
        hbox.addWidget(self.unselectButton)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.listView)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        #self.setLayout(layout)
        self.setWindowTitle(self.name)
        if self.icon is not None: self.setWindowIcon(self.icon)

        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
        self.selectButton.clicked.connect(self.select)
        self.unselectButton.clicked.connect(self.unselect)

    def reject(self):
        QtWidgets.QDialog.reject(self)

    def accept(self):
        self.choices = []
        i = 0
        while self.model.item(i):
            if self.model.item(i).checkState():
                self.choices.append(self.model.item(i).text())
            i += 1
        QtWidgets.QDialog.accept(self)

    def select(self):
        i = 0
        while self.model.item(i):
            item = self.model.item(i)
            if not item.checkState():
                item.setCheckState(True)
            i += 1

    def unselect(self):
        i = 0
        while self.model.item(i):
            item = self.model.item(i)
            item.setCheckState(False)
            i += 1

if __name__ == "__main__":
    fruits = ["Banana", "Apple", "Elderberry", "Clementine", "Fig",
        "Guava", "Mango", "Honeydew Melon", "Date", "Watermelon",
        "Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi", "Lemon",
        "Nectarine", "Plum", "Raspberry", "Strawberry", "Orange"]
    app = QtWidgets.QApplication(sys.argv)
    form = ChecklistDialog("Fruit", fruits, checked=True)
    if form.exec_():
        print("\n".join([str(s) for s in form.choices]))