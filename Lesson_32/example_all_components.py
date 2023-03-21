from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog, QDialogButtonBox,
                             QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox,
                             QTextEdit, QVBoxLayout)


class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()
        self.createMenu()
        self.createHorizontalGroupBox()
        self.createGridGroupBox()
        self.createFormGroupBox()

        bigeditor = QTextEdit()
        bigeditor.setPlainText('Оно занимает всё пространство в '
                               'макете верхнего уровня')
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(bigeditor)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle('Basic Layouts')

    def createMenu(self):
        self.menuBar = QMenuBar()
        self.fileMenu = QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction('E&xit')
        self.menuBar.addMenu(self.fileMenu)

        self.exitAction.triggered.connect(self.accept)

    def createHorizontalGroupBox(self):
        self.horizontalGroupBox = QGroupBox('Horizontal layout')
        layout = QHBoxLayout()

        for i in range(Dialog.NumButtons):
            button = QPushButton("Button %d" % (i + 1))
            layout.addWidget(button)
        self.horizontalGroupBox.setLayout(layout)

    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("Grid layout")
        layout = QGridLayout()

        for i in range(Dialog.NumGridRows):
            label = QLabel(f'Line {i + 1}')
            lineEdit = QLineEdit()
            layout.addWidget(label, i + 1, 0)
            layout.addWidget(lineEdit, i + 1, 1)

        self.smallEditor = QTextEdit()
        self.smallEditor.setPlainText('Виджет 2/3 занимает макета сетки  \n'
                                      'Смотреть соотношение setColumnStretch ')
        layout.addWidget(self.smallEditor, 0, 2, 5, 2)
        # layout.setColumnStretch(0,1) # labe
        layout.setColumnStretch(1, 10)  # lineEdit
        layout.setColumnStretch(2, 20)  # smallEditor
        self.gridGroupBox.setLayout(layout)

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel('Line1:'), QLineEdit())
        layout.addRow(QLabel('Line2, длинный текст:'), QComboBox())
        layout.addRow(QLabel('Line3:'), QSpinBox())
        self.formGroupBox.setLayout(layout)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())
