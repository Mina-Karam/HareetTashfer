import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout

class HareetTashferConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('HareetTashfer - Arabic to Code Converter')

        # Entry widget for user input (Arabic text)
        self.entry_label = QLabel('Enter Arabic Text:')
        self.entry_text = QTextEdit()

        # Button to trigger conversion
        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.convert_text)

        # Text widget to display converted code
        self.code_label = QLabel('Converted Code:')
        self.code_text = QTextEdit()
        self.code_text.setReadOnly(True)

        # Button to copy to clipboard
        self.copy_button = QPushButton('Copy to Clipboard')
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.copy_button.setEnabled(False)

        # Key entries dictionary
        self.key_entries = {}
        self.create_key_entries()

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.entry_label)
        main_layout.addWidget(self.entry_text)
        main_layout.addWidget(self.convert_button)
        main_layout.addWidget(self.code_label)
        main_layout.addWidget(self.code_text)
        main_layout.addWidget(self.copy_button)

        self.setLayout(main_layout)

    def create_key_entries(self):
        characters = [
            'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز',
            'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك',
            'ل', 'م', 'ن', 'ه', 'و', 'ي', ' '
        ]

        for char in characters:
            label = QLabel(f"Enter Key for '{char}':")
            entry_text = QTextEdit()
            self.key_entries[char] = entry_text

    def arabic_to_code(self, text, key):
        # Convert the Arabic text to code
        code_sequence = [key[char] for char in text if char in key]
        return code_sequence

    def convert_text(self):
        arabic_text = self.entry_text.toPlainText()
        key = {char: entry_text.toPlainText() for char, entry_text in self.key_entries.items()}

        code_sequence = self.arabic_to_code(arabic_text, key)
        converted_code = ', '.join([f'({key[char]})' for char in arabic_text if char in key])
        self.code_text.setPlainText(converted_code)

        # Enable the copy button
        self.copy_button.setEnabled(True)

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.code_text.toPlainText())
        self.copy_button.setEnabled(False)  # Disable the button after copying

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hareet_tashfer_converter = HareetTashferConverter()
    hareet_tashfer_converter.show()
    sys.exit(app.exec_())
