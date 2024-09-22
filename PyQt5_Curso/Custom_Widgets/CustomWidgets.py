"""
@autor: MBI
Description: Script to customize widgets
"""
#==== Packages ====#
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5 import QtCore,QtGui,QtWidgets
import sys 

#==== Class ====#
class _Bar(QtWidgets.QWidget):

    clickedValue = pyqtSignal(int)

    def __init__(self,steps,*args,**kwars) -> None:
        super().__init__(*args,**kwars)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )
        if isinstance(steps,list):
            self.n_steps = len(steps)
            self.steps = steps

        elif isinstance(steps,int):
            self.n_steps = steps
            self.steps = ['red'] * steps
        
        else: raise TypeError('steps must be a list or int')

        self._bar_solid_percent = 0.8
        self._background_color = QtGui.QColor('black')
        self._padding = 4.0

    
    def sizeHint(self) -> QtCore.QSize:
        return QtCore.QSize(40,120)

    
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        #brush.setColor(QtGui.QColor(self._background_color))
        brush.setColor(self._background_color)
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0,0,painter.device().width(),painter.device().height())
        painter.fillRect(rect,brush)

        #dial = self.parent()._dial
        parent = self.parent()
        #vmin,vmax = dial.minimum(),dial.maximum()
        #value = dial.value()
        vmin,vmax = parent.minimum(),parent.maximum()
        value = parent.value()
        pc = (value - vmin )/(vmax - vmin)
        #n_steps_to_draw = int(pc * 5)
        n_steps_to_draw = int(pc * self.n_steps)
        #padding = 5

        #d_height = painter.device().height() - (padding * 2)
        #d_width = painter.device().width() - (padding * 2)

        d_height = painter.device().height() - (self._padding * 2)
        d_width = painter.device().width() - (self._padding * 2)

        #step_size = d_height / 5
        step_size = d_height / self.n_steps
        #bar_height = step_size * 0.60
        #bar_spacer = step_size * 0.4 / 2
        bar_height = step_size * self._bar_solid_percent
        bar_spacer = step_size * (1 - self._bar_solid_percent) / 2


        #brush.setColor(QtGui.QColor('red'))
        
        for n in range(n_steps_to_draw):
            brush.setColor(QtGui.QColor(self.steps[n]))
            rect = QtCore.QRect(
                self._padding,self._padding + d_height - ((n + 1) * step_size) + bar_spacer,
                d_width,bar_height
            )
            painter.fillRect(rect,brush)
            
 
        #pen = painter.pen()
        #pen.setColor(QtGui.QColor('red'))
        #painter.setPen(pen)

        #font = painter.font()
        #font.setFamily('Times')
        #font.setPointSize(18)
        #painter.setFont(font)
        
        #painter.drawText(25,25,"{}-->{}<--{}".format(vmin,value,vmax))
        #painter.drawText(25,25,"{}".format(n_steps_to_draw))
        painter.end()
    
    def _trigger_refresh(self) -> None:
        self.update()

    
    def _calculate_clicked_value(self, e) -> None:
        parent = self.parent()
        vmin,vmax = parent.minimum(),parent.maximum()
        d_height = self.size().height() + (self._padding  * 2)
        step_size = d_height / self.n_steps
        click_y = e.y() - self._padding - step_size / 2

        pc = (d_height - click_y) / d_height
        value = vmin + pc * (vmax - vmin)
        self.clickedValue.emit(value)
    
    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        self._calculate_clicked_value(a0)
    
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self._calculate_clicked_value(a0)


class PowerBar(QtWidgets.QWidget):

    colorChanged = pyqtSignal(object)

    def __init__(self,steps=5,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        layout = QtWidgets.QVBoxLayout()
        self._bar = _Bar(steps)
        layout.addWidget(self._bar)

        self._dial = QtWidgets.QDial()
        self._dial.setNotchesVisible(True)
        self._dial.setWrapping(False)
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        self._bar.clickedValue.connect(self._dial.setValue)

        layout.addWidget(self._dial)

        self.setLayout(layout)
    
    def __getattr__(self, name: str) -> str:
        if name in self.__dict__:
            return self[name]
        return getattr(self._dial,name)
    
    def setColor(self,color) -> None:
        self._bar.steps = [color] * self._bar.n_steps
        self._bar.update()
    
    def setColors(self,colors) -> None:
        self._bar.n_steps = len(colors)
        self._bar.steps = colors
        self._bar.update()
    
    def setBarPadding(self,i) -> None:
        self._bar._padding = int(i)
        self._bar.update()
    
    def setBarSolidPercent(self,f:int) -> None:
        self._bar._bar_solid_percent = float(f)
        self._bar.update()
    
    def setBackgroundColor(self, color:str) -> None:
        self._bar._background_color = QtGui.QColor(color)
        self._bar.update()
        

#==== Main ====#
app = QtWidgets.QApplication(sys.argv)
volume = PowerBar(["#49006a", "#7a0177", "#ae017e", "#dd3497", "#f768a1",
"#fa9fb5", "#fcc5c0", "#fde0dd", "#fff7f3"])
volume.setBarPadding(2)
volume.setBarSolidPercent(0.85)
volume.setBackgroundColor('green')
volume.show()
app.exec_()
