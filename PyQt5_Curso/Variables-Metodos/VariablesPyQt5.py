"""
@author: MBI
Descripcion: Scripts introductorio al uso de PyQt5
"""
#==== Package ====#
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMainWindow
import sys
#%%==== Algoritmo ====#
app = QApplication(sys.argv)
window = QWidget()
window.show()
app.exec_()
#%%==== Remplazando QtWidget por QPushbutton ====#
app = QApplication(sys.argv)
window1 = QPushButton('Push me')
window1.show()
app.exec_()

#%%==== Remplazando por QMainWindow ====#
app = QApplication(sys.argv)
window2 = QMainWindow()
window2.show()
app.exec_()
#%%==== Uso de clases ====#
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('May App')
        button = QPushButton('Press Me!')
        self.setFixedSize(400,300) # Reajustando el tamaño de la ventana
        # self.setMinimumSize()
        # self.setMaximumSize()
        self.setCentralWidget(button)

app = QApplication([])
window3 = MainWindow()
window3.show()
app.exec_()

