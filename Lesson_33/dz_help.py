from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Позиционирование таблицей или сеткой')
# window.resize(150, 100)
lineEdit1 = QtWidgets.QLineEdit('Имя', window)
lineEdit2 = QtWidgets.QLineEdit('Фамилия', window)
qde = QtWidgets.QDateEdit(window)
hbox = QtWidgets.QVBoxLayout()  # создаём сетку
hbox.addWidget(lineEdit1)
hbox.addWidget(lineEdit2)
hbox.addWidget(qde)
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())
