from PyQt5 import QtWidgets, QtPrintSupport, QtWinExtras

# QtPrintSupport.QPrinter.setPageSize()
# QtPrintSupport.QPrinter.set()

mydialog = QtPrintSupport.QPrintDialog()
mydialog.setOption(QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintSelection)

mydialog.setOptions(QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintSelection |
                    QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintPageRange)

mydialog.testOption(QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintSelection)
mydialog.options()
mydialog.printer()

pgSetup = QtPrintSupport.QPageSetupDialog()
pgSetup.printer()

preview = QtPrintSupport.QPrintPreviewDialog()

wintaskbarbutton = QtWinExtras.QWinTaskbarButton()
wintaskbarbutton.setWindow()
progress = wintaskbarbutton.progress()

progress = QtWinExtras.QWinTaskbarProgress()

progress.setRange(0,100)
progress.setValue()
progress.pause()
progress.resume()
progress.reset()
