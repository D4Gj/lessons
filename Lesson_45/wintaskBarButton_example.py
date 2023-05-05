from PyQt5 import QtWidgets, QtWinExtras, QtGui, QtCore
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.WindowType.Window |
                                                       QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Печать изображений")
        self.icon1 = QtGui.QIcon('logo.png')
        self.icon2 = QtGui.QIcon('open-file.png')
        # Создаём кнопку панели задач
        self.taskbarButton = QtWinExtras.QWinTaskbarButton(parent=self)
        hbox = QtWidgets.QHBoxLayout()
        btnIcon1 = QtWidgets.QPushButton(self.icon1, "Значок &1")
        btnIcon1.clicked.connect(self.setIcon1)
        hbox.addWidget(btnIcon1)
        btnIcon2 = QtWidgets.QPushButton(self.icon2, "Значок &2")
        btnIcon2.clicked.connect(self.setIcon2)
        hbox.addWidget(btnIcon2)
        btnClearIcon = QtWidgets.QPushButton("&Убрать значок")
        btnClearIcon.clicked.connect(self.taskbarButton.clearOverlayIcon)
        hbox.addWidget(btnClearIcon)
        self.setLayout(hbox)
        self.resize(200, 50)

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        self.taskbarButton.setWindow(self.windowHandle())

    def setIcon1(self):
        self.taskbarButton.setOverlayIcon(self.icon1)

    def setIcon2(self):
        self.taskbarButton.setOverlayIcon(self.icon2)


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
