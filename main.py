import time
from PyQt5.QtCore import QEventLoop, QTimer
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
        self.Numbers = []
        self.Buttons = []
        self.text = None
        self.clicked_text = None
        self.current_button = None
        self.correct = 0
        self.incorrect = 0
        self.button = None
        self.time2 = 500
        self.exit = False

    def start(self):
        if self.massage_box():
            self.ButtonStart.hide()
            self.change_complexity.hide()
            self.Levels.hide()

            self.loop = QEventLoop()
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.loop.quit)

            self.task = QtWidgets.QLabel(self)
            self.task.setText("Нажмите на числа по возрастанию")
            self.task.setGeometry(180, 10, 440, 70)
            self.task.setStyleSheet("background-color: none;"
                                    "font: 20pt MS Shell Dlg 2;"
                                    "color: rgb(255, 255, 255);")
            self.task.show()

            self.time = 0
            if self.complexity_light.isChecked():
                self.time = 7000
            elif self.complexity_middle.isChecked():
                self.time = 5000
            elif self.complexity_hard.isChecked():
                self.time = 3000

            current_level = QtWidgets.QLabel(self)
            for i in range(1, self.level_num+1):


                current_level.setText(f'{i}/10')
                current_level.setGeometry(10, 560, 71, 30)
                current_level.setStyleSheet("background-color: none;"
                                        "font: 20pt MS Shell Dlg 2;"
                                        "color: rgb(255, 255, 255);")
                current_level.show()


                num = 1
                self.add_numbers(i + 1)

                self.timer.start(self.time)
                self.loop.exec_()

                self.concealment()

                self.timer.start(self.time2)
                self.loop.exec_()

                while True:
                    self.timer.start(self.time2)
                    self.loop.exec_()

                    if self.clicked_text is not None:
                        if self.clicked_text == str(num):
                            self.current_button.hide()
                            num += 1
                            self.clicked_text = None
                            self.current_button = None
                            self.correct += 1
                            if num == i+2:
                                self.correct += 1
                                self.Points = []
                                for k in self.Numbers:
                                    k.hide()
                                self.Numbers = []
                                for j in self.Buttons:
                                    j.hide()
                                self.timer.start(self.time2)
                                self.loop.exec_()

                                break
                        else:
                            self.current_button.hide()
                            self.timer.start(self.time2)
                            self.loop.exec_()
                            self.incorrect += 1
                            self.clicked_text = None
                            self.current_button = None
                            self.Points = []


                            for k in self.Numbers:
                                k.hide()
                            self.Numbers = []
                            for j in self.Buttons:
                                j.hide()
                            self.timer.start(self.time2)
                            self.loop.exec_()
                            break
                    if self.exit:
                        exit()

    def but_clicked(self):
        button = self.sender()
        for i in self.Numbers:
            if button.x()+6 == i.x() and button.y() == i.y():
                self.clicked_text = i.text()
                self.current_button = button



    def create_number(self, x: int, y, num):
        self.text = QtWidgets.QLabel(self)
        self.text.setText(num)
        self.text.setGeometry(x, y, 25, 50)
        self.text.setFont(QFont("MS Shell Dlg 2", 30))
        self.text.setStyleSheet("color: white;"
                                "background-color: none;")
        self.text.adjustSize()
        self.text.show()

        self.Points.append((x, y))
        self.Numbers.append(self.text)

    def create_round_button(self, x, y):
        self.button = QtWidgets.QPushButton(self)
        self.button.setGeometry(x, y, 50, 50)
        self.button.setStyleSheet("border-radius: 25;"
                                  "background-color: rgb(255, 255, 255);")
        self.button.show()
        self.button.clicked.connect(self.but_clicked)

        self.Buttons.append(self.button)

    def closeEvent(self, event):
        self.exit = True



    def concealment(self):


        for i in range(len(self.Points)):
            self.create_round_button(self.Points[i][0]-6, self.Points[i][1])


    def add_numbers(self, count):
        if count > 10:
           count = 10

        for a in range(count):
            while True:

                coord_x = random.randint(15, 725)
                coord_y = random.randint(85, 525)
                for point in self.Points:
                    if (coord_x > point[0]-65 and coord_x < point[0]+65) and (coord_y > point[1]-67 and coord_y < point[1]+67):
                        break
                else:
                    break

            self.create_number(coord_x, coord_y, str(a+1))

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