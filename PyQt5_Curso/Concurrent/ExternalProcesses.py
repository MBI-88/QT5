__author__ = 'MBI'
__doc__ = 'Script for run external processes'

#==== Packages ====#
import subprocess as sub 
import sys,time,traceback,uuid
from collections import namedtuple
from PyQt5.QtCore import QObject,QRunnable,QThreadPool,pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import (QApplication, QLineEdit,QMainWindow,QPlainTextEdit,QPushButton,QVBoxLayout,QWidget,
QSpinBox)

#==== Classes ====#

class WorkerSignals(QObject):
    result = pyqtSignal(str)
    finished = pyqtSignal()

class SubPorcessWorker(QRunnable):
    def __init__(self,command:str) -> None:
        super().__init__()
        self.signals = WorkerSignals()
        self.command = command
    
    @pyqtSlot()
    def run(self) -> None:
        output = sub.getoutput(self.command)
        self.signals.result.emit(output)
        self.signals.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.text = QPlainTextEdit()
        layout.addWidget(self.text)

        btn = QPushButton('EXECUTE')
        btn.clicked.connect(self.start_process)

        layout.addWidget(btn)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.threadpool = QThreadPool()
    
    def start_process(self) -> None:
        self.runner = SubPorcessWorker('help')
        self.runner.signals.result.connect(self.result)
        self.threadpool.start(self.runner)
    
    def result(self,s) -> None:
        self.text.appendPlainText(s)

# Parsing result
def extract_vars(l) -> dict[str,object]:
    data:dict[str,object] = {}
    for s in l.splitlines():
        if '=' in s:
            name,value = s.split('=')
            data[name] = value
    
    data['number_of_lines'] = len(l)
    return data

class WorkerSignal(QObject):
    result = pyqtSignal(dict)
    finished = pyqtSignal()

class SubPro(QRunnable):
    def __init__(self,command:str,process_result = None) -> None:
        super().__init__()
        self.signals = WorkerSignal()
        self.command = command
        self.process_result = process_result
    
    @pyqtSlot()
    def run(self) -> None:
        output = sub.getoutput(self.command)
        if self.process_result:
            output = self.process_result(output)
        
        self.signals.result.emit(output)
        self.signals.finished.emit()

class MainWindowParser(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout()
        self.name = QLineEdit()
        layout.addWidget(self.name)

        self.country = QLineEdit()
        layout.addWidget(self.country)

        self.website = QLineEdit()
        layout.addWidget(self.website)

        self.number_of_lines = QSpinBox()
        layout.addWidget(self.number_of_lines)
        
        btn = QPushButton('EXECUTE')
        btn.clicked.connect(self.start)

        layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.threadpool = QThreadPool()
    
    def start(self) -> None:
        self.runner = SubPro('python Concurrent\\dummy_script.py',process_result=extract_vars)
        self.runner.signals.result.connect(self.result)
        self.threadpool.start(self.runner)
    
    def result(self,data) -> None:
        print(data)
        self.name.setText(data['name'])
        self.country.setText(data['country'])
        self.website.setText(data['website'])
        self.number_of_lines.setValue(data['number_of_lines'])
        


#==== Main ====#
app = QApplication(sys.argv)
#window = MainWindow()
window = MainWindowParser()
window.show()
app.exec_()