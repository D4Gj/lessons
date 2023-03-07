from PyQt5 import QtWidgets, QtCore
import sys
import time

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget(flags=QtCore.Qt.WindowType.Dialog)

window.setWindowTitle('Close program?')
window.resize(300, 60)
button = QtWidgets.QPushButton('Закрыть окно', window)
button.setFixedSize(150, 30)
button.move(70, 20)
button.clicked.connect(window.close)
window.show()
sys.exit(app.exec_())
