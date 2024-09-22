"""
@autor: MBI
Description: Script for ilustrate the use of Events

Event handler           Event type moved
mouseMoveEvent          Mouse moved
mousePressEvent         Mouse button pressed
mouseReleaseEvent       Mouse button released
mouseDoubleClickEvent   Double click detected

Mouse events:
Method                  Returns
.button()               Specific button that trigger this event
.buttons()              State of all mouse buttons (OR’ed flags)
.globalPos()            Application-global position as a QPoint
.globalX()              Application-global horizontal X position
.globalY()              Application-global vertical Y position
.pos()                  Widget-relative position as a QPoint integer
.posF()                 Widget-relative position as a QPointF float


Identifier              Value (binary)                Represents
Qt.NoButton             0     (000)                   No button pressed, orthe event is not related to button press.
Qt.LeftButton           1     (001)                   The left button is pressed
Qt.RightButton          2     (010)                   The right button is pressed.
Qt.MiddleButton         4     (100)                   The middle button is pressed

"""
#==== Packages ====#
import sys
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QMenu,QAction
from PyQt5 import QtGui
#==== Class ====#

class MainWindowEvents(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = QLabel('Click in this window')
        self.setCentralWidget(self.label)
        #self.setMouseTracking(True) # Para seguir el movimeinto del mouse en toda la GUI
    
    def mouseMoveEvent(self,e) -> None:
        self.label.setText('mouseMoveEvent')

    def mousePressEvent(self,e) -> None:
        self.label.setText('mousePressEvnet')

    def mouseReleaseEvent(self,e) -> None:
        self.label.setText('mouseReleaseClickEvent')
    
    def mouseDoubleClickEvent(self,e) -> None:
        self.label.setText('mouseDoubleClickEvent')


class MainWindowMethos(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = QLabel('Click in this window')
        self.setCentralWidget(self.label)

    def mousePressEvent(self,e) -> None:
        if e.button() == Qt.LeftButton:
            self.label.setText('mousePressEvent LEFT')
        
        elif e.button() == Qt.MiddleButton:
            self.label.setText('mousePressEvent MIDDLE')
        
        elif e.button() == Qt.RightButton:
            self.label.setText('mousePressEvent RIGHT')
    
    def mouseReleaseEvent(self,e) -> None:
        if e.button() == Qt.LeftButton:
            self.label.setText('mousePressEvent LEFT')
        
        elif e.button() == Qt.MiddleButton:
            self.label.setText('mousePressEvent MIDDLE')
        
        elif e.button() == Qt.RightButton:
            self.label.setText('mousePressEvent RIGHT')
    
    def mouseDoubleClickEvent(self,e) -> None:
        if e.button() == Qt.LeftButton:
            self.label.setText('mousePressEvent LEFT')
        
        elif e.button() == Qt.MiddleButton:
            self.label.setText('mousePressEvent MIDDLE')
        
        elif e.button() == Qt.RightButton:
            self.label.setText('mousePressEvent RIGHT')

#=== Context Menu ====#

class MainContextGlobal(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
       
    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        context = QMenu(self)
        context.addAction(QAction('text 1',self))
        context.addAction(QAction('text 2',self))
        context.addAction(QAction('text 3',self))
        context.exec_(event.globalPos())


class MainContextMap(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.show()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
    
    def on_context_menu(self,pos) -> None:
        context = QMenu(self)
        context.addAction(QAction('text 1',self))
        context.addAction(QAction('text 2',self))
        context.addAction(QAction('text 3',self))
        context.exec_(self.mapToGlobal(pos))


#==== Layout forwarding ====#
""" 
Para concer el padre del widget se utiliza .parent(). Al momento  de adicionar un widget,
este pasa a ser hijo de la mainwindows.
Cuando un evento se crea este es pasado al widget mas alto en gerarquia en la UI. Si se tiene 
un boton en la ventana y se hace un click en el, el boton recivira el evento primero.

Si el primer widget no captura el evento este viajara hasta el widget padre. El viaje continua hasta
llegar al widget comprobado, hasta que sea capturado o rechazado por la main window.

Los eventos pueden marcarse como capturado o ignorado:

class CustomButton(Qbutton):
    def mousePressEvent(self,e) -> None:
        e.accept()

class CustomeButton(Qbutton):
    def event(self,e) -> None:
        e.ignore()

"""


#==== Main ====#
app = QApplication(sys.argv)
#window = MainWindowEvents()
#window = MainWindowMethos()
#window = MainContextGlobal()
window = MainContextMap()
window.show()
app.exec_()