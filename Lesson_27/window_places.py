from PyQt5 import QtWidgets, QtCore
import sys
import time

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()

window.setWindowTitle('123')
window.resize(300, 60)
print(window.height(), window.width())
print(window.frameSize().width())
print(window.frameSize().height())


rect = window.geometry()
print(rect)
print(window.frameGeometry())
desktop = QtWidgets.QApplication.desktop()
x = (desktop.width() - window.width()) // 2
y = (desktop.height() - window.height()) // 2

window.move(x, y)
window.show()
sys.exit(app.exec_())
