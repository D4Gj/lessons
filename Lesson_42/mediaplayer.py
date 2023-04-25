from PyQt5 import QtMultimedia
from PyQt5 import QtCore

print(QtMultimedia.QMediaPlayer.Flag.LowLatency)
print(QtMultimedia.QMediaPlayer.Flag.StreamPlayback)
print(QtMultimedia.QMediaPlayer.Flag.VideoSurface)

mp = QtMultimedia.QMediaPlayer()
mc = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(
    r'C:\Users\inzad\PycharmProjects\lessons\Lesson_42\media\Стандартный звонок на Blackberry.mp3'))
