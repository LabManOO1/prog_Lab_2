from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QPixmap
import sys
import random

from PyQt5 import QtWidgets


class MainWindow(QMainWindow):  # Класс с окном
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindow.ui', self)  # Подгружаем основное окно, созданное в Qt Designer
        self.setWindowIcon(QIcon('MainIcon.png'))  # Ставим иконку для основного окна
        self.ButtonStart.clicked.connect(self.start)  # Подключаем к кнопке Start метод start
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
        self.result = None
        self.flag = False
        self.correct_answers = None
        self.results = None
        self.again = None
        self.loop = QEventLoop()
        self.timer = QTimer(self)
        self.time = 0

    def start(self):  # Метод в котором выполняется основная программа
        self.correct = 0
        self.incorrect = 0

        if self.massage_box():  # Проверка на выбор сложности
            self.ButtonStart.hide()  # Скрытие виджетов с экрана
            self.change_complexity.hide()
            self.Levels.hide()

            self.timer.timeout.connect(self.loop.quit)

            task = QtWidgets.QLabel(self)  # Создание виджета "Нажмите на числа по возрастанию"
            task.setText("Нажмите на числа по возрастанию")
            task.setGeometry(180, 10, 440, 70)
            task.setStyleSheet("background-color: none;"
                               "font: 20pt MS Shell Dlg 2;"
                               "color: rgb(255, 255, 255);")
            task.show()

            if self.complexity_light.isChecked():  # Установка времени задержки в зависимости от сложности
                self.time = 7000
            elif self.complexity_middle.isChecked():
                self.time = 5000
            elif self.complexity_hard.isChecked():
                self.time = 3000
            # Создание виджетов с номером уровня и кол-вом правильных и неправильных ответов
            current_level = QtWidgets.QLabel(self)
            correct = QtWidgets.QLabel(self)
            correct_text = QtWidgets.QLabel(self)
            pixmap = QPixmap('check_mark.png')
            incorrect_text = QtWidgets.QLabel(self)

            incorrect = QtWidgets.QLabel(self)
            pixmap1 = QPixmap('cross.png')

            correct.setGeometry(575, 545, 40, 30)
            correct.setStyleSheet("background-color: none;")

            correct.setPixmap(pixmap)
            correct.resize(pixmap.width(), pixmap.height())

            correct.show()

            correct_text.setText(str(self.correct))
            correct_text.setGeometry(640, 560, 40, 30)
            correct_text.setStyleSheet("background-color: none;"
                                       "font: 26pt MS Shell Dlg 2;"
                                       "color: rgb(255, 255, 255);")

            correct_text.show()

            incorrect.setGeometry(700, 545, 40, 30)
            incorrect.setStyleSheet("background-color: none;")
            # incorrect.setWindowIcon(QIcon('coss.png'))

            incorrect.setPixmap(pixmap1)
            incorrect.resize(pixmap1.width(), pixmap1.height())

            incorrect.show()

            incorrect_text.setText(str(self.incorrect))
            incorrect_text.setGeometry(765, 560, 40, 30)
            incorrect_text.setStyleSheet("background-color: none;"
                                         "font: 26pt MS Shell Dlg 2;"
                                         "color: rgb(255, 255, 255);")
            incorrect_text.setWindowIcon(QIcon('check_mark.png'))

            incorrect_text.show()
            for i in range(1, self.level_num + 1):  # Цикл всех уровней

                current_level.setText(f'{i}/10')
                current_level.setGeometry(10, 560, 71, 30)
                current_level.setStyleSheet("background-color: none;font: 26pt MS Shell Dlg 2;"
                                            "color: rgb(255, 255, 255);")
                current_level.adjustSize()
                current_level.show()

                num = 1
                self.add_numbers(i + 1)

                self.timer.start(self.time)  # Задержка времени
                self.loop.exec_()

                self.concealment()

                self.timer.start(self.time2)
                self.loop.exec_()

                while True:  # Цикл, который ждет нажатия кнопки
                    self.timer.start(self.time2)
                    self.loop.exec_()

                    if self.clicked_text is not None:  # Проверка на нажатие кнопки
                        if self.clicked_text == str(num):
                            self.current_button.hide()
                            num += 1
                            self.clicked_text = None
                            self.current_button = None
                            if num == i + 2:  # проверка на нажатие правильной кнопки
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
                    if self.exit:  # Завершение программы при закрытии приложения
                        exit()

                correct_text.setText(str(self.correct))
                correct_text.setGeometry(640, 560, 40, 30)
                correct_text.setStyleSheet("background-color: none;"
                                           "font: 26pt MS Shell Dlg 2;"
                                           "color: rgb(255, 255, 255);")
                correct_text.show()

                incorrect_text.setText(str(self.incorrect))
                incorrect_text.setGeometry(765, 560, 40, 30)
                incorrect_text.setStyleSheet("background-color: none;"
                                             "font: 26pt MS Shell Dlg 2;"
                                             "color: rgb(255, 255, 255);")
                incorrect_text.setWindowIcon(QIcon('check_mark.png'))

                incorrect_text.show()

            # Скрытие виджетов при прохождении всех уровней
            task.hide()
            current_level.hide()
            correct_text.hide()
            incorrect_text.hide()
            correct.hide()
            incorrect.hide()

            # Создание виджетов при прохождении всех уровней
            self.correct_answers = QtWidgets.QLabel(self)
            self.correct_answers.setText(f"Правильных ответов: {self.correct}")
            self.correct_answers.setGeometry(210, 160, 400, 30)
            self.correct_answers.setStyleSheet("background-color: none;"
                                               "font: 26pt MS Shell Dlg 2;"
                                               "color: rgb(255, 255, 255);")
            self.correct_answers.show()

            # Оценка результатов
            if self.correct > 7:
                self.result = "Отличный результат!"
            elif self.correct > 4 and self.correct < 8:
                self.result = "Хороший результат!"
            else:
                self.result = "Низкий результат :("

            self.results = QtWidgets.QLabel(self)
            self.results.setText(self.result)
            self.results.setGeometry(260, 220, 310, 30)
            self.results.setStyleSheet("background-color: none;"
                                       "font: 20pt MS Shell Dlg 2;"
                                       "color: rgb(255, 255, 255);")
            self.results.show()

            self.again = QtWidgets.QPushButton(self)
            self.again.setText("Еще раз")
            self.again.setGeometry(285, 310, 230, 81)
            self.again.setStyleSheet('font: 36pt "MS Shell Dlg 2";'
                                     'color: rgb(255, 255, 255);'
                                     'border-color: rgb(92, 0, 149);')
            self.again.show()

            self.again.clicked.connect(self.from_the_start)
            self.flag = True

    def from_the_start(self):  # Метод, который вызывается при нажатии кнопки "Еще раз"
        self.correct_answers.hide()
        self.results.hide()
        self.again.hide()
        self.ButtonStart.show()
        self.change_complexity.show()
        self.Levels.show()

    def but_clicked(self):  # Метод, который вызывается при нажатии кнопки, закрывающей число
        button = self.sender()
        for i in self.Numbers:
            if button.x() + 6 == i.x() and button.y() == i.y():
                self.clicked_text = i.text()
                self.current_button = button

    def create_number(self, x: int, y, num):  # Создание виджета с числом
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

    def create_round_button(self, x, y):  # Создание кнопки, которая скрывает число
        self.button = QtWidgets.QPushButton(self)
        self.button.setGeometry(x, y, 50, 50)
        self.button.setStyleSheet("border-radius: 25;"
                                  "background-color: rgb(255, 255, 255);")
        self.button.show()
        self.button.clicked.connect(self.but_clicked)

        self.Buttons.append(self.button)

    def closeEvent(self, event):  # Переопределение метода closeEvent, чтобы при закрытии
        # приложения останавливалась программа
        self.exit = True

    def concealment(self):  # Метод, при вызове которого создаются все кнопки, закрывающие числа

        for i in range(len(self.Points)):
            self.create_round_button(self.Points[i][0] - 6, self.Points[i][1])

    def add_numbers(self, count):  # Метод, при вызове которого создаются виджеты с числами, в случайных местах
        if count > 10:
            count = 10

        for a in range(count):
            while True:

                coord_x = random.randint(15, 725)
                coord_y = random.randint(85, 500)
                for point in self.Points:
                    if (coord_x > point[0] - 65 and coord_x < point[0] + 65) and (
                            coord_y > point[1] - 67 and coord_y < point[1] + 67):
                        break
                else:
                    break

            self.create_number(coord_x, coord_y, str(a + 1))

    def massage_box(self):  # Метод, при вызове которого создается всплывающее окно
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
