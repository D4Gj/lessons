from PyQt5.QtWidgets import *
import sys


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Python')
        self.setGeometry(100, 100, 500, 400)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        scroll = QScrollBar(self)
        scroll.setGeometry(100, 50, 30, 200)
        label = QLabel('Python', self)
        label.setGeometry(200, 100, 300, 80)
        scroll.valueChanged.connect(lambda : do_action())

        def do_action():
            value = scroll.value()
            label.setText("Current value of scroll: " + str(value))

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
