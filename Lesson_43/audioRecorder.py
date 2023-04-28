from PyQt5 import QtCore, QtWidgets, QtMultimedia
import sys
import os


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window |
                                         QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Простой диктофон")
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
        vbox = QtWidgets.QVBoxLayout()
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


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
