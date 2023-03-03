from PyQt5 import QtCore

arr = QtCore.QByteArray(bytes('str', 'cp1251'))
print(type(arr))
# QVariant
n = QtCore.QVariant(10)
print(n)
print(n.value())
print(n.typeName())
data = QtCore.QDate()
time = QtCore.QTime()
datetime = QtCore.QDateTime()
text_stream = QtCore.QTextStream()
url = QtCore.QUrl()
# others = QtCore.Q
# 