from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QLCDNumber, QVBoxLayout

from PyQt5.QtCore import QDate
import sys


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)
        self.lcd_1 = QLCDNumber(self) # 1
        self.lcd_1.setDigitCount(10)
        self.lcd_1.display(123456890)

        self.lcd_2 = QLCDNumber(self)  # 2
        self.lcd_2.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_2.setDigitCount(10)
        self.lcd_2.display(0.123456890)

        self.lcd_3 = QLCDNumber(self)  # 3
        self.lcd_3.setSegmentStyle(QLCDNumber.Filled)
        self.lcd_3.display('Hello')

        self.lcd_4 = QLCDNumber(self)  # 4
        self.lcd_4.setSegmentStyle(QLCDNumber.Outline)
        self.lcd_4.setMode(QLCDNumber.Hex)
        self.lcd_4.display(666)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.lcd_1)
        self.v_layout.addWidget(self.lcd_2)
        self.v_layout.addWidget(self.lcd_3)
        self.v_layout.addWidget(self.lcd_4)
        self.setLayout(self.v_layout)


def main():
    app = QApplication(sys.argv)
    ex = Demo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
