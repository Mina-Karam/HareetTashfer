from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import webbrowser
import json
from HareetTashferGUI import Ui_HareetTashfer
from predefined_codes import *

class HareetTashferApp(QtWidgets.QMainWindow, Ui_HareetTashfer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set the window to be fixed size
        self.setFixedSize(self.size())

        # Connect the convertArabicToCode method to the clicked signal of the Convert button
        self.convertButton.clicked.connect(self.convertArabicToCode)

        # Connect the Copy button to the copy method
        self.copyButton.clicked.connect(self.copyToClipboard)

        self.copyButton.setStyleSheet("background-color: #4CAF50; color: white;")
        self.convertButton.setStyleSheet("background-color: #008CBA; color: white;")

        # Add buttons for project links
        self.facebookButton.clicked.connect(lambda: self.openUrl("https://www.facebook.com/minakaram.me/"))
        self.linkedinButton.clicked.connect(lambda: self.openUrl("https://www.linkedin.com/in/mina-karam/"))
        self.githubButton.clicked.connect(lambda: self.openUrl("https://github.com/Mina-Karam/"))
        self.repoButton.clicked.connect(lambda: self.openUrl("https://github.com/Mina-Karam/HareetTashfer"))

        self.Open_Code.triggered.connect(self.load_input_from_file)
        self.Save_Code.triggered.connect(self.save_input_to_file)
        self.Clean.triggered.connect(self.clear_text_fields)

        # Connect custom codes
        self.Numbering_Code.triggered.connect(lambda: self.load_code(NUMBERING_CODE))
        self.Opposite_Numbering_Code.triggered.connect(lambda: self.load_code(OPPOSITE_NUMBERING_CODE))
        self.Jesus_Code.triggered.connect(lambda: self.load_code(JESUS_CODE))
        self.Arabic_Morse_Code.triggered.connect(lambda: self.load_code(ARABIC_MORSE_CODE))
        self.XBOX_Code.triggered.connect(lambda: self.load_code(XBOX_CODE))
        self.Semaphore_Squares_Code.triggered.connect(lambda: self.load_code(SEMAPHORE_SQUARES_CODE))
        self.Semaphore_Power_Code.triggered.connect(lambda: self.load_code(SEMAPHORE_POWER_CODE, show_warning=True))
        self.Braille_Code.triggered.connect(lambda: self.load_code(BRAILE_CODE))
        self.Arabic_Char_Code.triggered.connect(lambda: self.load_code(ARABIC_CHAR_CODE))
        self.Number_Addition_Code.triggered.connect(lambda: self.load_code(NUMBER_ADDITION_CODE))
        self.Clock_Code.triggered.connect(lambda: self.load_code(CLOCK_CODE, show_warning=True))
        self.Arabic_English_Code.triggered.connect(lambda: self.load_code(ARABIC_ENGLISH_CODE))
        self.Coordinate_Code.triggered.connect(lambda: self.load_code(COORDINATE_CODE))
        self.Binary_Morse_Code.triggered.connect(lambda: self.load_code(BINARY_MORSE_CODE))

        # Create a mapping dictionary for fields
        self.mapping_fields = {
            'ا': self.T_1, 'آ': self.T_1, 'أ': self.T_1, 'إ': self.T_1,
            'ب': self.T_2, 'ت': self.T_3, 'ث': self.T_4, 'ج': self.T_5,
            'ح': self.T_6, 'خ': self.T_7, 'د': self.T_8, 'ذ': self.T_9,
            'ر': self.T_10, 'ز': self.T_11, 'س': self.T_12, 'ش': self.T_13,
            'ص': self.T_14, 'ض': self.T_15, 'ط': self.T_16, 'ظ': self.T_17,
            'ع': self.T_18, 'غ': self.T_19, 'ف': self.T_20, 'ق': self.T_21,
            'ك': self.T_22, 'ل': self.T_23, 'م': self.T_24, 'ن': self.T_25,
            'ه': self.T_26, 'و': self.T_27, 'ي': self.T_28, 'ى': self.T_28,
            ' ': self.T_33, 'ؤ': self.T_34, 'ء': self.T_31, 'ئ': self.T_0,
            'ة': self.T_32
        }

    def arabic_to_code(self, text, key):
        # Convert the Arabic text to code
        code_sequence = [f'({key[char]})' if char in key else ' ' for char in text]
        return code_sequence

    def convertArabicToCode(self):
        arabic_text = self.T_30.toPlainText()

        non_convertible_chars = '،'
        non_convertible_found = [char for char in arabic_text if char in non_convertible_chars]

        # Define the base key mapping
        base_key_mapping = set(self.mapping_fields.keys())

        # Check for characters not in the base key mapping
        for char in arabic_text:
            if char not in base_key_mapping:
                non_convertible_found.append(char)

        # Check optional characters and add them to non_convertible_found if their text inputs are empty
        optional_chars = {
            'ؤ': self.T_34.toPlainText(),
            'ء': self.T_31.toPlainText(),
            'ئ': self.T_0.toPlainText(),
            'ة': self.T_32.toPlainText(),
        }

        for char, key in optional_chars.items():
            if char in arabic_text and not key:
                non_convertible_found.append(char)

        if non_convertible_found:
            # Display a warning message
            message = f"الحروف التي لن تتحول: {', '.join(non_convertible_found)}"
            QMessageBox.warning(self, "Warning", message)

        # Get the user-inputted keys for each Arabic character
        key_mapping = self.get_key_mapping()

        # Check if any required key mapping is not defined
        missing_mappings = [char for char, key in key_mapping.items() if not key]
        if missing_mappings:
            message = f"الحروف التالية ليس لها تعيين: {', '.join(missing_mappings)}"
            QMessageBox.critical(self, "Error", message)
            return

        # Convert the Arabic text to code using the user-inputted keys
        code_sequence = self.arabic_to_code(arabic_text, key_mapping)

        # Join the code sequence and return
        converted_code = ', '.join(code_sequence)
        self.T_29.setPlainText(converted_code)

    def copyToClipboard(self):
        # Copy the text from T_29 to the clipboard
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.T_29.toPlainText())

    def openUrl(self, url):
        webbrowser.open(url)

    def get_key_mapping(self):
        # Return the key mapping for Arabic characters
        return {char: field.toPlainText() for char, field in self.mapping_fields.items()}

    def save_input_to_file(self):
        # Get the user-inputted keys for each Arabic character
        key_mapping = self.get_key_mapping()

        # Open a file dialog to save the file
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                json.dump(key_mapping, file, ensure_ascii=False, indent=4)
    
    def load_input_from_file(self):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                key_mapping = json.load(file)

            # Update the text fields with the loaded key mapping
            for char, key in key_mapping.items():
                if char in self.mapping_fields:
                    self.mapping_fields[char].setPlainText(key)

    def load_code(self, code_dict, show_warning=False):
        for char, code in code_dict.items():
            if char in self.mapping_fields:
                text_field = self.mapping_fields[char]
                text_field.setPlainText(code)
        
        if show_warning:
            message = f"الشفرة دي هتحتاج تدخل منك من خلال ميكروسوف ورد"
            QMessageBox.warning(self, "تحذير", message)
    
    def clear_text_fields(self):
        for field in self.mapping_fields.values():
            field.setPlainText("")

