from PyQt5 import QtWidgets, QtGui, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('QToolBox')
window.resize(200, 100)
splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
label1 = QtWidgets.QLabel('lb1')
label2 = QtWidgets.QLabel('lb2')
label1.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
label2.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
splitter.addWidget(label1)
splitter.addWidget(label2)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(splitter)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
