from PyQt5 import QtCore, QtWidgets
import sys


class MyClass(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        print('method slot on_clicked')

    @QtCore.pyqtSlot(int, name='myslot')
    def on_clicked2(self, status):
        print('method myslot.', status)

obj = MyClass()
app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Нажми')
button.clicked.connect(obj.on_clicked)
button.clicked.connect(obj.myslot)
button.show()
sys.exit(app.exec_())
