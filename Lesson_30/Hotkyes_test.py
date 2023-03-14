import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.id = None

    def event(self, e: QtCore.QEvent) -> bool:
        if e.type() == QtCore.QEvent.Shortcut:
            if self.id == e.shortcutId():
                self.setFocus(QtCore.Qt.FocusReason.ShortcutFocusReason)
                return True
        return QtWidgets.QLineEdit.event(self, e)


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(200, 100)
        self.label = QtWidgets.QLabel("Устано&вить фокус на поле 1")
        self.lineEdit1 = QtWidgets.QLineEdit()
        self.label.setBuddy(self.lineEdit1)
        self.lineEdit2 = MyLineEdit()

        self.lineEdit3 = QtWidgets.QLineEdit()
        self.shc = QtWidgets.QShortcut(QtGui.QKeySequence.mnemonic('&а'), self)
        self.shc.setContext(QtCore.Qt.ShortcutContext.WindowShortcut)
        self.shc.activated.connect(self.lineEdit3.setFocus)

        self.act = QtWidgets.QAction(self)
        self.act.setShortcut(QtGui.QKeySequence('Ctrl+а'))
        self.act.triggered.connect(self.lineEdit1.setFocus)
        self.addAction(self.act)

        self.lineEdit2.id = self.lineEdit2.grabShortcut(QtGui.QKeySequence.mnemonic('&е'))

        self.button = QtWidgets.QPushButton("&Убрать фокус с поля 1")

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.lineEdit1)
        self.vbox.addWidget(self.lineEdit2)
        self.vbox.addWidget(self.lineEdit3)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.lineEdit1.clearFocus()


if __name__ in '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
