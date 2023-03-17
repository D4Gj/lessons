import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon


class Window(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Программа расчёта')
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(500, 200)

        self.base_layout = QtWidgets.QVBoxLayout()
        self.text_layout = QtWidgets.QHBoxLayout()
        self.button_layout = QtWidgets.QHBoxLayout()
        self.base_layout.addLayout(self.text_layout)
        self.base_layout.addLayout(self.button_layout)
        self.text_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.text1 = QtWidgets.QLineEdit()
        self.text2 = QtWidgets.QLineEdit()
        self.text_layout.addWidget(self.text1)
        self.text_layout.addWidget(self.text2)
        self.label = QtWidgets.QLabel(f'Ответ:')
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setFont(QtGui.QFont('Arial', 20))

        self.area_button = QtWidgets.QPushButton('Площадь')
        self.perimetr_button = QtWidgets.QPushButton('Периметр')
        self.button_layout.addWidget(self.area_button)
        self.button_layout.addWidget(self.perimetr_button)
        self.base_layout.addWidget(self.label)
        self.setLayout(self.base_layout)
        self.area_button.clicked.connect(self.get_area)
        self.perimetr_button.clicked.connect(self.get_perimetr)

    def get_area(self):
        try:
            text1 = float(self.text1.text())
            text2 = float(self.text2.text())
            result = text1 * text2

            self.label.setText(f'Ответ: {result}')
        except ValueError:
            self.label.setText('Ошибочно введены данные')
        finally:
            self.perimetr_button.setEnabled(False)
            self.area_button.setEnabled(False)
            timer = QtCore.QTimer()
            timer.setInterval(1000)
            timer.singleShot(5000, self.reset_data)

    def get_perimetr(self):
        try:
            text1 = float(self.text1.text())
            text2 = float(self.text2.text())
            result = (text1 + text2) * 2

            self.label.setText(f'Ответ: {result}')
        except ValueError:
            self.label.setText('Ошибочно введены данные')
        finally:
            self.perimetr_button.setEnabled(False)
            self.area_button.setEnabled(False)
            timer = QtCore.QTimer()
            timer.setInterval(1000)
            timer.singleShot(5000, self.reset_data)

    def reset_data(self):
        self.label.setText(f'Ответ:')
        self.text1.clear()
        self.text2.clear()
        self.text1.setFocus()
        self.perimetr_button.setEnabled(True)
        self.area_button.setEnabled(True)

    def mouseDoubleClickEvent(self, e: QtGui.QMouseEvent) -> None:
        print('Двойное нажатие мышью')
        self.label.setStyleSheet('border: 1px solid black;')
        print(self.label.geometry().x())
        print(self.label.geometry().y())
        print(self.label.geometry().height())
        print(self.label.geometry().width())


    def closeEvent(self, e: QtGui.QCloseEvent) -> None:
        reply = QtWidgets.QMessageBox.question(self, 'Информация',
                                               'Вы уверены, что хотите выйти?',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No
                                               )
        if reply == QtWidgets.QMessageBox.Yes:
            window.close()
            e.accept()
        else:
            e.ignore()


if __name__ in '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
