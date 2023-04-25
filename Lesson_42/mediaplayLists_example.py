from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
import sys
import os


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window |
                                         QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Видеопроигрыватель")
        self.mplPlayer = QtMultimedia.QMediaPlayer()
        self.mplPlayer.setVolume(1)
        self.playlist = QtMultimedia.QMediaPlaylist()
        files = ['media/sample-3s.mp3', 'media/sample-6s.mp3', 'media/sample-3s.mp3',
                 'media/Стандартный звонок на Blackberry.mp3']
        for f in files:
            fn = QtCore.QUrl.fromLocalFile(os.path.abspath(f))
            self.playlist.addMedia(QtMultimedia.QMediaContent(fn))
        self.playlist.insertMedia(4, self.playlist.media(1))
        self.playlist.removeMedia(1)
        self.playlist.setCurrentIndex(0)
        self.mplPlayer.setPlaylist(self.playlist)
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        self.btnPlay = QtWidgets.QPushButton("Пуск")
        self.btnPlay.clicked.connect(self.mplPlayer.play)
        hbox.addWidget(self.btnPlay)
        self.btnNext = QtWidgets.QPushButton("Следующий")
        self.btnNext.clicked.connect(self.playlist.next)
        hbox.addWidget(self.btnNext)
        self.btnPrevious = QtWidgets.QPushButton("Предыдущий")
        self.btnPrevious.clicked.connect(self.playlist.previous)
        hbox.addWidget(self.btnPrevious)
        self.lblCurrent = QtWidgets.QLabel("")
        vbox.addLayout(hbox)
        vbox.addWidget(self.lblCurrent)
        self.playlist.currentMediaChanged.connect(self.showFile)
        self.setLayout(vbox)
        self.resize(300, 70)

    def showFile(self, content):
        self.lblCurrent.setText(content.canonicalUrl().fileName())


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
