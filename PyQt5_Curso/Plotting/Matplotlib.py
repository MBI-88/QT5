__author__ = 'MBI'
__doc__ = 'Script to plot using matplotlib in Qt'

#==== Packages ====#
import sys,random
from PyQt5 import QtCore, QtWidgets
import matplotlib
from  matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg,NavigationToolbar2QT
from matplotlib.figure import Figure

#==== Classes ====#
matplotlib.use('Qt5Agg')

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self,parent=None,width=5,height=4,dpi=100) -> None:
        fig = Figure(figsize=(width,height),dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        sc = MplCanvas(self,width=5,height=4,dpi=100)
        sc.axes.plot([0,1,2,3,4],[10,1,20,3,40])
        
        toolbar = NavigationToolbar2QT(sc,self)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

# Updating Plots (Clear and Redraw (slower))
class MainWindowUpdSlow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.canvas = MplCanvas(self,width=5,height=4,dpi=100)
        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0,100) for _ in range(n_data)]

        self.update_plot()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
    
    def update_plot(self) -> None:
        self.ydata = self.ydata[1:] + [random.randint(0,100)]
        self.canvas.axes.cla() # clear the canvas
        self.canvas.axes.plot(self.xdata,self.ydata,'r')
        self.canvas.draw()

# Updating Plots (faster)
class MainWindowUpdFast(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.canvas = MplCanvas(self,5,4,100)
        self.setCentralWidget(self.canvas)
        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0,100) for _ in range(n_data)]

        self._plot_ref = None
        self.update_plot()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self) -> None:
        self.ydata = self.ydata[1:] + [random.randint(0,10)]

        if self._plot_ref is None:
            plot_refs = self.canvas.axes.plot(self.xdata,self.ydata,'r')
            self._plot_ref = plot_refs[0] # retrun a list of plots
        
        else:
            self._plot_ref.set_ydata(self.ydata)
        
        self.canvas.draw()




#==== Main ====#
app = QtWidgets.QApplication(sys.argv)
#window = MainWindow()
#window = MainWindowUpdSlow()
window = MainWindowUpdFast()
window.show()
app.exec_()