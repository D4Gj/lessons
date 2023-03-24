import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class ButtonExample(QWidget):

    def __init__(self):
        super().__init__()
        self.btn = QPushButton('&Нажми', self)
        self.setToolTip('Кнопка')
        self.btn.setGeometry(100, 20, 100, 30)
        self.btn.clicked.connect(self.onClicked)
        self.msgLabel = QLabel('', self)
        self.msgLabel.setGeometry(90, 60, 290, 60)

        self.setWindowTitle('Использование кнопки')
        self.setGeometry(10, 10, 300, 150)
        self.btn.setAutoRepeat(True)
        self.btn.animateClick(1000)
        self.btn.click()
        self.btn.setCheckable(True)
        # self.btn.toggle()
        self.btn.setAutoExclusive(True)
        self.btn.setDown(False)
        self.move(850, 300)
        self.show()

    def onClicked(self):
        self.msgLabel.setText('Нажата кнопка')
        print(self.btn.text())


app = QApplication(sys.argv)
button = ButtonExample()
app.exec()
