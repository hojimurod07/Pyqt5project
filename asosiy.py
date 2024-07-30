

from PyQt5.QtWidgets import *
from login import  LogiPage

class Asosiy(QMainWindow):
    def __init__(self):
        super().__init__()
        self.oynalar = []
        self.setWindowTitle("Asosiy oyna")
        self.setMinimumSize(200,200)
        self.vertical = QVBoxLayout()
        self.btn1 =QPushButton("Royxatdan otish")
        self.btn2 = QPushButton("Royxatni korish")
        self.vertical.addWidget(self.btn1)
        self.vertical.addWidget(self.btn2)
        self.btn1.clicked.connect(self.loginPress)
        w = QWidget()
        w.setLayout(self.vertical)
        self.setCentralWidget(w)

    def loginPress(self):
        l  = LogiPage()
        l.show()
        self.oynalar.append(l)