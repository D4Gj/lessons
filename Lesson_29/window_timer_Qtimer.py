import sys
from PyQt5 import QtWidgets, QtCore
import time


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle('Программа')
        self.resize(200, 100)
        self.label = QtWidgets.QLabel("")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button1 = QtWidgets.QPushButton('Запустить')
        self.button2 = QtWidgets.QPushButton('Остановить')
        self.button2.setEnabled(False)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        self.setLayout(vbox)

        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked.connect(self.on_clicked_button2)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_timeout)

    def on_clicked_button1(self):
        self.timer.start(1000)
        self.button1.setEnabled(False)
        self.button2.setEnabled(True)

    def on_clicked_button2(self):
        self.timer.stop()
        self.button1.setEnabled(True)
        self.button2.setEnabled(False)

    def on_timeout(self) -> None:
        self.label.setText(f'<h1>{time.strftime("%H:%M:%S")}</h1>')


if __name__ in '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
