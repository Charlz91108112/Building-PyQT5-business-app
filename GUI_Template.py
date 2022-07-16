from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from os import path
from PyQt5.uic import loadUiType
import sqlite3
import time
FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), 'main.ui'))

class Main(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

    def Handle_Buttons(self):
        pass


def main():
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()