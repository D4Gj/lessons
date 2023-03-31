from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider
from PyQt5.QtCore import QBasicTimer, Qt
from PyQt5.QtGui import QPixmap
import sys


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        # sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 80, 30)
        sld.setTickPosition(QSlider.TicksLeft)
        sld.setRange(0, 10)
        # sld.sliderMoved()
        self.setWindowTitle("QTextBrowser")
        self.setGeometry(400, 300, 300, 300)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
