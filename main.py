import pt as parts 

from PyQt5 import QtCore, QtGui, QtWidgets
import sys 

listVal = [1,2,3,45,6,7]; 
 
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
        self.genButton.setGeometry(QtCore.QRect(240, 10, 113, 32))
        self.genButton.setObjectName("genButton")
        self.genButton.clicked.connect(self.genListValues) 

        self.ansList = QtWidgets.QListWidget(self.centralwidget)
        self.ansList.setGeometry(QtCore.QRect(10, 50, 341, 501))
        self.ansList.setObjectName("ansList")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 550, 191, 51))
        self.label1.setText("Total number of partitions:- ")
        self.label1.setObjectName("label1")

        self.partCount = QtWidgets.QLabel(self.centralwidget)
        self.partCount.setGeometry(QtCore.QRect(240, 550, 81, 51))
        self.partCount.setText("")
        self.partCount.setObjectName("partCount")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.genButton.setText(_translate("MainWindow", "Generate"))

    def setCount(self): 
        txt = str(self.ansList.count())
        self.partCount.setText(txt)
        pass


    def genListValues(self):
        text = self.inputNo.text() 
        try: 
            toPart = int(text)
            print(toPart)  

            listVal = parts.getPartitions(toPart)
            
            self.ansList.clear()
            list_string = map(str, listVal) 
            self.ansList.addItems(list_string)

            self.setCount() 

        except ValueError: 
            print("handle string error") 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


#a = int(input("Enter the number u want to partion:- "))
#ans = parts.getPartitions(a) 
#print(len(ans))

