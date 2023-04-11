import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt'

        self.initUi()

    def initUi(self):
        self.text = 'Hello'
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Draw something')
        self.autoFillBackground()
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        self.m = PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(500, 500)

        self.show()


class PaintWidget(QWidget):
    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        qp = QPainter(self)
        qp.setPen(Qt.black)
        size = self.size()
        qp.setBrush(QColor(200, 2, 0))
        qp.drawRect(0, 0, 100, 100)

        qp.setBrush(QColor(0, 200, 0))
        qp.drawRect(100, 0, 100, 100)

        qp.setBrush(QColor(0, 0, 200))
        qp.drawRect(200, 0, 100, 100)

        for i in range(0, 100):
            qp.setBrush(QColor(i * 10, 0, 0))
            qp.drawRect(10 * i, 100, 10, 32)

            qp.setBrush(QColor(i * 10, i * 10, 0))
            qp.drawRect(10 * i, 100 + 32, 10, 32)

            qp.setBrush(QColor(i * 2, i * 10, i * 1))
            qp.drawRect(10 * i, 100+64, 10, 32)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
