"""
@autor: MBI
Description: Script to development of Model View Architecture

The MVC pattern splits the interface into the following components —
• Model holds the data structure which the app is working with.
• View is any representation of information as shown to the user, whether
graphical or tables. Multiple views of the same data are allowed.
• Controller accepts input from the user, transforms it into commands and
applies these to the model or view.

The two parts are essentially responsible for —
1. The model stores the data, or a reference to it and returns individual or
ranges of records, and associated metadata or display instructions.
2. The view requests data from the model and displays what is returned on
the widget

Role                 Value         Description
Qt.DisplayRole       0             The key data to be rendered in the form of text. QString
Qt.DecorationRole    1             The data to be rendered as a decoration in the form of an icon. QColor, QIcon or QPixmap
Qt.EditRole          2             The data in a form suitable for editing in an editor. QString
Qt.ToolTipRole       3             The data displayed in the item’s tooltip. QString
Qt.StatusTipRole     4             The data displayed in the status bar. QString
Qt.WhatsThisRole     5             The data displayed for the item in  "What’s This?" mode. QString
Qt.SizeHintRole      13            The size hint for the item that will be supplied to views. QSize

"""
#==== Packages ====#
import sys,json
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import Qt 
from MainWindow import Ui_MainWindow

#==== Class ====#

tick = QtGui.QImage('Model_View_Architecture\\tick.png')

class TodoModel(QtCore.QAbstractListModel):
    def __init__(self,todos=None) -> None:
        super().__init__()
        self.todos = []
    
    def data(self,index,role) -> str:
        if role  == Qt.DisplayRole:
            _,text = self.todos[index.row()]
            return text
        
        if role == Qt.DecorationRole:
            status,_ = self.todos[index.row()]
            if status:
                return tick
    
    def rowCount(self,index) -> int:
        return len(self.todos)
    

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.load()
        self.todoView.setModel(self.model)
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)
    
    def add(self) -> None:
        text = self.todoEdit.text()
        text = text.strip()
        if text:
            self.model.todos.append((False,text))
            self.model.layoutChanged.emit()
            self.todoEdit.setText("")
            #self.save()
    
    def delete(self) -> None:
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.todoView.clearSelection()
            self.save()
    
    def complete(self) -> None:
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status,text = self.model.todos[row]
            self.model.todos[row] = (True,text)
            self.model.dataChanged.emit(index,index)
            self.todoView.clearSelection()
            self.save()
    
    def load(self) -> None:
        try:
            with open('data.json', 'r') as f:
                self.model.todos = json.load(f)
            f.close()
        except Exception:
            pass
    
    def save(self) -> None:
        try:
            with open('data.json', 'w') as f:
                json.dump(self.model.todos,f)
            f.close()
        except Exception:
            pass


#==== Main ====#
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()