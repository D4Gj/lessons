import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(200, 100)

    # def changeEvent(self, e: QtCore.QEvent) -> None:
    #     if e.type() == QtCore.QEvent.Type.WindowStateChange:
    #         if self.isMinimized():
    #             print('Окно свёрнуто')
    #         elif self.isMaximized():
    #             print('Окно развёрнуто')
    #         elif self.isFullScreen():
    #             print('Окно в полноэкранном режиме')
    #         elif self.isActiveWindow():
    #             print('Окно в фокусе ввода')
    #
    #     QtWidgets.QWidget.changeEvent(self, e)

    # def event(self, e):
    #     if e.type() == QtCore.QEvent.Type.KeyPress:
    #         print('Клавиша нажата')
    #         print(f'Koд:{e.key()} {e.text()}')
    #     elif e.type() == QtCore.QEvent.Type.MouseButtonPress:
    #         print(f'Координаты- {e.x()},{e.y()}')
    #     elif e.type() == QtCore.QEvent.Type.Close:
    #         print('Окно закрыто')
    #     return QtWidgets.QWidget.event(self, e)  # Отправляем событие дальше
    # def showEvent(self, e: QtGui.QShowEvent) -> None:
    #     print('Окно отображено')
    #     QtWidgets.QWidget.showEvent(self, e)  # Отправляем событие дальше
    #
    # def hideEvent(self, e: QtGui.QHideEvent) -> None:
    #     print('Окно скрыто')
    #     QtWidgets.QWidget.hideEvent(self, e) # Отправляем событие дальше
    # def moveEvent(self, e: QtGui.QMoveEvent) -> None:
    #     print(f'x={e.pos().x()} y={e.pos().y()}')
    #     QtWidgets.QWidget.moveEvent(self, e) # Отправляем событие дальше
    #
    # def resizeEvent(self, e: QtGui.QResizeEvent) -> None:
    #     print(f'old_width = {e.oldSize().width()} old_height = {e.oldSize().height()}')
    #     print(f'width = {e.size().width()} height = {e.size().height()}')
    #     QtWidgets.QWidget.resizeEvent(self, e) # Отправляем событие дальше
    def closeEvent(self, e: QtGui.QCloseEvent) -> None:
        result = QtWidgets.QMessageBox.question(self, 'Подтверждение закрытия окна',
                                                'Вы действительно хотите закрыть окно?',
                                                QtWidgets.QMessageBox.StandardButton.Yes |
                                                QtWidgets.QMessageBox.StandardButton.No,
                                                QtWidgets.QMessageBox.StandardButton.No)
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
        else:
            e.ignore()
    # setFocus([<Причина>])


if __name__ in '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
