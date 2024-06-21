from PyQt5 import QtWidgets 
import sys

from HareetTashferApp import HareetTashferApp

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = HareetTashferApp()
    main_app.show()
    sys.exit(app.exec_())
