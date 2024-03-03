from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HareetTashfer(object):
    def convertArabicToCode(self):
        # Replace this with your actual conversion logic
        arabic_text = self.T_30.toPlainText()
        # Perform the conversion and set the result to T_29
        converted_code = self.performConversion(arabic_text)
        self.T_29.setPlainText(converted_code)

    def copyToClipboard(self):
        # Copy the text from T_29 to the clipboard
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.T_29.toPlainText())

    def performConversion(self, arabic_text):
        # Replace this with your actual conversion logic
        # For demonstration, just return the same text
        return arabic_text
