

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
        self.submit.clicked.connect(self.submit_bosilganda)






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

    def submit_bosilganda(self):
        if not self.line1.text().strip() or self.combo.currentIndex() == 0 or not self.salary.text().strip():
            QMessageBox.warning(self, "Warning", "Barcha maydonlar to'ldirilgan bo'lishi kerak")
        else:
            QMessageBox.information(self, "Success", "Muvaffaqiyatli qoshildi")
            self.malumot_yozish()
            self.close()

    def malumot_yozish(self):
        id  = 1
        fullname = self.line1.text().lower().capitalize()
        position = self.combo.currentText().lower()
        salary = self.salary.text()
        with open("base.txt", "a") as file:
            file.write(f"{id}.{fullname}, {position},{salary}\n")
        id+=1

