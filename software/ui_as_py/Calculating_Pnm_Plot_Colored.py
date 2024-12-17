# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculating_Pnm_Plot_Colored.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(872, 796)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 30, 751, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;")
        self.label.setObjectName("label")
        self.Nmax_Push = QtWidgets.QLineEdit(Form)
        self.Nmax_Push.setGeometry(QtCore.QRect(250, 120, 111, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Nmax_Push.setFont(font)
        self.Nmax_Push.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"border-radius: 7px;")
        self.Nmax_Push.setText("")
        self.Nmax_Push.setMaxLength(360)
        self.Nmax_Push.setAlignment(QtCore.Qt.AlignCenter)
        self.Nmax_Push.setObjectName("Nmax_Push")
        self.Degree_Push = QtWidgets.QLineEdit(Form)
        self.Degree_Push.setGeometry(QtCore.QRect(250, 250, 111, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Degree_Push.setFont(font)
        self.Degree_Push.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"border-radius: 7px;")
        self.Degree_Push.setText("")
        self.Degree_Push.setAlignment(QtCore.Qt.AlignCenter)
        self.Degree_Push.setPlaceholderText("")
        self.Degree_Push.setObjectName("Degree_Push")
        self.Calculate = QtWidgets.QPushButton(Form)
        self.Calculate.setGeometry(QtCore.QRect(410, 240, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Calculate.setFont(font)
        self.Calculate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Calculate.setStyleSheet("background-color: rgb(149, 163, 255);\n"
"border-radius: 25px;")
        self.Calculate.setObjectName("Calculate")
        self.Clear = QtWidgets.QPushButton(Form)
        self.Clear.setGeometry(QtCore.QRect(580, 240, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Clear.setFont(font)
        self.Clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Clear.setStyleSheet("background-color: rgb(177, 177, 177);\n"
"border-radius: 25px;")
        self.Clear.setObjectName("Clear")
        self.Nmax_label = QtWidgets.QLabel(Form)
        self.Nmax_label.setGeometry(QtCore.QRect(140, 140, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Nmax_label.setFont(font)
        self.Nmax_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Nmax_label.setObjectName("Nmax_label")
        self.Degree_Label = QtWidgets.QLabel(Form)
        self.Degree_Label.setGeometry(QtCore.QRect(140, 270, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Degree_Label.setFont(font)
        self.Degree_Label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Degree_Label.setObjectName("Degree_Label")
        self.TextBrowser = QtWidgets.QTextBrowser(Form)
        self.TextBrowser.setGeometry(QtCore.QRect(90, 430, 671, 341))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.TextBrowser.setFont(font)
        self.TextBrowser.setStyleSheet("background-color: rgb(90, 90, 90);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.TextBrowser.setObjectName("TextBrowser")
        self.results_label = QtWidgets.QLabel(Form)
        self.results_label.setGeometry(QtCore.QRect(370, 390, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.results_label.setFont(font)
        self.results_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.results_label.setObjectName("results_label")
        self.Plot_Matrix = QtWidgets.QPushButton(Form)
        self.Plot_Matrix.setGeometry(QtCore.QRect(410, 120, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Plot_Matrix.setFont(font)
        self.Plot_Matrix.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Plot_Matrix.setMouseTracking(False)
        self.Plot_Matrix.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(148, 162, 255), stop:1 rgb(243, 245, 255));\n"
"border-radius: 25px;\n"
"")
        self.Plot_Matrix.setObjectName("Plot_Matrix")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(790, 760, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        # Actions
        self.Clear.clicked.connect(self.clear_All)
        self.Calculate.clicked.connect(self.legd)
        self.Plot_Matrix.clicked.connect(self.plot_legd)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculating Pnm"))
        self.label.setText(_translate("Form", "Computing Normalized Associated Legendre Functions"))
        self.Calculate.setText(_translate("Form", "Calculate"))
        self.Clear.setText(_translate("Form", "Clear"))
        self.Nmax_label.setText(_translate("Form", "Mmax"))
        self.Degree_Label.setText(_translate("Form", "Angle"))
        self.TextBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.results_label.setText(_translate("Form", "Results"))
        self.Plot_Matrix.setText(_translate("Form", "Plot Matrix"))
        self.label_2.setText(_translate("Form", "Doğu İlmak"))

    def clear_All(self):
        self.Nmax_Push.clear()
        self.Degree_Push.clear()
        self.TextBrowser.clear()

    def plot_legd(self, nmax=None, x=None):

        nmax = self.Nmax_Push.text()
        nmax = int(nmax)

        x = self.Degree_Push.text()
        x = float(x)

        import numpy as np
        import math as m
        import matplotlib.pyplot as plt
        import seaborn as sns

        nmx = nmax + 1
        t = x * m.pi / 180
        p = np.zeros((nmx, nmx))
        p[0, 0] = 1
        p[1, 1] = m.sqrt(3) * m.sin(t)

        if nmx >= 2:
            for f in range(3, nmx + 1):
                p[f - 1, f - 1] = m.sqrt((2 * (f - 1) + 1) / (2 * (f - 1))) * m.sin(t) * p[f - 2, f - 2]

        for k in range(0, nmx):
            if k == 1:
                p[k, k - 1] = m.sqrt(3) * m.cos(t)

            elif k == 2:
                p[k, k - 1] = m.sqrt(5) * m.cos(t) * p[k - 1, k - 1]

            else:
                p[k, k - 1] = m.sqrt(2 * k + 1) * m.cos(t) * p[k - 1, k - 1]
                p[0, nmax] = 0

            for g in range((k + 1), nmx):
                p[g, k] = m.sqrt(((2 * g - 1) * (2 * g + 1)) / ((g - k) * (g + k))) * p[g - 1, k] * m.cos(t) - m.sqrt(
                    ((2 * g + 1) * (g + k - 1) * (g - k - 1)) / ((g - k) * (g + k) * (2 * g - 3))) * p[g - 2, k]

        # self.TextBrowser.setText(f"Pnm Matrix:\n {p}")
        sns.set_style("whitegrid")
        plt.figure(figsize=(16, 8))
        plt.title("Computing Normalized Associated Legendre Functions", fontsize=16)
        plt.xlabel("Number of n")
        plt.plot(p)
        plt.show()

    def legd(self, nmax=None, x=None):

        nmax = self.Nmax_Push.text()
        nmax = int(nmax)

        x = self.Degree_Push.text()
        x = float(x)

        import numpy as np
        import math as m
        import matplotlib.pyplot as plt
        import seaborn as sns
        import pandas as pd

        nmx = nmax + 1
        t = x * m.pi / 180
        p = np.zeros((nmx, nmx))
        p[0, 0] = 1
        p[1, 1] = m.sqrt(3) * m.sin(t)

        if nmx >= 2:
            for f in range(3, nmx + 1):
                p[f - 1, f - 1] = m.sqrt((2 * (f - 1) + 1) / (2 * (f - 1))) * m.sin(t) * p[f - 2, f - 2]

        for k in range(0, nmx):
            if k == 1:
                p[k, k - 1] = m.sqrt(3) * m.cos(t)

            elif k == 2:
                p[k, k - 1] = m.sqrt(5) * m.cos(t) * p[k - 1, k - 1]

            else:
                p[k, k - 1] = m.sqrt(2 * k + 1) * m.cos(t) * p[k - 1, k - 1]
                p[0, nmax] = 0

            for g in range((k + 1), nmx):
                p[g, k] = m.sqrt(((2 * g - 1) * (2 * g + 1)) / ((g - k) * (g + k))) * p[g - 1, k] * m.cos(t) - m.sqrt(
                    ((2 * g + 1) * (g + k - 1) * (g - k - 1)) / ((g - k) * (g + k) * (2 * g - 3))) * p[g - 2, k]

        df = pd.DataFrame(p, columns=np.arange(0, nmx), index=np.arange(0, nmx))
        df.index.name = 'n'
        df.columns.name = 'm'
        pd.set_option('display.max_rows', None)
        pd.set_option('max_columns', None)
        print("Pnm Matrix:\n")
        print(df)

        self.TextBrowser.setText(f"Pnm Matrix:\n {df}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

