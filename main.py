import pt as parts
from PyQt5 import QtCore, QtGui, QtWidgets
import sys 


#DONE todo: create a new ui on addFunction that prints seleced list item  
#todo: change select to return and add that to the functions ui 
#todo: create a go thro functions list to modify when generate is called 

#list of functions to be added 
partitionFns = ["oddParts", "evenParts","smallerThan","biggerThan","removeN", "removeDiv"] 

#list of functions being used 
liveFunctions = [] 

#global check to add function

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

     
#main wndow class            
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addFnButton.clicked.connect(self.get_value)

    def get_value(self):
        dialog = InputDialog(self)

        # this will show the dialog and wait 
        if dialog.exec():
            print("waiting for result")
        
        if (getGlobalFnAdd()!= None): 
            print(getGlobalFnAdd())
        
        setGlobalFnAdd(None)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    setGlobalFnAdd(None)
    MainWindow.show()
    sys.exit(app.exec_())


#a = int(input("Enter the number u want to partion:- "))
#ans = parts.getPartitions(a) 
#print(len(ans))

