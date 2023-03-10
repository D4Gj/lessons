# self.button.clicked.connect(lambda: self.on_clicked_button1(5))
# y = 10
# self.button.clicked.connect(lambda x=y: self.on_clicked_button1(x))
# self.button.clicked.connect(MyClass(10))
#
from functools import partial
# self.button.clicked.connect(partial(self.on_clicked_button1,5))
