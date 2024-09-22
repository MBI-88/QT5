"""
@autor: MBI
Description: Script to working command line
"""
#==== Packages ====#
from PyQt5.QtWidgets import QApplication, QTextEdit,QWidget,QLabel,QVBoxLayout,QMainWindow
import sys

#==== Class ===#

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()

        for arg in sys.argv:
            l = QLabel(arg)
            layout.addWidget(l)
        
        self.setLayout(layout)
        self.setWindowTitle('Arguments')

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.editor = QTextEdit()

        if __file__ in sys.argv:
            sys.argv.remove((__file__))
        
        if sys.argv:
            filename = sys.argv[0]
            self.open_file(filename)
        
        self.setCentralWidget(self.editor)
        self.setWindowTitle('Text viewer')
    
    def open_file(self,fn) -> None:
        with open(fn,'r') as f:
            text = f.read()
        self.editor.setPlainText(text)

#==== Main ====#
app = QApplication(sys.argv)
#window = Window()
window = MainWindow()
window.show()
app.exec_()