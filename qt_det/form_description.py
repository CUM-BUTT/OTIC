# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_det/window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(542, 300)
        #self.sourse_matrix = QtWidgets.QTableView(Dialog)
        self.sourse_matrix = QtWidgets.QTableWidget(Dialog)
        self.sourse_matrix.setGeometry(QtCore.QRect(30, 50, 211, 192))
        self.sourse_matrix.setObjectName("sourse_matrix")
        #self.reverse_matrix = QtWidgets.QTableView(Dialog)
        self.reverse_matrix = QtWidgets.QTableWidget(Dialog)
        self.reverse_matrix.setEnabled(True)
        self.reverse_matrix.setGeometry(QtCore.QRect(290, 50, 211, 192))
        self.reverse_matrix.setObjectName("reverse_matrix")
        self.set_size_Button = QtWidgets.QPushButton(Dialog)
        self.set_size_Button.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.set_size_Button.setObjectName("set_size_Button")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 12, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.get_result_Button_2 = QtWidgets.QPushButton(Dialog)
        self.get_result_Button_2.setGeometry(QtCore.QRect(290, 10, 75, 23))
        self.get_result_Button_2.setObjectName("get_result_Button_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 250, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(370, 250, 81, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.set_size_Button.setText(_translate("Dialog", "set size"))
        self.lineEdit_2.setText(_translate("Dialog", "determinant"))
        self.get_result_Button_2.setText(_translate("Dialog", "get result"))
        self.label.setText(_translate("Dialog", "source matrix"))
        self.label_2.setText(_translate("Dialog", "reverse matrix"))
