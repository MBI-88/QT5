__author__ = 'MBI'
__doc__ = """Script to plot use pandas in Qt

DataFrame.plot(
    x=None, y=None, kind='line', ax=None, subplots=False,
    sharex=None, sharey=False, layout=None, figsize=None,
    use_index=True, title=None, grid=None, legend=True, style=None,
    logx=False, logy=False, loglog=False, xticks=None, yticks=None,
    xlim=None, ylim=None, rot=None, fontsize=None, colormap=None,
    table=False, yerr=None, xerr=None, secondary_y=False,
    sort_columns=False, **kwargs)
"""
#==== Packages ====#
import sys 
from PyQt5 import QtCore,QtWidgets
import matplotlib
import pandas as pd 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg,NavigationToolbar2QT
from matplotlib.figure import Figure

#==== Classes ====#
matplotlib.use('Qt5Agg')

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self,parent=None,width=5,height=4,dpi=100) -> None:
        fig = Figure(figsize=(width,height),dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class MainWindowPandas(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        sc = MplCanvas(self,width=5,height=4,dpi=100)
        df = pd.DataFrame(
            [[0,10],[5,15],[2,20],[15,25],[4,10]],columns=['A','B']
        )
        df.plot(ax=sc.axes)
        toolbar = NavigationToolbar2QT(sc,self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(sc)
        layout.addWidget(toolbar)

        widgets = QtWidgets.QWidget()
        widgets.setLayout(layout)

        self.setCentralWidget(widgets)


#==== Main ====#
app = QtWidgets.QApplication(sys.argv)
window = MainWindowPandas()
window.show()
app.exec_()

