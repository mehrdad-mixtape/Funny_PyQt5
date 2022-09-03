# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class WorkSpace(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._setupUi()

    def _setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 621, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 291, 361))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
        self.groupBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")

        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(0, 30, 291, 241))
        self.textEdit.setObjectName("textEdit")

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(0, 280, 291, 32))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(0, 320, 91, 32))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/7774226221582004489-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 320, 91, 32))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/14787197661582004498-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 320, 91, 32))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icon/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")

        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(310, 10, 291, 361))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 30, 291, 321))
        self.textEdit_2.setObjectName("textEdit_2")

        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 381, 361))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.groupBox_3 = QtWidgets.QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_3.setObjectName("groupBox_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 320, 101, 32))
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.refresh)

        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setGeometry(QtCore.QRect(0, 30, 381, 281))
        self.listWidget.setObjectName("listWidget")

        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(400, 10, 201, 361))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.groupBox_4 = QtWidgets.QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_4.setObjectName("groupBox_4")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 201, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 54)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.progressBar_2 = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar_2.setProperty("value", 30)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout.addWidget(self.progressBar_2)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.progressBar_3 = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar_3.setProperty("value", 60)
        self.progressBar_3.setObjectName("progressBar_3")
        self.verticalLayout.addWidget(self.progressBar_3)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.progressBar_4 = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar_4.setProperty("value", 80)
        self.progressBar_4.setObjectName("progressBar_4")
        self.verticalLayout.addWidget(self.progressBar_4)

        self.gridLayout_5.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_3)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 180, 591, 186))
        self.calendarWidget.setObjectName("calendarWidget")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 20, 211, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 70, 211, 41))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 120, 211, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(30, 17, 70, 41))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(30, 70, 70, 41))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 70, 41))
        self.label_7.setObjectName("label_7")

        self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.toolBox = QtWidgets.QToolBox(self.tab_4)
        self.toolBox.setGeometry(QtCore.QRect(10, 10, 591, 341))
        self.toolBox.setObjectName("toolBox")

        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 591, 205))
        self.page.setObjectName("page")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(60, 10, 160, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.horizontalSlider)

        self.horizontalSlider_3 = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")

        self.verticalLayout_2.addWidget(self.horizontalSlider_3)

        self.horizontalSlider_2 = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")

        self.verticalLayout_2.addWidget(self.horizontalSlider_2)

        self.toolBox.addItem(self.page, "")

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 591, 205))
        self.page_2.setObjectName("page_2")

        self.timeEdit = QtWidgets.QTimeEdit(self.page_2)
        self.timeEdit.setGeometry(QtCore.QRect(440, 20, 123, 32))
        self.timeEdit.setObjectName("timeEdit")

        self.lcdNumber = QtWidgets.QLCDNumber(self.page_2)
        self.lcdNumber.setGeometry(QtCore.QRect(370, 70, 191, 71))
        self.lcdNumber.setObjectName("lcdNumber")

        self.toolBox.addItem(self.page_2, "")

        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")

        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.page_3)
        self.commandLinkButton.setGeometry(QtCore.QRect(60, 10, 188, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.page_3)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(60, 70, 188, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")

        self.toolBox.addItem(self.page_3, "")

        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")

        self.toolBox.addItem(self.page_4, "")

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 29))
        self.menubar.setObjectName("menubar")

        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)

        self.actionSSH = QtWidgets.QAction(self)
        self.actionSSH.setObjectName("actionSSH")
        self.actionTelnet = QtWidgets.QAction(self)
        self.actionTelnet.setObjectName("actionTelnet")
        self.actionInfo = QtWidgets.QAction(self)
        self.actionInfo.setObjectName("actionInfo")
        self.actionVersion = QtWidgets.QAction(self)
        self.actionVersion.setObjectName("actionVersion")

        self.menuConnection.addAction(self.actionSSH)
        self.menuConnection.addAction(self.actionTelnet)

        self.menuHelp.addAction(self.actionInfo)
        self.menuHelp.addAction(self.actionVersion)
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self._retranslateUi()

        self.tabWidget.setCurrentIndex(3)
        self.toolBox.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(self)

    def _retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "WorkSpace"))
        self.groupBox.setTitle(_translate("MainWindow", "Sending"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "message ..."))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton_2.setText(_translate("MainWindow", "Retry"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Receiving"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Messages"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Logging"))
        self.pushButton_4.setText(_translate("MainWindow", "Refresh"))
        self.groupBox_4.setTitle(_translate("MainWindow", "HardWare"))
        self.label.setText(_translate("MainWindow", "CPU:"))
        self.label_2.setText(_translate("MainWindow", "Memory:"))
        self.label_3.setText(_translate("MainWindow", "Disk"))
        self.label_4.setText(_translate("MainWindow", "Network:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Monitoring"))
        self.lineEdit_2.setText(_translate("MainWindow", "Mehrdad"))
        self.lineEdit_3.setText(_translate("MainWindow", "123456"))
        self.lineEdit_4.setText(_translate("MainWindow", "0900 000 000"))
        self.label_5.setText(_translate("MainWindow", "Name:"))
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.label_7.setText(_translate("MainWindow", "Phone:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "User"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2"))
        self.commandLinkButton.setText(_translate("MainWindow", "CommandLinkButton"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "CommandLinkButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Page 3"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Page 4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Setting"))
        self.menuConnection.setTitle(_translate("MainWindow", "Connection"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSSH.setText(_translate("MainWindow", "SSH"))
        self.actionTelnet.setText(_translate("MainWindow", "Telnet"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
    
    def refresh(self):
        date = self.calendarWidget.selectedDate()
        self.listWidget.addItem(f"{date.year()}/{date.month()}/{date.day()}")

def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    win = WorkSpace()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
