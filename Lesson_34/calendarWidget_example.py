from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel

from PyQt5.QtCore import QDate
import sys


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        cal.setMaximumDate(QDate(2024,2,2))
        self.setWindowTitle("Spinboxes")
        cal.setHorizontalHeaderFormat(3)
        cal.setVerticalHeaderFormat(1)
        cal.setSelectionMode(0)
        self.lbl.move(130, 260)
        self.setGeometry(400, 300, 400, 400)
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
