from PyQt5 import QtWidgets, QtTextToSpeech


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TextToSpeech")
        self.resize(300, 300)
        self.vbox = QtWidgets.QVBoxLayout()
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText('Введите текст')
        self.btn = QtWidgets.QPushButton("Преобразовать")
        self.vbox.addWidget(self.lineEdit)
        self.vbox.addWidget(self.btn)
        self.setLayout(self.vbox)
        engine = QtTextToSpeech.QTextToSpeech.availableEngines()[0]
        self.text_to_speech = QtTextToSpeech.QTextToSpeech(engine)
        self.btn.clicked.connect(self.say_text)

    def say_text(self):
        text = self.lineEdit.text()
        self.text_to_speech.say(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    app.exec_()
