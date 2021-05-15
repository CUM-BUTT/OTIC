from  PyQt5 import  QtWidgets
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QTableWidgetItem

from qt_det.form_description import Ui_Dialog
#import numpy as np

#pyuic5 window.ui -o form_description.py
from qt_det.my_math import det, inv


class Events(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(Events, self).__init__()
        self.setupUi(self)

        self.set_size_Button.clicked.connect(self.SetSizePressed)
        self.get_result_Button_2.clicked.connect(self.GetResultPressed)

    def SetSizePressed(self):
        size = int(self.lineEdit.text())
        self.sourse_matrix.setRowCount(size)
        self.sourse_matrix.setColumnCount(size)


    def GetResultPressed(self):
        size = self.sourse_matrix.rowCount()
        self.reverse_matrix.setRowCount(size)
        self.reverse_matrix.setColumnCount(size)


        matrix = [[float(self.sourse_matrix.item(row, column).text())
                   for column in range(size)]
                  for row in range(size)]

        #inv_matrix = np.linalg.inv(matrix)
        inv_matrix = inv(matrix)

        for i, row in enumerate(inv_matrix):
            for j, item in enumerate(row):
                cell = QTableWidgetItem(str(item)) # 1
                self.reverse_matrix.setItem(i, j, cell)  # 3


        #d = np.linalg.det(matrix)
        d = det(matrix)
        self.lineEdit_2.setText(str(d))







