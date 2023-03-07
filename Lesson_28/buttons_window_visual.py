from PyQt5 import QtCore, QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.btnMin = QtWidgets.QPushButton('Свернуть окно')
        self.btnMax = QtWidgets.QPushButton('Развернуть окно')
        self.btnFull = QtWidgets.QPushButton('Полный экран')
        self.btnNormal = QtWidgets.QPushButton('Нормальный размер экрана')
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.btnMax)
        vbox.addWidget(self.btnMin)
        vbox.addWidget(self.btnFull)
        vbox.addWidget(self.btnNormal)
        self.setLayout(vbox)
        self.btnMin.clicked.connect(self.on_min)
        self.btnMax.clicked.connect(self.on_max)
        self.btnFull.clicked.connect(self.on_full)
        self.btnNormal.clicked.connect(self.on_normal)

    def on_min(self):
        self.showMinimized()

    def on_max(self):
        self.showMaximized()

    def on_full(self):
        self.showFullScreen()

    def on_normal(self):
        self.showNormal()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('Тест кнопок сворачивания')
    # от 0.0 до 1.0
    window.setWindowOpacity(0.9)
    window.resize(300, 30)
    window.show()
    print(window.windowOpacity())
    sys.exit(app.exec_())
