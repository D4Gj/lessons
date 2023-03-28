from PyQt5 import QtWidgets
import sys


def save_file():
    file = open("fio.txt", "w")
    file.write(f"""{lineEdit1.text()}
{lineEdit2.text()}
{qde.text()}""")
    file.close()


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Домашняя работа 33')
# window.resize(150, 100)
lineEdit1 = QtWidgets.QLineEdit('Имя', window)
lineEdit2 = QtWidgets.QLineEdit('Фамилия', window)
qde = QtWidgets.QDateEdit(window)
button = QtWidgets.QPushButton('Сохранить в файл')
button.clicked.connect(save_file)
hbox = QtWidgets.QVBoxLayout()  # создаём сетку
hbox.addWidget(lineEdit1)
hbox.addWidget(lineEdit2)
hbox.addWidget(qde)
hbox.addWidget(button)
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())
