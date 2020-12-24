from  PyQt5 import  QtWidgets
from UI.form_description import Ui_Form
from base_classes.format import Format


#pyuic5 window.ui -o form_description.py

class FormEvents(QtWidgets.QDialog, Ui_Form):
    def __init__(self):
        super(FormEvents, self).__init__()
        self.setupUi(self)
        self.archiver = Format()

        self.button_zip.clicked.connect(self.ZipPressed)
        self.button_unzip.clicked.connect(self.UnZipPressed)
        self.pushButton_replace.pressed.connect(self.ReplacePressed)

    def ZipPressed(self):
        method, source, target = \
            self.lineEdit_method.text(), self.textEdit_from.toPlainText(), self.textEdit_to.toPlainText()
        self.archiver.ZipFromTo(source=source, target=target, zip_method=method)

    def UnZipPressed(self):
        self.archiver.UnZipFromTo(self.textEdit_from.toPlainText(), target=self.textEdit_to.toPlainText())

    def ReplacePressed(self):
        source = self.textEdit_from.toPlainText()
        target = self.textEdit_to.toPlainText()

        self.textEdit_from.setText(target)
        self.textEdit_to.setText(source)






