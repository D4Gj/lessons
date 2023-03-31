from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer, Qt
import sys


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(80, 80)
        self.btn.clicked.connect(self.doAction)
        #self.pbar.setRange(0,100)
        self.timer = QBasicTimer()
        self.step = 0
        self.pbar.setOrientation(Qt.Vertical)

        self.setWindowTitle("QTextBrowser")
        self.setGeometry(400, 300, 300, 300)
        self.show()

    def timerEvent(self, e) -> None:
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('End timer')
            return
        self.step += 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
