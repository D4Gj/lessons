import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtGui


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
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        # qp.setPen(QColor('darkmagenta'))
        # qp.setPen(QColor().fromHsvF(0.0, 1.0, 1.0, 0.5))
        # qp.setPen(QColor().fromRgbF(1.0, 1.0, 1.0, 1.0))
        qp.setPen(QColor().fromCmykF(1.0, 1.0, 1.0, 1.0, 1.0))
        qp.setFont(QFont('Calibri', 50, 1, True))
        qp.drawText(event.rect(), Qt.AlignHCenter, self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
