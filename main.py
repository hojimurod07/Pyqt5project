
from  db import *

from PyQt5.QtWidgets import  *

from asosiy import  Asosiy
from  login import  LogiPage


app  = QApplication([])

a = Asosiy()
a.show()
Create_table()

app.exec_()

