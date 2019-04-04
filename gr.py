#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 600)
    
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1201, 601)) #801
        self.label.setStyleSheet('background-color:#D4D4D4')
        self.label.setText("")
        self.label.setObjectName("label")
        self.graph = QtWidgets.QLabel(Form)
        self.graph.setGeometry(QtCore.QRect(200, 10, 591, 531))
        self.graph.setText("")
        self.graph.setScaledContents(True)
        self.graph.setObjectName("graph")
        self.forward = QtWidgets.QPushButton(Form)
        self.forward.setGeometry(QtCore.QRect(40, 180, 113, 32))
        self.forward.setObjectName("forward")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(5, 220, 191, 31))
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.time = QtWidgets.QComboBox(Form)
        self.time.setGeometry(QtCore.QRect(40, 510, 121, 26))

        self.label_100 = QtWidgets.QLabel(Form)
        self.label_100.setGeometry(QtCore.QRect(820, -20, 10000, 600))
        # ............................................
        self.label_100.setText(
            'The given graph shows Oxygen Rate v/s Time(in years).\n\n\nThe input in the graph includes :\n\n1) Population growth rate \n\n2) Phytoplankton growth rate \n\n3) Fuel burned in kgs \n\n4) Plant growth rate.\n\n\nOut of all these factors population and fuel burned in kgs. act as sinks of oxygen\nand contributes towards decreasing oxygen, increase rate in atmosphere\nand remaining factors that are phytoplankton and plants act as sources of oxygen\nand contribute towards increasing oxygen increase rate in atmosphere.\n\nIf we increase the growth rate of sources as compared to the growth rate of sinks,\nthe oxygen increase rate will be positive whereas if the growth rate of sinks is more\nas compared to growth rate of sources; the oxygen increase rate will be negative.\nThe graph depicts what will happen to oxygen levels over a span of 2019 to 2100.\n\n\nThe “Simulate” button will make the graph once proper input is provided.\n\nThe “Reset” button will reset the graph.\n\nGroup Members:\n\n1) Harsh Patel:\t201701021\t\t2) Dushyant:\t201701062\n\n3) Dhruv Charan:\t201701023\t\t4) Harin Jani:\t201701421\n\n5) Amit Agrawal:\t201701060\t\t6) Ritvik Sanghvi:\t201701059\n\n7) Sagar Singh:\t201701017\t\t8) Mann Shah:\t201701019\n\n9) Raj Patel:\t201701422\t\t10) Jigar Kapadia:\t201701424\n\n11) Manthan:\t201701063\t\t12) Sparsh Goil:\t201701061\n\n13) Jash Vithlani:\t201701426\t\t14) Idika Mittal:\t201701022\n\n15) Smit Jasani:\t201701020\t\t16) Gaurav Udani:\t201701064\n\n17) Devesh Ahuja:\t201701018\t\t18) Kevin Patel:\t201701057\n\n19) Pranav Pandey:\t201701058\t\t20) Siddharth:\t201701024')
        # ............................................
        newfont = QtGui.QFont("Ariel", 8, QtGui.QFont.Bold)
        self.label_100.setFont(newfont)
        self.label_56 = QtWidgets.QLabel(Form)
        self.label_56.setGeometry(QtCore.QRect(5, 310, 191, 31))
        self.label_56.setText('Phytoplankton Growth Rate')
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)

        self.use = QtWidgets.QComboBox(Form)
        self.use.setGeometry(QtCore.QRect(40, 340, 121, 26))

        self.label_45 = QtWidgets.QLabel(Form)
        self.label_45.setGeometry(QtCore.QRect(5, 400, 191, 31))
        self.label_45.setText('Fuel burned(in 100B kgs.)')
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)

        self.loss = QtWidgets.QComboBox(Form)
        self.loss.setGeometry(QtCore.QRect(40, 440, 121, 26))

        self.time.setObjectName("Plant Population")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(9, 490, 181, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.val = QtWidgets.QLabel(Form)
        self.val.setGeometry(80, 265, 60, 22)
        self.val.setText('0')
        self.reset = QtWidgets.QPushButton(Form)
        self.reset.setText('Reset')
        self.reset.setGeometry(QtCore.QRect(600, 550, 113, 32))
        self.ppm = QtWidgets.QSlider(Form)
        self.ppm.setGeometry(QtCore.QRect(20, 240, 160, 22))
        self.ppm.setMinimum(5)
        self.ppm.setMaximum(20)
        self.ppm.setSingleStep(1)
        self.ppm.setOrientation(QtCore.Qt.Horizontal)
        self.ppm.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.ppm.setTickInterval(1)
        self.ppm.setObjectName("rate")
        self.time.addItems(['0', '1', '2', '3', '4'])
        self.use.addItems(['0', '1', '2', '3', '4'])
        self.loss.addItems(['10', '15', '20', '25', '30'])
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 177, 101))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        ###
        self.oxy = QtWidgets.QPushButton(Form)
        self.oxy.setText('Oxygen Levels')
        self.oxy.setGeometry(QtCore.QRect(40, 50, 113, 32))
        self.oxy.setStyleSheet("background-color: green")
        self.heat = QtWidgets.QPushButton(Form)
        self.heat.setText('Heat Levels')
        self.heat.setGeometry(QtCore.QRect(40, 100, 113, 32))
        self.heat.setStyleSheet("background-color: red")
        ###
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.retranslateUi(Form)
        '''
        if isOxy:
            self.retranslateUi(Form)
        else:
            self.retranslateUiHeat(Form)
        '''

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Oxygen and Heat Rate Simulator"))
        self.forward.setText(_translate("Form", "Simulate"))
        self.forward.setGeometry(QtCore.QRect(210, 550, 113, 32))
        self.label_3.setText(_translate("Form", "Population Growth Rate"))
        self.label_4.setText(_translate("Form", "Plant Growth Rate"))

    def retranslateUiHeat(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Heat Rate Simulator"))
        self.forward.setText(_translate("Form", "Simulate"))
        self.forward.setGeometry(QtCore.QRect(210, 550, 113, 32))
        self.label_3.setText(_translate("Form", "Population Growth Rate"))
        self.label_4.setText(_translate("Form", "Plant Growth Rate"))