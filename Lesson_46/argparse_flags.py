import sys
import argparse
from PyQt5 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Аргументы')
        self.resize(300, 300)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-gui', action='store_const', const=True)
    flag = parser.parse_args().no_gui
    if not flag:
        app = QtWidgets.QApplication(sys.argv)
        window = Window()
        window.show()
        app.exec_()
    else:
        print('Консольная версия приложения')
