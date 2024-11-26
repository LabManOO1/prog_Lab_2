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
        self.ButtonStart.clicked.connect(self.start)
        self.level_num = 10
        self.Points = []
        self.text = None

    def start(self):
        if self.massage_box():
            self.ButtonStart.hide()
            self.change_complexity.hide()
            self.Levels.hide()
            self.coordinates(10)

    def add_number(self, x: int, y, num):
        self.text = QtWidgets.QLabel(self)
        self.text.setText(num)
        self.text.setGeometry(x, y, 25, 50)
        self.text.setFont(QFont("MS Shell Dlg 2", 30))
        self.text.setStyleSheet("color: white;"
                                "background-color: none;")
        self.text.adjustSize()
        self.text.show()

        self.Points.append((x, y))

    def coordinates(self, count):
        if count > 10:
           count = 10

        for a in range(count):
            while True:

                coord_x = random.randint(0, 750)
                coord_y = random.randint(0, 550)
                for point in self.Points:
                    if (coord_x > point[0]-50 and coord_x < point[0]+50) and (coord_y > point[1]-52 and coord_y < point[1]+52):
                        break
                else:
                    break

            self.add_number(coord_x, coord_y, str(a+1))

    def massage_box(self):
        if self.complexity_light.isChecked() or self.complexity_middle.isChecked() or self.complexity_hard.isChecked():
            return 1
        else:
            mas_box = QMessageBox()
            mas_box.setWindowTitle("Ошибка")
            mas_box.setText("Вы не выбрали уровень сложности!")
            mas_box.setIcon(QMessageBox.Warning)
            mas_box.setStandardButtons(QMessageBox.Ok)
            mas_box.exec_()
            return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()