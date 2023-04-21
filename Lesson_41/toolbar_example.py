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
        menu = self.createPopupMenu()
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        print(self.centralWidget())
        print(self.menuWidget())
        self.setMenuWidget(QMenuBar())
        print(self.menuWidget())

        self.setStatusBar(QStatusBar())
        stbar = self.statusBar()
        stbar.showMessage('Приложение работает')

        self.setWindowTitle("Window with MDI")
        # my_tools = QToolBar('123')
        # # my_tools.setObjectName()
        # my_tools.addWidget(QPushButton("123fsad"))
        # my_tools.addWidget(QPushButton("123fsad"))
        # my_tools.addWidget(QPushButton("123fsad"))
        # self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, my_tools)
        # self.addToolBar(Qt.ToolBarArea.RightToolBarArea, my_tools)
        # self.addToolBar(my_tools)
        # self.addToolBar(Qt.NoToolBarArea, my_tools)
        # button_toolbar = self.addToolBar("Кнопки")
        # button_toolbar.addWidget(QPushButton(icon=QIcon('logo.png')))
        # self.addToolBarBreak(Qt.ToolBarArea.RightToolBarArea)
        # self.addToolBar(Qt.ToolBarArea.RightToolBarArea, QToolBar('1233'))
        self._create_actions()

        self._createToolBars()
        self._createMenuBar()

        self.exitAction.triggered.connect(lambda: sys.exit())
        self.aboutAction.triggered.connect(lambda: QDialog())
        self._createContextMenu()
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
        # ContexMenuPolicy
        # print(fileMenu.contextMenuPolicy().ActionsContextMenu)
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

    def _createToolBars(self):
        fileToolBar = self.addToolBar("File")
        editToolBar = QToolBar("Edit", self)
        self.addToolBar(editToolBar)
        helpToolBar = QToolBar("&Help", self)
        self.addToolBar(Qt.ToolBarArea.RightToolBarArea, helpToolBar)
        btn1 = QPushButton('&123')
        helpToolBar.addWidget(btn1)
        btn1.clicked.connect(lambda: print(123))

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

    def _createContextMenu(self):
        self.centralWidget().setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.centralWidget().addAction(self.newAction)
        self.centralWidget().addAction(self.openAction)
        self.centralWidget().addAction(self.saveAction)
        self.centralWidget().addAction(self.copyAction)
        self.centralWidget().addAction(self.pasteAction)
        self.centralWidget().addAction(self.cutAction)
        self.centralWidget().addAction(self.exitAction)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
