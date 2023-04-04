import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1000, 500)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.setWindowTitle("Простой браузер")
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Введите адрес в формете https://www.google.com')
        self.btn1 = QPushButton('Перейти')
        self.btn2 = QPushButton('Сохранить')
        self.browser = QWebEngineView()
        self.browser.page().pdfPrintingFinished.connect(lambda *args: print('finished', args))
        self.btn1.clicked.connect(self.input_url)
        self.btn2.clicked.connect(self.emit_pdf)
        self.browser.load(QUrl('https://google.com'))
        self.hbox.addWidget(self.line_edit)
        self.hbox.addWidget(self.btn1)
        self.hbox.addWidget(self.btn2)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.browser)
        self.setLayout(self.vbox)

    def input_url(self):
        if self.line_edit.text():
            text = self.line_edit.text()
            self.browser.load(QUrl(text))

    def emit_pdf(self, finished):
        self.browser.show()
        self.browser.page().printToPdf("page.pdf")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exit(app.exec_())
