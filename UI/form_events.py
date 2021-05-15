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

    def GetFromTo(self):
        source, target = self.textEdit_from.toPlainText(), self.textEdit_to.toPlainText()
        source, target = source.split(sep='\n'), target.split(sep='\n')
        return source, target

    def ZipPressed(self):
        method = self.lineEdit_method.text()
        source, target = self.GetFromTo()
        for s, t in zip(source, target):
            self.archiver.Zip(source=s, target=t, zip_method=method)

    def UnZipPressed(self):
        source, target = self.GetFromTo()
        for s, t in zip(source, target):
            self.archiver.UnZip(source=s, target=t)

    def ReplacePressed(self):
        source = self.textEdit_from.toPlainText()
        target = self.textEdit_to.toPlainText()

        self.textEdit_from.setText(target)
        self.textEdit_to.setText(source)





