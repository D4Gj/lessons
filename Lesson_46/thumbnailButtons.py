from PyQt5 import QtCore, QtWidgets, QtWinExtras, QtGui
import sys, time


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.WindowType.Window |
                                                       QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Панель инструментов на миниатюре")
        icon1 = QtGui.QIcon('box.png')
        icon2 = QtGui.QIcon('tax-free.png')
        icon3 = QtGui.QIcon('shipped.png')
        self.thumbnailToolbar = QtWinExtras.QWinThumbnailToolBar(parent=self)
        # Создаём кнопки 1 и 2
        button1 = QtWinExtras.QWinThumbnailToolButton(parent=self)
        button1.setIcon(icon1)
        button1.setToolTip("Кнопка 1")
        button1.setDismissOnClick(True)
        button1.clicked.connect(self.button1Clicked)
        self.thumbnailToolbar.addButton(button1)
        button2 = QtWinExtras.QWinThumbnailToolButton(parent=self)
        button2.setIcon(icon2)
        button2.setToolTip("Кнопка 2")
        button2.setDismissOnClick(True)
        button2.clicked.connect(self.button2Clicked)
        self.thumbnailToolbar.addButton(button2)
        # Создаём кнопку для свободного простраства между 2 и 3 кнопкой
        button0 = QtWinExtras.QWinThumbnailToolButton(parent=self)
        button0.setInteractive(False)
        button0.setFlat(True)
        self.thumbnailToolbar.addButton(button0)
        # 3 кнопка
        button3 = QtWinExtras.QWinThumbnailToolButton(parent=self)
        button3.setIcon(icon3)
        button3.setToolTip("Кнопка 3")
        button3.clicked.connect(self.button3Clicked)
        self.thumbnailToolbar.addButton(button3)
        # Создаём надпись, куда будут выводиться сообщения о нажатии кнопок
        # с панели инструментов и кнопку выхода
        vbox = QtWidgets.QVBoxLayout()
        self.lblOutput = QtWidgets.QLabel(parent=self)
        vbox.addWidget(self.lblOutput)
        btnClose = QtWidgets.QPushButton("Выход")
        btnClose.clicked.connect(QtWidgets.qApp.quit)
        vbox.addWidget(btnClose)
        self.setLayout(vbox)
        self.resize(200, 100)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.thumbnailToolbar.setWindow(self.windowHandle())

    def button1Clicked(self):
        self.lblOutput.setText('Кнопка 1 нажата')

    def button2Clicked(self):
        self.lblOutput.setText('Кнопка 2 нажата')

    def button3Clicked(self):
        self.lblOutput.setText('Кнопка 3 нажата')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()