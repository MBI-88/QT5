"""
@autor: MBI
Description: Script to custom widgets

Method                            Description
drawLine(line)                    Draw a QLine instance
drawLine(line)                    Draw a QLineF instance
drawLine(x1, y1, x2, y2)          Draw a line between x1, y2 and x2, y2 (both int).
drawLine(p1, p2)                  Draw a line between point p1 and p2 (both QPoint)
drawLine(p1, p2)                  Draw a line between point p1 and p2 (both QPointF)
"""
#==== Packages ====#
from random import choice,randint
import sys,random
from PyQt5.QtCore import Qt 
from PyQt5 import QtGui,QtWidgets,QtCore
#==== Class ====#

# drawLine
class MainWidowLine(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400,300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
    
    def draw_something(self) -> None:
        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawLine(10,10,300,200)
        painter.end()

# drawPoint
class MainWidowPoint(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400,300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
    
    def draw_something(self) -> None:
        colors =  ["#FFD141", "#376F9F", "#0D1F2D", "#E9EBEF","#EB5160"]
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(5)
        painter.setPen(pen)
        for n in range(10000):
            pen.setColor(QtGui.QColor(choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(
                200 + randint(-100,100),150 + randint(-100,100)
            )
        painter.end()

# drawLine 1
class MainWidowLine1(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400,300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
    
    def draw_something(self) -> None:
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(15)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        painter.drawLine(QtCore.QPoint(100,100),QtCore.QPoint(300,200))
        painter.end()


# drawRect,drawRects and drawRoundedRect
class MainWidowRect(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400,300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
    
    def draw_something(self) -> None:
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor('#EB5460'))
        painter.setPen(pen)

        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('yellow'))
        brush.setStyle(Qt.Dense1Pattern)
        painter.setBrush(brush)

        painter.drawRect(50,50,100,100)
        painter.drawRect(70,70,100,100)
        painter.drawRect(80,80,150,100)
        painter.drawRect(90,90,100,150)
        # Variant
       # painter.drawRects(
            #QtCore.QRect(50, 50, 100, 100),
            #QtCore.QRect(60, 60, 150, 100),
            #QtCore.QRect(70, 70, 100, 150),
            #QtCore.QRect(80, 80, 150, 100),
            #QtCore.QRect(90, 90, 100, 150)
       # )
       # drawRooundedRect
        #painter.drawRoundedRect(40, 40, 100, 100, 10, 10)
        #painter.drawRoundedRect(80, 80, 100, 100, 10, 50)
        #painter.drawRoundedRect(120, 120, 100, 100, 50, 10)
        #painter.drawRoundedRect(160, 160, 100, 100, 50, 50)

        painter.end()

# drawEllipse
class MainWidowEllipse(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400,300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
    
    def draw_something(self) -> None:
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(204,0,0))
        painter.setPen(pen)
        #painter.drawEllipse(10,10,100,100)
        #painter.drawEllipse(10,10,150,200)
        #painter.drawEllipse(10,10,200,300)
        # QPoint(x,y) center and x,y radio
        painter.drawEllipse(QtCore.QPoint(100, 100), 10, 10)
        painter.drawEllipse(QtCore.QPoint(100, 100), 15, 20)
        painter.drawEllipse(QtCore.QPoint(100, 100), 20, 30)
        painter.drawEllipse(QtCore.QPoint(100, 100), 25, 40)
        painter.drawEllipse(QtCore.QPoint(100, 100), 30, 50)
        painter.drawEllipse(QtCore.QPoint(100, 100), 35, 60)
        painter.end()

# Text
class MainWidowText(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(500,300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
    
    def draw_something(self) -> None:
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)
        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)
        painter.drawText(100,100,'Hello World')
        #painter.drawText(100,100,100,100,Qt.AlignHCenter,'Hello, world!')
        painter.end()

# Draw with canvas points
class MainWindowCanvasPoint(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400,400)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawPoint(a0.x(),a0.y())
        painter.end()
        self.update()


# Draw with canvas line
class MainWindowCanvasLine(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400,400)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        self.last_x,self.last_y = None,None
    
    def mouseMoveEvent(self, a0:QtGui.QMouseEvent) -> None:
        if self.last_x is None:
            self.last_x = a0.x()
            self.last_y = a0.y()
            return 
    
        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawLine(self.last_x,self.last_y,a0.x(),a0.y())
        painter.end()
        self.update()
        self.last_x = a0.x()
        self.last_y = a0.y()
    
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.last_x = None
        self.last_y = None

# Model Canvas
class Canvas(QtWidgets.QLabel):
    def __init__(self) -> None:
        super().__init__()

        pixmap = QtGui.QPixmap(600,400)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)
        self.last_x,self.last_y = None,None
        self.pen_color = QtGui.QColor('#000000')
    
    def set_pen_color(self,c) -> None:
        self.pen_color = QtGui.QColor(c)
    
    def mouseMoveEvent(self, a0:QtGui.QMouseEvent) -> None:
        if self.last_x is None :
            self.last_x = a0.x()
            self.last_y = a0.y()
            return
        
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x,self.last_y,a0.x(),a0.y())
        painter.end()
        self.update()
        self.last_x = a0.x()
        self.last_y = a0.y()
    
    def mouseReleaseEvent(self, a0) -> None:
        self.last_x = None
        self.last_y = None
    

COLORS = ["#000000",
"#141923",
"#414168",
"#3a7fa7",
"#35e3e3",
"#8fd970",
"#5ebb49",
"#458352",
"#dcd37b",
"#fffee5",
"#ffd035",
"#cc9245",
"#a15c3e",
"#a42f3b",
"#f45b7a",
"#c24998",
"#81588d",
"#bcb0c2",
"#ffffff",]

class QPaletteButton(QtWidgets.QPushButton):
    def __init__(self,color) -> None:
        super().__init__()

        self.setFixedSize(QtCore.QSize(24,24))
        self.color = color 
        self.setStyleSheet('background-color: %s;'%color)

class MainWindowCanvaLineColors(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.canvas = Canvas()
        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        l.addLayout(palette)
        
        self.setCentralWidget(w)
    
    def add_palette_buttons(self,layout)  -> None:
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c:self.canvas.set_pen_color(c))
            layout.addWidget(b)

# Spray
SPRAY_PARTICLES = 100
SPRAY_DIAMETER = 10
class SprayCanvas(QtWidgets.QLabel):
    def __init__(self) -> None:
        super().__init__()

        pixmap = QtGui.QPixmap(600,400)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)

        self.pen_color = QtGui.QColor('#000000')
    
    def set_pen_color(self,c) -> None:
        self.pen_color = QtGui.QColor(c)
    
    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(1)
        p.setColor(self.pen_color)
        painter.setPen(p)

        for n in range(SPRAY_PARTICLES):
            xo = random.gauss(0,SPRAY_DIAMETER)
            yo = random.gauss(0,SPRAY_DIAMETER)
            painter.drawPoint(ev.x()+xo,ev.y()+yo)
        
        self.update()

class MainWindowSpray(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.canvas = SprayCanvas()
        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        l.addLayout(palette)
        
        self.setCentralWidget(w)
    
    def add_palette_buttons(self,layout)  -> None:
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c:self.canvas.set_pen_color(c))
            layout.addWidget(b)





#==== Main ====#
app = QtWidgets.QApplication(sys.argv)
#window = MainWidowLine()
#window = MainWidowPoint()
#window = MainWidowLine1()
#window = MainWidowRect()
#window = MainWidowEllipse()
#window = MainWidowText()
#window = MainWindowCanvasPoint()
#window = MainWindowCanvasLine()
#window = MainWindowCanvaLineColors()
window = MainWindowSpray()
window.show()
app.exec_()