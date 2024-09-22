__author__ = 'MBI'
__doc__ = 'Script generic for threading'

#==== Packages ====#
import sys,time,traceback
from PyQt5.QtCore import QObject,QRunnable,QThreadPool,QTimer,pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QVBoxLayout,QWidget

#==== Functions ====#

def execute_this_fn(signal) -> str:
    for n in range(5):
        time.sleep(1)
        signal.progress.emit(n * 100 /4)
    
    return 'Done'

#==== Classes ====#

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)

class Worker(QRunnable):
    def __init__(self,fn:object,*args,**kwargs) -> None:
        super().__init__()
        self.fn = fn 
        self.args = args
        self.kwargs = kwargs
        self.signal = WorkerSignals()
        kwargs['signals'] = self.signal
    
    @pyqtSlot()
    def run(self) -> None:
        try:
            result = self.fn(*self.args,**self.kwargs)
        except:
            traceback.print_exc()
            exctype,value = sys.exc_info()[:2]
            self.signal.error.emit((exctype,value,traceback.format_exc()))
        else:
            self.signal.result.emit(result)
        
        finally:
            self.signal.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.counter = 0 
        layout = QVBoxLayout()

        self.label = QLabel('START')
        btn = QPushButton('DANGER!')
        btn.pressed.connect(self.oh_no)

        layout.addWidget(self.label)
        layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.threadpool = QThreadPool()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
    
    def print_output(self,s) -> None:
        print(s)
    
    def thread_complete(self) -> None:
        print('THREAD COMPLETE')
    
    def oh_no(self) -> None:
        worker = Worker(execute_this_fn)
        worker.signal.result.connect(self.print_output)
        worker.signal.finished.connect(self.thread_complete)
        worker.signal.progress.connect(self.progress_fn)

        self.threadpool.start()
    
    def recurring_timer(self) -> None:
        self.counter += 1
        self.label.setText('Counter: %d' % self.counter)
    
    def progress_fn(self,n) -> None:
        print('%d%% done'% n)

#==== Main ====#
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

