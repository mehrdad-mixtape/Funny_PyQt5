from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys

geometry: tuple = (100, 100, 720, 480)
maxSize: tuple = (720, 480)
minSize: tuple = (720, 480)

def form_1():
    # App:
    app = QApplication(sys.argv)
    # Form:
    form = QMainWindow()
    form.setGeometry(*geometry) # setGeometry(X_pos, Y_pos, Width, Height)
    form.setWindowTitle('Hello PyQt5')
    form.setMaximumSize(*maxSize)
    form.setMinimumSize(*minSize)
    # Font:
    font = QtGui.QFont()
    font.setPointSize(16)
    font.setBold(False)
    font.setItalic(False)
    font.setWeight(100)
    form.setFont(font)
    # Widgets:
    label = QtWidgets.QLabel(form)
    label.setText('I am First Label:')
    label.setGeometry(QtCore.QRect(0, 0, 100, 50))
    label.adjustSize()

    # lineEdit = QtWidgets.QLineEdit(form)
    # lineEdit.setPlaceholderText('LineEdit')
    # lineEdit.setGeometry(QtCore.QRect(300, 0, 200, 30))
    # lineEdit.setEchoMode(3) # 1: readonly, 2: password, 3: R/W-able
    # lineEdit.setText('hello')
    # End:
    form.show()
    sys.exit(app.exec_())

def main():
    form_1()

if __name__ == '__main__':
    try: main()
    except KeyboardInterrupt: sys.exit()
