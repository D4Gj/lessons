from PyQt5 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('QToolBox')
window.resize(200, 100)
toolbox = QtWidgets.QToolBox()
toolbox.addItem(QtWidgets.QLabel("Вкладка 1 - text"), QtGui.QIcon('../Lesson_41/resources/logo.png'), "Вкладка &1")
toolbox.addItem(QtWidgets.QLabel("Вкладка 2 - text"), "Вкладка &2")
toolbox.addItem(QtWidgets.QLabel("Вкладка 3 - text"), "Вкладка &3")
toolbox.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(toolbox)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
