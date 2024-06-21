from PyQt5 import QtWidgets 
import sys

from HareetTashferApp import HareetTashferApp

__author__ = "Mina Karam"
__license__ = "MIT"

def get_version():
    try:
        with open('version.txt', 'r') as f:
            version = f.read().strip()
    except FileNotFoundError:
        version = "unknown"
    return version

__version__ = get_version()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = HareetTashferApp()
    main_app.show()
    sys.exit(app.exec_())
