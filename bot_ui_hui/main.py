from PyQt5 import QtWidgets, uic
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = 'model_finded.ui'
    win = uic.loadUi(f'ui/{win}')  # расположение вашего файла .ui

    win.show()
    sys.exit(app.exec())