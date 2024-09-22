"""
@autor: MBI
Description: Script for loading a .ui file

If you’re not a designer, it can be hard to create beautiful interfaces, or
even know what they are. Thankfully there are simple rules you can
follow to create interfaces that, if not beautiful at least won’t be ugly
The key concepts are — alignment, groups and space.
Alignment is about reducing visual noise. Think of the corners of
widgets as alignment points and aim to minimize the number of
unique alignment points in the UI. In practice, this means making sure
the edges of elements in the interface line up with one another.
Figure 84. The effect of alignment of interface clarity.

If you have differently sized inputs, align the edge you
read from. English is a left-to-right language, so if your
app is in English align the left.
Groups of related widgets gain context making them easier to
understand. Structure your interface so related things are found
together.
Space is key to creating visually distinct regions in your
interface — without space between groups, there are no groups! Keep
spacing consistent and meaningful.
"""
#==== Packages ====#
from PyQt5 import QtWidgets,uic
import sys,random
from PyQt5.QtCore import Qt
from MainWindows import Ui_MainWindow

#==== Class ====#
class MainWindow(QtWidgets.QMainWindow,uic.loadUiType('Qt_Disigner\\MainWindows.ui')[0]):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('MainWindow Title')

class MainWindowsUI(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args,obj=None,**kwargs) -> None:
        super(MainWindowsUI,self).__init__(*args,**kwargs)
        self.setupUi(self)

class MainWindowsUi(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        f = self.label.font()
        f.setPointSize(25)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.pushButton.pressed.connect(self.update_label)
        
    
    def update_label(self) -> None:
        n = random.randint(1,6)
        self.label.setText("%d"% n)
    

#==== Main ====#
app = QtWidgets.QApplication(sys.argv)
#window = MainWindow()
#window = MainWindowsUI()
window = MainWindowsUi()
window.show()
app.exec_()

