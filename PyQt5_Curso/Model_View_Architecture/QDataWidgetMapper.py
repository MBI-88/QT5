"""
@autor: MBI
Description: Script to describe the use of QDataWidgetMapper

Values to Drive in QSqlDatabase('<driver>'):
Note: The value of <driver> can be any one of the following ['QSQLITE',
'QMYSQL', 'QMYSQL3', 'QODBC', 'QODBC3', 'QPSQL', 'QPSQL7']. To get this list on
your system run QSqlDatabase.drivers().

To connect to servers:
# Create database connection.
db = QSqlDatabase('<driver>')
db.setHostName('<localhost>')
db.setDatabaseName('<databasename>')
db.setUserName('<username>')
db.setPassword('<password>')
db.open()
That’s it! Once the connection is established, the models will behave exactly
as before
"""
#==== Packages ====#
import sys
from PyQt5.QtCore import QSize,Qt 
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel
from PyQt5.QtWidgets import (QApplication,QComboBox,QDataWidgetMapper,
                            QDoubleSpinBox,QFormLayout,QLabel,QLineEdit,
                            QMainWindow, QPushButton,QSpinBox,QTableView,QWidget,QHBoxLayout,QVBoxLayout)
#==== Class ====#
db = QSqlDatabase('QSQLITE')
db.setDatabaseName('Model_View_Architecture\\chinook.sqlite')
db.open()

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        form = QFormLayout()

        self.track_id = QSpinBox()
        self.track_id.setDisabled(True)
        self.name = QLineEdit()
        self.album = QComboBox()
        self.media_type = QComboBox()
        self.genre = QComboBox()
        self.composer = QLineEdit()

        self.milliseconds = QSpinBox()
        self.milliseconds.setRange(0,2147483647) # Configuracion del widget para aceptar valores
        self.milliseconds.setSingleStep(1)

        self.bytes = QSpinBox()
        self.bytes.setRange(0,2147483647)
        self.bytes.setSingleStep(1)

        self.unit_price = QDoubleSpinBox()
        self.unit_price.setRange(0,999)
        self.unit_price.setSingleStep(0.01)
        self.unit_price.setPrefix("$")

        form.addRow(QLabel('Track ID'),self.track_id)
        form.addRow(QLabel('Track name'),self.name)
        form.addRow(QLabel('Composer'),self.composer)
        form.addRow(QLabel('Milliseconds'),self.milliseconds)
        form.addRow(QLabel('Bytes'),self.bytes)
        form.addRow(QLabel('Unit Price'),self.unit_price)

        self.model = QSqlTableModel(db=db)
        
        self.mapper = QDataWidgetMapper() 
        self.mapper.setModel(self.model)

       # Los widgets son mapeados a columnas

        self.mapper.addMapping(self.track_id,0)
        self.mapper.addMapping(self.name,1)
        self.mapper.addMapping(self.composer,5)
        self.mapper.addMapping(self.milliseconds,6)
        self.mapper.addMapping(self.bytes,7)
        self.mapper.addMapping(self.unit_price,8)

        prev_rec = QPushButton('Previous')
        prev_rec.clicked.connect(self.mapper.toPrevious)
        next_rec = QPushButton('Next')
        next_rec.clicked.connect(self.mapper.toNext)
        save_rec = QPushButton('Save')
        save_rec.clicked.connect(self.mapper.submit)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        h_layout.addWidget(prev_rec)
        h_layout.addWidget(next_rec)
        h_layout.addWidget(save_rec)

        v_layout.addLayout(form)
        v_layout.addLayout(h_layout)


        self.model.setTable('Track')
        self.model.select() # Populando el modelo

        self.mapper.toFirst() # Primer avance del mapeador para grabar datos

        self.setMinimumSize(QSize(400,400))

        widget = QWidget()
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)



#==== Main ====#
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()