from PyQt5 import QtCore, QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel('Hello world')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnQuit = QtWidgets.QPushButton("&Close window")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('OOP type window')
    window.resize(300,150)
    window.show()
    sys.exit(app.exec_())