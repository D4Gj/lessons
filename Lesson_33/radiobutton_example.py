import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QRadioButton, QHBoxLayout,
                             QVBoxLayout)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        rb1 = QRadioButton('Large', self)
        rb1.toggled.connect(self.updateLabel)

        rb2 = QRadioButton('Medium', self)
        rb2.toggled.connect(self.updateLabel)

        rb3 = QRadioButton('Small', self)
        rb3.toggled.connect(self.updateLabel)

        self.label = QLabel('', self)

        hbox.addWidget(rb1)
        hbox.addWidget(rb2)
        hbox.addWidget(rb3)

        vbox.addSpacing(15)
        vbox.addLayout(hbox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.setWindowTitle("QRadioButton")
        self.setGeometry(400, 300, 300, 300)
        self.show()
        rb2.setChecked(True)

    def updateLabel(self):
        rbtn = self.sender()
        print(rbtn)
        if rbtn.isChecked() == True:
            self.label.setText(rbtn.text())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
