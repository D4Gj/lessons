from PyQt5 import QtWidgets, QtCore
import sys
import time

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()

window.setWindowTitle('123')
window.resize(300, 60)
# window.setWindowFlags(QtCore.Qt.Popup)
# window.setWindowFlags(QtCore.Qt.Tool)
# window.setWindowFlags(QtCore.Qt.ToolTip)
# window.setWindowFlags(QtCore.Qt.SplashScreen)
# window.setWindowFlags(QtCore.Qt.SubWindow)
# window.setWindowFlags(QtCore.Qt.ForeignWindow)
# window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint |
#                       QtCore.Qt.WindowTitleHint)


# Sheet Drawer
window.show()

# time.sleep(5)
# window.setVisible(False)

print(window.isVisible())
window.setFixedSize(QtCore.QSize(100, 500))
# time.sleep(3)
# window.setGeometry(100, 100, 400, 400)
sys.exit(app.exec_())
