import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQT цветные прямоугольники'
        self.left = 10
        self.top = 50
        self.width = 440
        self.height = 280
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 205, 255))
        self.setPalette(p)
        self.m = PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(self.width, self.height)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, QDockWidget(), Qt.Orientation.Horizontal)
        self.show()


class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QColor(0, 0, 0))
        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(30, 90, 100, 100)
        qp.setBrush(QColor(200, 150, 0))
        qp.drawRect(150, 90, 100, 100)
        qp.setBrush(QColor(200, 150, 250))
        qp.drawRect(270, 90, 100, 100)


if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    app.exec_()
