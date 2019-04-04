from gr import Ui_Form
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sys import argv
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import tkinter as tk


class mas2(QWidget, Ui_Form):
    def __init__(self):
        super(mas2, self).__init__()
        self.setupUi(self)
        self.bool = True
        self.plant_gr = 0
        self.seax = [2013]
        self.seay = [0]
        self.pop = 0.5
        self.phyto = 0
        self.fuel = 10
        self.coal = 0
        self.ppm.valueChanged.connect(self.se)
        self.forward.clicked.connect(self.go)
        self.time.currentIndexChanged.connect(self.t)
        self.use.currentIndexChanged.connect(self.u)
        self.loss.currentIndexChanged.connect(self.l)
        self.reset.clicked.connect(self.re)
        ##
        self.oxy.clicked.connect(self.oxygen)
        self.heat.clicked.connect(self.heating)
        ##
        fig, self.ax1 = plt.subplots()
        self.ax1.plot([], [])
        # self.ax1.axis([2018, 2100, 0, 1200])
        self.ax1.xaxis.grid()
        self.ax1.yaxis.grid()
        self.ax1.set_facecolor('black')
        self.ax1.set_ylabel('Oxygen Increase Rate')
        self.ax1.yaxis.label.set_color('black')
        self.ax1.tick_params(axis='y', colors='black')

        self.ax1.set_xlabel('Date (Year)')

        plt.savefig('fig.png')
        self.graph.setPixmap(QPixmap('fig.png'))
        self.show()

    ###
    def oxygen(self):
        self.label_56.setText('Phytoplankton Growth Rate')
        self.time.setObjectName("Plant Population")
        self.label_100.setText(
                'The given graph shows Oxygen Rate v/s Time(in years).\n\n\nThe input in the graph includes :\n\n1) Population growth rate \n\n2) Phytoplankton growth rate \n\n3) Fuel burned in kgs \n\n4) Plant growth rate.\n\n\nOut of all these factors population and fuel burned in kgs. act as sinks of oxygen\nand contributes towards decreasing oxygen, increase rate in atmosphere\nand remaining factors that are phytoplankton and plants act as sources of oxygen\nand contribute towards increasing oxygen increase rate in atmosphere.\n\nIf we increase the growth rate of sources as compared to the growth rate of sinks,\nthe oxygen increase rate will be positive whereas if the growth rate of sinks is more\nas compared to growth rate of sources; the oxygen increase rate will be negative.\nThe graph depicts what will happen to oxygen levels over a span of 2019 to 2100.\n\n\nThe “Simulate” button will make the graph once proper input is provided.\n\nThe “Reset” button will reset the graph.\n\nGroup Members:\n\n1) Harsh Patel:\t201701021\t\t2) Dushyant:\t201701062\n\n3) Dhruv Charan:\t201701023\t\t4) Harin Jani:\t201701421\n\n5) Amit Agrawal:\t201701060\t\t6) Ritvik Sanghvi:\t201701059\n\n7) Sagar Singh:\t201701017\t\t8) Mann Shah:\t201701019\n\n9) Raj Patel:\t201701422\t\t10) Jigar Kapadia:\t201701424\n\n11) Manthan:\t201701063\t\t12) Sparsh Goil:\t201701061\n\n13) Jash Vithlani:\t201701426\t\t14) Idika Mittal:\t201701022\n\n15) Smit Jasani:\t201701020\t\t16) Gaurav Udani:\t201701064\n\n17) Devesh Ahuja:\t201701018\t\t18) Kevin Patel:\t201701057\n\n19) Pranav Pandey:\t201701058\t\t20) Siddharth:\t201701024')
        self.label_56.setText('Phytoplankton Growth Rate')
        self.bool = True
        self.ax1.set_ylabel('Oxygen Increase Rate')

    def heating(self):
        self.label_56.setText('Heat Rate')
        self.label_100.setText(
                'The given graph shows Heat Rate v/s Time(in years).\n\n\nThe input in the graph includes :\n\n1) Population growth rate \n\n2) Increase in Coal Demand \n\n3) Fuel burned in kgs \n\n4) Plant growth rate.\n\n\nOut of all these factors population, increase in coal demand and fuel burned in kgs.\n act as source of CO2 and thus contributes towards increasing heat in environment\nand remaining factor that is plant growth rate act as sources of oxygen, thus\ncontributing towards decreasing ocean warming.\n\nIf we increase the growth rate of sources as compared to the growth rate of sinks,\nthe heat rate will be positive whereas if the growth rate of sinks is more\nas compared to growth rate of sources; the heat increase rate will be negative.\nThe graph depicts what will happen to heat levels over a span of 2019 to 2100.\n\n\nThe “Simulate” button will make the graph once proper input is provided.\n\nThe “Reset” button will reset the graph.\n\nGroup Members:\n\n1) Harsh Patel:\t201701021\t\t2) Dushyant:\t201701062\n\n3) Dhruv Charan:\t201701023\t\t4) Harin Jani:\t201701421\n\n5) Amit Agrawal:\t201701060\t\t6) Ritvik Sanghvi:\t201701059\n\n7) Sagar Singh:\t201701017\t\t8) Mann Shah:\t201701019\n\n9) Raj Patel:\t201701422\t\t10) Jigar Kapadia:\t201701424\n\n11) Manthan:\t201701063\t\t12) Sparsh Goil:\t201701061\n\n13) Jash Vithlani:\t201701426\t\t14) Idika Mittal:\t201701022\n\n15) Smit Jasani:\t201701020\t\t16) Gaurav Udani:\t201701064\n\n17) Devesh Ahuja:\t201701018\t\t18) Kevin Patel:\t201701057\n\n19) Pranav Pandey:\t201701058\t\t20) Siddharth:\t201701024')
        self.label_56.setText('Increase in Coal Demand')
        self.bool = False
        self.ax1.set_ylabel('Heat Increase Rate')
    ###

    def u(self):
        self.phyto = float(self.use.currentText().split()[0])
        self.coal = float(self.use.currentText().split()[0])

    def l(self):
        self.fuel = float(self.loss.currentText().split()[0])

    def t(self):
        self.plant_gr = float(self.time.currentText().split()[0])

    def re(self):
        self.hide()
        self.__init__()

    def init():
        line.set_data([], [])
        return line,

    def se(self):
        self.pop = self.ppm.value() / 10
        self.val.setText(str(self.pop) + ' %')

    def go(self):
        if self.bool:
            sm = (260 * 0.45 * 10 ** 10 + 5.15 * 10 ** 18 * 0.2 * 0.65 * 10 ** (
            -6) * 7.5 - 4.2 * self.fuel * 10 ** 11 - 5 * 550 * 365 * 1.49 * 10 ** (-3) * 7 * 10 ** 9) / 10 ** 9 + 20000
            self.seay = [sm];
            for i in range(20):
                self.seax.append(self.seax[-1] + 5)
                self.seay.append(((117 * (10 ** 10) * np.exp(self.plant_gr * (self.seax[-1] - 2018) / 50)) +
                                  (5.25 * 10 ** (12) * np.exp(self.phyto * (self.seax[-1] - 2018) / 500) - 4.2 * (
                                  10 ** 11) * self.fuel -
                                   1.04 * (10 ** 13) * np.exp(self.pop * (self.seax[-1] - 2018) / 50))) / 10 ** 9 + 20000)
                plt.scatter(self.seax, self.seay)
                # equation and plot

                plt.savefig('fig.png')
                self.graph.setPixmap(QPixmap('fig.png'))
        else:
            sm = (260 * 0.45 * 10 ** 10 + 5.15 * 10 ** 18 * 0.2 * 0.65 * 10 ** (
            -6) * 7.5 - 4.2 * self.fuel * 10 ** 11 - 5 * 550 * 365 * 1.49 * 10 ** (-3) * 7 * 10 ** 9) / 10 ** 9 + 20000
            self.seay = [sm];
            for i in range(20):
                self.seax.append(self.seax[-1] + 5)
                
                self.seay.append(((-117 * (10 ** 10) * np.exp(self.plant_gr * (self.seax[-1] - 2018) / 50)) +
                                  (5.25 * 10 ** (12) * np.exp(self.coal * (self.seax[-1] - 2018) / 500) + 4.2 * (
                                  10 ** 11) * self.fuel +
                                   1.04 * (10 ** 13) * np.exp(self.pop * (self.seax[-1] - 2018) / 50))) / 10 ** 9 + 20000)
                
                plt.scatter(self.seax, self.seay)
                # equation and plot

                plt.savefig('fig.png')
                self.graph.setPixmap(QPixmap('fig.png'))        

if __name__ == '__main__':
    app = QApplication(argv)
    m = mas2()
    app.exec_()
