from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QColor

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget()
window.resize(400, 400)

vbox = QtWidgets.QVBoxLayout()
label = QtWidgets.QLabel("12312")
image = QtGui.QBitmap('logo.png')
print(image.colorCount())
image1 = image.copy(rect=QtCore.QRect(100, 200, 300, 400))
image1.save('logo2.png')
# image.fill(QColor().fromRgbF(0.0, 1.0, 1.0, 0.5))
image = image.scaled(250, 200, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                     transformMode=QtCore.Qt.TransformationMode.SmoothTransformation
                     )
# mask_image = image.createMaskFromColor(QColor().fromRgbF(0.0, 1.0, 1.0, 0.5),mode=)
label.setPixmap(image)
image.swap(image1)
vbox.addWidget(label)
print(image.size())
print(image.isQBitmap())

window.setLayout(vbox)
window.show()
app.exec()
