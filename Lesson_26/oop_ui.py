from PyQt5 import QtCore, QtWidgets, uic


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('MyForm.ui', self)
        self.pushButton.clicked.connect(QtWidgets.qApp.quit)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
