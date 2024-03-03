from PyQt5 import QtCore, QtGui, QtWidgets
from hareettashfer_ui import Ui_HareetTashfer
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    HareetTashfer = QtWidgets.QMainWindow()
    ui = Ui_HareetTashfer()
    ui.setupUi(HareetTashfer)
    HareetTashfer.show()
    sys.exit(app.exec_())
