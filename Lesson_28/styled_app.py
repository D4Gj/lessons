from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
# На уровне приложения задаём синий цвет текста для надписей, вложенных в
# группы, и курсивное начиртание текста кнопок
app.setStyleSheet("QGroupBox QLabel {color:blue;} QPushButton {font-style: italic;} QPushButton:pressed:hover {"
                  "color:red;background-color:blue;} QLabel {color:black;}")
# app.setStyleSheet("QGroupBox,QGroupBox * {color:blue;}")

window = QtWidgets.QWidget()
window.setWindowTitle('Таблицы стилей')
# На уровне окна зададим зелёный цвет текста для надписи с именем first и
# красный цвет текста для надписи, на которую наведён курсор
window.setStyleSheet("QLabel#first {color:green;} QLabel:hover {color:red;}")
window.resize(200, 200)

lbl1 = QtWidgets.QLabel("Зелёный текст")
lbl1.setObjectName('first')
lbl2 = QtWidgets.QLabel("Полужирным текстом")
lbl2.setStyleSheet("font-weight:bold")
lbl3 = QtWidgets.QLabel('Синий текст')
btn = QtWidgets.QPushButton('Курсивный текст')
box = QtWidgets.QGroupBox()
# Создадим контейнер, поместим в него третью надпись и вставим в группу
bbox = QtWidgets.QVBoxLayout()
bbox.addWidget(lbl3)
box.setLayout(bbox)
# Создадим основной контейнер, поместим в него 2 первые надписи, группу, кнопку и
# вставим в окно
mainbox = QtWidgets.QVBoxLayout()
mainbox.addWidget(lbl1)
mainbox.addWidget(lbl2)
mainbox.addWidget(box)
mainbox.addWidget(btn)
window.setLayout(mainbox)
window.show()
# setAttribute(AA_UseStyleSheetPropagationInWidgetStyles)
# a = QtWidgets.QLineEdit()
# a.text()
sys.exit(app.exec_())
