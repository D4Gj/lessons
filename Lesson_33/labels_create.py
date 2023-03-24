import sys
from PyQt5 import QtWidgets, QtGui


def main():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    labelA = QtWidgets.QLabel(windowExample)
    labelA.setText('Hello')
    windowExample.setWindowTitle('Label example')
    windowExample.setGeometry(100, 100, 300, 200)
    labelA.move(400, 40)
    windowExample.show()
    #labelA.show()
    sys.exit(app.exec_())

main()