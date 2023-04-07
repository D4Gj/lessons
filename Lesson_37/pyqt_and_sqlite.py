import os
import zipfile
import sqlite3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class AuthWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Вход в систему")
        self.setWindowIcon(QIcon('res/logo.png'))
        vbox = QVBoxLayout()
        self.label = QLabel('Войти')
        self.hint = QLabel('Введите данные для входа')
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.hint.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.button = QPushButton("Войти")
        self.button.clicked.connect(self.auth)
        vbox.addWidget(self.label)
        vbox.addWidget(self.hint)
        vbox.addWidget(self.username)
        vbox.addWidget(self.password)
        vbox.addWidget(self.button)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.show()

    def auth(self):
        try:
            login = self.username.text()
            password = self.password.text()
            if login != '' and password != '':
                conn = sqlite3.connect('myprogram.db')
                cur = conn.cursor()
                cur.execute(f'SELECT * FROM users WHERE login="{login}"')
                value = cur.fetchone()
                if value is None:
                    self.hint.setText("Пользователя не существует")
                else:
                    if value[1] == password:
                        self.hide()
                        window.show()
                    else:
                        self.username.clear()
                        self.password.clear()
                        self.hint.setText("Логин и пароль не верны")
            else:
                self.hint.setText("Заполните поля!")

        except Exception as err:
            print(err)


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Zip система")
        self.setWindowIcon(QIcon('res/logo.png'))
        vbox = QVBoxLayout()
        # Menu
        self.menu = QMenuBar()
        file_menu = self.menuBar().addMenu('&File')
        zip_file_action = QAction(QIcon('res/zip.png'), 'Zip', self)
        zip_file_action.triggered.connect(self.zip_file)
        unzip_file_action = QAction(QIcon('res/unzip.png'), 'Unzip', self)
        unzip_file_action.triggered.connect(self.unzip_file)
        exit_app = QAction('Exit', self)
        exit_app.triggered.connect(self.close)

        file_menu.addActions([zip_file_action, unzip_file_action, exit_app])

        selection_menu = self.menuBar().addMenu('&Selection')

        help_menu = self.menuBar().addMenu("&Help")
        about = QAction('About', self)
        help = QAction('Help', self)
        help_menu.addActions([about, help])
        self.list_widget = QListWidget(self)
        self.list_widget.move(0, 20)
        self.list_widget.resize(600, 380)

        vbox.addWidget(self.menu)
        vbox.addWidget(self.list_widget)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.list_widget.doubleClicked.connect(self.item_clicked)
        self.update_list()

    def update_list(self):
        cur_dir = os.listdir()
        last_dir = '..'
        self.list_widget.insertItem(0, last_dir)
        for i, item in enumerate(cur_dir):
            self.list_widget.insertItem(i + 1, item)

    def item_clicked(self):
        path = os.path.abspath(os.getcwd())
        item = self.list_widget.currentItem()
        if item.text() == '..':
            os.chdir('..')
        elif os.path.isdir(item.text()):
            os.chdir(os.path.join(path, item.text()))
        else:
            os.system(item.text())
        self.list_widget.clear()
        self.update_list()

    def zip_file(self):
        file = self.list_widget.currentItem().text()
        file_name = file.split('.')
        with zipfile.ZipFile(f'{file_name[0]}.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
            zf.write(file)
        self.list_widget.clear()
        self.update_list()

    def unzip_file(self):
        file = self.list_widget.currentItem().text()
        try:
            archive = zipfile.ZipFile(file, 'r')
            archive.extractall('.')
            archive.close()
            print('Готово')
        except:
            print('Error')
        self.list_widget.clear()
        self.update_list()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Explorer")
    auth = AuthWindow()
    window = MainWindow()
    app.exec()
