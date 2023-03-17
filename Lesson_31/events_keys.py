import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from events_simulate import MyEvent


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
    # def closeEvent(self, e: QtGui.QCloseEvent) -> None:
    #     result = QtWidgets.QMessageBox.question(self, 'Подтверждение закрытия окна',
    #                                             'Вы действительно хотите закрыть окно?',
    #                                             QtWidgets.QMessageBox.StandardButton.Yes |
    #                                             QtWidgets.QMessageBox.StandardButton.No,
    #                                             QtWidgets.QMessageBox.StandardButton.No)
    #     if result == QtWidgets.QMessageBox.StandardButton.Yes:
    #         e.accept()
    #         QtWidgets.QWidget.closeEvent(self, e)
    #     else:
    #         e.ignore()
    # # setFocus([<Причина>])
    # def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
    #     if e.key() == QtCore.Qt.Key.Key_B:
    #         print('Нажата B')
    #     # if e.modifiers() == [QtCore.Qt.Modifier.ALT,
    #     #                      QtCore.Qt.Modifier.SHIFT,
    #     #                      QtCore.Qt.Modifier.CTRL,
    #     #                      QtCore.Qt.Modifier.META,
    #     #                      QtCore.Qt.NoModifier,
    #     #                      QtCore.Qt.KeypadModifier,
    #     #                      QtCore.Qt.GroupSwitchModifier,
    #     #                      ]:
    #     # if e.modifiers() & QtCore.Qt.Modifier.SHIFT:
    #     #     print('Нажата шифт с клавишей:', e.text())
    #     # print(f'Нажата клавиша: {e.text()} {e.modifiers()}')
    #     # if e.isAutoRepeat():
    #     #     print('Зажали',e.text())
    #     if e.matches(QtGui.QKeySequence.Copy):
    #         print('Нажато ctrl+c копия')
    #
    # def keyReleaseEvent(self, e: QtGui.QKeyEvent) -> None:
    #     print(f'Отжата клавиша: {e.text()} {e.key()}')
    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        print(e.type()) # MouseButtonPress
        print('Зажата', e.x(), e.y())

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        print('Отжата', e.x(), e.y())

    def mouseDoubleClickEvent(self, e: QtGui.QMouseEvent) -> None:
        print('Дабл клик', e.x(), e.y())
        QtCore.QCoreApplication.sendEvent(self, MyEvent(f'{e.x(), e.y()}'))
        # MousePress
        # MouseRelease
        # MouseDblClick
        # MousePress
        # MouseRelease

    def customEvent(self, e) -> None:
        if e.type() == MyEvent.idType:
            self.setWindowTitle(f'Получены данные {e.get_data()}')


if __name__ in '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
