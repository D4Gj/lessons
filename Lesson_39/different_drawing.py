from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.text = 'Hello'
        self.setGeometry(300, 500, 350, 280)
        self.setWindowTitle('Brushes')
        self.show()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, qp):
        brush = QBrush(QColor('darkmagenta'), Qt.SolidPattern)
        qp.setBrush(brush)
        qp.setPen(QPen(QColor().fromCmykF(0.0, 0.5, 0.5, 0.0, 1.0), 10, join=Qt.SvgMiterJoin))
        qp.drawArc(10, 15, 90, 60, 200, 300)
        qp.drawEllipse(10, 200, 90, 60)
        qp.drawPolygon(QPoint(100, 100), QPoint(200, 100), QPoint(300, 100), QPoint(100, 200), QPoint(100, 300), )

        qp.drawPie(150, 15, 90, 60, -50, 1800)

        qp.drawRect()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
