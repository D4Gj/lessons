from PyQt5 import QtWidgets
import sys


def on_clicked():
    print("Кнопка нажата. func on_clicked")


class MyClass():
    def __init__(self, x=0):
        self.x = x

    def __call__(self, *args, **kwargs):
        print('Кнопка нажата. class __call__()')
        print(f'{self.x=}')

    def on_clicked(self):
        print('Кнопка нажата. method on_clicked')


obj = MyClass()
app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Нажмите сюда')
# функция
button.clicked.connect(on_clicked)
# метод класса
button.clicked.connect(obj.on_clicked)
# ссылка на экземпляр класса
button.clicked.connect(MyClass(10))
# анонимная функция
button.clicked.connect(lambda: MyClass(5)())
button.show()
sys.exit(app.exec_())
