# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2018

@author: ortizca
"""

import sys
import os
import time
import datetime as dt
from PyQt5 import QtCore, QtWidgets
from Transac import Transac
from UIScripts.SA import Ui_SA
from UIScripts.mainMenu import Ui_mainMenu
from UIScripts.DialogNewAccount import Ui_DialogNewAccount
from UIScripts.DialogNewSA import Ui_DialogNewSA
from UIScripts.DialogDeleteSA import Ui_DialogDeleteSA
from UIScripts.DialogNewTransac import Ui_DialogNewTransac
from UIScripts.DialogConfirmation import Ui_DialogConfirmation




class MonAppli(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()
        self.File = 0
        self.lines = []
        self.AccountNames = []
        self.AccountName = ""
        self.AccountSolde = 0

        self.SANames = []
        self.SASoldes = []

        self.workingID = (0, 0)
        self.current_index = 0
        self.SAtoTransferFunds = ""

        self.accountFile = 0
        self.diag = 0
        self.confirmDialog = 0


    def launchApp(self):
        self.ui = Ui_mainMenu()
        self.ui.setupUi(self)
        self.show()
        self.File = open("../testfiles/AccountsHeader.txt", "r")
        self.AccountNames = self.File.readlines()
        self.File.close()
        self.ui.comboBox.addItems(self.AccountNames)
        connectButtonsMainMenu(self)

    def GoToSA(self):
        index = self.ui.comboBox.currentIndex()
        name = self.ui.comboBox.itemText(index)
        self.AccountName = name[:-1]

        self.refreshSA_Ui()

    def refreshSA_Ui(self):
        # We recreate completely the window from scratch. The adjustements will be taken into account
        self.ui = Ui_SA()
        self.ui.setupUi(self)
        self.adaptUi()
        self.displayBilans()
        print("########### REFRESHED", len(self.ui.SA), len(self.SANames), len(self.SASoldes), " Nombre de SA")
        for k in range(len(self.SASoldes)):
            formatted_string = f"{self.SASoldes[k]:.{2}f}"
            self.ui.SA[k].setTitle(self.SANames[k]+ " : " + formatted_string + " €")
        formatted_string = f"{self.AccountSolde:.{2}f}"
        self.ui.displaySolde.setText(self.AccountName + "\nSolde : " + formatted_string + " €")
        connectButtonsSA(self)
        self.ui.tabWidget.setCurrentIndex(self.current_index)
        self.show()


    def adaptUi(self):
        self.File = open("../testfiles/"+self.AccountName+".txt", "r")
        self.lines = self.File.readlines()
        soldeMA = 0
        soldeSA = 0
        self.SANames = []
        self.SASoldes = []
        for k in self.lines:
            if k[:2] == "%%":
                self.ui.addSA_ui(k[2:-3])
                self.SANames.append(k[2:-3])
                self.SASoldes.append(soldeSA)
                soldeMA += soldeSA
                soldeSA = 0
            elif k[:1] == "%":
                liste = k.split("%")
                self.ui.addTransac_ui(liste[1], liste[2], liste[3])
                soldeSA += eval(liste[3])
        self.SASoldes.append(soldeSA)
        self.SASoldes.pop(0)
        soldeMA += soldeSA
        self.AccountSolde = soldeMA
        self.File.close()


    def displayBilans(self):
        self.File = open("../testfiles/BilanFile"+self.AccountName+".txt", "r")
        texte = self.File.readlines()
        l = len(texte)
        self.File.close()
        self.ui.scrollwidget2.setGeometry(QtCore.QRect(0, 0, 1020, 17*l + 10))
        self.ui.labelBilan.setGeometry(QtCore.QRect(15, 0, 1010, 17*l))
        for k in texte:
            self.ui.labelBilan.setText(self.ui.labelBilan.text() + k)





    def blockUntilConfirm(self, message):
        self.confirmDialog = DialogConfirmationPop(self, message)
        return self.confirmDialog.exec_()




    def createAccount(self):
        self.diag = DialogCreateAccount(self)

    def createSA(self):
        self.diag = DialogCreateSA(self)

    def addTransac(self, id):
        print(id)
        self.workingID = id
        self.diag = DialogCreateTransac(self)



    def newTransac(self, name, date, value):
        print("oui j'ajoute transac")
        print(self.workingID)
        self.File = open("../testfiles/"+self.AccountName+".txt", 'r')
        text = self.File.readlines()
        self.File.close()
        T = Transac(name, date, value)

        compteurSA = 0
        for k in range(len(text)): #Pour chaque ligne du fichier de compte
            if text[k][:2] == "%%": # Si la ligne est celle d'un sous compte
                compteurSA += 1 #alors on incrémente compteurSA
            if compteurSA == self.workingID[0]: # Si compteurSA vaut l'ID, alors on est sur le bon sous compte
                try:
                    if text[k][:2] == "%%": # Cas 1 : il n'y a pas d'autre transac dans le SA
                        if text[k+1][:2] == "%%":
                            text.insert(k+1, "%"+name+"%"+date+"%"+str(value)+"%\n")
                            break
                    elif Transac(0, 0, ligne=text[k]) < T: # Cas 2 : la transac en cours est plus tôt que la nouvelle
                        text.insert(k, "%"+name+"%"+date+"%"+str(value)+"%\n") # alors on insert la nouvelle juste avant
                        break
                    elif Transac(0, 0, ligne=text[k]) > T and text[k+1][:2] == "%%": # Cas 3 : la transac est la plus tot de toutes
                        text.insert(k+1, "%"+name+"%"+date+"%"+str(value)+"%\n")
                        break
                except IndexError:
                    text.append("%"+name+"%"+date+"%"+str(value)+"%\n")

        self.File = open("../testfiles/"+self.AccountName+".txt", 'w') # on réécrit totalement le fichier de compte
        for k in range(len(text)):
            self.File.write(text[k])
        self.File.close()

        self.current_index = self.ui.tabWidget.currentIndex()
        self.refreshSA_Ui()


### Bug, le transfer se passe mal
    def deleteSA(self, id):

        self.workingID = id
        print(self.workingID)
        self.diag = DialogDeleteSA(self)
        self.diag.exec_()

        self.workingID = (self.SAtoTransferFunds, 0)
        self.newTransac("Transfering from "+self.SANames[id[0]], str(dt.datetime.now().date().strftime("%d/%m/%Y")), self.SASoldes[id[0]-1])

        self.File = open("../testfiles/"+self.AccountName+".txt", 'r')
        text = self.File.readlines()
        self.File.close()

        self.workingID = id
        indexDebut = 0
        indexFin = 0
        for k in range(len(text)):
            if text[k][:2] == "%%" and text[k][2:-3] == self.SANames[self.workingID[0] -1]:
                indexDebut = k
            if text[k][:2] == "%%" and text[k][2:-3] == self.SANames[self.workingID[0]]:
                indexFin = k
        newtext = text[:indexDebut] + text[indexFin:]

        self.File = open("../testfiles/"+self.AccountName+".txt", 'w') # on réécrit totalement le fichier de compte
        for k in range(len(newtext)):
            self.File.write(newtext[k])
        self.File.close()
        print("SA Deleted !")
        self.refreshSA_Ui()



    def editTransac(self):
        pass



    def deleteAccount(self):
        if self.blockUntilConfirm("Etes-vous sûr de vouloir supprimer ce compte ?"):
            self.File = open("../testfiles/AccountsHeader.txt", "r")
            text = self.File.readlines()
            self.File.close()
            index = self.ui.comboBox.currentIndex()
            name = self.ui.comboBox.itemText(index)[:-1]
            for k in text:
                if k[:-1] == name:
                    text.remove(k)
                    self.File = open("../testfiles/AccountsHeader.txt", "w")
                    for x in text:
                        self.File.write(x)
                    self.File.close()
            os.remove("../testfiles/" + name + ".txt")
            os.remove("../testfiles/BilanFile" + name + ".txt")

            self.launchApp()






    def Bilan(self):
        self.File = open("../testfiles/"+self.AccountName+".txt", "r")
        texte = self.File.readlines()
        self.File.close()

        lastTransacDate = dt.date(2000, 1, 1)
        lastTransac = ["transac de base"]
        for k in texte:
            if k[:2] != "%%":
                ligne = k.split("%")
                date = ligne[2].split("/")
                date = dt.date(int(date[2], base=10), int(date[1], base=10), int(date[0], base=10))
                if date > lastTransacDate:
                    lastTransacDate = date
                    lastTransac = [k]
                elif date == lastTransacDate:
                    lastTransac.append(k)
        #ici on a une liste lastTransac qui contient toutes les transac de la dernière date

        self.File = open("../testfiles/BilanFile"+self.AccountName+".txt", "a")
        self.File.write("\n")
        self.File.write("############## NEW BILAN ################\n")
        self.File.write("le : " + str(dt.datetime.now().date().strftime("%d/%m/%Y")) + "\n")
        self.File.write("derniers paiements : le " + str(lastTransacDate.strftime("%d/%m/%Y")) + "\n")
        for k in lastTransac:
            try:
                self.File.write(k.split("%")[1] + "\n")
            except IndexError:
                print("no transac available")
        for k in range(len(self.SANames)):
            formatted_string = f"{self.SASoldes[k]:.{2}f}"
            self.File.write(self.SANames[k] + " : " + formatted_string + "\n")
        self.File.close()

        self.current_index = self.ui.tabWidget.currentIndex()
        self.refreshSA_Ui()






def connectButtonsMainMenu(window):
    window.ui.pushButton.clicked.connect(window.createAccount)
    window.ui.GoButton.clicked.connect(window.GoToSA)
    window.ui.pushButton_2.clicked.connect(window.deleteAccount)



def connectButtonsSA(window):
    window.ui.BackButton.clicked.connect(window.launchApp)
    window.ui.NewSAButton.clicked.connect(window.createSA)
    window.ui.BilanButton.clicked.connect(window.Bilan)

    # connecting AddTransac and deleteSA buttons
    for k in range(window.ui.nbSA):
        window.ui.deleteSAButtons[k].connectButton(window.deleteSA)
        window.ui.addTransacButtons[k].connectButton(window.addTransac)






class DialogCreateAccount(QtWidgets.QDialog):
    def __init__(self, window):
        super().__init__()
        self.File = 0
        self.window = window
        self.ui = Ui_DialogNewAccount()
        self.ui.setupUi(self)
        self.connect_Buttons()
        self.show()

    def connect_Buttons(self):
        self.ui.buttonBox.disconnect()
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.lineEdit.textChanged.connect(self.checkValues)

    def checkValues(self):
        SAName = self.ui.lineEdit.text()
        if SAName == "" or SAName+"\n" in self.window.AccountNames:
            self.ui.buttonBox.accepted.connect(self.vide)
            self.ui.buttonBox.accepted.disconnect()
            self.ui.buttonBox.blockSignals(True)
            self.ui.ErrorMsg.setText("Account Name not available")
        else:
            self.ui.buttonBox.accepted.connect(self.vide)
            self.ui.buttonBox.accepted.disconnect()
            self.ui.buttonBox.blockSignals(False)
            self.ui.buttonBox.accepted.connect(self.keepValues)
            self.ui.buttonBox.accepted.connect(self.accept)
            self.ui.ErrorMsg.setText("")

    def vide(self):
        pass

    def keepValues(self):
        AccountName = self.ui.lineEdit.text()

        self.File = open("../testfiles/AccountsHeader.txt", "a")
        self.File.write(AccountName+"\n")
        self.File.close()
        self.File = open("../testfiles/"+AccountName+".txt", 'x')
        self.File.close()
        self.File = open("../testfiles/BilanFile" + AccountName + ".txt", "x")
        self.File.close()

        self.window.launchApp()






class DialogCreateSA(QtWidgets.QDialog):
    def __init__(self, window):
        super().__init__()
        self.File = 0
        self.validSaisie = False
        self.window = window
        self.ui = Ui_DialogNewSA()
        self.ui.setupUi(self)
        self.connect_Buttons()
        self.show()

    def connect_Buttons(self):
        self.ui.buttonBox.disconnect()
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.lineEdit.textChanged.connect(self.checkValues)

    def checkValues(self):
        SAName = self.ui.lineEdit.text()
        if SAName == "" or SAName in self.window.SANames:
            self.ui.buttonBox.accepted.connect(self.vide)
            self.ui.buttonBox.accepted.disconnect()
            self.ui.buttonBox.blockSignals(True)
            self.ui.ErrorMsg.setText("SA Name not possible")
        else:
            self.ui.buttonBox.accepted.connect(self.vide)
            self.ui.buttonBox.accepted.disconnect()
            self.ui.buttonBox.blockSignals(False)
            self.ui.buttonBox.accepted.connect(self.keepValues)
            self.ui.buttonBox.accepted.connect(self.accept)
            self.ui.ErrorMsg.setText("")

    def vide(self):
        pass

    def keepValues(self):
        SAName = self.ui.lineEdit.text()
        print("Entrée validée, j'ajoute SA")
        self.File = open("../testfiles/"+self.window.AccountName+".txt", 'a')
        self.File.write("%%"+SAName+"%%\n")
        self.File.close()

        self.window.current_index = self.window.ui.tabWidget.currentIndex()
        self.window.refreshSA_Ui()





class DialogDeleteSA(QtWidgets.QDialog):
    def __init__(self, window):
        super().__init__()
        self.File = 0
        self.validSaisie = False
        self.window = window
        self.ui = Ui_DialogDeleteSA()
        self.ui.setupUi(self)
        self.connect_Buttons()
        self.show()

    def connect_Buttons(self):
        self.ui.buttonBox.accepted.connect(self.keepValues)
        self.ui.comboBox.addItems([self.window.SANames[k] for k in range(len(self.window.SANames)) if k+1 != self.window.workingID[0]])


    def keepValues(self):
        index = self.ui.comboBox.currentIndex()
        name = self.ui.comboBox.itemText(index)
        self.window.SAtoTransferFunds = self.window.SANames.index(name) + 1
        #self.window.SAtoTransferFunds = index + 1
        print(self.window.SAtoTransferFunds)






class DialogCreateTransac(QtWidgets.QDialog):
    def __init__(self, window):
        super().__init__()
        self.File = 0
        self.window = window
        self.ui = Ui_DialogNewTransac()
        self.ui.setupUi(self)
        self.connect_Buttons()
        self.show()

    def connect_Buttons(self):
        self.ui.buttonBox.accepted.connect(self.keepValues)

    def keepValues(self):
        TransacName = self.ui.lineEdit.text()
        TransacDate = self.ui.lineEdit_2.text()
        TransacValue = self.ui.lineEdit_3.text()
        self.window.newTransac(TransacName, TransacDate, TransacValue)


    """
    def keepValues2(self):
        TransacName = self.ui.lineEdit.text()
        TransacDate = self.ui.lineEdit_2.text()
        TransacValue = self.ui.lineEdit_3.text()

        self.File = open("../testfiles/"+self.window.AccountName+".txt", 'r')
        text = self.File.readlines()
        self.File.close()

        compteurSA = 0
        for k in range(len(text)):
            if text[k][:2] == "%%":
                compteurSA += 1
                if compteurSA == self.window.workingID[0]:
                    text.insert(k+1, "%"+TransacName+"%"+TransacDate+"%"+TransacValue+"%\n")
                    break

        self.File = open("../testfiles/"+self.window.AccountName+".txt", 'w')
        for k in range(len(text)):
            self.File.write(text[k])
        self.File.close()

        self.window.current_index = self.window.ui.tabWidget.currentIndex()
        self.window.refreshSA_Ui()
    """




class DialogConfirmationPop(QtWidgets.QDialog):
    def __init__(self, window, message):
        super().__init__()
        self.window = window
        self.ui = Ui_DialogConfirmation()
        self.ui.setupUi(self)
        self.ui.label.setText(message)
        self.show()









if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.launchApp()
    app.exec_()