import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qrc_resources


# ":logo.png"

class MainWindow(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCentralWidget(QTextEdit())

        self.setWindowTitle("Блокнот")
        self._create_actions()
        self._createMenuBar()

        self.exitAction.triggered.connect(lambda: sys.exit())
        newIcon = QIcon(":/sub-icons/lg.png")
        self.saveAction.setIcon(newIcon)

    def _createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu('&File', self)
        menuBar.addMenu(fileMenu)
        fileMenu.setIcon(QIcon(":/icons/open.png"))
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)
        editMenu = menuBar.addMenu('&Edit')
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        findMenu = editMenu.addMenu("Find and Replace")
        findMenu.addAction("Find")
        findMenu.addAction("Replace")
        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

    def _create_actions(self):
        self.newAction = QAction(self)
        self.newAction.setText("New")
        self.openAction = QAction("Open", self)
        self.saveAction = QAction("Save", self)
        self.exitAction = QAction("Exit", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("Cut", self)
        self.helpContentAction = QAction("Help", self)
        self.aboutAction = QAction("About", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
