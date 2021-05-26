#-------------------Intro Note----------------------------------#
#Function: UI of partitions program 
#Made by: Jaision Thomas 
#---------------------------------------------------------------#

import pt as parts
from PyQt5 import QtCore, QtGui, QtWidgets
import sys 


#DONE: create a new ui on addFunction that prints seleced list item  
#DONE: change select to return and add that to the functions ui 
#DONE: create a go thro functions list to modify when generate is called 


#DONE: create delete function for list 
#DONE: handle input error (throw error popup)

#list of functions to be added 
partitionFns = ["oddParts", "evenParts","sizeSmallerThan","sizeBiggerThan","removeN", "removeDiv", "lesserThanN", "greaterThanN"] 

#list of functions being used 
liveFunctions = [] 

def goThroFns(listVal): 
    for i in liveFunctions: 

        if i in partitionFns: 
            if  partitionFns.index(i) == 0:
                listVal = parts.oddParts(listVal) 
            elif partitionFns.index(i) == 1: 
                listVal = parts.evenParts(listVal) 
        else:
            if partitionFns.index(i[0]) == 2:
                listVal = parts.smallerThan(listVal,i[1])
            elif partitionFns.index(i[0]) == 3:
                listVal = parts.biggerThan(listVal,i[1])
            elif partitionFns.index(i[0]) == 4:
                listVal = parts.removeN(listVal,i[1])
            elif partitionFns.index(i[0]) == 5:
                listVal = parts.removeDiv(listVal,i[1])
            elif partitionFns.index(i[0]) == 6:
                listVal = parts.lessThanN(listVal,i[1])
            elif partitionFns.index(i[0]) == 7:
                listVal = parts.greaterThanN(listVal,i[1])
           
    return listVal

#return a set of strings for the funtions display main 
def liveToStr():
    retVal = []  
    for i in liveFunctions: 
        if i in partitionFns: 
            retVal.append(i)
        else: 
            st = i[0] + '(' + str(i[1]) + ')'
            retVal.append(st)
    return retVal


def setGlobalFnAdd(val): 
    global globalFnAdd 
    globalFnAdd = val 

def getGlobalFnAdd(): 
    return globalFnAdd 

#second list screen UI 
class Ui_Dialog(object):

    def selected(self,item): 
        setGlobalFnAdd(item.text())
        self.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(250, 350)

        self.fnList = QtWidgets.QListWidget(Dialog)
        self.fnList.setGeometry(QtCore.QRect(10, 30, 231, 311))
        self.fnList.setObjectName("fnList")
        self.fnList.itemClicked.connect(self.selected)
        self.fnList.addItems(partitionFns)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Functions"))
        self.label.setText(_translate("Dialog", "Choose Your Function:"))

#sceond screen class 
class InputDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        

#enter number screen ui 
class Ui_EnterNO(object):

    def quickClose(self): 
        self.close() 

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(244, 69)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label.setObjectName("label")
        self.submitButton = QtWidgets.QPushButton(Dialog)
        self.submitButton.setGeometry(QtCore.QRect(150, 30, 91, 31))
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.quickClose)

        self.fnNo = QtWidgets.QLineEdit(Dialog)
        self.fnNo.setGeometry(QtCore.QRect(10, 30, 131, 31))
        self.fnNo.setObjectName("fnNo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Number :"))
        self.submitButton.setText(_translate("Dialog", "OK"))



#sceond screen class 
class EnterNODialog(QtWidgets.QDialog, Ui_EnterNO):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def get_val(self):
        return self.fnNo.text() 


#mainwindow ui class  
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(500, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.inputNo = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNo.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.inputNo.setObjectName("inputNo")

        self.genButton = QtWidgets.QPushButton(self.centralwidget)
        self.genButton.setGeometry(QtCore.QRect(220, 10, 113, 32))
        self.genButton.setObjectName("genButton")
        self.genButton.clicked.connect(self.genListValues) 

        self.ansList = QtWidgets.QListWidget(self.centralwidget)
        self.ansList.setGeometry(QtCore.QRect(10, 50, 311, 451))
        self.ansList.setObjectName("ansList")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 550, 191, 51))
        self.label1.setText("Total number of partitions:- ")
        self.label1.setObjectName("label1")

        self.partCount = QtWidgets.QLabel(self.centralwidget)
        self.partCount.setGeometry(QtCore.QRect(240, 550, 81, 51))
        self.partCount.setText("")
        self.partCount.setObjectName("partCount")

        self.fnLabel = QtWidgets.QLabel(self.centralwidget)
        self.fnLabel.setGeometry(QtCore.QRect(340, 20, 81, 20))
        self.fnLabel.setObjectName("fnLabel")

        self.addFnButton = QtWidgets.QPushButton(self.centralwidget)
        self.addFnButton.setGeometry(QtCore.QRect(380, 510, 113, 32))
        self.addFnButton.setObjectName("addFnButton")

        self.fnList = QtWidgets.QListWidget(self.centralwidget)
        self.fnList.setGeometry(QtCore.QRect(340, 50, 141, 451))
        self.fnList.setObjectName("fnList")
        self.fnList.itemClicked.connect(self.deleteMessage)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Partitions"))
        self.genButton.setText(_translate("MainWindow", "Generate"))
        self.fnLabel.setText(_translate("MainWindow", "Functions: "))
        self.addFnButton.setText(_translate("MainWindow", "AddFunction"))

    def setCount(self): 
        txt = str(self.ansList.count())
        self.partCount.setText(txt)
     
    def errorMessage(self,title, txt):
        msg =  QtWidgets.QMessageBox() 
        msg.setWindowTitle(title)
        msg.setText(txt) 
        #msg.setIcon(QtWidgets.QMessageBox.critical)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
       
        x = msg.exec_()

     
    def deleteMessage(self,i): 
        msg =  QtWidgets.QMessageBox() 
        msg.setWindowTitle("Delete Function")
        msg.setText("are u sure u want to delete " + i.text())
        msg.setStandardButtons(QtWidgets.QMessageBox.Cancel|QtWidgets.QMessageBox.Yes)
        msg.setDefaultButton(QtWidgets.QMessageBox.Yes)

        
        msg.buttonClicked.connect(self.popItem)
        x = msg.exec_()
    
    def popItem(self, i):
        if i.text() == "&Yes":
            index = self.fnList.currentRow() 
            liveFunctions.pop(index) 

            self.fnList.clear()
            newL = liveToStr() 
            self.fnList.addItems(newL)


    #generates the partions and adds to list 
    def genListValues(self):
        text = self.inputNo.text() 
        try: 
            toPart = int(text)
            listVal = parts.getPartitions(toPart)
            #create the go thro functions here 
            listVal = goThroFns(listVal)

            
            self.ansList.clear()
            list_string = map(str, listVal) 
            self.ansList.addItems(list_string)

            self.setCount() 

        except ValueError as e : 
            self.errorMessage("Type Mismatch", "Please Make sure to enter a number")
            #print(e)
     
#main wndow class            
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addFnButton.clicked.connect(self.get_value)

    #addFunction from list 
    def get_value(self):
        dialog = InputDialog(self)

        # this will show the dialog and wait 
        if dialog.exec():
            print("waiting for result")
        
        #if item was selected add to fn list 
        if (getGlobalFnAdd()!= None): 
            sel = getGlobalFnAdd()
            
            if partitionFns.index(sel)==0 or partitionFns.index(sel)==1:
                liveFunctions.append(sel)
            
            else: 
                dialog = EnterNODialog(self)

                if dialog.exec(): 
                    print("waiting for result")

                try: 
                    fnParameter = int(dialog.get_val())
                    a = [] 
                    a.append(sel)
                    a.append(fnParameter)
                    liveFunctions.append(a)
        
                except ValueError: 
                    self.errorMessage("Type Mismatch", "Please Make sure to enter a number")


            self.fnList.clear()
            newL = liveToStr() 
            self.fnList.addItems(newL)
        
        setGlobalFnAdd(None)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    setGlobalFnAdd(None)
    MainWindow.show()
    sys.exit(app.exec_())


