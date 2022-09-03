# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MenuBar_StatusBar(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._setupUi()

    def _setupUi(self) -> None:
        self.setObjectName("MainWindow")
        self.resize(641, 160)
        self.setMinimumSize(QtCore.QSize(641, 160))
        self.setMaximumSize(QtCore.QSize(641, 160))

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 24))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.setMenuBar(self.menubar)

        self.actionNew = QtWidgets.QAction(self)
        self.actionNew.setObjectName("actionNew")

        self.actionOpen = QtWidgets.QAction(self)
        self.actionOpen.setObjectName("actionOpen")

        self.actionCopy = QtWidgets.QAction(self)
        self.actionCopy.setObjectName("actionCopy")

        self.actionCut = QtWidgets.QAction(self)
        self.actionCut.setObjectName("actionCut")

        self.actionPaste = QtWidgets.QAction(self)
        self.actionPaste.setObjectName("actionPaste")

        self.actionUndo = QtWidgets.QAction(self)
        self.actionUndo.setObjectName("actionUndo")

        self.actionRedo = QtWidgets.QAction(self)
        self.actionRedo.setObjectName("actionRedo")

        self.actionApp_info = QtWidgets.QAction(self)
        self.actionApp_info.setObjectName("actionApp_info")

        self.actionVersion = QtWidgets.QAction(self)
        self.actionVersion.setObjectName("actionVersion")

        self.actionSave_2 = QtWidgets.QAction(self)
        self.actionSave_2.setObjectName("actionSave_2")

        self.actionSave_as = QtWidgets.QAction(self)
        self.actionSave_as.setObjectName("actionSave_as")

        self.menuSave.addAction(self.actionSave_2)
        self.menuSave.addAction(self.actionSave_as)

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuSave.menuAction())

        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)

        self.menuHelp.addAction(self.actionApp_info)
        self.menuHelp.addAction(self.actionVersion)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionNew.triggered.connect(lambda: self.show_status('New was clicked'))
        self.actionOpen.triggered.connect(lambda: self.show_status('Open was clicked'))
        self.actionSave_2.triggered.connect(lambda: self.show_status('Save was clicked'))
        self.actionSave_as.triggered.connect(lambda: self.show_status('Save as was clicked'))
        self.actionCopy.triggered.connect(lambda: self.show_status('Copy was clicked'))
        self.actionCut.triggered.connect(lambda: self.show_status('Cut was clicked'))
        self.actionPaste.triggered.connect(lambda: self.show_status('Paste was clicked'))
        self.actionUndo.triggered.connect(lambda: self.show_status('Undo was clicked'))
        self.actionRedo.triggered.connect(lambda: self.show_status('Redo was clicked'))
        self.actionApp_info.triggered.connect(lambda: self.show_status('App_info: menuBar and statusBar'))
        self.actionVersion.triggered.connect(lambda: self.show_status('Version: 0.0.1v'))

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self._retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def _retranslateUi(self) -> None:
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "create new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "open file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionApp_info.setText(_translate("MainWindow", "App info"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionSave_2.setStatusTip(_translate("MainWindow", "save file"))
        self.actionSave_2.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave_as.setStatusTip(_translate("MainWindow", "save file as"))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))

    def show_status(self, msg: str) -> None:
        self.statusbar.showMessage(f"{msg}")

def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    win = MenuBar_StatusBar()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
