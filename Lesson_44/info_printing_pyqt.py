from PyQt5 import Qt
from PyQt5 import QtGui

a = Qt.QPrinterInfo()
print(a.availablePrinterNames())
# pdfWriter = Qt.QPdfWriter()
my_printer = Qt.QPrinter()
# PrintPreviewDialog - Вывод документа в отдельное диалоговое окно
# PrintPreviewWidget - Используется с другими изученными компонентами внутри интерфейса.
# QPrinterInfo - какие принтеры в наличии, инфа о принтерах
# QPdfWriter
# my_printer.setPrinterName() # подключение к принтеру
# print(my_printer.printerName())  # имя подключенного принтера
# my_printer.setOutputFileName() # путь к файлу
# my_printer.setOutputFormat() # - форматы вывода принтера
# print(my_printer.isValid()) # проверка на валидность принтера
# my_printer.setPageSize(QtGui.QPageSize.A4)
# my_printer.setPageOrientation(QtGui.QPageLayout.Orientation.Portrait)
# my_printer.setPageMargins(10, 10, 10, 10, QtGui.QPageLayout.Unit.Millimeter)
# my_printer.pageLayout()
# my_printer.setCopyCount(10)
# my_printer.setCollateCopies(True)
# my_printer.setDuplex(Qt.QPrinter.DuplexMode.DuplexLongSide)
# my_printer.setPrintRange(Qt.QPrinter.PrintRange.AllPages)
# my_printer.setFromTo() указание страниц на печать
# my_printer.setColorMode(1)
# my_printer.setResolution()
# my_printer.setPaperSource(Qt.QPrinter.PaperSource.Auto)

