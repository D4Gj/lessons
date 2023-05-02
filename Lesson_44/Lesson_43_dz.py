from PyQt5 import QtCore, QtWidgets, QtMultimedia
import sys
import os


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

        self.ardRecorder = QtMultimedia.QAudioRecorder()
        self.ardRecorder.setVolume(50)
        # Звук сохраняется в .wav
        # Находится в папке рядом с программой
        # C:\Users\inzad\PycharmProjects\lessons\Lesson_43
        fn = QtCore.QUrl.fromLocalFile(os.path.abspath('record.wav'))
        self.ardRecorder.setOutputLocation(fn)
        # Устанавливаем звуковой выход
        self.ardRecorder.setAudioInput(self.ardRecorder.defaultAudioInput())
        # Указываем формат WAV
        self.ardRecorder.setContainerFormat("audio/x-wav")
        # Задаём параметры кодирования звук
        aes = QtMultimedia.QAudioEncoderSettings()
        aes.setCodec('audio/pcm')
        aes.setSampleRate(8000)
        aes.setChannelCount(1)
        aes.setEncodingMode(QtMultimedia.QMultimedia.EncodingMode.ConstantQualityEncoding)
        aes.setQuality(QtMultimedia.QMultimedia.EncodingQuality.VeryHighQuality)

        self.ardRecorder.setAudioSettings(aes)
        self.ardRecorder.statusChanged.connect(self.initRecorder)
        self.ardRecorder.durationChanged.connect(self.showDuration)
        hbox = QtWidgets.QHBoxLayout()

        self.btnRecord = QtWidgets.QPushButton("&Запись")
        self.btnRecord.clicked.connect(self.ardRecorder.record)
        hbox.addWidget(self.btnRecord)

        self.btnPause = QtWidgets.QPushButton("&Пауза")
        self.btnPause.clicked.connect(self.ardRecorder.pause)
        hbox.addWidget(self.btnPause)

        self.btnStop = QtWidgets.QPushButton("&Стоп")
        self.btnStop.clicked.connect(self.ardRecorder.stop)
        hbox.addWidget(self.btnStop)
        vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        lblVolume = QtWidgets.QLabel("&Уровень записи")
        hbox.addWidget(lblVolume)
        sldVolume = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        sldVolume.setRange(0, 100)
        sldVolume.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        sldVolume.setTickInterval(10)
        sldVolume.setValue(10)
        lblVolume.setBuddy(sldVolume)
        sldVolume.valueChanged.connect(self.ardRecorder.setVolume)
        hbox.addWidget(sldVolume)
        vbox.addLayout(hbox)
        self.lblStatus = QtWidgets.QLabel("Готово")
        vbox.addWidget(self.lblStatus)
        self.setLayout(vbox)
        self.resize(300, 100)

    def initRecorder(self, status):
        if status == QtMultimedia.QMediaRecorder.Status.RecordingStatus:
            self.btnRecord.setEnabled(False)
            self.btnPause.setEnabled(True)
            self.btnStop.setEnabled(True)
            self.lblStatus.setText("Запись идёт")
        elif status == QtMultimedia.QMediaRecorder.Status.PausedStatus:
            self.btnRecord.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.lblStatus.setText("Пауза")
        elif status == QtMultimedia.QMediaRecorder.Status.FinalizingStatus:
            self.btnRecord.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)
            self.lblStatus.setText("Готово")

    def showDuration(self, duration):
        self.lblStatus.setText("Записано " + str(duration // 1000) + " секунд")

    def openFile(self):
        try:
            file = QtWidgets.QFileDialog.getOpenFileUrl(parent=self, caption="Выберите звуковой файл",
                                                        filter="Звуковые файлы (*.mp3 *.ac3 *.wav)")
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
