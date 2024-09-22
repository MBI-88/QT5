__author__ = 'MBI'
__doc__ = 'Script to develop tracking process'

#==== Packages ====#
import re,sys
import subprocess as sub 
from PyQt5.QtCore import QObject,QRunnable,QThreadPool,pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import (QApplication,QMainWindow,QPlainTextEdit,QProgressBar,QPushButton,
QVBoxLayout,QWidget)

#==== Classes ====#
progress_re = re.compile('Total complete: (\d+)%')

def simple_percent_parser(output) -> int:
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)

class WorkerSignals(QObject):
    result = pyqtSignal(str)
    progress = pyqtSignal(int)
    finished = pyqtSignal()

class SubProcessWorker(QRunnable):
    def __init__(self,command:str,parser=None) -> None:
        super().__init__()
        self.signals = WorkerSignals()
        self.command = command
        self.parser = parser

    @pyqtSlot()
    def run(self) -> None:
        result:list[str] = []
        with sub.Popen(self.command,
                        bufsize=1,
                        stdout=sub.PIPE,
                        stderr=sub.STDOUT,
                        universal_newlines=True) as proc:
                        while proc.poll() is None:
                            data = proc.stdout.readline()
                            result.append(data)
                            if self.parser:
                                value = self.parser(data)
                                if value:
                                    self.signals.progress.emit(value)
        
        output = "".join(result)
        self.signals.result.emit(output)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.text = QPlainTextEdit()
        layout.addWidget(self.text)

        self.progressbar = QProgressBar()
        self.progressbar.setRange(0,100)
        self.progressbar.setValue(0)
        layout.addWidget(self.progressbar)

        btn = QPushButton('EXECUTE')
        btn.clicked.connect(self.start)
        layout.addWidget(btn)

        widgets = QWidget()
        widgets.setLayout(layout)
        self.setCentralWidget(widgets)

        self.threadpool = QThreadPool()
    
    def start(self) -> None:
        self.runner = SubProcessWorker(command='python Concurrent\\dummy_script.py',parser=simple_percent_parser)
        self.runner.signals.result.connect(self.result)
        self.runner.signals.progress.connect(self.progressbar.setValue)
        self.threadpool.start(self.runner)

    def result(self,s) -> None:
        self.text.appendPlainText(s)


#==== Main ====#
app = QApplication(sys.argv)
window= MainWindow()
window.show()
app.exec_()