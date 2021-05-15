from PyQt5 import QtWidgets
import sys
from UI.form_events import FormEvents

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = FormEvents()
    application.show()
    sys.exit(app.exec())


# test
"""
C:\\Users\\ilya\\Desktop\\1.docx
C:\\Users\\ilya\\Desktop\\1.png

C:\\Users\\ilya\\Desktop\\2.docx
C:\\Users\\ilya\\Desktop\\2.png

C:\\Users\\ilya\\Desktop\\3.docx
C:\\Users\\ilya\\Desktop\\3.png
"""