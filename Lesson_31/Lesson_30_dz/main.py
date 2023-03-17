import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_MainCalcWindow


class Calculator(QtWidgets.QMainWindow):
    calc_string = ''

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainCalcWindow()
        # self.setStyleSheet(open("style.qss", "r").read())
        self.ui.setup_ui(self)
        self.init_ui()

    def init_ui(self):
        self.ui.btn_one.clicked.connect(lambda: self.btn_clicked(self.calc_string, 1))
        self.act = QtWidgets.QAction(self)
        self.act.setShortcut(QtGui.QKeySequence('1'))
        self.act.triggered.connect(lambda: self.btn_clicked(self.calc_string, 1))
        self.addAction(self.act)

        self.ui.btn_two.clicked.connect(lambda: self.btn_clicked(self.calc_string, 2))
        self.act = QtWidgets.QAction(self)
        self.act.setShortcut(QtGui.QKeySequence('2'))
        self.act.triggered.connect(lambda: self.btn_clicked(self.calc_string, 2))
        self.addAction(self.act)

        self.ui.btn_three.clicked.connect(lambda: self.btn_clicked(self.calc_string, 3))
        self.act = QtWidgets.QAction(self)
        self.act.setShortcut(QtGui.QKeySequence('3'))
        self.act.triggered.connect(lambda: self.btn_clicked(self.calc_string, 3))
        self.addAction(self.act)

        self.ui.btn_four.clicked.connect(lambda: self.btn_clicked(self.calc_string, 4))
        self.ui.btn_five.clicked.connect(lambda: self.btn_clicked(self.calc_string, 5))
        self.ui.btn_six.clicked.connect(lambda: self.btn_clicked(self.calc_string, 6))
        self.ui.btn_seven.clicked.connect(lambda: self.btn_clicked(self.calc_string, 7))
        self.ui.btn_eight.clicked.connect(lambda: self.btn_clicked(self.calc_string, 8))
        self.ui.btn_nine.clicked.connect(lambda: self.btn_clicked(self.calc_string, 9))
        self.ui.btn_zero.clicked.connect(lambda: self.btn_clicked(self.calc_string, 0))

        self.ui.btn_add.clicked.connect(lambda: self.btn_clicked(self.calc_string, '+'))
        self.act = QtWidgets.QAction(self)
        self.act.setShortcut(QtGui.QKeySequence('Ctrl+а'))
        self.act.triggered.connect(lambda: self.btn_clicked(self.calc_string, '+'))
        self.addAction(self.act)

        self.ui.btn_subtract.clicked.connect(lambda: self.btn_clicked(self.calc_string, '-'))
        self.ui.btn_multiply.clicked.connect(lambda: self.btn_clicked(self.calc_string, '*'))
        self.ui.btn_divide.clicked.connect(lambda: self.btn_clicked(self.calc_string, '/'))
        self.ui.btn_clear.clicked.connect(lambda: self.clear())
        self.ui.btn_equals.clicked.connect(lambda: self.calculate(self.calc_string))

    def btn_clicked(self, calc_string, btn):
        self.calc_string += str(btn)
        self.ui.lcd_label.setText(self.calc_string)

    def calculate(self, calc_string):
        try:
            self.calc_string = str(eval(calc_string))
            self.ui.lcd_label.setText(self.calc_string)
        except Exception:
            self.calc_string = 'Err'
            self.ui.lcd_label.setText(self.calc_string)
            self.calc_string = ''

    def clear(self):
        self.calc_string = '0'
        self.ui.lcd_label.setText(self.calc_string)
        self.calc_string = ''


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_app = Calculator()
    my_app.show()
    sys.exit(app.exec_())
