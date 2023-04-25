from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Позиционирование таблицей или сеткой')
#window.resize(150, 100)
button1 = QtWidgets.QPushButton('1')
button2 = QtWidgets.QPushButton('2')
button3 = QtWidgets.QPushButton('3')
button4 = QtWidgets.QPushButton('4')
button5 = QtWidgets.QPushButton('5')
button6 = QtWidgets.QPushButton('6')
button7 = QtWidgets.QPushButton('7')
button8 = QtWidgets.QPushButton('8')
button9 = QtWidgets.QPushButton('9')
grid = QtWidgets.QGridLayout()  # создаём сетку
grid.addWidget(button1, 0, 0)
grid.addWidget(button2, 0, 1)
grid.addWidget(button3, 0, 2)
grid.addWidget(button4, 1, 0)
grid.addWidget(button5, 1, 1)
grid.addWidget(button6, 1, 2)
grid.addWidget(button7, 2, 0)
grid.addWidget(button8, 2, 1)
grid.addWidget(button9, 2, 2)
window.setLayout(grid)
window.show()
sys.exit(app.exec_())