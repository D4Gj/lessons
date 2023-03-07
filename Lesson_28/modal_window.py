from PyQt5 import QtCore, QtWidgets, QtGui
import sys


# NoModal - 0
# WindowModal - 1
# ApplicationModal - 2

def show_modal_window():
    global modalWindow
    modalWindow = QtWidgets.QWidget(window1, QtCore.Qt.WindowType.Window)
    modalWindow.setWindowTitle('Modal window')
    modalWindow.resize(200, 50)
    modalWindow.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
    modalWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
    modalWindow.move(window1.geometry().center() - modalWindow.rect().center() - QtCore.QPoint(4, 30))
    modalWindow.show()


app = QtWidgets.QApplication(sys.argv)

window1 = QtWidgets.QWidget()

window1.setWindowTitle('Window1')
window1.resize(300, 60)
button = QtWidgets.QPushButton('Open modal window')
button.clicked.connect(show_modal_window)
# button.setToolTip('<h1>Эта кнопка нажимается</h1>')
# button.setToolTipDuration(-1)
# print(button.toolTip())
# print(button.toolTipDuration())
button.setWhatsThis('<h2>Это большая справка</h2>')
print(button.whatsThis())
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button)
window1.setLayout(vbox)
ico = QtGui.QIcon('logo.png')
window1.setWindowIcon(ico)  # значок окна
app.setWindowIcon(ico)  # значок приложения
window1.show()

window2 = QtWidgets.QWidget()
window2.setWindowTitle('Window2')
window2.resize(600, 100)
window2.show()

sys.exit(app.exec_())

