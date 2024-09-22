"""
@autor: MBI
Description: Script to develop the concurrency
"""
#==== Packages ====#
import sys,time 
from PyQt5.QtCore import QRunnable, QThreadPool, QTimer,pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import (QApplication,QLabel,QMainWindow,QPushButton,QVBoxLayout,QWidget)

#==== Class ====#
class MainWindowConcurrency(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
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
        # The wrong approach
        for n in range(5):
            QApplication.processEvents()
            time.sleep(1)
    
    def recurring_timer(self) -> None:
        self.counter += 1
        self.label.setText('Counter: %d'% self.counter)

# Runners

class Worker(QRunnable):
    """
    Worker thread
    """
    @pyqtSlot()
    def run(self) -> None:
        print('Thread start')
        time.sleep(5)
        print('Thread complete')
    

class MainWindowsThread(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.counter = 0
        layout = QVBoxLayout()
        btn = QPushButton('DANGER!')
        self.label = QLabel('START')
        btn.pressed.connect(self.oh_no)
        self.threadpool = QThreadPool()
        print('Multithreading with maximum %d threads' % self.threadpool.maxThreadCount())

        layout.addWidget(self.label)
        layout.addWidget(btn)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def oh_no(self) -> None:
        worker = Worker()
        self.threadpool.start(worker)
    
    def recurring_timer(self) -> None:
        self.counter += 1
        self.label.setText('Counter: %d'% self.counter)

# Extended Runners

class ExRunner(QRunnable):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__()
        self.args = args
        self.kwargs = kwargs
       
    
    @pyqtSlot()
    def run(self) -> None:
        print(self.args,'  ',self.kwargs)
    
    def oh_no(self) -> None:
        worker = Worker('Some','argumets',keywords=2)
        self.threadpool.start(worker)



  



#==== Main ====#
app = QApplication(sys.argv)
#window = MainWindowConcurrency()
window = MainWindowsThread()

window.show()
app.exec_()
