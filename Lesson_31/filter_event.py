from PyQt5 import QtCore, QtWidgets


class MyFilter(QtCore.QObject):
    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, e) -> bool:
        if e.type() == QtCore.QEvent.Type.KeyPress:
            if e.key() == QtCore.Qt.Key.Key_B:
                print('Событие от <B> не дойдёт до компонента')
                return True
        return QtCore.QObject.eventFilter(self, obj, e)


class Window(QtWidgets.QLabel):

    def __init__(self):
        QtWidgets.QLabel.__init__(self, 'Я заголовок')
        self.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.resize(300, 100)

if __name__ in '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    label = Window()
    filter = MyFilter(label)
    label.installEventFilter(MyFilter(label))
    label.show()
    sys.exit(app.exec_())
