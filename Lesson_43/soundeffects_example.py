from PyQt5 import QtCore, QtWidgets, QtMultimedia
import sys
import os


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window |
                                         QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Звуковые эффекты")
        self.sndEffect = QtMultimedia.QSoundEffect()
        self.sndEffect.setVolume(1)
        # Задаём файл-источник
        # C:\Users\inzad\PycharmProjects\lessons\Lesson_43
        fn = QtCore.QUrl.fromLocalFile(os.path.abspath('effect.wav'))
        self.sndEffect.setSource(fn)
        self.sndEffect.loopsRemainingChanged.connect(self.showCount)
        self.sndEffect.playingChanged.connect(self.clearCount)
        # Кнопки для запуска звуков
        vbox = QtWidgets.QVBoxLayout()
        lblPlay = QtWidgets.QLabel("Воспроизвести...")
        vbox.addWidget(lblPlay)
        btnOnce = QtWidgets.QPushButton("... один раз")
        btnOnce.clicked.connect(self.playOnce)
        vbox.addWidget(btnOnce)
        btnTen = QtWidgets.QPushButton("... десять раз")
        btnTen.clicked.connect(self.playTen)
        vbox.addWidget(btnTen)
        btnInfinite = QtWidgets.QPushButton("... бесконечно")
        btnInfinite.clicked.connect(self.playInfinite)
        vbox.addWidget(btnInfinite)
        btnStop = QtWidgets.QPushButton("&Стоп")
        btnStop.clicked.connect(self.sndEffect.stop)
        vbox.addWidget(btnStop)
        self.lblStatus = QtWidgets.QLabel("")
        vbox.addWidget(self.lblStatus)
        self.setLayout(vbox)
        self.resize(200, 100)

    def playOnce(self):
        self.sndEffect.setLoopCount(1)
        self.sndEffect.play()

    def playTen(self):
        self.sndEffect.setLoopCount(10)
        self.sndEffect.play()

    def playInfinite(self):
        self.sndEffect.setLoopCount(QtMultimedia.QSoundEffect.Loop.Infinite)
        self.sndEffect.play()

    def showCount(self):
        self.lblStatus.setText("Воспроизведено " + str(self.sndEffect.loopCount() - self.sndEffect.loopsRemaining())
                               + " раз")

    def clearCount(self):
        if not self.sndEffect.isPlaying():
            self.lblStatus.setText("")


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
