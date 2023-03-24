import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QCheckBox)
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.setTristate(True)
        cb.stateChanged.connect(self.changeWindowTitle)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeWindowTitle(self, state):
        print(state)
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')

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
