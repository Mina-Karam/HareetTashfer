from PyQt5 import QtCore, QtGui, QtWidgets
from HareetTashferApp import HareetTashferApp
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = HareetTashferApp()
    main_app.show()
    sys.exit(app.exec_())
