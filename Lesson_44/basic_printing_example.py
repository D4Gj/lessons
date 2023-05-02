from PyQt5 import QtCore, QtWidgets, QtGui, QtPrintSupport
import sys

app = QtWidgets.QApplication(sys.argv)
# Создаём принтер
printer = QtPrintSupport.QPrinter()
# Для отладки раскомментировать строчку, которая предоставляет вывод в формат PDF
# строчка :
# printer.setOutputFileName("output.pdf")
# Создаем поверхность рисования и привязываем к принтеру
painter = QtGui.QPainter()
painter.begin(printer)
# Рамка вокруг страницы
pen = QtGui.QPen(QtGui.QColor(QtGui.QColorConstants.Blue), 5, style=QtCore.Qt.PenStyle.DotLine)
painter.setPen(pen)
painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
painter.drawRect(0, 0, printer.width(), printer.height())
# Выводим надпись
color = QtGui.QColor(QtGui.QColorConstants.Black)
painter.setPen(QtGui.QPen(color))
painter.setBrush(QtGui.QBrush(color))
font = QtGui.QFont("Verdana", pointSize=42)
painter.setFont(font)
painter.drawText(10, printer.height() // 2 - 100, printer.width() - 20,
                 50, QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.TextFlag.TextDontClip, "QPrinter")
# Изменим ориентацию страницы. Это делается перед newPage()
printer.setPageOrientation(QtGui.QPageLayout.Orientation.Landscape)
# Переходим на новую страницу
printer.newPage()
# Выводим изображение
pixmap = QtGui.QPixmap('logo.png')
pixmap = pixmap.scaled(printer.width(), printer.height(), aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
painter.drawPixmap(0, 0, pixmap)
painter.end()
