import pt as parts 
import time
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import sys 


#DONE todo: create a new ui on addFunction that prints seleced list item  
#todo: change select to return and add that to the functions ui 
#todo: create a go thro functions list to modify when generate is called 

#list of functions to be added 
partitionFns = ["oddParts", "evenParts","smallerThan","biggerThan","removeN", "removeDiv"] 

#global async parameter 
def setSelectedState(val):
    global selectedState 
    selectedState = val  

def getSelectedState(): 
    return selectedState  

#second screen the list that addsFunctions 
class SecondWindow(QtWidgets.QMainWindow): 

    def printTest(self): 
        print("heelo world")

    def __init__(self): 
        super(SecondWindow, self).__init__() 
        self.setWindowTitle("Functions")
        self.itemSelected = True 
        self.retval = None 
        self.setupUi()
    
    def setupUi(self): 
        self.setObjectName("SecondWindow")
        self.setFixedSize(252, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        def selected(item):
            print(item.text())
            self.close()
            
            
               
        self.fnList = QtWidgets.QListWidget(self.centralwidget)
        self.fnList.setGeometry(QtCore.QRect(10, 30, 231, 291))
        self.fnList.setObjectName("fnList")
        self.fnList.addItems(partitionFns)
        self.fnList.itemClicked.connect(selected)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 151, 21))
        self.label.setObjectName("label")
        self.label.setText("Choose Your Function: ")

        self.setCentralWidget(self.centralwidget)
       
    def closeEvent(self, event):
        setSelectedState(True)


#main ui class  
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
        self.addFnButton.clicked.connect(self.addFunction) 

        self.fnList = QtWidgets.QListWidget(self.centralwidget)
        self.fnList.setGeometry(QtCore.QRect(340, 50, 141, 451))
        self.fnList.setObjectName("fnList")

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
     
    #generates the partions and adds to list 
    def genListValues(self):
        text = self.inputNo.text() 
        try: 
            toPart = int(text)
            listVal = parts.getPartitions(toPart)
            self.ansList.clear()
            list_string = map(str, listVal) 
            self.ansList.addItems(list_string)

            self.setCount() 

        except ValueError: 
            print("handle string error") 

     
    #created new window with listwidget and returns the selected item 
    def addFunction(self): 
        self.win = SecondWindow() 
        self.win.show()
        self.win.printTest()

        print("here, after the close")
    
                

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    setSelectedState(False)
    sys.exit(app.exec_())


#a = int(input("Enter the number u want to partion:- "))
#ans = parts.getPartitions(a) 
#print(len(ans))

