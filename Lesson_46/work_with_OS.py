from PyQt5 import QtWinExtras

qwjList = QtWinExtras.QWinJumpList()

qwjList.recent()
qwjList.frequent()
qwjList.tasks()
qwjList.addCategory(QtWinExtras.QWinJumpListCategory())
qwjList.addCategory("QtWinExtras.QWinJumpListCategory()", [QtWinExtras.QWinJumpListItem()])
qwjList.categories()
qwjList.identifier()
qwjList.setIdentifier()
qwjCategory = QtWinExtras.QWinJumpListCategory("Заголовок")
qwjCategory.addItem()
qwjCategory.addDestination()
qwjCategory.addLink(executablePath='')
qwjCategory.addSeparator()
qwjCategory.items()
qwjCategory.count()
qwjCategory.clear()
qwjCategory.type()
# print(sep=)
qwjItem = QtWinExtras.QWinJumpListItem()
qwjItem.setIcon()
qwjItem.setTitle()
qwjItem.setType()
qwjItem.setArguments()
qwjItem.arguments()
qwjItem.setWorkingDirectory()
