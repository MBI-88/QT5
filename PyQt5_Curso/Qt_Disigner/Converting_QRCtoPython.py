"""
@autor: MBI
Description: Script for development of qrc file and convertion
Conmands:
pyrcc5  for converting qrc to python file
"""
#==== Packages ====#
import sys
from PyQt5 import QtGui,QtWidgets
import icon_py

#==== Class ====#
class MainWindosQRC(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Hello World')

        b = QtWidgets.QPushButton('My Button')
        icon = QtGui.QIcon(':/iconfile/230.ico')
        b.setIcon(icon)
        self.setCentralWidget(b)
        self.show()

#==== Main ====#
app = QtWidgets.QApplication(sys.argv)
window = MainWindosQRC()
app.exec_()