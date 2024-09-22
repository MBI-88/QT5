__author__ = 'MBI'
__doc__ = """Script to run external process in QT

Constant                         Value         Description
QProcess.NotRunning              0             The process is not running.
QProcess.Starting                1             The process is starting, but the program has not yet been invoked.
QProcess.Running                 2             The process is running and is ready for reading and writing


"""

#==== Packages ====#
from typing import no_type_check_decorator
from PyQt5.QtCore import (QAbstractListModel, Qt,QObject,QRunnable,pyqtSlot,pyqtSignal,QProcess,QTimer,QThreadPool)
from PyQt5.QtWidgets import (QApplication,QMainWindow,QVBoxLayout,QPlainTextEdit,QPushButton,QWidget,
QProgressBar)
import re,sys,uuid

#==== Classes ====#

STATES:dict[object,str] = {
    QProcess.NotRunning: 'Not running',
    QProcess.Starting: 'Starting...',
    QProcess.Running: 'Running...'
}
progress_re = re.compile('Total complete: (\d+)%')

def simple_percent_parser(output) -> int:
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)

def extract_vars(l) -> dict:
    data:dict[str,str] = {}
    for s in l.splitlines():
        if '=' in s:
            name,value = s.split('=')
            data[name] = value
    
    return data

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.p = None
        layout = QVBoxLayout()

        self.text = QPlainTextEdit()
        layout.addWidget(self.text)

        self.process = QProgressBar()
        layout.addWidget(self.process)

        btn_run = QPushButton('Execute')
        btn_run.clicked.connect(self.start)
        layout.addWidget(btn_run)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def start(self) -> None:
        if self.p is not None:
            return
        
        self.p = QProcess()
        self.p.readyReadStandardOutput.connect(self.handle_stdout)
        self.p.readyReadStandardError.connect(self.handle_stderr)
        self.p.stateChanged.connect(self.handle_state)
        self.p.finished.connect(self.cleanup)
        self.p.start('python Concurrent\\dummy_script.py')
    
    def handle_stderr(self) -> None:
        result = bytes(self.p.readAllStandardError()).decode('utf8')
        progress = simple_percent_parser(result)
        self.process.setValue(progress)
    
    def handle_stdout(self) -> None:
        result = bytes(self.p.readAllStandardOutput()).decode('utf8')
        data = extract_vars(result)
        self.text.appendPlainText(str(data))
    
    def handle_state(self,state) -> None:
        self.statusBar().showMessage(STATES[state])
    
    def cleanup(self) -> None:
        self.p = None


    
#==== Main ====#
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

