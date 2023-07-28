# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SA.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from CPushButton import CPushButton


class Ui_SA(object):

    def __init__(self):
        self.nbSA = 0
        self.SA = []
        self.deleteSAButtons = []
        self.addTransacButtons = []
        self.scrollAreas = []
        self.scrollAreasWidget = []
        self.Layouts0 = []
        self.Layouts1 = []

        # listes de listes correspondant aux objets de l'UI rangés par SA
        self.editButtons = []
        self.widgetsTransac = []
        self.labelTransac = []
        self.LCDTransac = []
        self.lineTransac = []




    def SAPlacement(self):
        x, y = 10, 25
        y = 25 + (415)*((self.nbSA-1)//2)
        #if (self.nbSA - 1)//2 == 1:
        #    y = 440
        self.scrollwidget.setGeometry(QtCore.QRect(0, 0, 1020, max(840, 420*((self.nbSA+1)//2))))
        if self.nbSA % 2 == 0:
            x = 524
        return x, y



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 980)
        MainWindow.setAcceptDrops(True)
        MainWindow.move(10, 10)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: hsv(190, 20, 255);")

        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(9, 9, 300, 50))
        self.BackButton.setText("Back")
        self.BackButton.setStyleSheet("background-color: rgb(200, 109, 107);")

        self.NewSAButton = QtWidgets.QPushButton(self.centralwidget)
        self.NewSAButton.setGeometry(QtCore.QRect(320, 9, 300, 50))
        self.NewSAButton.setText("New Sub Account")
        self.NewSAButton.setStyleSheet("background-color: rgb(114, 159, 207);")

        self.BilanButton = QtWidgets.QPushButton(self.centralwidget)
        self.BilanButton.setGeometry(QtCore.QRect(850, 9, 100, 50))
        self.BilanButton.setText("Bilan")
        self.BilanButton.setStyleSheet("background-color: hsv(150, 255, 150);")

        self.displaySolde = QtWidgets.QLabel(self.centralwidget)
        self.displaySolde.setGeometry((QtCore.QRect(640, 9, 200, 50)))
        font = self.displaySolde.font()
        font.setPointSize(15)
        self.displaySolde.setFont(font)
        self.displaySolde.setText("Name of the account \nSolde : 55")

        # creation of the tabs widgets
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setGeometry(QtCore.QRect(9, 71, 1042, 880))

        self.SAwidget = QtWidgets.QWidget()
        self.tabWidget.addTab(self.SAwidget, "Sub Accounts")
        self.scroll = QtWidgets.QScrollArea(self.SAwidget)
        self.scroll.setGeometry(QtCore.QRect(0, 0, 1038, 848))
        self.scrollwidget = QtWidgets.QWidget()
        self.scrollwidget.setGeometry(QtCore.QRect(0, 0, 1020, 840))
        self.scroll.setWidget(self.scrollwidget)

        self.charts = QtWidgets.QWidget()
        self.tabWidget.addTab(self.charts, "Charts")

        self.Bilan = QtWidgets.QWidget()
        self.tabWidget.addTab(self.Bilan, "Bilan")
        self.scrollBilan = QtWidgets.QScrollArea(self.Bilan)
        self.scrollBilan.setGeometry(QtCore.QRect(0, 0, 1038, 848))
        self.scrollwidget2 = QtWidgets.QWidget()
        self.scrollwidget2.setGeometry(QtCore.QRect(0, 0, 1020, 840))
        self.scrollBilan.setWidget(self.scrollwidget2)
        self.labelBilan = QtWidgets.QLabel(self.scrollwidget2)


        MainWindow.setCentralWidget(self.centralwidget)



    def addSA_ui(self, name):
        self.nbSA += 1
        x, y = self.SAPlacement()
        self.SA.append(QtWidgets.QGroupBox(self.scrollwidget))
        self.SA[-1].setGeometry(QtCore.QRect(x, y, 491, 391))
        self.SA[-1].setObjectName("groupBox")
        self.SA[-1].setTitle(name)

        self.Layouts0.append(QtWidgets.QGridLayout(self.SA[-1]))

        self.deleteSAButtons.append(CPushButton(self.SA[-1], (self.nbSA, 0)))
        self.deleteSAButtons[-1].setGeometry(QtCore.QRect(12, 354, 230, 25))
        self.deleteSAButtons[-1].setText("Delete SubAccount")
        self.deleteSAButtons[-1].setObjectName(str(self.nbSA))
        self.deleteSAButtons[-1].setStyleSheet("background-color: hsv(230, 180, 205);")

        self.addTransacButtons.append(CPushButton(self.SA[-1], (self.nbSA, 0)))
        self.addTransacButtons[-1].setGeometry(QtCore.QRect(250, 354, 230, 25))
        self.addTransacButtons[-1].setText("Add Transaction")
        self.addTransacButtons[-1].setObjectName(str(self.nbSA))
        self.addTransacButtons[-1].setStyleSheet("background-color: hsv(180, 150, 205);")

        self.scrollAreas.append(QtWidgets.QScrollArea(self.SA[-1]))
        self.scrollAreas[-1].setGeometry(QtCore.QRect(12, 30, 467, 315))
        self.scrollAreas[-1].setWidgetResizable(False)
        self.scrollAreas[-1].setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollAreas[-1].setStyleSheet("background-color: hsv(180, 45, 245);")

        self.scrollAreasWidget.append(QtWidgets.QWidget())
        self.scrollAreasWidget[-1].setGeometry(QtCore.QRect(0, 0, 451, 210))
        self.scrollAreas[-1].setWidget(self.scrollAreasWidget[-1])

        self.Layouts1.append(QtWidgets.QVBoxLayout(self.scrollAreasWidget[-1]))

        self.editButtons.append([])
        self.widgetsTransac.append([])
        self.labelTransac.append([])
        self.LCDTransac.append([])
        self.lineTransac.append([])



    def addTransac_ui(self, name, date, value):
        """
        fonction qui est supposée être executée juste après addSA_ui donc on utilisera l'indice -1 pour chaque appel de liste
        """
        self.widgetsTransac[-1].append(QtWidgets.QWidget(self.scrollAreasWidget[-1]))

        self.labelTransac[-1].append(QtWidgets.QLabel(self.widgetsTransac[-1][-1]))
        self.labelTransac[-1][-1].setTextFormat(QtCore.Qt.PlainText)
        self.labelTransac[-1][-1].setText(name + "\n" + date)
        self.labelTransac[-1][-1].setGeometry(QtCore.QRect(9, 9, 228, 34))

        self.LCDTransac[-1].append(QtWidgets.QLCDNumber(self.widgetsTransac[-1][-1]))
        self.LCDTransac[-1][-1].setProperty("value", value)
        self.LCDTransac[-1][-1].setGeometry(QtCore.QRect(243, 9, 88, 34))

        self.editButtons[-1].append(CPushButton(self.widgetsTransac[-1][-1], (self.nbSA, len(self.editButtons))))
        self.editButtons[-1][-1].setText("edit")
        self.editButtons[-1][-1].setGeometry(QtCore.QRect(337, 13, 87, 25))

        self.lineTransac[-1].append(QtWidgets.QFrame(self.widgetsTransac[-1][-1]))
        self.lineTransac[-1][-1].setFrameShape(QtWidgets.QFrame.HLine)
        self.lineTransac[-1][-1].setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineTransac[-1][-1].setGeometry(QtCore.QRect(9, 50, 415, 3))

        self.Layouts1[-1].addWidget(self.widgetsTransac[-1][-1])
        self.scrollAreasWidget[-1].setGeometry(QtCore.QRect(0, 0, 450, 70*len(self.widgetsTransac[-1])))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SA()
    ui.setupUi(MainWindow)

    ui.addSA_ui("bouffer")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")

    ui.addSA_ui("bouffer")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")

    ui.addSA_ui("bouffer")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")
    ui.addTransac_ui("burger king", "10/05/2023", "11.9")


    MainWindow.show()

    sys.exit(app.exec_())
