import sys
import argparse
from PyQt5 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Аргументы')
        self.resize(300, 300)
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()
        self.textedit = QtWidgets.QTextEdit()
        self.vbox.addWidget(self.textedit)
        parse = argparse.ArgumentParser()
        parse.add_argument('-f', '--file', required=True)
        file = parse.parse_args().file

        if file:
            try:
                with open(file, encoding='utf-8') as file:
                    text = file.read()
                self.textedit.setText(text)
            except FileNotFoundError:
                QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical,
                                      'Ошибка', 'Данного файла не существует',
                                      QtWidgets.QMessageBox.StandardButton.Ok).exec_()

        self.setLayout(self.vbox)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
