__author__ = 'MBI'
__doc__ = """Script to plotting data

Color                    Letter_code
blue                     b
green                    g
red                      r
cyan (bright blue-green) c
magenta (bright pink)    m
yellow                   y
black                    k
white                    w

In addition to these single letter codes, you can also set colors using hex
notation eg. #672922 as a string.

The standard Qt line styles can all be used, including Qt.SolidLine, Qt.DashLine,
Qt.DotLine, Qt.DashDotLine and Qt.DashDotDotLine

Variable Marker Type
o        Circular
s        Square
t        Triangular
d        Diamond
+        Cross

Style         Type
color         (str) e.g. 'CCFF00'
size          (str) e.g. '8pt'
bold          (bool) True or False
italic        (bool) True or False
"""

#==== Package ===#
import sys
from random import randint
from PyQt5 import QtWidgets,QtGui,QtCore
import pyqtgraph as pg

#==== Classes ====#

styles:dict[str,str] = {'color':'r','font-size':'20pt'}

class MainWindowPlot(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour:list[int] = [1,2,3,4,5,6,7,8,9,10]
        temperature:list[int] = [30,32,34,32,33,31,29,32,35,45]

        #self.graphWidget.setBackground('w')
        #self.graphWidget.setBackground((100,50,255)) # RGB
        #self.graphWidget.setBackground((100,50,255,25)) # RGBA
        #self.graphWidget.setBackground(QtGui.QColor(100,50,254,20))
        color = self.palette().color(QtGui.QPalette.Window)  # get the default window background
        self.graphWidget.setBackground(color)
        pen = pg.mkPen(color=(255,0,0),width=10,style=QtCore.Qt.DashLine)
        #self.graphWidget.plot(hour,temperature)
        self.graphWidget.setTitle('Plotting Graph',color='r',size='20pt',bolt=True)
        #self.graphWidget.setLabel('left','Temperatue (C)',**styles)
        #self.graphWidget.setLabel('bottom','Hour (H)',**styles)
        self.graphWidget.setLabel('left',"<span style=\"color:red;font-size:20px\">Temperature(C)</span>")
        self.graphWidget.setLabel('bottom',"<span style=\"color:red;font-size:20px\">Hour(H)</span>")
        self.graphWidget.addLegend()
        self.graphWidget.showGrid(x=True,y=True)
        self.graphWidget.setXRange(0,20,padding=0)
        self.graphWidget.setYRange(20,55,padding=0)
        self.graphWidget.plot(hour,temperature,name='Sensor1',pen=pen,symbol='+',symbolSize=20,symbolBrush=('b'))
        
# Multi-Plotting
class MainWidnowMultPlot(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour:list[int] = [1,2,3,4,5,6,7,8,9,10]
        temperature_1:list[int] = [30,32,34,32,33,31,29,32,35,45]
        temperature_2:list[int] = [50,35,44,22,38,32,27,38,32,44]

        self.graphWidget.setBackground('w')
        self.graphWidget.setTitle('Multi-Plotting',color='b',size='20pt')
        self.graphWidget.setLabel('left','Temperature(C)',**styles)
        self.graphWidget.setLabel('bottom','Hour(H)',**styles)

        self.graphWidget.addLegend()
        self.graphWidget.showGrid(x=True,y=True)
        self.graphWidget.setXRange(0,10,padding=0)
        self.graphWidget.setYRange(20,55,padding=0)

        self.plot(hour,temperature_1,'Sensor1','r')
        self.plot(hour,temperature_2,'Sensor2','b')
    
    def plot(self,x:list[int],y:list[int],plotname:str,color:str) -> None:
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x,y,name=plotname,pen=pen,symbol='o',symbolSize=10,symbolBrush=(color))
        #self.graphWidget.clear() # clearing de data

# Updating a plot
class MainwindowUpd(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(100))
        self.y = [randint(0,100) for _ in range(100)]

        self.graphWidget.setBackground('w')
        
        pen = pg.mkPen(color=(255,0,0))
        self.data_line = self.graphWidget.plot(self.x,self.y,pen=pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self) -> None:
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)
        
        self.y = self.y[1:]
        self.y.append(randint(0,100))
        
        self.data_line.setData(self.x,self.y)

#==== Main ====#
app = QtWidgets.QApplication(sys.argv)
#window = MainWindowPlot()
#window = MainWidnowMultPlot()
window = MainwindowUpd()
window.show()
app.exec_()