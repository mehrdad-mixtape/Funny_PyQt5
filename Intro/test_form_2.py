from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from threading import Thread
import sys, time

class Form_2(QMainWindow):
    geometry: tuple = (100, 100, 720, 480)
    maxSize: tuple = (720, 480)
    minSize: tuple = (720, 480)
    def __init__(self):
        super().__init__()
        self.setGeometry(*Form_2.geometry) # setGeometry(X_pos, Y_pos, Width, Height)
        self.setWindowTitle('Hello PyQt5')
        self.setMaximumSize(*Form_2.maxSize)
        self.setMinimumSize(*Form_2.minSize)
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        self.font = QtGui.QFont()
        self.font.setPointSize(16)
        self.font.setBold(False)
        self.font.setItalic(False)
        self.font.setWeight(100)
        self.setFont(self.font)
        # Widgets:
        self.label = QtWidgets.QLabel(self)
        self.label.setText('I am First Label:')
        self.label.setGeometry(QtCore.QRect(0, 0, 100, 50))
        self.label.adjustSize()
    
    def timer(self):
        time.sleep(3)
        for i in reversed(range(0, 10)):
            self.label.setText(f"Timer: {i}")
            self.label.adjustSize()
            time.sleep(1)
        self.label.setText('Window will close automatically')
        self.label.adjustSize()
        time.sleep(1)
        self.close()

def main() -> None:
    app = QApplication(sys.argv)
    window = Form_2()
    t1 = Thread(target=window.show)
    t2 = Thread(target=window.timer)
    # window.show()
    t1.start()
    t2.start()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
