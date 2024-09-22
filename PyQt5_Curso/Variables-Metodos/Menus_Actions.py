"""
@autor: MBI
Description: Script for develop of Menus and Actions
"""
#==== Package ===#
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (QMenu,QMainWindow,QLabel,QAction,QCheckBox,
QStatusBar,QApplication, QToolBar)

#==== Class ====#
class MainMenu(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16,16))
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(toolbar)
        # & : es una llave rapida para saltar por los menu creados
        button_action = QAction(QIcon('plus.png'),'Your button',self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolButton)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()
        
        button_action2 = QAction(QIcon('puzzle.png'),'Your button2',self)
        button_action2.triggered.connect(self.onMyToolButton)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())

        menu = self.menuBar()
        file_menu = menu.addMenu('&File')
        file_menu.addAction(button_action)
    
    def onMyToolButton(self,z) -> None:
        print('clicked ',z)

class MainMenu2(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16,16))
        toolbar.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.addToolBar(toolbar)
        # & : es una llave rapida para saltar por los menu creados
        button_action = QAction(QIcon('plus.png'),'&Your button',self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolButton)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()
        
        button_action2 = QAction(QIcon('puzzle.png'),'&Your button2',self)
        button_action2.setStatusTip('This is your button2')
        button_action2.triggered.connect(self.onMyToolButton)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())

        menu = self.menuBar()
        file_menu = menu.addMenu('&File')
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)
    
    def onMyToolButton(self,z) -> None:
        print('clicked ',z)

class MainSubMenu(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16,16))
        toolbar.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.addToolBar(toolbar)
        # & : es una llave rapida para saltar por los menu creados
        button_action = QAction(QIcon('plus.png'),'&Your button',self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolButton)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()
        
        button_action2 = QAction(QIcon('puzzle.png'),'&Your button2',self)
        button_action2.setStatusTip('This is your button2')
        button_action2.triggered.connect(self.onMyToolButton)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())

        menu = self.menuBar()
        file_menu = menu.addMenu('&File')
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_submenu = file_menu.addMenu('Submenu')
        file_submenu.addAction(button_action2)
    
    def onMyToolButton(self,z) -> None:
        print('clicked ',z)

class MainShorcut(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16,16))
        toolbar.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.addToolBar(toolbar)
      
        button_action = QAction(QIcon('plus.png'),'&Your button',self)
        button_action.setStatusTip('This is your button')
        button_action.setShortcut(QKeySequence('Ctrl+p'))
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()
        
        button_action2 = QAction(QIcon('puzzle.png'),'&Your button2',self)
        button_action2.setStatusTip('This is your button2')
        button_action2.triggered.connect(self.onMyToolButton)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())
        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        file_menu = menu.addMenu('&File')
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_submenu = file_menu.addMenu('Submenu')
        file_submenu.addAction(button_action2)
    
    def onMyToolButton(self,z) -> None:
        print('clicked ',z)



#==== Main ====#
app = QApplication(sys.argv)
#window = MainMenu()
#window = MainMenu2()
#window = MainSubMenu()
window = MainShorcut()
window.show()
app.exec_()
