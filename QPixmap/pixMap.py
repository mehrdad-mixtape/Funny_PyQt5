# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class PixMap(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._setupUi()

    def _setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(802, 518)
        self.setMinimumSize(QtCore.QSize(802, 518))
        self.setMaximumSize(QtCore.QSize(802, 518))

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 10, 781, 451))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("2.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(10, 470, 391, 38))
        self.next_button.setObjectName("next_button")

        self.back_Button = QtWidgets.QPushButton(self.centralwidget)
        self.back_Button.setGeometry(QtCore.QRect(408, 470, 381, 38))
        self.back_Button.setObjectName("back_Button")

        self._retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.next_button.clicked.connect(self.show_2)
        self.back_Button.clicked.connect(self.show_1)

    def _retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_button.setText(_translate("MainWindow", "next"))
        self.back_Button.setText(_translate("MainWindow", "back"))

    def show_1(self):
        self.photo.setPixmap(QtGui.QPixmap("2.jpg"))
	
    def show_2(self):
        self.photo.setPixmap(QtGui.QPixmap("1.jpg"))
	
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = PixMap()
    win.show()
    sys.exit(app.exec_())
