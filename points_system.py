# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'points_system.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from system_plot import TopLevelWindow
from second_system_chart import TopLevelWindowSystem2
from first_plot import TopLevelWindow3
from second_plot import TopLevelWindow4
from third_plot import TopLevelWindow5
from fourth_plot import TopLevelWindow6
from third_system_chart import TopLevelWindowSystem3
from fifth_plot import TopLevelWindow7

class Ui_points_system(object):
    def __init__(self):
        self.make_test = False

    def chart(self, eq):
        if eq == 'system1':
            self.window2 = TopLevelWindow(self.input_euler.toPlainText(), self.input_runge.toPlainText())
        elif eq == 'system2':
            self.window2 = TopLevelWindowSystem2(self.input_euler.toPlainText(), self.input_runge.toPlainText())
        elif eq == 'first_equation':
            self.window2 = TopLevelWindow3(self.input_euler.toPlainText(), self.input_runge.toPlainText())
        elif eq == 'second_equation':
            self.window2 = TopLevelWindow4(self.input_euler.toPlainText(), self.input_runge.toPlainText())
        elif eq == 'third_equation':
            self.window2 = TopLevelWindow5(self.input_euler.toPlainText(), self.input_runge.toPlainText())
        elif eq == 'fourth_equation':
            self.window2 = TopLevelWindow6(self.input_euler.toPlainText(), self.input_runge.toPlainText())
        elif eq == 'third_system':
            self.window2 = TopLevelWindowSystem3(self.input_euler.toPlainText(), self.input_runge.toPlainText())
        elif eq == 'fifth_equation':
            self.window2 = TopLevelWindow7(self.input_euler.toPlainText(), self.input_runge.toPlainText())
        
        # self.window2.euler_steps = self.input_euler.toPlainText()
        # self.window2.runge_steps = self.input_runge.toPlainText()
        # self.ui = TopLevelWindow()
        # self.ui.setupUi(self.window2)
        self.window2.show()

    def show_test(self):
        self.window3 = QtWidgets.QMainWindow()
        

    def setupUi(self, points_system, eq):
        points_system.setObjectName("points_system")
        points_system.resize(481, 550)
        points_system.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.centralwidget = QtWidgets.QWidget(points_system)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 340, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.pushButton.setObjectName("pushButton")


        # self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton2.setGeometry(QtCore.QRect(30, 420, 421, 71))
        # self.pushButton2.setFont(font)
        # self.pushButton2.setStyleSheet("background-color: rgb(159, 43, 104);")
        # self.pushButton2.setObjectName("pushButton2")



        self.input_euler = QtWidgets.QTextEdit(self.centralwidget)
        self.input_euler.setGeometry(QtCore.QRect(240, 160, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.input_euler.setFont(font)
        self.input_euler.setStyleSheet("background-color: rgb(252, 233, 79);\n"
"")
        self.input_euler.setObjectName("input_euler")

        self.euler_steps = self.input_euler.toPlainText()


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 81))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgb(193, 125, 17);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.input_runge = QtWidgets.QTextEdit(self.centralwidget)
        self.input_runge.setGeometry(QtCore.QRect(240, 240, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.input_runge.setFont(font)
        self.input_runge.setStyleSheet("background-color: rgb(252, 233, 79);\n"
"")
        self.input_runge.setObjectName("input_runge")

        self.runge_steps = self.input_runge.toPlainText()
        self.pushButton.clicked.connect(lambda: self.chart(eq))



        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 240, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        points_system.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(points_system)
        self.statusbar.setObjectName("statusbar")
        points_system.setStatusBar(self.statusbar)

        self.retranslateUi(points_system)
        QtCore.QMetaObject.connectSlotsByName(points_system)



    def print(self):
        print(self.input_euler.toPlainText())
        print(self.input_runge.toPlainText())


    def retranslateUi(self, points_system):
        _translate = QtCore.QCoreApplication.translate
        points_system.setWindowTitle(_translate("points_system", "MainWindow"))
        self.pushButton.setText(_translate("points_system", "CONTINUE"))
        # self.pushButton2.setText(_translate("points_system", "TEST"))
        self.input_euler.setHtml(_translate("points_system", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Chilanka\'; font-size:22pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-weight:400;\">0</span></p></body></html>"))
        self.label.setText(_translate("points_system", "Enter the number of points"))
        self.label_2.setText(_translate("points_system", "Euler\'s method"))
        self.input_runge.setHtml(_translate("points_system", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Chilanka\'; font-size:22pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-weight:400;\">0</span></p></body></html>"))
        self.label_3.setText(_translate("points_system", "Runge-Kutta method"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    points_system = QtWidgets.QMainWindow()
    ui = Ui_points_system()
    ui.setupUi(points_system)
    points_system.show()
    sys.exit(app.exec_())
