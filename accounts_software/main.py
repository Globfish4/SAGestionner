# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2018

@author: ortizca
"""

import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from UIScripts.SA import Ui_SA
from UIScripts.mainMenu import Ui_mainMenu


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_mainMenu()
    ui2 = Ui_mainMenu()
    ui.setupUi(MainWindow)
    ui2.setupUi(MainWindow2)
    MainWindow.show()
    MainWindow2.show()
    sys.exit(app.exec_())
