from PyQt5 import uic, QtWidgets
import sys

# loadUi(<ui-file>[,<Экземпляр класса>])
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('MyForm.ui')
window.pushButton.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())
