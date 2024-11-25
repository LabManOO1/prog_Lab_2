from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QFont
import sys
import random

from PyQt5 import QtWidgets




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindow.ui', self)
        self.setWindowIcon(QIcon('MainIcon.png'))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()