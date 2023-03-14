import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, id, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.id = id

    def focusInEvent(self, e: QtGui.QFocusEvent) -> None:
        print(f'Фокус на {self.id}')
        print(f'Причина получения фокуса {e.reason()}')
        QtWidgets.QLineEdit.focusInEvent(self, e)

    def focusOutEvent(self, e: QtGui.QFocusEvent) -> None:
        print(f'Потерян фокус полем {self.id}')
        QtWidgets.QLineEdit.focusInEvent(self, e)


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(200, 100)
        self.button = QtWidgets.QPushButton("Установить фокус на поле 2")
        self.line1 = MyLineEdit(1)
        self.line2 = MyLineEdit(2)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.line2)
        self.setLayout(self.vbox)
        self.button.clicked.connect(self.on_clicked)
        # Порядок обхода с помощью клавиши <Tab>
        QtWidgets.QWidget.setTabOrder(self.line1,self.line2)
        QtWidgets.QWidget.setTabOrder(self.line2,self.button)

    def on_clicked(self):
        self.line2.setFocus()


if __name__ in '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
