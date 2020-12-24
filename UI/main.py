from PyQt5 import QtWidgets
import sys
from UI.form_events import FormEvents

app = QtWidgets.QApplication([])
application = FormEvents()
application.show()
sys.exit(app.exec())