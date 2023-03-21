from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Позиционирование таблицей или сеткой')
window.resize(150, 100)
button1 = QtWidgets.QPushButton('&1')
button2 = QtWidgets.QPushButton('&2')
lineEdit = QtWidgets.QLineEdit()
textEdit = QtWidgets.QTextEdit()
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
form = QtWidgets.QFormLayout()
form.addRow("&Навание:",lineEdit)
form.addRow("&Описание:",textEdit)
form.addRow(hbox)
window.setLayout(form)
window.show()
sys.exit(app.exec_())
