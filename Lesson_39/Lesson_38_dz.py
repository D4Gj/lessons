from PyQt5 import QtWidgets
import sqlite3


def add_item(item, grade):
    conn = sqlite3.connect('base.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists users (item text, grade text);")
    data = (item, grade)
    cur.execute("INSERT INTO users VALUES (?, ?);", data)
    conn.commit()
    conn.close()


def get_item():
    conn = sqlite3.connect('base.db')
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM users")
        items = cur.fetchall()
        for item in items:
            print(*item)
    except Exception as err:
        print(err)


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Оценки')
        self.resize(300, 300)

        self.vbox = QtWidgets.QVBoxLayout(self)
        self.item = QtWidgets.QLineEdit()
        self.item.setPlaceholderText('Введите предмет')
        self.grade = QtWidgets.QLineEdit()
        self.grade.setPlaceholderText('Введите оценку')

        self.hbox = QtWidgets.QHBoxLayout()
        self.bnt_send = QtWidgets.QPushButton('Записать')
        self.btn_get = QtWidgets.QPushButton('Вывести')
        self.bnt_send.clicked.connect(self.push_item)
        self.btn_get.clicked.connect(self.get_items)
        self.hbox.addWidget(self.bnt_send)
        self.hbox.addWidget(self.btn_get)

        self.vbox.addWidget(self.item)
        self.vbox.addWidget(self.grade)
        self.vbox.addLayout(self.hbox)

    def push_item(self):
        item = self.item.text()
        grade = self.grade.text()
        print(grade, item)
        add_item(item, grade)

    def get_items(self):
        get_item()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    app.exec_()
