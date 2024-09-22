__author__ = 'MBI'
__doc__ = 'Stopping a running QRunner'

#==== Packages ====#
import sys,time 
from PyQt5.QtCore import QObject,QRunnable,Qt,QThreadPool,pyqtSignal,pyqtSlot 
from PyQt5.QtWidgets import (QApplication,QHBoxLayout,QMainWindow,QProgressBar,
QPushButton,QWidget)
#==== Class ====#

class WorkerKilledException(Exception):
    pass 

class WorkerSignals(QObject):
    progress = pyqtSignal(int)

class JobRunner(QRunnable):
    signals = WorkerSignals()
    def __init__(self) -> None:
        super().__init__()
        self.is_killed = False
    
    @pyqtSlot()
    def run(self) -> None:
        try:
            for n in range(100):
                self.signals.progress.emit(n + 1)
                time.sleep(0.1)
                if self.is_killed:
                    raise WorkerKilledException 
        except WorkerKilledException:
            pass
    
    def kill(self) -> None:
        self.is_killed = True

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        w = QWidget()
        l = QHBoxLayout()
        w.setLayout(l)

        btn_stop = QPushButton('STOP')
        l.addWidget(btn_stop)

        self.setCentralWidget(w)
        
        self.status = self.statusBar()
        self.progress = QProgressBar()
        self.status.addPermanentWidget(self.progress)

        self.threadpool = QThreadPool()

        self.runner = JobRunner()
        self.runner.signals.progress.connect(self.update_progress)
        self.threadpool.start(self.runner)

        btn_stop.pressed.connect(self.runner.kill)
    
    def update_progress(self,n) -> None:
        self.progress.setValue(n)

#==== Main ====#
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

