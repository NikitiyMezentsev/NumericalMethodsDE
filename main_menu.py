# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diff_eq.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from points_system import Ui_points_system
from instruction import Ui_Instruction

class Ui_main_menu(object):
    def points_system(self, eq):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_points_system()
        self.ui.setupUi(self.window2, eq)
        self.window2.show()

    def show_instruction(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui_instr = Ui_Instruction()
        self.ui_instr.setupUi(self.window3)
        self.window3.show()

    def resource_path(self, path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, path)

    def setupUi(self, main_menu):
        main_menu.setObjectName("main_menu")
        main_menu.resize(661, 1005)
        main_menu.setStyleSheet("background-color: rgb(143, 89, 2);")
        self.centralwidget = QtWidgets.QWidget(main_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 671, 111))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(252, 175, 62);\n"
                                 
                                )
        self.label.setObjectName("label")


        self.first_equation = QtWidgets.QPushButton(self.centralwidget)
        self.first_equation.setGeometry(QtCore.QRect(0, 110, 661, 101))
        self.first_equation.setIcon(QtGui.QIcon(self.resource_path('first_equation.jpg')))
        self.first_equation.setIconSize(QtCore.QSize(600,600))
        self.first_equation.setFont(font)
        self.first_equation.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.first_equation.setObjectName("first_equation")
        self.first_equation.clicked.connect(lambda: self.points_system('first_equation'))

        self.second_equation = QtWidgets.QPushButton(self.centralwidget)
        self.second_equation.setGeometry(QtCore.QRect(0, 210, 661, 101))
        self.second_equation.setIcon(QtGui.QIcon(self.resource_path('second_equation.jpg')))
        self.second_equation.setIconSize(QtCore.QSize(600,600))
        self.second_equation.setFont(font)
        self.second_equation.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.second_equation.setObjectName("second_equation")
        self.second_equation.clicked.connect(lambda: self.points_system('second_equation'))

        self.system = QtWidgets.QPushButton(self.centralwidget)
        self.system.setGeometry(QtCore.QRect(0, 310, 661, 101))
        self.system.setIcon(QtGui.QIcon(self.resource_path('system.jpg')))
        self.system.setIconSize(QtCore.QSize(600,600))
        self.system.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.system.setObjectName("system")
        self.system.clicked.connect(lambda: self.points_system("system1"))

        self.system_2 = QtWidgets.QPushButton(self.centralwidget)
        self.system_2.setGeometry(QtCore.QRect(0, 410, 661, 101))
        self.system_2.setIcon(QtGui.QIcon(self.resource_path('second_system.jpg')))
        self.system_2.setIconSize(QtCore.QSize(600,600))
        self.system_2.setFont(font)
        self.system_2.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.system_2.setObjectName("system_2")
        self.system_2.clicked.connect(lambda: self.points_system("system2"))

        self.third_equation = QtWidgets.QPushButton(self.centralwidget)
        self.third_equation.setGeometry(QtCore.QRect(0, 510, 661, 101))
        self.third_equation.setIcon(QtGui.QIcon(self.resource_path('third_equation.jpg')))
        self.third_equation.setIconSize(QtCore.QSize(600,600))
        self.third_equation.setFont(font)
        self.third_equation.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.third_equation.setObjectName("third_equation")
        self.third_equation.clicked.connect(lambda: self.points_system("third_equation"))

        self.fourth_equation = QtWidgets.QPushButton(self.centralwidget)
        self.fourth_equation.setGeometry(QtCore.QRect(0, 610, 661, 101))
        self.fourth_equation.setIcon(QtGui.QIcon(self.resource_path('fourth_equation.jpg')))
        self.fourth_equation.setIconSize(QtCore.QSize(600,600))
        self.fourth_equation.setFont(font)
        self.fourth_equation.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.fourth_equation.setObjectName("fourth_equation")
        self.fourth_equation.clicked.connect(lambda: self.points_system("fourth_equation"))

        self.third_system = QtWidgets.QPushButton(self.centralwidget)
        self.third_system.setGeometry(QtCore.QRect(0, 710, 661, 101))
        self.third_system.setIcon(QtGui.QIcon(self.resource_path('third_system.jpg')))
        self.third_system.setIconSize(QtCore.QSize(600,600))
        self.third_system.setFont(font)
        self.third_system.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.third_system.setObjectName("third_system")
        self.third_system.clicked.connect(lambda: self.points_system("third_system"))


        self.fifth_equation = QtWidgets.QPushButton(self.centralwidget)
        self.fifth_equation.setGeometry(QtCore.QRect(0, 810, 661, 101))
        self.fifth_equation.setIcon(QtGui.QIcon(self.resource_path('fifth_equation.jpg')))
        self.fifth_equation.setIconSize(QtCore.QSize(600,600))
        self.fifth_equation.setFont(font)
        self.fifth_equation.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.fifth_equation.setObjectName("third_system")
        self.fifth_equation.clicked.connect(lambda: self.points_system("fifth_equation"))



        


        self.instruction = QtWidgets.QPushButton(self.centralwidget)
        self.instruction.setGeometry(QtCore.QRect(0, 915, 661, 101))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.instruction.setFont(font)
        self.instruction.setObjectName("info")
        self.instruction.clicked.connect(self.show_instruction) # change

        main_menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_menu)
        self.statusbar.setObjectName("statusbar")
        main_menu.setStatusBar(self.statusbar)

        self.retranslateUi(main_menu)
        QtCore.QMetaObject.connectSlotsByName(main_menu)

    def retranslateUi(self, main_menu):
        _translate = QtCore.QCoreApplication.translate
        main_menu.setWindowTitle(_translate("main_menu", "DifferentialEquations"))
        self.label.setText(_translate("main_menu", "Differential Equations"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.instruction.setText(_translate("main_menu", "INSTRUCTION"))
        self.instruction.setStyleSheet("padding-left: 5px; padding-right: 3px;"
                                "padding-top: 1px; padding-bottom: 30px;"
                                "background-color: rgb(0, 128, 0);")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_menu = QtWidgets.QMainWindow()
    ui = Ui_main_menu()
    ui.setupUi(main_menu)
    main_menu.show()
    sys.exit(app.exec_())
