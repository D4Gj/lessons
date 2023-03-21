from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Относительное позициионирование')
window.resize(300, 120)
label = QtWidgets.QLabel('Текст')
label.setStyleSheet('border: 1px solid black;')
button = QtWidgets.QPushButton('Кнопка')
hbox = QtWidgets.QHBoxLayout()  # Создаём контейнер
hbox.addWidget(label)  # Добавили компоненты
hbox.addWidget(button)
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())
