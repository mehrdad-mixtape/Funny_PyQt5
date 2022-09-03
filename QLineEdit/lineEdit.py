# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class LineEdit(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._setupUi()

    def _setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(291, 264)
        self.setMinimumSize(QtCore.QSize(291, 264))
        self.setMaximumSize(QtCore.QSize(291, 264))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/1388560951582004484-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 70, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('ex: mehrdad')

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 110, 181, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 150, 181, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText('ex: mehrdad@****')

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 10, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setMaxLength(0)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.NoEcho)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 220, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 220, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.signin)

        self.setCentralWidget(self.centralwidget)
        self._retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def _retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username:"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.label_3.setText(_translate("MainWindow", "Email:"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Signin"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Login Or Sign in - readonly"))
    
    def login(self) -> None:
        if self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '' or self.lineEdit_4.text():
            self.lineEdit_4.setPlaceholderText('Fill all!')
        else:
            self.lineEdit_4.setPlaceholderText('You login successfully')
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
    def signin(self) -> None:
        if self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '' or self.lineEdit_4.text():
            self.lineEdit_4.setPlaceholderText('Fill all!')
        else:
            self.lineEdit_4.setPlaceholderText('You signin successfully')
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()

def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    win = LineEdit()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
