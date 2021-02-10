from PyQt5.QtCore import QObject, pyqtProperty

class Foo(QObject):

    def __init__(self):
        QObject.__init__(self)

        self._total = 0

    @pyqtProperty(int)
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value