from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('calc_form.ui')
window.show()
sys.exit(app.exec_())
