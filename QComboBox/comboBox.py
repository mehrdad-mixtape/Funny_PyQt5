# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class ComboBox(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._setupUi()

    def _setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(301, 328)
        self.setMinimumSize(QtCore.QSize(301, 328))
        self.setMaximumSize(QtCore.QSize(301, 328))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/1388560951582004484-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 100, 131, 24))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(161, 100, 131, 24))
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(('Size', 'small', 'medium', 'large'))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 200, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 283, 131, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.submit)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 283, 131, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close)
        
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "FastFood"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Food"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Pizza 10.45$"))
        self.comboBox.setItemText(2, _translate("MainWindow", "KFC 15.30$"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Burger 20.99$"))
        self.label.setText(_translate("MainWindow", "Welcome To My FastFood"))
        self.label_2.setText(_translate("MainWindow", "Price:"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "..........."))
    
    def submit(self) -> None:
        food: dict = {0: 0, 1: 10.45, 2: 15.30, 3: 20.99}
        size: dict = {'Size': 0, 'small': 1, 'medium': 2, 'large': 3}
        index_1: int = self.comboBox.currentIndex()
        text_1: str = self.comboBox.currentText()
        text_2: str = self.comboBox_2.currentText()
        self.label_3.setText(f"{text_2} {text_1.split(' ')[0]} is {round(food[index_1] * size[text_2], 2)}")

def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    win = ComboBox()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
