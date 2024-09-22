__author__ = 'MBI'
__doc__ = 'Paussing a runner'
#==== Class ====#
import sys,time 
from PyQt5.QtCore import QObject,QRunnable,Qt,QThreadPool,pyqtSignal,pyqtSlot 
from PyQt5.QtWidgets import (QApplication,QMainWindow,QHBoxLayout,QProgressBar,QPushButton,
QWidget)
#==== Class ====#

class WorkerKilledException(Exception):
    pass 

class WorkerSignals(QObject):
    progress = pyqtSignal(int)

class JobRunner(QRunnable):
    signal = WorkerSignals()
    def __init__(self) -> None:
        super().__init__()

        self.is_paused = False
        self.is_killled = False 
    
    @pyqtSlot()
    def run(self) -> None:
        for n in range(100):
            self.signal.progress.emit(n + 1)
            time.sleep(0.1)

            while self.is_paused:
                time.sleep(0)
            
            if self.is_killled:
                raise WorkerKilledException 
    
    def pause(self) -> None:
        self.is_paused = True
    
    def resume(self) -> None:
        self.is_paused = False
    
    def kill(self) -> None:
        self.is_killled = True

class Mainwindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        w = QWidget()
        l = QHBoxLayout()
        w.setLayout(l)

        btn_stop = QPushButton('STOP')
        btn_pause = QPushButton('PAUSE')
        btn_resume = QPushButton('RESUME')

        l.addWidget(btn_stop)
        l.addWidget(btn_pause)
        l.addWidget(btn_resume)

        self.setCentralWidget(w)

        self.status = self.statusBar()
        self.progress = QProgressBar()
        self.status.addPermanentWidget(self.progress)

        self.threadpool = QThreadPool()

        self.runner = JobRunner()
        self.runner.signal.progress.connect(self.update_progress)
        self.threadpool.start(self.runner)

        btn_stop.pressed.connect(self.runner.kill)
        btn_pause.pressed.connect(self.runner.pause)
        btn_resume.pressed.connect(self.runner.resume)

    
    def update_progress(self,n) -> None:
        self.progress.setValue(n)

#==== Main ====#
app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec_()

