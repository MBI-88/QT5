__author__ = 'MBI'
__doc__ = 'Script for development of workers in app'

#==== Packages ====#
import random,sys,time,traceback,uuid
import subprocess as sub 
from PyQt5.QtCore import (QAbstractListModel,QObject,QRect,QRunnable,Qt,QThreadPool,
QTimer,pyqtSignal,pyqtSlot)
from PyQt5.QtGui import QBrush,QColor,QPen
from PyQt5.QtWidgets import (QApplication,QMainWindow,QPlainTextEdit,QPushButton,QListView, 
QStyledItemDelegate,QVBoxLayout,QWidget,QStyle)

#==== Packages ====#

STATUS_WAITING = "waiting"
STATUS_RUNNING = "running"
STATUS_ERROR = "error"
STATUS_COMPLETE = "complete"
STATUS_STOPPED = 'stopped'


STATUS_COLORS:dict[str,str] = {
    STATUS_RUNNING: "#33a02c",
    STATUS_ERROR: "#e31a1c",
    STATUS_STOPPED: "#cccccc",
    STATUS_COMPLETE: "#b2df8a",
}
DEFAULT_STATE:dict[str,object] = {'progress':0,'status':STATUS_WAITING}

class WorkerKilledException(Exception):
    pass

class WorkerSignals(QObject):
    error = pyqtSignal(str,str)
    result = pyqtSignal(str,object)
    status = pyqtSignal(str,str)
    progress = pyqtSignal(str,int)
    finished = pyqtSignal(str)

class Worker(QRunnable):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__()
        self.signals = WorkerSignals()
        self.job_id = str(uuid.uuid4())
        self.args = args
        self.kwargs = kwargs
        
        self.signals.status.emit(self.job_id,STATUS_WAITING)
        self.is_killed = False

    @pyqtSlot()
    def run(self) -> None:
        self.signals.status.emit(self.job_id,STATUS_RUNNING)
        x,y = self.args
        try:
            value = random.randint(0,100) * x
            delay = random.random() / 10
            result:list[int] = []

            for n in range(100):
                value = value / y
                y -= 1
                result.append(value)
                self.signals.progress.emit(self.job_id, n + 1)
                time.sleep(delay)

                if self.is_killed:
                    raise WorkerKilledException

        except WorkerKilledException:
            self.signals.status.emit(self.job_id,STATUS_STOPPED)

        except Exception as e:
            print(e)
            self.signals.error.emit(self.job_id,str(e))
            self.signals.status.emit(self.job_id,STATUS_ERROR)
        
        else:
            self.signals.result.emit(self.job_id,result)
            self.signals.status.emit(self.job_id,STATUS_COMPLETE)
        
        self.signals.finished.emit(self.job_id)
    
    def Kill(self) -> None:
        self.is_killed = True
        print(self.is_killed)


class WorkerManager(QAbstractListModel):
    _workers:dict = {}
    _state:dict = {}
    status = pyqtSignal(str)
    
    def __init__(self) -> None:
        super().__init__()
        self.threadpool = QThreadPool()
        self.max_threads = self.threadpool.maxThreadCount()

        self.status_timer = QTimer()
        self.status_timer.setInterval(100)
        self.status_timer.timeout.connect(self.notify_status)
        self.status_timer.start()

    def notify_status(self) -> None:
        n_workers = len(self._workers)
        running = min(n_workers,self.max_threads)
        waiting = max(0,n_workers - self.max_threads)
        self.status.emit("{} running, {} waiting, {} threads".format(running,waiting,self.max_threads))
    
    def enqueue(self,worker) -> None:
        worker.signals.error.connect(self.receive_error)
        worker.signals.status.connect(self.receive_status)
        worker.signals.progress.connect(self.receive_progress)
        worker.signals.finished.connect(self.done)

        self.threadpool.start(worker)
        self._workers[worker.job_id] = worker

        self._state[worker.job_id] = DEFAULT_STATE.copy()
        self.layoutChanged.emit()
    
    def receive_status(self,job_id,status) -> None:
        self._state[job_id]['status'] = status
        self.layoutChanged.emit()
    
    def receive_progress(self,job_id,progress) -> None:
        self._state[job_id]['progress']  = progress
        self.layoutChanged.emit()
    
    def receive_error(self,job_id,message) -> None:
        print(job_id,': ',message)
    
    def done(self,job_id) -> None:
        del self._workers[job_id]
        self.layoutChanged.emit()
    
    def cleanup(self) -> None:
        for job_id,s in list(self._state.items()):
            if s['status'] in (STATUS_COMPLETE,STATUS_ERROR):
                del self._state[job_id]
        self.layoutChanged.emit()
    
    def data(self,index,role) -> tuple:
        if role == Qt.DisplayRole:
            job_ids = list(self._state.keys())
            job_id = job_ids[index.row()]
            return job_id,self._state[job_id]
    
    def kill(self,job_id) -> None:
        if  job_id in self._workers:
            self._workers[job_id].Kill()
    
    def rowCount(self,index) -> int:
        return len(self._state)
    
class ProgressBarDelegate(QStyledItemDelegate):
    def paint(self,painter,option,index) -> None:
        job_id,data = index.model().data(index,Qt.DisplayRole)

        if  data['progress'] > 0:
            color = QColor(STATUS_COLORS[data['status']])
            brush = QBrush()
            brush.setColor(color)
            brush.setStyle(Qt.SolidPattern)
            width = option.rect.width() * data['progress'] / 100 

            rect = QRect(option.rect)
            rect.setWidth(width)
            painter.fillRect(rect,brush)
        
        pen = QPen()
        pen.setColor(Qt.black)
        painter.drawText(option.rect,Qt.AlignLeft,job_id)

        if option.state & QStyle.State_Selected:
            painter.drawRect(option.rect)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.workers = WorkerManager()
        self.workers.status.connect(self.statusBar().showMessage)

        layout = QVBoxLayout()
        self.progress = QListView()
        self.progress.setModel(self.workers)
        delegate = ProgressBarDelegate()
        self.progress.setItemDelegate(delegate)
        layout.addWidget(self.progress)

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        start = QPushButton('Start a worker')
        start.pressed.connect(self.start_worker)

        stop = QPushButton('Stop')
        stop.pressed.connect(self.stop_worker)

        clear = QPushButton('Clear')
        clear.pressed.connect(self.workers.cleanup)

        layout.addWidget(self.text)
        layout.addWidget(start)
        layout.addWidget(stop)
        layout.addWidget(clear)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def start_worker(self) -> None:
        x = random.randint(0,1000)
        y = random.randint(0,1000)

        worker = Worker(x,y)
        worker.signals.result.connect(self.display_result)
        worker.signals.error.connect(self.display_result)
        self.workers.enqueue(worker)
    
    def stop_worker(self) -> None:
        selected = self.progress.selectedIndexes()
        print(selected)
        for idx in selected:
            job_id,_ = self.workers.data(idx,Qt.DisplayRole)
            self.workers.kill(job_id)
    
    def display_result(self,job_id,data) -> None:
        self.text.appendPlainText('WORKER %s: %s'% (job_id,data))


#==== Main ====#
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()



        


