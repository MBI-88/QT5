"""
@autor: MBI
Description: Script to development Routing
"""
#==== Packages ====#

from PyQt5.QtCore import QSize,Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QLabel,QMainWindow
import sys

#==== Class ====#

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = QLabel('Click in this window')
        self.status = self.statusBar()
        self.setFixedSize(QSize(200,100))
        self.setCentralWidget(self.label)
    
    def mouseMoveEvent(self, a0:QtGui.QMouseEvent) -> None:
        self.label.setText('mouseMoveEvent')
    
    def mousePressEvent(self, a0:QtGui.QMouseEvent) -> None:
        button = a0.button()
        if button == Qt.LeftButton:
            self.label.setText('mousePressEvent left')
            if a0.x() < 100:
                self.status.showMessage('Left click on left')
                self.move(self.x() - 10,self.y())
            else:
                self.status.showMessage('Lef click on right')
                self.move(self.x() + 10,self.y())
        
        elif button == Qt.MiddleButton:
            self.label.setText('mousePressEvent Middle')
        
        elif button == Qt.RightButton:
            self.label.setText('mousePressEvent right')
            if a0.x() < 100:
                self.status.showMessage('Right click on left')
                print('Something else here')
        
        else: 
            self.status.showMessage('Right click on right')


# Routing dictionaries

class MainWindowRouteDic(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = QLabel('Click in this window')
        self.status = self.statusBar()
        self.setFixedSize(QSize(200,200))
        self.setCentralWidget(self.label)
    
    def mousePressEvent(self, a0:QtGui.QMouseEvent) -> object:
        route:dict = {
            Qt.LeftButton: self.left_mousePressEvent,
            Qt.MiddleButton: self.middle_mousePressEvent,
            Qt.RightButton: self.right_mousePressEvent
        } 
        button = a0.button()
        fn = route.get(button) # Usar esta estrategia para evitar eventos no capturados
        if fn: 
            return fn(a0)
        
    
    def left_mousePressEvent(self, a0:QtGui.QMouseEvent) -> None:
        self.label.setText('mousePressEvent left')
        if a0.x() < 100:
            self.status.showMessage('Left click on left')
            self.move(self.x() - 10,self.y())
        else:
            self.status.showMessage('Left click on right')
            self.move(self.x() + 10,self.y())
    
    def middle_mousePressEvent(self, a0:QtGui.QMouseEvent) -> None:
        self.label.setText('mousePressEvent Middle')


    def right_mousePressEvent(self, a0:QtGui.QMouseEvent) -> None:
        if a0.x() < 100:
            self.status.showMessage('Right click on left')
            print('Something else here')
            self.move(10,10)
        else:
            self.status.showMessage('Right click on right')
            self.move(400,400)

    


#==== Main ====#
app = QApplication(sys.argv)
#window = MainWindow()
window = MainWindowRouteDic()
window.show()
app.exec_()
