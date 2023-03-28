from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
from PyQt5.QtGui import QTextDocument, QPdfWriter

import sys
from pprint import pprint


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle('Example QTextEdit')
        self.resize(300, 200)
        self.textEdit = QTextEdit()

        self.btnPress1 = QPushButton('Показать текст')
        self.btnPress2 = QPushButton('Показ Html кода')
        self.btnPress3 = QPushButton('Увеличить шрифт')
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        layout.addWidget(self.btnPress3)

        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.btnPress1_clicked)
        self.btnPress2.clicked.connect(self.btnPress2_clicked)
        self.btnPress3.clicked.connect(self.textEdit.zoomIn)
        self.btnPress3.clicked.connect(self.textEdit.undo)
        self.btnPress3.clicked.connect(self.textEdit.redo)
        self.textEdit.textChanged.connect(lambda: print(123))
        self.textEdit.currentCharFormatChanged.connect(lambda : print(321))
        self.textEdit.cursorPositionChanged.connect(lambda : print(f'Вы перенесли курсор{self.textEdit.cursor().pos()}'))
        self.textEdit.setAcceptRichText(False)
        self.textEdit.ensureCursorVisible()
        self.textEdit.copyAvailable()

    def btnPress1_clicked(self):
        self.textEdit.setPlainText("Здравствуйте Нажмите кнопку")

    def btnPress2_clicked(self):
        self.textEdit.setHtml("<font color='red' size = '6'> "
                              "Здравствуйте, PyQt5! \nНажмите кнопку. </font>")
        pprint(self.textEdit.toHtml())
        print(self.textEdit.toPlainText())
        # QTextDocument.FindBackward
        # QTextDocument.FindCaseSensitively
        self.textEdit.find('PyQt5!', QTextDocument.FindWholeWords)
        pdf = QPdfWriter('doc.pdf')
        self.textEdit.print(pdf)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())
