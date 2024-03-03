from PyQt5 import QtCore, QtGui, QtWidgets
from hareettashfer_ui import Ui_HareetTashfer

class HareetTashferApp(QtWidgets.QMainWindow, Ui_HareetTashfer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect the convertArabicToCode method to the clicked signal of the Convert button
        self.Convert.clicked.connect(self.convertArabicToCode)

        # Connect the Copy button to the copy method
        self.Copy.clicked.connect(self.copyToClipboard)

    def arabic_to_code(self, text, key):
        # Convert the Arabic text to code
        code_sequence = [f'({key[char]})' if char in key else ' ' for char in text]

        return code_sequence

    def convertArabicToCode(self):
        # Replace this with your actual conversion logic
        arabic_text = self.T_30.toPlainText()

        # Get the user-inputted keys for each Arabic character
        key_mapping = {
            'أ': self.T_1.toPlainText(),
            'ب': self.T_2.toPlainText(),
            'ت': self.T_3.toPlainText(),
            'ث': self.T_4.toPlainText(),
            'ج': self.T_5.toPlainText(),
            'ح': self.T_6.toPlainText(),
            'خ': self.T_7.toPlainText(),
            'د': self.T_8.toPlainText(),
            'ذ': self.T_9.toPlainText(),
            'ر': self.T_10.toPlainText(),
            'ز': self.T_11.toPlainText(),
            'س': self.T_12.toPlainText(),
            'ش': self.T_13.toPlainText(),
            'ص': self.T_14.toPlainText(),
            'ض': self.T_15.toPlainText(),
            'ط': self.T_16.toPlainText(),
            'ظ': self.T_17.toPlainText(),
            'ع': self.T_18.toPlainText(),
            'غ': self.T_19.toPlainText(),
            'ف': self.T_20.toPlainText(),
            'ق': self.T_21.toPlainText(),
            'ك': self.T_22.toPlainText(),
            'ل': self.T_23.toPlainText(),
            'م': self.T_24.toPlainText(),
            'ن': self.T_25.toPlainText(),
            'ه': self.T_26.toPlainText(),
            'و': self.T_27.toPlainText(),
            'ي': self.T_28.toPlainText(),
            ' ': self.T_0.toPlainText(),
        }

        print("Key Mapping:")
        for char, key in key_mapping.items():
            print(f"{char}: {key}")

        # Convert the Arabic text to code using the user-inputted keys
        code_sequence = self.arabic_to_code(arabic_text, key_mapping)

        print("Code Sequence:")
        for code in code_sequence:
            print(code)

        # Join the code sequence and return
        converted_code = ', '.join(code_sequence)
        print(f"Converted Code: {converted_code}")

        self.T_29.setPlainText(converted_code)

    def copyToClipboard(self):
        # Copy the text from T_29 to the clipboard
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.T_29.toPlainText())

        print(f"Copied to Clipboard: {self.T_29.toPlainText()}")
