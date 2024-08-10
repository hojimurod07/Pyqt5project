from db import *
from  PyQt5.QtWidgets import *




class Jadval(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(500,600)
        data = malumotOqish()
        table = QTableWidget()
        table.setRowCount(len(data))
        table.setColumnCount(len(data[0]))
        table.setHorizontalHeaderLabels(["FullName", "Position","Salary"])

        for i,(id, full_name,position,salary) in enumerate(data):
            item_id = QTableWidgetItem(id)


            item_name = QTableWidgetItem(str(full_name))
            item_position = QTableWidgetItem(str(position))
            item_salary = QTableWidgetItem(str(salary))


            table.setItem(i, 0, item_name)
            table.setItem(i, 1, item_position)
            table.setItem(i, 2, item_salary)
        self.setCentralWidget(table)