from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditTime(object):
    def setupUi(self, EditTime):
        EditTime.setObjectName("EditTime")
        EditTime.resize(392, 293)
        EditTime.setAutoFillBackground(False)
        self.timeEdit = QtWidgets.QTimeEdit(EditTime)
        self.timeEdit.setGeometry(QtCore.QRect(140, 160, 118, 22))
        self.timeEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(1999, 12, 31), QtCore.QTime(23, 59, 59)))
        self.timeEdit.setMaximumDate(QtCore.QDate(1999, 12, 31))
        self.timeEdit.setMinimumDate(QtCore.QDate(1999, 12, 31))
        self.timeEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.timeEdit.setMinimumTime(QtCore.QTime(00, 00, 00))
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit.setTimeSpec(QtCore.Qt.OffsetFromUTC)
        self.timeEdit.setTime(QtCore.QTime(24,0,0))
        self.timeEdit.setObjectName("timeEdit")
        self.HourLCD = QtWidgets.QLCDNumber(EditTime)
        self.HourLCD.setGeometry(QtCore.QRect(60, 70, 111, 51))
        self.HourLCD.setObjectName("HourLCD")
        self.MinuteLCD = QtWidgets.QLCDNumber(EditTime)
        self.MinuteLCD.setGeometry(QtCore.QRect(200, 70, 111, 51))
        self.MinuteLCD.setObjectName("MinuteLCD")
        self.OK = QtWidgets.QPushButton(EditTime)
        self.OK.setGeometry(QtCore.QRect(160, 230, 75, 23))
        self.OK.setObjectName("OK")
        self.label = QtWidgets.QLabel(EditTime)
        self.label.setGeometry(QtCore.QRect(90, 46, 31, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(EditTime)
        self.label_2.setGeometry(QtCore.QRect(230, 50, 47, 13))
        self.label_2.setObjectName("label_2")

        # self.retranslateUi(EditTime)
        QtCore.QMetaObject.connectSlotsByName(EditTime)

class Widget(QtWidgets.QWidget, Ui_EditTime):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)
        self.OK.clicked.connect(self.onClicked)

    @QtCore.pyqtSlot()
    def onClicked(self):
        t = self.timeEdit.time()
        self.HourLCD.display(t.hour())
        self.MinuteLCD.display(t.minute())

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())