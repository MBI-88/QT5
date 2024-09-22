"""
@autor: MBI
Description: Script for make windows in separate threads
"""
#==== Packages ====#
import sys
from PyQt5.QtWidgets import (QApplication,QLabel,QMainWindow,QPushButton,QVBoxLayout,QWidget)
from random import randint
#==== Class ====#

class AnotherWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My Second Window')
        layout = QVBoxLayout()
        self.label = QLabel('Another Window {}'.format(randint(0,100)))
        layout.addWidget(self.label)
        self.setLayout(layout)

# Cerrando ventanas
class MainWindo(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.w = None
        self.button = QPushButton('Push for Window')
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)
    
    def show_new_window(self,checked) -> None:
        if self.w is None:
            self.w = AnotherWindow() # para que sea persistente se debe usar self , haciendo referencia al padre
            self.w.show()
        else:
            self.w.close() # para asegurar que la ventana se cierre
            self.w = None # se descarta la referencia y se cierra la ventana

# Ventanas persistentes
class MainWindow2(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.w = AnotherWindow()
        self.button = QPushButton('Push for Window')
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)
    
    def show_new_window(self,checked) -> None:
        self.w.show()

# Mostrando y ocultando ventanas
class MainWidow3(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.w = AnotherWindow()
        self.button = QPushButton('Push for Window')
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)
    
    def toggle_window(self,checked) -> None:
        if self.w.isVisible(): self.w.hide()
        else:
            self.w.show()




#==== Main ====#
app = QApplication(sys.argv)
#window = MainWindo()
#window = MainWindow2()
window = MainWidow3()
window.show()
app.exec_()