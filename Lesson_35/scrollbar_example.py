from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Python')
        self.setGeometry(100, 100, 500, 400)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        scroll = QScrollBar(self)
        scroll.setRange(0,3)
        
        scroll.setGeometry(100, 50, 30, 200)
        scroll.setStyleSheet("background: blue;")

        label = QLabel('Пример', self)
        label.setGeometry(200, 100, 300, 80)

        label.setWordWrap(True)
        scroll.valueChanged.connect(lambda: do_action())

        def do_action():
            value = scroll.value()
            label.setText(f'Значение {value}')


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
