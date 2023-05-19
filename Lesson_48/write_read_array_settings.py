from PyQt5 import QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
settings = QtCore.QSettings(QtCore.QSettings.Format.IniFormat, QtCore.QSettings.Scope.SystemScope, 'Настройки',
                            'Тест 2')
languages = ["Python", "Java", "Ruby", "C++"]
print(languages)
print('Сохраняем список')
settings.beginWriteArray("Список")
# (0,"Python")
for i, el in enumerate(languages):
    settings.setArrayIndex(i)
    settings.setValue("Элемент", el)
settings.endArray()
settings.sync()

languages1 = []

lSize = settings.beginReadArray("Список")
# (0,"Python")
for i in range(lSize):
    settings.setArrayIndex(i)
    languages1.append(settings.value("Элемент"))
settings.endArray()
print(languages1)
print(settings.status())
# settings.clear()
print(settings.isWritable())
