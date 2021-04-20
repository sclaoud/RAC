import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPlainTextEdit, QVBoxLayout
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class TextEdit(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        regexp = QRegExp(r'^[a-zA-Z]*$')
        self.validator = QRegExpValidator(regexp)

#    def keyPressEvent(self, event):
#        state = self.validator.validate(event.text(), 0)
#        if state[0] == QRegExpValidator.Acceptable or state[1] in ('\x08', '\r'):
#            super().keyPressEvent(event)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)

        mainLayout = QVBoxLayout()

        validator = QRegExpValidator(QRegExp(r'[0-9]+'))

        self.lineEdit = QLineEdit()
        self.lineEdit.setStyleSheet('font-size: 30px; height:50px; color: blue;')
        self.lineEdit.setValidator(validator)
        mainLayout.addWidget(self.lineEdit)

        self.textEdit = TextEdit()
        self.textEdit.setStyleSheet('''font-size: 30px;''')
        mainLayout.addWidget(self.textEdit)

        self.setLayout(mainLayout)

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())