from PyQt5 import QtCore, QtGui, QtWidgets
import time


# QSplashScreen(<Родитель>[, <Изображение>][,flags=<Тип окна>]_

class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText('Закрыть окно')
        self.clicked.connect(QtWidgets.qApp.quit)

    def load_data(self, sp):
        for i in range(1, 11):
            time.sleep(2)
            sp.showMessage("Loading data... {0}%".format(i * 10),
                           QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom,
                           QtCore.Qt.black)
        QtWidgets.qApp.processEvents()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap('logo.png'))
    splash.show()
    QtWidgets.qApp.processEvents()
    window = MyWindow()
    window.setWindowTitle('Splash screen')
    window.resize(300, 30)
    window.load_data(splash)
    window.show()
