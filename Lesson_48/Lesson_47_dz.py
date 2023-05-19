from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore, QtWinExtras


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 350)
        self.setWindowTitle('Печать')
        self.settings = QtCore.QSettings("Настройки", 'Печать')
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.textedit = QtWidgets.QTextEdit()
        self.textedit.setReadOnly(True)
        self.hbox = QtWidgets.QHBoxLayout()
        self.btn1 = QtWidgets.QPushButton('Загрузить')
        self.btn2 = QtWidgets.QPushButton('Печать')
        self.btn3 = QtWidgets.QPushButton('Предпросмотр печати')
        self.hbox.addWidget(self.btn1)
        self.hbox.addWidget(self.btn2)
        self.hbox.addWidget(self.btn3)
        self.vbox.addWidget(self.textedit)
        self.vbox.addLayout(self.hbox)

        self.btn1.clicked.connect(self.load_data)
        self.btn2.clicked.connect(self.print_text)
        self.btn3.clicked.connect(self.preview)

        self.printer = QtPrintSupport.QPrinter()
        self.printer.setPageOrientation(QtGui.QPageLayout.Orientation.Landscape)
        jumpList = QtWinExtras.QWinJumpList(parent=self)
        self.thumbnailToolbar = QtWinExtras.QWinThumbnailToolBar(self)
        jumpList.clear()
        # Получим категорию последних открывавшихся документов
        self.files = []
        recent = jumpList.recent()
        # Пункт лицензия Python и добавим в категорию
        item1 = QtWinExtras.QWinJumpListItem(QtWinExtras.QWinJumpListItem.Type.Link)
        item1.setFilePath(r'C:\Program Files (x86)\Notepad++\notepad++.exe')
        item1.setTitle("Последний файл")
        item1.setArguments([r'C:\Users\inzad\AppData\Local\Programs\Python\Python39\LICENSE.txt'])
        recent.addItem(item1)

        # Делаем категорию видимой
        recent.setVisible(True)
        # Получаем часто открываемые документы и добавим "Новости Python"
        self.frequent = jumpList.frequent()
        self.frequent.addLink("Новости Python", r'C:\Users\inzad\AppData\Local\Programs\Python\Python39\NEWS.txt')
        self.frequent.setVisible(True)
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
        if self.settings.contains('Данные/Текст'):
            self.textedit.setText(self.settings.value('Данные/Текст'))
        self.resize(200, 50)

    def showEvent(self, a0) -> None:
        self.thumbnailToolbar.setWindow(self.windowHandle())

    def load_data(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)
        file_dialog.setNameFilter('Текстовый документ, (*.txt)')
        file_dialog.exec()
        file = file_dialog.selectedFiles()[0]
        self.frequent.addLink('Последний файл', file)
        with open(file, 'r') as file:
            text = file.read()
        self.textedit.setText(text)

    def print_text(self):
        try:
            pd = QtPrintSupport.QPrintDialog(self.printer, parent=self)
            pd.setOptions(QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintToFile |
                          QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintSelection)
            if pd.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                self._printText(self.printer)
        except Exception as e:
            print(e)

    def _printText(self, printer):
        painter = QtGui.QPainter()
        painter.begin(printer)
        painter.drawText(100, 300, 200, 50, QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.TextFlag.TextDontClip
                         , self.textedit.toPlainText())
        painter.end()

    def preview(self):
        pp = QtPrintSupport.QPrintPreviewDialog(self.printer, parent=self)
        pp.paintRequested.connect(self._printText)
        pp.exec_()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        try:
            self.saveText()
        except Exception as e:
            print(e)

    def saveText(self):
        self.settings.beginGroup('Данные')
        self.settings.setValue('Текст', self.textedit.toPlainText())
        self.settings.endGroup()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    app.exec_()
