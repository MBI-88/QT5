"""
@autor: MBI
Descripcion: Script para el desarrollo del diseño de ventanas
Layouts adcequibles en PyQt5:
Layout        Behavior
QHBoxLayout Linear horizontal layout
QVBoxLayout Linear vertical layout
QGridLayout In indexable grid XxY
QStackedLayout Stacked (z) in front of one another
"""
#==== Package ====#
import sys
from PyQt5.QtGui import QColor,QPalette
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget,
QStackedLayout,QGridLayout,QPushButton,QTabWidget)

#==== Class ====#
class Color(QWidget):
    def __init__(self,color) -> None:
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)

class MainColorWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My app')
        widget = Color('red')
        self.setCentralWidget(widget)

class MainLayoutV(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        layout = QVBoxLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
     

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class MainLayoutH(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My app')
        layout = QHBoxLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('green'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class MainLayoutComplex(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        
        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)
        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout3)
        layout1.setContentsMargins(2,2,2,2)
        #layout1.setSpacing(20)

        widgets = QWidget()
        widgets.setLayout(layout1)

        self.setCentralWidget(widgets)

class MainLayoutGrid(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        layout = QGridLayout()
        layout.addWidget(Color('red'),0,0)
        layout.addWidget(Color('green'),1,0)
        layout.addWidget(Color('blue'),1,1)
        layout.addWidget(Color('purple'),2,1)
        layout.setSpacing(10)

        widgets = QWidget()
        widgets.setLayout(layout)
        self.setCentralWidget(widgets)

class MainStackedLayout(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        layout = QStackedLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('yellow'))

        layout.setCurrentIndex(3)

        widgets = QWidget()
        widgets.setLayout(layout)
        self.setCentralWidget(widgets)

# Ejemplo de uso practico
class MainEg1(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        btn = QPushButton('red')
        btn.pressed.connect(self.activate_tab1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('red'))

        btn = QPushButton('green')
        btn.pressed.connect(self.activate_tab2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('green'))

        btn = QPushButton('yellow')
        btn.pressed.connect(self.activate_tab3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('yellow'))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab1(self) -> None:
        self.stacklayout.setCurrentIndex(0)
    def activate_tab2(self) -> None:
        self.stacklayout.setCurrentIndex(1)
    def activate_tab3(self) -> None:
        self.stacklayout.setCurrentIndex(2)

# Ejemplo practico con Tab
class MainEg2(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)
        
        for color in ['red','green', 'blue','yellow']:
            tabs.addTab(Color(color),color)
        
        self.setCentralWidget(tabs)


        
#==== Main ====#
app = QApplication(sys.argv)
#window = MainColorWidget()
#window = MainLayoutV()
#window = MainLayoutH()
#window = MainLayoutComplex()
#window = MainLayoutGrid()
#window = MainStackedLayout()
#window = MainEg1()
window = MainEg2()
window.show()
app.exec_()


