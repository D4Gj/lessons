from PyQt5 import QtCore, QtWidgets, QtWinExtras
import sys, time


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.WindowType.Window |
                                                       QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Список быстрого доступа")
        # Создание списка быстрого доступа
        jumpList = QtWinExtras.QWinJumpList(parent=self)
        self.thumbnailToolbar = QtWinExtras.QWinThumbnailToolBar(self)
        jumpList.clear()
        # Получим категорию последних открывавшихся документов
        recent = jumpList.recent()
        # Пункт лицензия Python и добавим в категорию
        item1 = QtWinExtras.QWinJumpListItem(QtWinExtras.QWinJumpListItem.Type.Link)
        item1.setFilePath(r'C:\Program Files (x86)\Notepad++\notepad++.exe')
        item1.setTitle("Лицензия Python")
        item1.setArguments([r'C:\Users\inzad\AppData\Local\Programs\Python\Python39\LICENSE.txt'])
        recent.addItem(item1)
        # Делаем категорию видимой
        recent.setVisible(True)
        # Получаем часто открываемые документы и добавим "Новости Python"
        frequent = jumpList.frequent()
        frequent.addLink("Новости Python", r'C:\Users\inzad\AppData\Local\Programs\Python\Python39\NEWS.txt')
        frequent.setVisible(True)
        # Категория задач в неё пункт блокнот, разделитель и wordpad
        tasks = jumpList.tasks()
        tasks.addLink("Блокнот", r'C:\WINDOWS\system32\notepad.exe')
        tasks.addSeparator()
        tasks.addLink("WordPad", r'C:\Program Files\Windows NT\Accessories\wordpad.exe')
        tasks.setVisible(True)
        # Произвольная категория Инструменты
        otherCat = QtWinExtras.QWinJumpListCategory()
        otherCat.setTitle("Инструменты")
        # пункт Python shell
        otherCat.addLink('Python shell', r'C:\Users\inzad\AppData\Local\Programs\Python\Python39\python.exe')
        otherCat.setVisible(True)
        jumpList.addCategory(otherCat)
        self.resize(200, 50)

    def showEvent(self, a0) -> None:
        self.thumbnailToolbar.setWindow(self.windowHandle())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
