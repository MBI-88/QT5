__author__ = 'MBI'
__doc__ = 'The Communicator'


#==== Packages ====#
import sys,requests,re
from PyQt5.QtCore import QObject,QRunnable,Qt,QThreadPool,pyqtSignal,pyqtSlot 
from PyQt5.QtWidgets import (QApplication,QMainWindow,QHBoxLayout, QPlainTextEdit,QProgressBar,QPushButton, QVBoxLayout,
QWidget)

#==== Class ====#
class WorkerSignals(QObject):
    data = pyqtSignal(tuple)

class Worker(QRunnable):
    def __init__(self,id:int,url:str,parsers:dict[str,str]) -> None:
        super().__init__()
        self.id = id
        self.url = url
        self.parsers = parsers

        self.signal = WorkerSignals()
    
    @pyqtSlot()
    def run(self) -> None:
        r = requests.get(self.url)
        data:dict[int,str] = {}

        #for line in r.text.splitlines():
            #self.signal.data.emit((self.id,line))
        
        for name,parser in self.parsers.items():
            m = parser.search(r.text)
            if m:
                data[name] = m.group(1).strip()
        self.signal.data.emit((self.id,data))

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.url:list[str] = [
            "https://www.learnpyqt.com/",
            "https://www.mfitzp.com/",
            "https://www.google.com",
            "https://www.udemy.com/create-simple-gui-applicationswith-python-and-qt/",
        ]
        self.parsers:dict[str,str] = {
            "title": re.compile(r"<title.*?>(.*?)<\/title>", re.M |re.S),
            "h1": re.compile(r"<h1.*?>(.*?)<\/h1>", re.M | re.S),
            "h2": re.compile(r"<h2.*?>(.*?)<\/h2>", re.M | re.S),
        }
        layout = QVBoxLayout()
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        btn = QPushButton('GO GET EM')
        btn.pressed.connect(self.execute)

        layout.addWidget(self.text)
        layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.threadpool = QThreadPool()
    
    def execute(self) -> None:
        for n,url in enumerate(self.url):
            worker = Worker(n,url,self.parsers)
            worker.signal.data.connect(self.display_output)
            self.threadpool.start(worker)
    
    def display_output(self,data) -> None:
        id,s = data
        self.text.appendPlainText('Worker %d: %s'% (id,s))

#==== Main ====#
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()