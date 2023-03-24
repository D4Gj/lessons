import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDateTimeEdit, QHBoxLayout, QLabel)
from PyQt5.QtCore import QDate, QDateTime, QTime
from PyQt5.Qt import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        sbox = QDateTimeEdit(self)
        sbox.setDisplayFormat('yy.MM.dd HH:mm:ss')
        sbox.setTimeSpec(Qt.UTC)
        sbox.setCalendarPopup(True)
        hbox.addWidget(sbox)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('QCheckBox')
        self.show()

        print(sbox.dateTime())
        print(sbox.date())
        print(sbox.time())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
