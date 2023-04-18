import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


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
        my_tools = QToolBar('123')
        my_tools.setObjectName()
        my_tools.addWidget(QPushButton("123fsad"))
        my_tools.addWidget(QPushButton("123fsad"))
        my_tools.addWidget(QPushButton("123fsad"))
        self.addToolBar(Qt.ToolBarArea.RightToolBarArea, my_tools)
        self.addToolBarBreak(Qt.ToolBarArea.RightToolBarArea)
        self.addToolBar(Qt.ToolBarArea.RightToolBarArea, QToolBar('1233'))
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, QDockWidget('1'), Qt.Orientation.Horizontal)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, QDockWidget('2'), Qt.Orientation.Horizontal)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, QDockWidget('3'), Qt.Orientation.Horizontal)
        self.bar = self.menuBar()
        file = self.bar.addMenu("File")

        file.addAction("New")
        file.addAction("Cascade")
        file.addAction("Tiled")

        file.triggered[QAction].connect(self.windowaction)

    def windowaction(self, q):
        print(q.text())

        if q.text() == 'New':
            # pass
            MainWindow.count += 1
            sub = QMdiSubWindow()
            sub.setWindowTitle(f'Вложенное окно {MainWindow.count}')
            subwidget = QWidget()
            subvbox = QVBoxLayout()
            list_widget = QListWidget()
            cur_dir = os.listdir()
            last_dir = '..'
            list_widget.insertItem(0, last_dir)
            for i, item in enumerate(cur_dir):
                list_widget.insertItem(i + 1, item)
            button = QPushButton(f'Текст кнопки {MainWindow.count}')
            subvbox.addWidget(button)
            subvbox.addWidget(list_widget)
            subwidget.setLayout(subvbox)
            sub.setWidget(subwidget)
            self.mdi.addSubWindow(sub)

            sub.show()

        if q.text() == 'Cascade':
            self.mdi.cascadeSubWindows()

        if q.text() == 'Tiled':
            self.mdi.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
