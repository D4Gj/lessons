import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtCore
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        self.text = 'Hello'
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Draw text')
        self.show()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(event, qp)
        qp.end()

    def drawPoints(self, event, qp):
        # qp.setPen(QColor('darkmagenta'))
        # qp.setPen(QColor().fromHsvF(0.0, 1.0, 1.0, 0.5))
        # qp.setPen(QColor().fromRgbF(1.0, 1.0, 1.0, 1.0))
        qp.setPen(QPen(QColor().fromCmykF(1.0, 1.0, 1.0, 1.0, 0.3), 10, cap=Qt.RoundCap, join=Qt.BevelJoin))
        size = self.size()
        # qp.setBrush(QColor().fromCmykF(1.0, 1.0, 1.0, 1.0, 1.0))
        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)
        qp.setFont(QFont('Calibri', 50, 990, ))
        qp.setPen(QPen(QColor().fromCmykF(0.0, 0.5, 0.5, 0.0, 1.0), 100, join=Qt.SvgMiterJoin))
        qp.drawText(event.rect(), Qt.AlignHCenter, self.text)
        qp.drawLines([QtCore.QLine(50, 50, 50, 100), QtCore.QLine(30, 30, 200, 200)])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
