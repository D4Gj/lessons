from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys


@QtCore.pyqtSlot
def show():
    print(123)


# pyqtSlot(<Типы данных>, name=None, result=None)

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Закрыть приложение')
button.clicked.connect(app.quit)
button.show()
sys.exit(app.exec_())
