import pt as parts 
from  PyQt5 import QtWidgets 
import sys 

def window():
    app = QtWidgets.QApplication(sys.argv) 
    win = QtWidgets.QMainWindow()
    win.setGeometry(200,200,300,300) 
    win.setWindowTitle("Hello World")

    label = QtWidgets.QLabel(win)
    label.setText("hi there")
    label.move(50,50)
    
    win.show() 
    sys.exit(app.exec_())


window()

#a = int(input("Enter the number u want to partion:- "))
#ans = parts.getPartitions(a) 
#print(len(ans))

