from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Позиционирование таблицей или сеткой')
window.resize(150, 100)
button1 = QtWidgets.QPushButton('1')
button2 = QtWidgets.QPushButton('2')
button3 = QtWidgets.QPushButton('3')
button4 = QtWidgets.QPushButton('4')
grid = QtWidgets.QGridLayout()  # создаём сетку
grid.addWidget(button1, 0, 0)
grid.addWidget(button2, 1, 2)
# grid.addWidget(button3, 1, 0)
# grid.rowStretch(1)
grid.addWidget(button4, 2, 1)
window.setLayout(grid)
window.show()
sys.exit(app.exec_())
