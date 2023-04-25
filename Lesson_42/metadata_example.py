from PyQt5 import QtCore, QtWidgets, QtMultimedia
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window |
                                         QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Метаданные")
        self.mplPlayer = QtMultimedia.QMediaPlayer()
        self.mplPlayer.setVolume(1)
        self.mplPlayer.mediaStatusChanged.connect(self.showMetadata)
        vbox = QtWidgets.QVBoxLayout()
        btnOpen = QtWidgets.QPushButton("Открыть файл...")
        btnOpen.clicked.connect(self.openFile)
        vbox.addWidget(btnOpen)
        self.txtOutput = QtWidgets.QTextEdit()
        self.txtOutput.setReadOnly(True)
        vbox.addWidget(self.txtOutput)
        self.setLayout(vbox)
        self.resize(300, 300)

    def openFile(self):
        try:
            file = QtWidgets.QFileDialog.getOpenFileUrl(parent=self, caption="Выберите звуковой файл",
                                                        filter="Звуковые файлы (*.mp3 *.ac3)")
            self.mplPlayer.setMedia(QtMultimedia.QMediaContent(file[0]))
        except Exception as e:
            print(e)

    def showMetadata(self, state):
        self.txtOutput.clear()
        if state == QtMultimedia.QMediaPlayer.MediaStatus.LoadedMedia:
            keys = self.mplPlayer.availableMetaData()
            s = ''
            for k in keys:
                v = self.mplPlayer.metaData(k)
                if v is list:
                    v = ', '.join(v)
                s += "<strong>" + k + "</strong>: " + str(v) + "<br>"
            self.txtOutput.setHtml(s)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())