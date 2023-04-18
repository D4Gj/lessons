import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    """Main window"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Python menus &amp; Toolbars")
        self.resize(400, 200)
        self.centralWidget = QLabel("Hello world")
        self.centralWidget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createMenuBar()

    def _createMenuBar(self):
        menuBar = self.menuBar()  # QMenuBar
        fileMenu = QMenu('&File', self)
        menuBar.addMenu(fileMenu)
        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction('Test', lambda: print('Test pressed'))
        # editMenu.setVisible(False)
        # editMenu.setEnabled(False)
        # editMenu.clear()
        menuBar.setDefaultUp(True)
        # menuBar.setVisible(False)
        helpMenu = menuBar.addMenu("&Help")
        # helpMenu.setVisible(True)
        editMenu.triggered.connect(lambda: print(123))
        # self.setMenuBar(menuBar)
        # print(menuBar)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
