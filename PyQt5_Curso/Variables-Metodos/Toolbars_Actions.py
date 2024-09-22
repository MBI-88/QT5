"""
@autor: MBI
Description: Script for develop of Toolbars and Actions

Flag                                 Behavior
Qt.ToolButtonIconOnly                Icon only, no text
Qt.ToolButtonTextOnly                Text only, no icon
Qt.ToolButtonTextBesideIcon          Icon and text, with text beside the icon
Qt.ToolButtonTextUnderIcon           Icon and text, with text under the icon
Qt.ToolButtonIconOnly                Icon only, no text
Qt.ToolButtonFollowStyle             Follow the host desktop style
"""
#==== Package ====#
import sys
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QCheckBox, QToolBar,QLabel,QApplication,QMainWindow
,QAction,QStatusBar)
#==== Class ====#

class MainToolbar(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        self.addToolBar(toolbar)
    
    def onMyToolBarButtonClick(self,s):
        print('click ',s)


class MainAction(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        self.addToolBar(toolbar)

        button_action = QAction('Your button',self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)
    
    def onMyToolBarButtonClick(self,s):
        print('click',s)

class MainStatusBar(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')

        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        self.addToolBar(toolbar)

        button_action = QAction('Your button',self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolbarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))
    
    def onMyToolbarButtonClick(self,s) -> None:
        print('click',s)

class MainIcon(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('plus.png'),'Your button',self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))
    
    def onMyToolBarButtonClick(self,s) -> None:
        print('clicked',s)

class Main2Buttons(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16,16))
        toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon) # Cambinado el estilo de toolbar
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('puzzle.png'),'Your button',self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon('plus.png'),'Your button2',self)
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))
    
    def onMyToolBarButtonClick(self,s) -> None:
        print('clicked ',s)





#==== Main ====#

app = QApplication(sys.argv)
#window = MainToolbar()
#window = MainAction()
#window = MainStatusBar()
#window = MainIcon()
window = Main2Buttons()
window.show()
app.exec_()
