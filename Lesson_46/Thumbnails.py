from PyQt5 import QtWinExtras

toolbar = QtWinExtras.QWinThumbnailToolBar()
toolbar.setWindow()
toolbar.addButton(QtWinExtras.QWinThumbnailToolButton())
toolbar.setButtons([QtWinExtras.QWinThumbnailToolButton(),
                    QtWinExtras.QWinThumbnailToolButton()])

toolbar.removeButton(QtWinExtras.QWinThumbnailToolButton())
toolbar.clear()
toolbar.buttons()
toolbar.count()
button = QtWinExtras.QWinThumbnailToolButton()
button.setToolTip("пустое")
button.toolTip()
button.setInteractive()
button.isInteractive()
button.setDismissOnClick()
button.setFlat()
button.click()
