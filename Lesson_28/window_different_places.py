from PyQt5 import QtWidgets, QtCore
import sys
import time

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()

window.setWindowTitle('123')
window.resize(300, 60)
# window.showMaximized()
window.show()
time.sleep(1)
# window.activateWindow()
# window.showMinimized()
# time.sleep(1)
# window.showFullScreen()
# time.sleep(1)
# window.showMaximized()
# time.sleep(1)
# window.showNormal()
window.setWindowState(QtCore.Qt.WindowNoState)
time.sleep(1)
window.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
window.setWindowState(QtCore.Qt.WindowState.WindowMinimized)
window.setWindowState(QtCore.Qt.WindowState.WindowFullScreen)
window.setWindowState(QtCore.Qt.WindowState.WindowMinimized)
print(window.isMinimized())
sys.exit(app.exec_())
