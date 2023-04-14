from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.text = 'Hello'
        self.setGeometry(300, 300, 350, 280)
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
        qp.drawRect(10, 15, 90, 60)

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush = QBrush(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush = QBrush(Qt.Dense4Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 200, 90, 60)

        brush = QBrush(QColor('darkmagenta'), Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 150, 90, 60)

        brush = QBrush(Qt.LinearGradientPattern)
        qp.setBrush(brush)
        qp.drawRect(300, 300, 90, 60)

        brush = QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(150, 250, 90, 60)

        brush = QBrush(Qt.LinearGradientPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 150, 90, 60)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
