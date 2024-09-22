__author__ = 'MBI'
__doc__ = 'Use of threading'
#==== Packages ====#
import sys,time,uuid,random 
import pyqtgraph as pg
from PyQt5.QtCore import QObject,QRunnable,QThreadPool,pyqtSignal,pyqtSlot,QTimer
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QProgressBar,QPushButton,
QVBoxLayout,QWidget)
#==== Class =====#
#Ejemple Progress Bar

class WorkerSignal(QObject):
    progressBar = pyqtSignal(str,int)
    finished = pyqtSignal(str)

class Worker(QRunnable):
    def __init__(self,*args,**kwargs)  -> None:
        super().__init__()
        self.arg = args
        self.kwargs = kwargs
        self.job_id = uuid.uuid4().hex # id of worker
        self.signal = WorkerSignal()
    
    @pyqtSlot()
    def run(self) -> None:
        total_n = 100
        delay = random.random() / 100
        for n in range(total_n):
            progresspc = int(100 * float(n + 1)/ total_n)
            self.signal.progressBar.emit(self.job_id,progresspc)
            time.sleep(delay)

        self.signal.finished.emit(self.job_id)


class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        layout = QVBoxLayout()  
        self.progress = QProgressBar()
        btn = QPushButton('START IT UP')
        btn.pressed.connect(self.execute) 

        self.status = QLabel('0 Workers')

        layout.addWidget(self.progress)
        layout.addWidget(btn)
        layout.addWidget(self.status)

        widge = QWidget()
        widge.setLayout(layout)
        self.worker_progress = {}

        self.setCentralWidget(widge)
        self.threadpool = QThreadPool()

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.refresh_progress)
        self.timer.start()
    
    def execute(self) -> None:
        worker = Worker()
        worker.signal.progressBar.connect(self.update_progress) 
        worker.signal.finished.connect(self.cleanup)

        self.threadpool.start(worker)
    
    def update_progress(self,progress) -> None:
        self.progress.setValue(progress)

    def cleanup(self,job_id) -> None:
        if all(w == 100 for w in self.worker_progress.values()):
            self.worker_progress.clear()
        #if job_id in self.worker_progress:
            #del self.worker_progress[job_id]
            self.refresh_progress()
    
    def update_progress(self,job_id,progress) -> None:
        self.worker_progress[job_id] = progress
    
    def calculate_progress(self) -> int:
        if not self.worker_progress:
            return 0
        return sum(v for v in self.worker_progress.values())/len(self.worker_progress)
    
    def refresh_progress(self) -> None:
        progress = self.calculate_progress()
        print(self.worker_progress)
        self.progress.setValue(progress)
        self.status.setText("%d workers" % len(self.worker_progress))


# The Calculator

class WorkerSignals(QObject):
    data = pyqtSignal(tuple)

class Workers(QRunnable):
    def __init__(self) -> None:
        super().__init__()
        self.worker_id = uuid.uuid4().hex
        self.signal = WorkerSignals()
    
    @pyqtSlot()
    def run(self) -> None:
        total_n = 1000
        y2 = random.randint(0,10)
        delay = random.random() / 100
        value = 0 

        for n in range(total_n):
            y = random.randint(0,10)
            value +=  n * y2 - n * y 
            self.signal.data.emit((self.worker_id,n,value))

class MainWindowCalculator(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.threadpool = QThreadPool()

        self.x = {}
        self.y = {}
        self.lines = {}

        layout = QVBoxLayout()
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')
        layout.addWidget(self.graphWidget)

        btn = QPushButton('Create New Worker')
        btn.pressed.connect(self.execute)
        layout.addWidget(btn)

        widgets = QWidget()
        widgets.setLayout(layout)
        
        self.setCentralWidget(widgets)
    
    def execute(self) -> None:
        worker = Workers()
        worker.signal.data.connect(self.receive_data)
        self.threadpool.start(worker)
    
    def receive_data(self,data) -> None:
        worker_id,x,y = data
        if worker_id not in self.lines:
            self.x[worker_id] = [x]
            self.y[worker_id] = [y]
        
            pen = pg.mkPen(
                width=2,color=(
                random.randint(100,255), 
                random.randint(100,255), 
                random.randint(100,255))
            )
            self.lines[worker_id] = self.graphWidget.plot(
                self.x[worker_id],self.y[worker_id],pen=pen
            )
            return None
        
        self.x[worker_id].append(x)
        self.y[worker_id].append(y)
        self.lines[worker_id].setData(self.x[worker_id],self.y[worker_id])






#==== Main ====#
app = QApplication(sys.argv)
#window = MainWindow()
window = MainWindowCalculator()
window.show()
app.exec_()


