"""
@autor: MBI
Description: Script to develop QTableView

Type of control values expected

Role                   Type
Qt.BackgroundRole      QBrush (also QColor)
Qt.CheckStateRole      Qt.CheckState
Qt.DecorationRole      QIcon, QPixmap, QColor
Qt.DisplayRole         QString (also int, float, bool)
Qt.FontRole            QFont
Qt.SizeHintRole        QSize
Qt.TextAlignmentRole   Qt.Alignment
Qt.ForegroundRole      QBrush (also QColor)

"""
#==== Pacakes ====#
import sys 
from datetime import datetime
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore import Qt
import numpy as np
import pandas as pd

#==== Class ====#

COLORS:list[str] = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0',
'#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f',]

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self,data) -> None:
        super().__init__()
        self._data = data
    
    def data(self,index,role) -> str:
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            return value
            
        
    def rowCount(self,index) -> int:
        return len(self._data)
    
    def columnCount(self,index) -> int:
        return len(self._data[0])

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.table = QtWidgets.QTableView()
        data:list[int] = [
            [4,8,2],
            [1,1,20],
            [2,5,10],
            [3.025,3,3],
            [7,8,9]
        ]
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)



class TableMultiData(QtCore.QAbstractTableModel):
    def __init__(self,data) -> None:
        super().__init__()
        self._data = data
    
    def data(self,index,role) -> str:
        # Qt.DisplayRole
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
           
            if isinstance(value,datetime):
                return value.strftime("%Y-%m-%d")
            
            elif isinstance(value,float):
                return "%.2f"% value
            
            elif isinstance(value,str):
                return '"%s"' % value

            return value

        # Qt.BackgroundRole
        elif role == Qt.BackgroundRole and index.column() == 2:
            return QtGui.QColor(Qt.blue)
        
        # Qt.TextAlignmentRole
        elif role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value , int) or isinstance(value, float):
                return Qt.AlignVCenter | Qt.AlignCenter

        
        # Qt.ForegroundRole
        elif role == Qt.ForegroundRole:
            value = self._data[index.row()][index.column()]
            if (isinstance(value,int) or isinstance(value,float)) and value < 0:
                return  QtGui.QColor('red')
        
        elif role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value,datetime):
                return QtGui.QIcon("Model_View_Architecture\\ice-cream-sprinkles.png")
            if isinstance(value,bool):
                if value:
                    return QtGui.QIcon("Model_View_Architecture\\tick.png")
                return QtGui.QIcon('Model_View_Architecture\\cross.png')

            if isinstance(value,int)  or isinstance(value,float):
                value = int (value)
                value = max(-5,value)
                value = min(5,value)
                value = value + 5
                return QtGui.QColor(COLORS[value])        

        
    
    def rowCount(self,index) -> int:
        return len(self._data)
    
    def columnCount(self,index) -> int:
        return len(self._data[0])


class MainWindowMultiData(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.table = QtWidgets.QTableView()
        data:list[int] = [
            [True,8,2],
            [1,-1,"hello"],
            [2,5,datetime(2021,10,10)],
            [3.025,3,False],
            [7,8,9]
        ]
        self.model = TableMultiData(data)
        self.table.setModel(self.model)
        self.setGeometry(500,500,350,250)
        self.setCentralWidget(self.table)

# Using Numpy

class TableModelNumpy(QtCore.QAbstractTableModel):
    def __init__(self,data) -> None:
        super().__init__()
        self._data = data
    
    def data(self,index,role) -> str:
        if role == Qt.DisplayRole:
            value = self._data[index.row(),index.column()]
            return str(value)
        
    def rowCount(self,index) -> int:
        return self._data.shape[0]
        
    def columnCount(self,insex) -> int:
        return self._data.shape[1]

class MainWindowNumpy(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.table = QtWidgets.QTableView()
        data = np.array([[1,2,9], [1,0,-1], [3,2,5], [3,3,2], [5,8,9]],dtype=np.int32)
        self.model = TableModelNumpy(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)
        self.setGeometry(600,100,400,200)

# Using Pandas

class TableModelPandas(QtCore.QAbstractTableModel):
    def __init__(self,data) -> None:
        super().__init__()
        self._data = data
    
    def data(self,index,role:int) -> str:
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(),index.column()]
            return str(value)

        elif role == Qt.TextAlignmentRole:
            value = self._data.iloc[index.row(),index.column()]
            
            if isinstance(value,np.int64):
                return Qt.AlignVCenter | Qt.AlignRight
        
        elif role == Qt.DecorationRole:
            value = self._data.iloc[index.row(),index.column()]

            if isinstance(value,np.int64):
                value = int(value)
                return QtGui.QColor(COLORS[value])
        
    def rowCount(self,index) -> int:
        return self._data.shape[0]
        
    def columnCount(self,insex) -> int:
        return self._data.shape[1]
    
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> str:
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            
            if orientation == Qt.Vertical:
                return str(self._data.index[section])

           

class MainWindowsPandas(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.table = QtWidgets.QTableView()
        data = pd.DataFrame(
            [[1,9,2],[1,0,-1],[3,5,2],[3,3,2],[5,8,9]],
            columns=['A','B','C'],
            index=['Row 1','Row 2','Row 3','Row 4','Row 5']
        )
        self.model = TableModelPandas(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)
        self.setGeometry(600,100,400,200)



#==== Main ====#
app = QtWidgets.QApplication(sys.argv)
#window = MainWindow()
#window = MainWindowMultiData()
#window = MainWindowNumpy()
window = MainWindowsPandas()
window.show()
app.exec_()

