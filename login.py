

from PyQt5.QtWidgets import *


class LogiPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login page")

        self.katta = QVBoxLayout()

        self.a = QHBoxLayout()
        self.labl1 = QLabel("Full Name")
        self.line1 = QLineEdit()
        self.a.addWidget(self.labl1)
        self.a.addWidget(self.line1)

        # b blok==============
        self.b = QHBoxLayout()
        self.labl2 = QLabel("Position")
        self.combo = QComboBox()
        self.combo.addItem("-----")
        self.combo.addItem("Student")
        self.combo.addItem("Admin")
        self.combo.addItem("Teacher")
        self.b.addWidget(self.labl2)
        self.b.addWidget(self.combo)
        # b blok==============


        self.c = QHBoxLayout()
        self.labl3 = QLabel("Salary")
        self.salary = QLineEdit()
        self.c.addWidget(self.labl3)
        self.c.addWidget(self.salary)

        self.d = QHBoxLayout()
        self.reset = QPushButton("Reset")
        self.submit = QPushButton("Submit")
        self.d.addWidget(self.reset)
        self.d.addWidget(self.submit)

        self.reset.clicked.connect(self.reset_bosilganda)






        self.katta.addLayout(self.a)
        self.katta.addLayout(self.b)
        self.katta.addLayout(self.c)
        self.katta.addLayout(self.d)

        w = QWidget()
        w.setLayout(self.katta)
        self.setCentralWidget(w)

    def reset_bosilganda(self):

        self.combo.setCurrentIndex(0)
        self.line1.setText(" ")
        self.salary.setText(" ")
