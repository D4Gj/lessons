import sys

from PyQt5 import QtCore, QtWidgets, QtGui, QtPrintSupport


class PrintList:
    def __init__(self):
        self.printer = QtPrintSupport.QPrinter()
        self.headerFont = QtGui.QFont("Arial", pointSize=10, weight=QtGui.QFont.Weight.Bold)
        self.bodyFont = QtGui.QFont("Arial", pointSize=10)
        self.footerFont = QtGui.QFont("Arial", pointSize=9, italic=True)
        self.headerFlags = QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.TextFlag.TextWordWrap
        self.bodyFlags = QtCore.Qt.TextFlag.TextWordWrap
        self.footerFlags = QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.TextFlag.TextWordWrap
        color = QtGui.QColor(QtGui.QColorConstants.Black)
        self.headerPen = QtGui.QPen(color, 2)
        self.bodyPen = QtGui.QPen(color, 1)
        self.margin = 5
        self._resetData()

    def _resetData(self):
        self.headers = None
        self.columnWidths = None
        self.data = None
        self._brush = QtCore.Qt.BrushStyle.NoBrush
        self._currentRowHeight = 0
        self._currentPageHeight = 0
        self._headerRowHeight = 0
        self._footerRowHeight = 0
        self._currentPageNumber = 1
        self._painter = None

    def printData(self):
        self._painter = QtGui.QPainter()
        self._painter.begin(self.printer)
        self._painter.setBrush(self._brush)
        if self._headerRowHeight == 0:
            self._painter.setFont(self.headerFont)
            self._headerRowHeight = self._calculateRowHeight(self.columnWidths, self.headers)
        if self._footerRowHeight == 0:
            self._painter.setFont(self.footerFont)
            self._footerRowHeight = self._calculateRowHeight([self.printer.width()], "Страница")
        for i in range(len(self.data)):
            height = self._calculateRowHeight(self.columnWidths, self.data[i])
            if self._currentPageHeight + height > self.printer.height() - self._footerRowHeight - 2 * self.margin:
                self._printFooterRow()
                self._currentPageHeight = 0
                self._currentPageNumber += 1
                self.printer.newPage()
            if self._currentPageHeight == 0:
                self._painter.setPen(self.bodyPen)
                self._painter.setFont(self.bodyFont)
            self.printRow(self.columnWidths, self.data[i], height, self.bodyFlags)

        self._printFooterRow()
        self._painter.end()
        self._resetData()

    def _calculateRowHeight(self, widths, cellData):
        height = 0
        for i in range(len(widths)):
            r = self._painter.boundingRect(0, 0, widths[i] - 2 * self.margin, 50, QtCore.Qt.TextFlag.TextWordWrap,
                                           str(cellData[i]))
            h = r.height() + 2 * self.margin
            if height < h:
                height = h

        return height

    def printRow(self, widths, cellData, height, flags):
        x = 0
        for i in range(len(widths)):
            self._painter.drawText(x + self.margin, self._currentPageHeight + self.margin, widths[i] - self.margin,
                                   height - 2 * self.margin,
                                   flags, str(cellData[i]))
            self._painter.drawRect(x, self._currentPageHeight, widths[i], height)
            x += widths[i]
        self._currentPageHeight += height

    def _printFooterRow(self):
        self._painter.setFont(self.footerFont)
        self._painter.drawText(self.margin, self.printer.height() - self._footerRowHeight - self.margin,
                               self.printer.width() - 2 * self.margin, self._footerRowHeight - 2 * self.margin,
                               self.footerFlags, "Страница " + str(self._currentPageNumber))


app = QtWidgets.QApplication(sys.argv)
pl = PrintList()
# Если нужен формат PDF
# раскоментировать строку ниже:
pl.printer.setOutputFileName("output.pdf")
data = []
# pl.headerFlags = QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.TextFlag.TextWordWrap
for b in range(1, 101):
    data.append([b, b ** 2, b ** 3])
pl.data = data
pl.columnWidths = [100, 100, 200]
pl.headers = ["Число", "Квадрат", "Куб"]
pl.printData()
