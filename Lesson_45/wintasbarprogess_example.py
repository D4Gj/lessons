from PyQt5 import QtWidgets, QtWinExtras, QtGui, QtCore
import sys
import time


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.WindowType.Window |
                                                       QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Печать изображений")

        # Создаём кнопку панели задач
        self.taskbarButton = QtWinExtras.QWinTaskbarButton(parent=self)
        self.progress = self.taskbarButton.progress()
        self.progress.setRange(0, 10)
        self.progress.show()
        hbox = QtWidgets.QHBoxLayout()
        btnStart = QtWidgets.QPushButton("Пуск")
        btnStart.clicked.connect(self.start)
        hbox.addWidget(btnStart)
        btnPause = QtWidgets.QPushButton("Пауза")
        btnPause.clicked.connect(self.progress.pause)
        hbox.addWidget(btnPause)
        btnStop = QtWidgets.QPushButton("Стоп")
        btnStop.clicked.connect(self.progress.stop)
        hbox.addWidget(btnStop)
        btnResume = QtWidgets.QPushButton("Возобновить")
        btnResume.clicked.connect(self.progress.resume)
        hbox.addWidget(btnResume)
        self.setLayout(hbox)
        self.resize(200, 100)

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        self.taskbarButton.setWindow(self.windowHandle())

    def start(self):
        """При нажатии Старт последовательно, с секундным промежутком
        мы будем увеличивать значение индикатора от 0 до 10, если индикатор
        не поставлен на паузу и не остановлен"""
        i = 0
        while i < 11:
            if not self.progress.isPaused() and not self.progress.isStopped():
                self.progress.setValue(i)
                i += 1
            time.sleep(1)
            QtWidgets.qApp.processEvents()
        self.progress.reset()


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
