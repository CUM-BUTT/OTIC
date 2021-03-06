# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(452, 424)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(2, 45, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 80, 121))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 45, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 45, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 45, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 80, 121))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 45, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 45, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 45, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 80, 121))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 45, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 45, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        Form.setMouseTracking(False)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 45, 58);")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 50, 331, 294))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_method = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_method.setStyleSheet("background-color: rgb(255, 195, 92);")
        self.lineEdit_method.setObjectName("lineEdit_method")
        self.gridLayout.addWidget(self.lineEdit_method, 7, 0, 1, 3)
        self.pushButton_replace = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_replace.setStyleSheet("background-color: rgb(151, 193, 148);")
        self.pushButton_replace.setObjectName("pushButton_replace")
        self.gridLayout.addWidget(self.pushButton_replace, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("color:rgb(168, 255, 130)")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("color:rgb(168, 255, 130)")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 8, 0, 1, 1)
        self.textEdit_from = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_from.setStyleSheet("background-color: rgb(150, 176, 185);\n"
"")
        self.textEdit_from.setObjectName("textEdit_from")
        self.gridLayout.addWidget(self.textEdit_from, 1, 0, 1, 3)
        self.button_unzip = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_unzip.setStyleSheet("background-color: rgb(131, 197, 197);")
        self.button_unzip.setObjectName("button_unzip")
        self.gridLayout.addWidget(self.button_unzip, 5, 0, 1, 1)
        self.textEdit_to = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_to.setStyleSheet("background-color: rgb(150, 176, 185);")
        self.textEdit_to.setObjectName("textEdit_to")
        self.gridLayout.addWidget(self.textEdit_to, 9, 0, 1, 3)
        self.button_zip = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_zip.setStyleSheet("background-color: rgb(131, 197, 197);")
        self.button_zip.setObjectName("button_zip")
        self.gridLayout.addWidget(self.button_zip, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("color:rgb(168, 255, 130)")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_replace.setText(_translate("Form", "replace"))
        self.label.setText(_translate("Form", "from"))
        self.label_2.setText(_translate("Form", "to"))
        self.button_unzip.setText(_translate("Form", "unzip"))
        self.button_zip.setText(_translate("Form", "zip"))
        self.label_3.setText(_translate("Form", "zip method (huffman, add_zero, arithmetical, none)"))
