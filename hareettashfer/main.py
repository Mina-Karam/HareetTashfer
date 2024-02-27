from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import sys

# Load the UI file
Form, Window = uic.loadUiType("ui\hareettashfer.ui")

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    sys.exit(app.exec())