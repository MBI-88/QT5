"""
@autor: MBI
Description: Script to customize signal
"""
#==== Package ====#
import sys
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLineEdit,QPushButton,
                            QVBoxLayout,QHBoxLayout,QWidget,QLabel)

#==== Class ====#

class MainWidowSignal(QMainWindow):
    message = pyqtSignal(str)
    value = pyqtSignal(int,str,int)
    another = pyqtSignal(list)
    onemore = pyqtSignal(dict)
    anything = pyqtSignal(object)

    def  __init__(self) -> None:
        super().__init__()

        self.message.connect(self.custom_slot)
        self.value.connect(self.custom_slot)
        self.another.connect(self.custom_slot)
        self.onemore.connect(self.custom_slot)
        self.anything.connect(self.custom_slot)

        self.message.emit('my message')
        self.value.emit(23,'abc',1)
        self.another.emit([1,2,3,4,5])
        self.onemore.emit({'a':2,'b':7})
        self.anything.emit(1223)

    def custom_slot(self,a) -> None:
        print(a)

class MainWindowForwSignal(QMainWindow):
    message = pyqtSignal(str)
    def __init__(self) -> None:
        super().__init__()
        self.message.connect(self.my_custom_fn)

        le = QLineEdit('Enter some text')
        le.textChanged.connect(self.message.emit)

        self.setCentralWidget(le)
        self.setGeometry(1200,300,200,200)
    
    def my_custom_fn(self,a) -> None:
        print(a)

# Intercepting the signal

class MainWindowIntSignal(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        btn = QPushButton('Press me')
        btn.setCheckable(True)
        btn.clicked.connect(lambda chechked: self.button_clicked(chechked,btn))

        self.setCentralWidget(btn)
        self.setGeometry(1200,300,200,200)
    
    def button_clicked(self,chechked,btn) -> None:
        print(btn,chechked)
        btn.hide()

# Problems with loops

class MainWindowSignalLoop(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        for a in range(10):
            btn = QPushButton(str(a))
            # Solution use named parameters in intermediate functions (a = a)
            btn.clicked.connect(lambda chechked,a=a: self.button_clicked(a))
            h_layout.addWidget(btn)
        
        v_layout.addLayout(h_layout)
        self.label = QLabel("")
        v_layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)
    
    def button_clicked(self,n) -> None:
        self.label.setText(str(n))

# Examples of use intermediate functions

class MainWindowSigExamples(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.windowTitleChanged.connect(self.on_window_title_changed)
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x,25))

        self.setWindowTitle('This will trigger all th signals')
    
    def on_window_title_changed(self,s:str) -> None:
        print(s)
    
    def my_custom_fn(self,a:str = 'Hello!',b:int = 5) -> None:
        print(a,b)



#==== Main ====#
app = QApplication(sys.argv)
#window = MainWidowSignal()
#window = MainWindowForwSignal()
#window = MainWindowIntSignal()
#window = MainWindowSignalLoop()
window = MainWindowSigExamples()
window.show()
app.exec_()
