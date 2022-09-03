# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtWidgets import QMessageBox
import sys

class MessageBox(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._setupUi()

    def _setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(311, 111)
        self.setMinimumSize(QtCore.QSize(311, 111))
        self.setMaximumSize(QtCore.QSize(311, 111))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setItalic(True)
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/2252295991582004497-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 90, 90))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.popup_1)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 10, 90, 90))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.popup_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 10, 90, 90))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.popup_3)

        self.setCentralWidget(self.centralwidget)

        self._retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def _retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Popup1"))
        self.pushButton_2.setText(_translate("MainWindow", "Popup2"))
        self.pushButton_3.setText(_translate("MainWindow", "Popup3"))

    def popup_1(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Popup 1')
        msgBox.setText('I am popup_1')
        msgBox.setIcon(QMessageBox.Information)
        msgBox.exec_()

    def popup_2(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Popup 2')
        msgBox.setText('I am popup_2')
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        msgBox.setDefaultButton(QMessageBox.Ignore)
        msgBox.setInformativeText('Hi what is your faverite lang?')
        msgBox.setDetailedText('You can hide me')
        msgBox.exec_()

    def popup_3(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Popup 3')
        msgBox.setText('I am popup_3')
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.Yes)
        msgBox.buttonClicked.connect(self.messageBox_button_handler)
        msgBox.exec_()
    
    def messageBox_button_handler(self, which: QtWidgets.QPushButton):
        if which.text() == '&Yes': self.popup_1()
        elif which.text() == '&No': self.popup_2()

def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    win = MessageBox()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
   main()
