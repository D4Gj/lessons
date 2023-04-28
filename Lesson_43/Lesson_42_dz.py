from PyQt5 import QtCore, QtWidgets, QtMultimedia
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window |
                                         QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Аудиопроигрыватель")
        self.mplPlayer = QtMultimedia.QMediaPlayer()
        self.mplPlayer.setVolume(1)
        self.mplPlayer.mediaStatusChanged.connect(self.initPlayer)
        self.mplPlayer.stateChanged.connect(self.setPlayerState)
        vbox = QtWidgets.QVBoxLayout()
        btnOpen = QtWidgets.QPushButton("Открыть файл...")
        btnOpen.clicked.connect(self.openFile)
        vbox.addWidget(btnOpen)
        self.sldPosition = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sldPosition.setMinimum(0)
        self.sldPosition.valueChanged.connect(self.mplPlayer.setPosition)
        self.mplPlayer.positionChanged.connect(self.sldPosition.setValue)
        self.sldPosition.setEnabled(False)
        vbox.addWidget(self.sldPosition)
        hbox = QtWidgets.QHBoxLayout()

        self.btnPlay = QtWidgets.QPushButton("&Воспроизвести")
        self.btnPlay.clicked.connect(self.mplPlayer.play)
        self.btnPlay.setEnabled(False)
        hbox.addWidget(self.btnPlay)

        self.btnPause = QtWidgets.QPushButton("&Пауза")
        self.btnPause.clicked.connect(self.mplPlayer.pause)
        self.btnPause.setEnabled(False)
        hbox.addWidget(self.btnPause)

        self.btnStop = QtWidgets.QPushButton("&Остановить")
        self.btnStop.clicked.connect(self.mplPlayer.stop)
        self.btnStop.setEnabled(False)
        hbox.addWidget(self.btnStop)

        vbox.addLayout(hbox)
        hbox = QtWidgets.QHBoxLayout()
        lblVolume = QtWidgets.QLabel("&Громкость")
        hbox.addWidget(lblVolume)
        sldVolume = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        sldVolume.setRange(0, 100)
        sldVolume.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        sldVolume.setTickInterval(10)
        sldVolume.setValue(10)
        lblVolume.setBuddy(sldVolume)
        sldVolume.valueChanged.connect(self.mplPlayer.setVolume)
        hbox.addWidget(sldVolume)
        btnMute = QtWidgets.QPushButton("Выключить звук")
        btnMute.setCheckable(True)
        btnMute.toggled.connect(self.mplPlayer.setMuted)
        hbox.addWidget(btnMute)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.resize(300, 100)

    def openFile(self):
        try:
            file = QtWidgets.QFileDialog.getOpenFileUrl(parent=self, caption="Выберите звуковой файл",
                                                        filter="Звуковые файлы (*.mp3 *.ac3)")
            self.mplPlayer.setMedia(QtMultimedia.QMediaContent(file[0]))
        except Exception as e:
            print(e)

    def initPlayer(self, state):
        if state == QtMultimedia.QMediaPlayer.MediaStatus.LoadedMedia:
            self.mplPlayer.stop()
            self.btnPlay.setEnabled(True)
            self.btnPause.setEnabled(True)
            self.sldPosition.setEnabled(True)
            self.sldPosition.setMaximum(self.mplPlayer.duration())
        elif state == QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia:
            self.mplPlayer.stop()
            self.sldPosition.setValue(0)
            self.sldPosition.setEnabled(True)
            self.btnPlay.setEnabled(False)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)
        elif state == QtMultimedia.QMediaPlayer.MediaStatus.NoMedia or state == \
                QtMultimedia.QMediaPlayer.MediaStatus.InvalidMedia:
            self.sldPosition.setValue(0)
            self.btnPlay.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)

    def setPlayerState(self, state):
        if state == QtMultimedia.QMediaPlayer.State.StoppedState:
            self.sldPosition.setValue(0)
            self.btnPlay.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)
        elif state == QtMultimedia.QMediaPlayer.State.PlayingState:
            self.btnPlay.setEnabled(False)
            self.btnPause.setEnabled(True)
            self.btnStop.setEnabled(True)
        elif state == QtMultimedia.QMediaPlayer.State.PausedState:
            self.btnPlay.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(True)


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
