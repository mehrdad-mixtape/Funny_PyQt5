# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class All_Gate(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._setupUi()

    def _setupUi(self) -> None:
        self.setObjectName("MainWindow")
        self.resize(531, 115)
        self.setMinimumSize(QtCore.QSize(531, 115))
        self.setMaximumSize(QtCore.QSize(531, 115))

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 160, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.firstInput = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.firstInput.setObjectName("firstInput")
        self.verticalLayout_2.addWidget(self.firstInput)

        self.secondInput = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.secondInput.setObjectName("secondInput")
        self.verticalLayout_2.addWidget(self.secondInput)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 10, 331, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.orGate = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.orGate.setObjectName("orGate")
        self.gridLayout.addWidget(self.orGate, 1, 0, 1, 1)
        self.orGate.toggled.connect(self.OR)

        self.andGate = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.andGate.setObjectName("andGate")
        self.gridLayout.addWidget(self.andGate, 0, 0, 1, 1)
        self.andGate.toggled.connect(self.AND)

        self.nandGate = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.nandGate.setObjectName("nandGate")
        self.gridLayout.addWidget(self.nandGate, 0, 1, 1, 1)
        self.nandGate.toggled.connect(self.NAND)

        self.norGate = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.norGate.setObjectName("norGate")
        self.gridLayout.addWidget(self.norGate, 1, 1, 1, 1)
        self.norGate.toggled.connect(self.NOR)

        self.xorGate = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.xorGate.setObjectName("xorGate")
        self.gridLayout.addWidget(self.xorGate, 0, 2, 1, 1)
        self.xorGate.toggled.connect(self.XOR)

        self.xnorGate = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.xnorGate.setObjectName("xnorGate")
        self.gridLayout.addWidget(self.xnorGate, 1, 2, 1, 1)
        self.xnorGate.toggled.connect(self.XNOR)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.setCentralWidget(self.centralwidget)
        self._retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def _retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Logic Gate"))
        self.firstInput.setText(_translate("MainWindow", "First Input: 1-0"))
        self.secondInput.setText(_translate("MainWindow", "Second Input: 1-0"))
        self.orGate.setText(_translate("MainWindow", "OR Gate"))
        self.andGate.setText(_translate("MainWindow", "AND Gate"))
        self.nandGate.setText(_translate("MainWindow", "NAND Gate"))
        self.norGate.setText(_translate("MainWindow", "NOR Gate"))
        self.xorGate.setText(_translate("MainWindow", "XOR Gate"))
        self.xnorGate.setText(_translate("MainWindow", "XNOR Gate"))

    def AND(self) -> None:
        fin: int = int(self.firstInput.isChecked())
        sin: int = int(self.secondInput.isChecked())
        self.statusbar.showMessage(f"{fin} AND {sin} = {fin & sin}")
    
    def OR(self) -> None:
        fin: int = int(self.firstInput.isChecked())
        sin: int = int(self.secondInput.isChecked())
        self.statusbar.showMessage(f"{fin} OR {sin} = {fin | sin}")
    
    def NAND(self) -> None:
        fin: int = int(self.firstInput.isChecked())
        sin: int = int(self.secondInput.isChecked())
        self.statusbar.showMessage(f"{fin} NAND {sin} = {int(not (fin & sin))}")
    
    def NOR(self) -> None:
        fin: int = int(self.firstInput.isChecked())
        sin: int = int(self.secondInput.isChecked())
        self.statusbar.showMessage(f"{fin} NOR {sin} = {int(not (fin | sin))}")
    
    def XOR(self) -> None:
        fin: int = int(self.firstInput.isChecked())
        sin: int = int(self.secondInput.isChecked())
        self.statusbar.showMessage(f"{fin} XOR {sin} = {fin ^ sin}")
    
    def XNOR(self) -> None:
        fin: int = int(self.firstInput.isChecked())
        sin: int = int(self.secondInput.isChecked())
        self.statusbar.showMessage(f"{fin} XNOR {sin} = {int(not (fin ^ sin))}")

def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    win = All_Gate()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
