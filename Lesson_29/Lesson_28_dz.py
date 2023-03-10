import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Программа')
        self.resize(300, 200)

        self.layout = QtWidgets.QVBoxLayout()

        self.line_edit = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton('Кнопка')
        self.button.clicked.connect(self.button_click)

        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def button_click(self):
        text = self.line_edit.text()
        print(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
