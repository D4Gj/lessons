from PyQt5 import QtCore

# QtCore.QCoreApplication.setOrganizationName()
# QtCore.QCoreApplication.setApplicationName()

# settings1 = QtCore.QSettings()
# settings2 = QtCore.QSettings('BestCompany', application='123', )

# settings3 = QtCore.QSettings(scope=QtCore.QSettings.Scope.UserScope,
#                              format=QtCore.QSettings.Format.IniFormat)

settings4 = QtCore.QSettings(filename='test.ini', format=QtCore.QSettings.Format.IniFormat)

# settings4.applicationName()
# settings4.organizationName()
# settings4.scope()
# settings4.format()
# settings4.fileName()
# settings4.setValue(<Имя значения>, <Значение>)
# settings4.setValue('Python', '123')
# settings4.setValue('Python2', 13223)
# settings4.sync()
# print(settings4.value('Python', defaultValue=None))
# print(settings4.contains('Python'))
# print(settings4.contains('Python1'))
# # settings4.remove('')
# print(settings4.contains('Python'))
# print(settings4.childKeys())  # dict()
# # settings4.clear()
# settings4.beginWriteArray(<'Ключ'>,<'Размер списка'>)
# settings4.setArrayIndex()
# settings4.endArray()
# settings4.beginReadArray(<'Ключ'>,<'Размер списка'>)
settings4.remove()
