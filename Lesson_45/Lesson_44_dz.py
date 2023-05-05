from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 350)
        self.setWindowTitle('Печать')
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.textedit = QtWidgets.QTextEdit()
        self.textedit.setReadOnly(True)
        self.hbox = QtWidgets.QHBoxLayout()
        self.btn1 = QtWidgets.QPushButton('Загрузить')
        self.btn2 = QtWidgets.QPushButton('Печать')
        self.hbox.addWidget(self.btn1)
        self.hbox.addWidget(self.btn2)
        self.vbox.addWidget(self.textedit)
        self.vbox.addLayout(self.hbox)

        self.btn1.clicked.connect(self.load_data)
        self.btn2.clicked.connect(self.print_text)

        self.printer = QtPrintSupport.QPrinter()
        self.printer.setPageOrientation(QtGui.QPageLayout.Orientation.Landscape)

    def load_data(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)
        file_dialog.setNameFilter('Текстовый документ, (*.txt)')
        file_dialog.exec()
        file = file_dialog.selectedFiles()[0]
        with open(file, 'r') as file:
            text = file.read()
        self.textedit.setText(text)

    def print_text(self):
        print_dialog = QtPrintSupport.QPrintDialog(self.printer)
        print_dialog.setOption(QtPrintSupport.QPrintDialog.PrintDialogOption.PrintSelection)
        if print_dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            painter = QtGui.QPainter()
            painter.begin(self.printer)
            painter.drawText(100, 300, 200, 50, QtCore.Qt.AlignmentFlag.AlignCenter
                             , self.textedit.toPlainText())
            painter.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    app.exec_()
