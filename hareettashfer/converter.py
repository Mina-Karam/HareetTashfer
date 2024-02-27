from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HareetTashfer(object):
    def compareValues(self):
        # Define the expected values associated with each label
        expected_values = {
            "L_0": " ",
            "L_1": "أ",
            "L_2": "ب",
            "L_3": "ت",
            "L_4": "ث",
            "L_5": "ج",
            "L_6": "ح",
            "L_7": "خ",
            "L_8": "د",
            "L_9": "ذ",
            "L_10": "ر",
            "L_11": "ز",
            "L_12": "س",
            "L_13": "ش",
            "L_14": "ص",
            "L_15": "ض",
            "L_16": "ط",
            "L_17": "ظ",
            "L_18": "ع",
            "L_19": "غ",
            "L_20": "ف",
            "L_21": "ق",
            "L_22": "ك",
            "L_23": "ل",
            "L_24": "م",
            "L_25": "ن",
            "L_26": "ه",
            "L_27": "و",
            "L_28": "ي",
        }

        # Iterate through labels and compare their expected values with actual values
        for label_name, expected_value in expected_values.items():
            label = self.centralwidget.findChild(QtWidgets.QLabel, label_name)
            text_edit_name = "T_" + label_name[2:]
            text_edit = self.centralwidget.findChild(QtWidgets.QTextEdit, text_edit_name)

            if label and text_edit:
                actual_value = text_edit.toPlainText()
                if actual_value == expected_value:
                    print(f"{label_name}: Values match!")
                else:
                    print(f"{label_name}: Values do not match!")

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

    def setupUi(self, HareetTashfer):
        HareetTashfer.setObjectName("HareetTashfer")
        HareetTashfer.setEnabled(True)
        HareetTashfer.resize(488, 510)
        HareetTashfer.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(HareetTashfer)
        self.centralwidget.setObjectName("centralwidget")

        self.Copy = QtWidgets.QPushButton(self.centralwidget)
        self.Copy.setGeometry(QtCore.QRect(60, 460, 131, 31))
        self.Copy.setObjectName("Copy")

        self.Convert = QtWidgets.QPushButton(self.centralwidget)
        self.Convert.setGeometry(QtCore.QRect(280, 460, 151, 31))
        self.Convert.setObjectName("Convert")

        self.T_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_7.setGeometry(QtCore.QRect(40, 30, 41, 31))
        self.T_7.setObjectName("T_7")

        # ... (other QTextEdit widgets)

        self.T_29 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_29.setGeometry(QtCore.QRect(20, 280, 211, 171))
        self.T_29.setObjectName("T_29")

        self.T_30 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_30.setGeometry(QtCore.QRect(250, 280, 211, 171))
        self.T_30.setObjectName("T_30")

        # ... (other QLabel widgets)

        self.Convert.clicked.connect(self.convertArabicToCode)
        self.Copy.clicked.connect(self.copyToClipboard)
