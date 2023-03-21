from PyQt5 import QtWidgets, QtCore


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.text1 = QtWidgets.QTextEdit(self)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.text1)
        self.setLayout(vbox)
        self.resize(550, 100)
        self.mf = MyFilter(parent=self)


class MyFilter(QtCore.QObject):
    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)
        self.parent = parent

    def eventFilter(self, obj, e):
        if e.type() == QtCore.QEvent.Type.MouseButtonDblClick:
            print('X=', e.pos().x(), 'Y=', e.pos().y())
            xmouse = e.pos().x()
            ymouse = e.pos().y()
            h = self.parent.text1.geometry().height()
            w = self.parent.text1.geometry().width()
            xtxt = self.parent.text1.geometry().x()
            ytxt = self.parent.text1.geometry().y()
            print(xtxt, ytxt, xtxt + w, ytxt + h)
            if xtxt < xmouse < (xtxt + w) and ytxt < ymouse < (ytxt + h):
                print(self.parent.text1.toPlainText())
            return True

        return QtCore.QObject.eventFilter(self, obj, e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.installEventFilter(window.mf)
    sys.exit(app.exec())
