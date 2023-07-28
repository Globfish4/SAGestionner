# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2018

@author: ortizca

Une classe héritant de QtWidgets.QPushButton pour pouvoir gérer les QPuhsButtons plus facilement
"""

from PyQt5 import QtWidgets


class CPushButton(QtWidgets.QPushButton):
    def __init__(self, widget, id):
        super().__init__(widget)
        self.id = id #id is a tuple (a, b)

    def connectButton(self, slot):
        self.clicked.connect(lambda: slot(self.id))

    def whatSA(self):
        return self.id[0]
    def whatButton(self):
        return self.id[1]





if __name__ == "__main__":
    def slotTest(id):
        print("c'est bon ca marche")
        print(id)


    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    widget = QtWidgets.QWidget()
    MainWindow.setCentralWidget(widget)
    button = CPushButton(widget, (1, 1))
    button.connectButton(slotTest)
    MainWindow.show()

    sys.exit(app.exec_())