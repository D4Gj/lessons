from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QTextBrowser, QSpinBox, \
    QDoubleSpinBox, QHBoxLayout, QLabel
from PyQt5.QtCore import QUrl
import sys


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        sbox = QSpinBox(self)
        doublesbox = QDoubleSpinBox(self)
        sbox.valueChanged.connect(self.updateLabel)
        doublesbox.valueChanged.connect(self.updateLabel)
        self.label = QLabel('', self)
        hbox.addWidget(sbox)
        hbox.addSpacing(15)
        hbox.addWidget(doublesbox)

        hbox.addWidget(self.label)
        self.setLayout(hbox)
        self.setWindowTitle("Spinboxes")
        self.setGeometry(400, 300, 300, 300)
        self.show()

    def updateLabel(self, value):
        self.label.setText(str(value))


def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
