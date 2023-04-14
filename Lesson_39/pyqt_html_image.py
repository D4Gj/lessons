from PyQt5 import QtWidgets, QtCore, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName('centralWidget')
        self.centralWidget.setStyleSheet("""
        #centralWidget {
            border-image: url(logo.png);
        }
        """)
        self.setCentralWidget(self.centralWidget)
        rect = QtCore.QRect(0, 0, self.width(), self.height())
        region = QtGui.QRegion(rect, QtGui.QRegion.RegionType.Rectangle)
        self.setMask(region)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ex = MainWindow()
    ex.show()
    app.exec()
