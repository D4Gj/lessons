from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.WindowType.Window |
                                                       QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Печать изображений")
        self.printer = QtPrintSupport.QPrinter()
        self.printer.setPageOrientation(QtGui.QPageLayout.Orientation.Landscape)
        self.file = None
        vbox = QtWidgets.QVBoxLayout()
        btnOpen = QtWidgets.QPushButton("Открыть файл")
        btnOpen.clicked.connect(self.openFile)
        vbox.addWidget(btnOpen)
        btnPageOptions = QtWidgets.QPushButton("Настройка страниц")
        btnPageOptions.clicked.connect(self.showPageOptions)
        vbox.addWidget(btnPageOptions)
        btnPreview = QtWidgets.QPushButton("Предпросмотр")
        btnPreview.clicked.connect(self.preview)
        vbox.addWidget(btnPreview)
        btnPrint = QtWidgets.QPushButton("Напечатать")
        btnPrint.clicked.connect(self.printImage)
        vbox.addWidget(btnPrint)
        self.setLayout(vbox)
        self.resize(200, 100)

    def openFile(self):
        self.file = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption="Выберите графический файл"
                                                          , filter="Графические файлы (*.bmp *.jpg *.png")

    def showPageOptions(self):
        pd = QtPrintSupport.QPageSetupDialog(self.printer, parent=self)
        pd.exec()

    def preview(self):
        pp = QtPrintSupport.QPrintPreviewDialog(self.printer, parent=self)
        pp.paintRequested.connect(self._printImage)
        pp.exec_()

    def printImage(self):
        try:
            pd = QtPrintSupport.QPrintDialog(self.printer, parent=self)
            pd.setOptions(QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintToFile |
                          QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintSelection)
            if pd.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                self._printImage(self.printer)
        except Exception as e:
            print(e)

    def _printImage(self, printer):
        painter = QtGui.QPainter()
        painter.begin(printer)
        pixmap = QtGui.QPixmap(self.file[0])

        pixmap = pixmap.scaled(printer.width(), printer.height(),
                               aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio
                               )
        painter.drawPixmap(0, 0, pixmap)
        painter.end()


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
