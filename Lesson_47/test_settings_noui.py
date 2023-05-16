from PyQt5 import QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

# settings = QtCore.QSettings("Рога и копыта", "Приложение 1")
settings = QtCore.QSettings('test.ini', QtCore.QSettings.IniFormat)
v1 = 123
v2 = "python"
v3 = QtCore.QSize(640, 480)
print(v1, v2, v3, sep='|')
print('Сохраним настройки')
settings.setValue('Enabled', v1)
# settings.setValue(str(v1) + '/Значение 1/Значение2', v1)
settings.setValue('Значение 1', v1)
settings.setValue(v2 + '/Значение 1', v2)
settings.setValue('Значение 3', v3)
settings.beginGroup('Ключ 1')
settings.remove('')
settings.beginGroup('Ключ 2/Вложенный ключ 1')
settings.setValue('Ключ 2', v2)
print(settings.childKeys())
settings.endGroup()
settings.endGroup()
# remove contains childKeys()

settings.sync()
print('Считываем настройки')
lv1 = settings.value('Значение 1')
lv2 = settings.value('Значение 2')
lv3 = settings.value('Значение 3')
print(lv1, lv2, lv3, sep='|')
if settings.contains('Значение 4'):
    print('Значение 4 есть в настройках')
else:
    print('Значение 4 отсутсвует в настройках')
# print('Очистим настройки')
print(settings.contains('Значение 1'))
print(settings.allKeys())
print(settings.childGroups())
print(settings.group())
# settings.
# settings.clear()
