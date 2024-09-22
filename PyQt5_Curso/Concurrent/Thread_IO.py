__author__ = 'MBI'
__name__ = 'Thread_IO'
__doc__ = 'Script to use threading IO'
#==== Packages ====#
import sys,random,time
from PyQt5.QtCore import QObject,QRunnable,QThreadPool,QTimer,pyqtSignal,pyqtSlot 
from PyQt5.QtWidgets import (QApplication,QLabel,QMainWindow,QPushButton,QVBoxLayout,QWidget)
#==== Class ====#

class WorkerSignal(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(dict)

class Worker(QRunnable): 
    def __init__(self,iterations:int) -> None:
        super().__init__()
        self.signals = WorkerSignal()
        self.iterations = iterations
    
    @pyqtSlot()
    def run(self) -> None:
        try:
            for n in range(self.iterations):
                time.sleep(0.01)
                v = 5 / (40 - n)
        except Exception as e:
            self.signals.error.emit(str(e))
        
        else:
            self.signals.finished.emit()
            self.signals.result.emit({'n':n,'value':v})

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.threadpool = QThreadPool()
        print('Multithreading with maximun %d threads' % self.threadpool.maxThreadCount())

        self.counter = 0
        layout = QVBoxLayout()
        self.label = QLabel('Start')
        btn = QPushButton('DANGER!')
        btn.pressed.connect(self.oh_no)

        layout.addWidget(self.label)
        layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
    
    def oh_no(self) -> None:
        worker = Worker(iterations=random.randint(10,50))
        worker.signals.result.connect(self.worker_output)
        worker.signals.finished.connect(self.worker_complete)
        worker.signals.error.connect(self.worker_error)
        self.threadpool.start(worker)

    def worker_output(self,s) -> None:
        print('RESULT',s)
    
    def worker_complete(self) -> None:
        print('THREAD COMPLETE')
    
    def worker_error(self,t) -> None:
        print('ERROR: %s' % t)
    
    def recurring_timer(self) -> None:
        self.counter += 1
        self.label.setText('Counter: %d' % self.counter)

#==== Main ====#
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()