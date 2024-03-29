from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox
import sys

class Ui_HareetTashfer(object):
    def setupUi(self, HareetTashfer):
        HareetTashfer.setObjectName("HareetTashfer")
        HareetTashfer.setEnabled(True)
        HareetTashfer.resize(488, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\HareetTashferLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HareetTashfer.setWindowIcon(icon)
        HareetTashfer.setLayoutDirection(QtCore.Qt.RightToLeft)
        HareetTashfer.setAutoFillBackground(True)
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
        self.T_29 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_29.setGeometry(QtCore.QRect(20, 280, 211, 171))
        self.T_29.setObjectName("T_29")
        self.T_30 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_30.setGeometry(QtCore.QRect(250, 280, 211, 171))
        self.T_30.setObjectName("T_30")
        self.L_7 = QtWidgets.QLabel(self.centralwidget)
        self.L_7.setGeometry(QtCore.QRect(30, 10, 51, 20))
        self.L_7.setObjectName("L_7")
        self.L_6 = QtWidgets.QLabel(self.centralwidget)
        self.L_6.setGeometry(QtCore.QRect(90, 10, 51, 20))
        self.L_6.setObjectName("L_6")
        self.L_4 = QtWidgets.QLabel(self.centralwidget)
        self.L_4.setGeometry(QtCore.QRect(210, 10, 51, 20))
        self.L_4.setObjectName("L_4")
        self.L_5 = QtWidgets.QLabel(self.centralwidget)
        self.L_5.setGeometry(QtCore.QRect(150, 10, 51, 20))
        self.L_5.setObjectName("L_5")
        self.L_1 = QtWidgets.QLabel(self.centralwidget)
        self.L_1.setGeometry(QtCore.QRect(390, 10, 51, 20))
        self.L_1.setObjectName("L_1")
        self.L_3 = QtWidgets.QLabel(self.centralwidget)
        self.L_3.setGeometry(QtCore.QRect(270, 10, 51, 20))
        self.L_3.setObjectName("L_3")
        self.L_2 = QtWidgets.QLabel(self.centralwidget)
        self.L_2.setGeometry(QtCore.QRect(330, 10, 51, 20))
        self.L_2.setObjectName("L_2")
        self.T_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_6.setGeometry(QtCore.QRect(100, 30, 41, 31))
        self.T_6.setObjectName("T_6")
        self.T_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_5.setGeometry(QtCore.QRect(160, 30, 41, 31))
        self.T_5.setObjectName("T_5")
        self.T_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_4.setGeometry(QtCore.QRect(220, 30, 41, 31))
        self.T_4.setObjectName("T_4")
        self.T_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_3.setGeometry(QtCore.QRect(280, 30, 41, 31))
        self.T_3.setObjectName("T_3")
        self.T_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_2.setGeometry(QtCore.QRect(340, 30, 41, 31))
        self.T_2.setObjectName("T_2")
        self.T_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_1.setGeometry(QtCore.QRect(400, 30, 41, 31))
        self.T_1.setObjectName("T_1")
        self.L_8 = QtWidgets.QLabel(self.centralwidget)
        self.L_8.setGeometry(QtCore.QRect(390, 60, 51, 20))
        self.L_8.setObjectName("L_8")
        self.T_14 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_14.setGeometry(QtCore.QRect(40, 80, 41, 31))
        self.T_14.setObjectName("T_14")
        self.T_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_11.setGeometry(QtCore.QRect(220, 80, 41, 31))
        self.T_11.setObjectName("T_11")
        self.T_10 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_10.setGeometry(QtCore.QRect(280, 80, 41, 31))
        self.T_10.setObjectName("T_10")
        self.L_11 = QtWidgets.QLabel(self.centralwidget)
        self.L_11.setGeometry(QtCore.QRect(210, 60, 51, 20))
        self.L_11.setObjectName("L_11")
        self.L_13 = QtWidgets.QLabel(self.centralwidget)
        self.L_13.setGeometry(QtCore.QRect(80, 60, 61, 20))
        self.L_13.setObjectName("L_13")
        self.L_12 = QtWidgets.QLabel(self.centralwidget)
        self.L_12.setGeometry(QtCore.QRect(140, 60, 61, 20))
        self.L_12.setObjectName("L_12")
        self.L_10 = QtWidgets.QLabel(self.centralwidget)
        self.L_10.setGeometry(QtCore.QRect(270, 60, 51, 20))
        self.L_10.setObjectName("L_10")
        self.L_9 = QtWidgets.QLabel(self.centralwidget)
        self.L_9.setGeometry(QtCore.QRect(330, 60, 51, 20))
        self.L_9.setObjectName("L_9")
        self.T_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_8.setGeometry(QtCore.QRect(400, 80, 41, 31))
        self.T_8.setObjectName("T_8")
        self.T_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_12.setGeometry(QtCore.QRect(160, 80, 41, 31))
        self.T_12.setObjectName("T_12")
        self.L_14 = QtWidgets.QLabel(self.centralwidget)
        self.L_14.setGeometry(QtCore.QRect(20, 60, 61, 20))
        self.L_14.setObjectName("L_14")
        self.T_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_9.setGeometry(QtCore.QRect(340, 80, 41, 31))
        self.T_9.setObjectName("T_9")
        self.T_13 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_13.setGeometry(QtCore.QRect(100, 80, 41, 31))
        self.T_13.setObjectName("T_13")
        self.T_18 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_18.setGeometry(QtCore.QRect(220, 130, 41, 31))
        self.T_18.setObjectName("T_18")
        self.T_15 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_15.setGeometry(QtCore.QRect(400, 130, 41, 31))
        self.T_15.setObjectName("T_15")
        self.T_19 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_19.setGeometry(QtCore.QRect(160, 130, 41, 31))
        self.T_19.setObjectName("T_19")
        self.T_21 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_21.setGeometry(QtCore.QRect(40, 130, 41, 31))
        self.T_21.setObjectName("T_21")
        self.L_19 = QtWidgets.QLabel(self.centralwidget)
        self.L_19.setGeometry(QtCore.QRect(150, 110, 51, 20))
        self.L_19.setObjectName("L_19")
        self.T_16 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_16.setGeometry(QtCore.QRect(340, 130, 41, 31))
        self.T_16.setObjectName("T_16")
        self.L_15 = QtWidgets.QLabel(self.centralwidget)
        self.L_15.setGeometry(QtCore.QRect(380, 110, 61, 20))
        self.L_15.setObjectName("L_15")
        self.L_18 = QtWidgets.QLabel(self.centralwidget)
        self.L_18.setGeometry(QtCore.QRect(210, 110, 51, 20))
        self.L_18.setObjectName("L_18")
        self.T_17 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_17.setGeometry(QtCore.QRect(280, 130, 41, 31))
        self.T_17.setObjectName("T_17")
        self.L_20 = QtWidgets.QLabel(self.centralwidget)
        self.L_20.setGeometry(QtCore.QRect(90, 110, 51, 20))
        self.L_20.setObjectName("L_20")
        self.L_21 = QtWidgets.QLabel(self.centralwidget)
        self.L_21.setGeometry(QtCore.QRect(30, 110, 51, 20))
        self.L_21.setObjectName("L_21")
        self.T_20 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_20.setGeometry(QtCore.QRect(100, 130, 41, 31))
        self.T_20.setObjectName("T_20")
        self.L_17 = QtWidgets.QLabel(self.centralwidget)
        self.L_17.setGeometry(QtCore.QRect(270, 110, 51, 20))
        self.L_17.setObjectName("L_17")
        self.L_16 = QtWidgets.QLabel(self.centralwidget)
        self.L_16.setGeometry(QtCore.QRect(330, 110, 51, 20))
        self.L_16.setObjectName("L_16")
        self.T_24 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_24.setGeometry(QtCore.QRect(280, 180, 41, 31))
        self.T_24.setObjectName("T_24")
        self.L_28 = QtWidgets.QLabel(self.centralwidget)
        self.L_28.setGeometry(QtCore.QRect(30, 160, 51, 20))
        self.L_28.setObjectName("L_28")
        self.L_27 = QtWidgets.QLabel(self.centralwidget)
        self.L_27.setGeometry(QtCore.QRect(90, 160, 51, 20))
        self.L_27.setObjectName("L_27")
        self.T_26 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_26.setGeometry(QtCore.QRect(160, 180, 41, 31))
        self.T_26.setObjectName("T_26")
        self.T_25 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_25.setGeometry(QtCore.QRect(220, 180, 41, 31))
        self.T_25.setObjectName("T_25")
        self.T_28 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_28.setGeometry(QtCore.QRect(40, 180, 41, 31))
        self.T_28.setObjectName("T_28")
        self.L_25 = QtWidgets.QLabel(self.centralwidget)
        self.L_25.setGeometry(QtCore.QRect(210, 160, 51, 20))
        self.L_25.setObjectName("L_25")
        self.T_27 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_27.setGeometry(QtCore.QRect(100, 180, 41, 31))
        self.T_27.setObjectName("T_27")
        self.L_26 = QtWidgets.QLabel(self.centralwidget)
        self.L_26.setGeometry(QtCore.QRect(150, 160, 51, 20))
        self.L_26.setObjectName("L_26")
        self.T_22 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_22.setGeometry(QtCore.QRect(400, 180, 41, 31))
        self.T_22.setObjectName("T_22")
        self.T_23 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_23.setGeometry(QtCore.QRect(340, 180, 41, 31))
        self.T_23.setObjectName("T_23")
        self.L_24 = QtWidgets.QLabel(self.centralwidget)
        self.L_24.setGeometry(QtCore.QRect(270, 160, 51, 20))
        self.L_24.setObjectName("L_24")
        self.L_22 = QtWidgets.QLabel(self.centralwidget)
        self.L_22.setGeometry(QtCore.QRect(390, 160, 51, 20))
        self.L_22.setObjectName("L_22")
        self.L_23 = QtWidgets.QLabel(self.centralwidget)
        self.L_23.setGeometry(QtCore.QRect(330, 160, 51, 20))
        self.L_23.setObjectName("L_23")
        self.T_0 = QtWidgets.QTextEdit(self.centralwidget)
        self.T_0.setGeometry(QtCore.QRect(220, 230, 41, 31))
        self.T_0.setObjectName("T_0")
        self.L_0 = QtWidgets.QLabel(self.centralwidget)
        self.L_0.setGeometry(QtCore.QRect(210, 210, 51, 20))
        self.L_0.setObjectName("L_0")
        self.LT_1 = QtWidgets.QLabel(self.centralwidget)
        self.LT_1.setGeometry(QtCore.QRect(390, 259, 61, 21))
        self.LT_1.setObjectName("LT_1")
        self.LT_2 = QtWidgets.QLabel(self.centralwidget)
        self.LT_2.setGeometry(QtCore.QRect(160, 260, 61, 21))
        self.LT_2.setObjectName("LT_2")
        HareetTashfer.setCentralWidget(self.centralwidget)

        self.retranslateUi(HareetTashfer)
        QtCore.QMetaObject.connectSlotsByName(HareetTashfer)

    def retranslateUi(self, HareetTashfer):
        _translate = QtCore.QCoreApplication.translate
        HareetTashfer.setWindowTitle(_translate("HareetTashfer", "حريت تشفير - أداه لتحويل العربي الي شفرة"))
        self.Copy.setText(_translate("HareetTashfer", "انسخ"))
        self.Convert.setText(_translate("HareetTashfer", "حول"))
        self.L_7.setText(_translate("HareetTashfer", "تشفير \"خ\""))
        self.L_6.setText(_translate("HareetTashfer", "تشفير \"ح\""))
        self.L_4.setText(_translate("HareetTashfer", "تشفير \"ث\""))
        self.L_5.setText(_translate("HareetTashfer", "تشفير \"ج\""))
        self.L_1.setText(_translate("HareetTashfer", "تشفير \"ا\""))
        self.L_3.setText(_translate("HareetTashfer", "تشفير \"ت\""))
        self.L_2.setText(_translate("HareetTashfer", "تشفير \"ب\""))
        self.L_8.setText(_translate("HareetTashfer", "تشفير \"د\""))
        self.L_11.setText(_translate("HareetTashfer", "تشفير \"ز\""))
        self.L_13.setText(_translate("HareetTashfer", "تشفير \"ش\""))
        self.L_12.setText(_translate("HareetTashfer", "تشفير \"س\""))
        self.L_10.setText(_translate("HareetTashfer", "تشفير \"ر\""))
        self.L_9.setText(_translate("HareetTashfer", "تشفير \"ذ\""))
        self.L_14.setText(_translate("HareetTashfer", "تشفير \"ص\""))
        self.L_19.setText(_translate("HareetTashfer", "تشفير \"غ\""))
        self.L_15.setText(_translate("HareetTashfer", "تشفير \"ض\""))
        self.L_18.setText(_translate("HareetTashfer", "تشفير \"ع\""))
        self.L_20.setText(_translate("HareetTashfer", "تشفير \"ف\""))
        self.L_21.setText(_translate("HareetTashfer", "تشفير \"ق\""))
        self.L_17.setText(_translate("HareetTashfer", "تشفير \"ظ\""))
        self.L_16.setText(_translate("HareetTashfer", "تشفير \"ط\""))
        self.L_28.setText(_translate("HareetTashfer", "تشفير \"ي\""))
        self.L_27.setText(_translate("HareetTashfer", "تشفير \"و\""))
        self.L_25.setText(_translate("HareetTashfer", "تشفير \"ن\""))
        self.L_26.setText(_translate("HareetTashfer", "تشفير \"ه\""))
        self.L_24.setText(_translate("HareetTashfer", "تشفير \"م\""))
        self.L_22.setText(_translate("HareetTashfer", "تشفير \"ك\""))
        self.L_23.setText(_translate("HareetTashfer", "تشفير \"ل\""))
        self.L_0.setText(_translate("HareetTashfer", "تشفير \" \""))
        self.LT_1.setText(_translate("HareetTashfer", "ادخل العربي"))
        self.LT_2.setText(_translate("HareetTashfer", "بعد التحويل"))

class HareetTashferApp(QtWidgets.QMainWindow, Ui_HareetTashfer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set the window to be fixed size
        self.setFixedSize(self.size())
        
        # Connect the convertArabicToCode method to the clicked signal of the Convert button
        self.Convert.clicked.connect(self.convertArabicToCode)

        # Connect the Copy button to the copy method
        self.Copy.clicked.connect(self.copyToClipboard)

        self.Copy.setStyleSheet("background-color: #4CAF50; color: white;")
        self.Convert.setStyleSheet("background-color: #008CBA; color: white;")

    def arabic_to_code(self, text, key):
        # Convert the Arabic text to code
        code_sequence = [f'({key[char]})' if char in key else ' ' for char in text]

        return code_sequence

    def convertArabicToCode(self):
        # Replace this with your actual conversion logic
        arabic_text = self.T_30.toPlainText()

        non_convertible_chars = 'ءؤئآإ،'
        non_convertible_found = [char for char in arabic_text if char in non_convertible_chars]

        if non_convertible_found:
            # Display a warning message
            message = f"الحروف الي انت مستخدمها دي مش هتتحول: {', '.join(non_convertible_found)}"
            QMessageBox.warning(self, "Warning", message)

        # Get the user-inputted keys for each Arabic character
        key_mapping = {
            'ا': self.T_1.toPlainText(),
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = HareetTashferApp()
    main_app.show()
    sys.exit(app.exec_())
