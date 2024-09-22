"""
@author: MBI
Description: Scripts para la demostracion del uso de widgets

Lista de widgets mas usados:
QCheckbox A checkbox
QComboBox A dropdown list box
QDateEdit For editing dates
QDateTimeEdit For editing dates and datetimes
QDial Rotatable dial
QDoubleSpinbox A number spinner for floats
QFontComboBox A list of fonts
QLCDNumber A quite ugly LCD display
QLabel Just a label, not interactive
QLineEdit Enter a line of text
QProgressBar A progress bar
QPushButton A button
QRadioButton A group with only one active choice
QSlider A slider
QSpinBox An integer spinner
QTimeEdit For editing times

Banderas existente para la aliniacion horizontal:
Qt.AlignLeft Aligns with the left edge.
Qt.AlignRight Aligns with the right edge.
Qt.AlignHCenter Centers horizontally in the available
space.
Qt.AlignJustify Justifies the text in the available
space.

Banderas existente para la aliniacion vertical:
Qt.AlignTop Aligns with the top.
Qt.AlignBottom Aligns with the bottom.
Qt.AlignVCenter Centers vertically in the available
space.

Banderas para aliniar automaticamente en horizontal y vertical:
Qt.AlignCenter Centers horizontally and vertically
"""
#=== Modulos ===#
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap 
from PyQt5.QtWidgets import (QApplication, QDial,QLabel,QMainWindow,QCheckBox,
QComboBox,QListWidget,QLineEdit,QSpinBox,QSlider)
#=== Clases ===#

class MainLabel(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')
        
        
        widget = QLabel('Hello')
        widget.setPixmap(QPixmap('otje.jpg'))
        #font = widget.font()
        #font.setPointSize(30)
        #widget.setFont(font)
        #widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        widget.setScaledContents(True)
        self.setCentralWidget(widget)


class MainCheckBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')

        widget = QCheckBox('This is a checkbox')
        widget.setCheckState(Qt.Checked) # o  .setChecked()
        """
        Banderas usadas:
        Qt.Checked Item is checked
        Qt.Unchecked Item is unchecked
        Qt.PartiallyChecked Item is partially checked
        """

        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)
    
    def show_state(self,S):
        print(S == Qt.Checked)
        print(S)

class MainCombobox(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        widget = QComboBox()
        widget.addItems(['One','Two','Three'])
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        widget.setEditable(True) # para insertar etiquetas
        """
        Banderas usadas:
        QComboBox.NoInsert No insert
        QComboBox.InsertAtTop Insert as first item
        QComboBox.InsertAtCurrent Replace currently selected item
        QComboBox.InsertAtBottom Insert after last item
        QComboBox.InsertAfterCurrent Insert after current item
        QComboBox.InsertBeforeCurrent Insert before current item
        QComboBox.InsertAlphabetically Insert in alphabetical order

        """
        widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        widget.setMaxCount(5)


        self.setCentralWidget(widget)
    
    def index_changed(self,i) -> None:
        print(i)
    
    def text_changed(self,s) -> None:
        print(s)
        


class MainLisBox(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        widget = QListWidget()
        widget.addItems(['One','Two','Three'])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)
    
    def index_changed(self,i) -> None:
        print(i.text())
    
    def text_changed(self,s) -> None:
        print(s)

class MainLineEdit(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My app')
        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText('Enter your text')
        #widget.setReadOnly(True)
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        #widget.setInputMask('000.000.000.000/00;_') # Usado para validar una ip

        self.setCentralWidget(widget)
    
    def return_pressed(self) -> None:
        print('Return pressed!')
        self.centralWidget().setText('BOOM!')

    def selection_changed(self) -> None:
        print('Selection changed')
        print(self.centralWidget().selectedText())
    
    def text_changed(self,s) -> None:
        print('Text changed...')
        print(s)
    
    def text_edited(self,s) -> None:
        print('Text edited...')
        print(s)

class MainSpingBox(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        widget = QSpinBox()# o QDoubleSpinBox()
        widget.setMinimum(-10)
        widget.setMaximum(3)
        #widget.setRange(-10,3)
        widget.setPrefix('$')
        widget.setSuffix('c')
        widget.setSingleStep(3) # e.g 0.5 para QDoubleSpinBox()
        widget.valueChanged.connect(self.value_changed) # devuelve solo el valor numerico de la etiqueta
        widget.valueChanged[str].connect(self.value_changed_str) # devuelve todo la etiqueta 

        self.setCentralWidget(widget)
    
    def value_changed(self,i) -> None:
        print(i)
    
    def value_changed_str(self,s) -> None:
        print(s)


class MainSlider(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        widget = QSlider(Qt.Horizontal) # o Qt.Vertical
        widget.setRange(-10,3)
        #widget.setMinimun(-10)
        #widget.setMaximun(3)
        widget.setSingleStep(3)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)
    
    def value_changed(self,i) -> None:
        print(i)
    
    def slider_position(self,p) -> None:
        print('Position ',p)
    
    def slider_pressed(self) -> None:
        print('Pressed!')
    
    def slider_released(self) -> None:
        print('Released')

class MainDial(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        widget = QDial()
        widget.setRange(-10,100)
        widget.setSingleStep(0.5)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self,i) -> None:
        print(i)
    
    def slider_position(self,p) -> None:
        print('Position ',p)
    
    def slider_pressed(self) -> None:
        print('Pressed!')
    
    def slider_released(self) -> None:
        print('Released')


#=== Main ===#

app = QApplication(sys.argv)
#window = MainLabel()
#window = MainCheckBox()
#window = MainCombobox()
#window = MainLisBox()
#window = MainLineEdit()
#window = MainSpingBox()
#window = MainSlider()
window = MainDial()
window.show()
app.exec_()
