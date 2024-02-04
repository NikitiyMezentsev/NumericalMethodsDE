# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instruction.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Instruction(object):
    def setupUi(self, Instruction):
        Instruction.setObjectName("Instruction")
        Instruction.resize(1236, 803)
        self.centralwidget = QtWidgets.QWidget(Instruction)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1251, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("instruction.jpg"))
        self.label.setObjectName("label")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(0, 690, 1241, 91))
        self.clear.clicked.connect(Instruction.close)
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.clear.setObjectName("clear")
        Instruction.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Instruction)
        self.statusbar.setObjectName("statusbar")
        Instruction.setStatusBar(self.statusbar)

        self.retranslateUi(Instruction)
        QtCore.QMetaObject.connectSlotsByName(Instruction)

    def retranslateUi(self, Instruction):
        _translate = QtCore.QCoreApplication.translate
        Instruction.setWindowTitle(_translate("Instruction", "MainWindow"))
        self.clear.setText(_translate("Instruction", "CLEAR!"))
