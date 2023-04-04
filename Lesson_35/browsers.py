import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Пример внешней веб-страницы')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        self.browser.page().pdfPrintingFinished.connect(lambda *args: print('finished', args))
        # Загрузить внешний веб интерфейс
        self.browser.load(QUrl('https://www.ya.ru/'))
        self.setCentralWidget(self.browser)
        self.browser.history()
        self.browser.loadFinished.connect(self.emit_pdf)

    def emit_pdf(self, finished):
        self.browser.show()
        self.browser.page().printToPdf('1.pdf')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())

