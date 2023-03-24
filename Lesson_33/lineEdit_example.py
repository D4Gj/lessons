import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QCompleter)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)
        # qle.setText()
        # qle.displayText()
        # qle.clear()
        # qle.backspace()
        # qle.setSelection()
        # qle.setEchoMode(0)
        # qle.setEchoMode(1)
        # qle.setEchoMode(2)
        # qle.setEchoMode(3)
        completer = QCompleter(['rock', 'sun', 'привет'], parent=self)
        qle.setCompleter(completer)
        # qle.setReadOnly(True)
        # qle.setAlignment()
        # qle.setMaxLength(10)
        # qle.setDragEnabled(True)
        # qle.setCursorPosition(5)
        # qle.home()
        # qle.end()
        # qle.undo()
        # qle.redo()
        # qle.createStandardContextMenu()

        qle.setPlaceholderText('Type something')
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
