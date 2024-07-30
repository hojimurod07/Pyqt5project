

from PyQt5.QtWidgets import *


class Asosiy(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asosiy oyna")
        self.setMinimumSize(200,200)
        self.vertical = QVBoxLayout()
        self.btn1 =QPushButton("Royxatdan otish")
        self.btn2 = QPushButton("Royxatni korish")
        self.vertical.addWidget(self.btn1)
        self.vertical.addWidget(self.btn2)

        w = QWidget()
        w.setLayout(self.vertical)
        self.setCentralWidget(w)

