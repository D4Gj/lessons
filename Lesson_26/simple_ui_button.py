from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('PyQt Program')
window.resize(100, 200)
label = QtWidgets.QLabel("<center>Hello world!</center>")
btnQuit = QtWidgets.QPushButton("&Close window")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window.setLayout(vbox)
btnQuit.clicked.connect(app.quit)
window.show()
# print(QtWidgets.qApp.argv())
sys.exit(app.exec_())
