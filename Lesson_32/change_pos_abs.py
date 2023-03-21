from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Абсолютное позициионирование')
window.resize(300, 120)
label = QtWidgets.QLabel('Текст', window)
button = QtWidgets.QPushButton('Кнопка', window)
label.setGeometry(5, 5, 290, 60)
button.resize(280, 30)
button.move(10, 20)
window.show()
sys.exit(app.exec_())
