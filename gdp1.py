import sys
import os
from gdp import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.othfactrs)
     self.ui.pushButton_2.clicked.connect(self.qda)
     self.ui.pushButton_3.clicked.connect(self.gpc)
     self.ui.pushButton_4.clicked.connect(self.dplot)
     self.ui.pushButton_5.clicked.connect(self.finfactrs)
     self.ui.pushButton_6.clicked.connect(self.gbc)
     self.ui.pushButton_7.clicked.connect(self.rfc)

      

  def othfactrs(self):
    os.system("python other1.py")

  def qda(self):
    os.system("python -W ignore qda1.py")

  def gpc(self):
    os.system("python gpc1.py")

  def dplot(self):
    os.system("python plot1.py")

  def finfactrs(self):  
    os.system("python financial1.py")
	
  def gbc(self):
    os.system("python -W ignore gbc1.py")
	
  def rfc(self):
    os.system("python -W ignore rfc1.py")

       
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
