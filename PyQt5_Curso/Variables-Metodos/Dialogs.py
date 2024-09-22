"""
@autor: MBI
Description: Script for develop of Dialog Widgets

Button types:
QDialogButtonBox.Ok
QDialogButtonBox.Open
QDialogButtonBox.Save
QDialogButtonBox.Cancel
QDialogButtonBox.Close
QDialogButtonBox.Discard
QDialogButtonBox.Apply
QDialogButtonBox.Reset
QDialogButtonBox.RestoreDefaults
QDialogButtonBox.Help
QDialogButtonBox.SaveAll
QDialogButtonBox.Yes
QDialogButtonBox.YesToAll
QDialogButtonBox.No
QDialogButtonBox.NoToAll
QDialogButtonBox.Abort
QDialogButtonBox.Retry
QDialogButtonBox.Ignore
QDialogButtonBox.NoButton

Button types:
QMessageBox.Ok
QMessageBox.Open
QMessageBox.Save
QMessageBox.Cancel
QMessageBox.Close
QMessageBox.Discard
QMessageBox.Apply
QMessageBox.Reset
QMessageBox.RestoreDefaults
QMessageBox.Help
QMessageBox.SaveAll
QMessageBox.Yes
QMessageBox.YesToAll
QMessageBox.No
QMessageBox.NoToAll
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore
QMessageBox.NoButton

Icon state                  Description
QMessageBox.NoIcon          The message box does not have an icon.
QMessageBox.Question        The message is asking a question.
QMessageBox.Information     The message is informational only.
QMessageBox.Warning         The message is warning.
QMessageBox.Critical        The message indicates a critical problem.

Methods:
QMessageBox.about(parent, title, message)
QMessageBox.critical(parent, title, message)
QMessageBox.information(parent, title, message)
QMessageBox.question(parent, title, message)
QMessageBox.warning(parent, title, message)

"""
#==== Packages ====#
import sys
from PyQt5.QtWidgets import (QApplication, QDialogButtonBox,QLabel,
QMainWindow, QMessageBox,QPushButton,QDialog, QVBoxLayout)
#==== Class ====#

class CustomDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Hello!')

        btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(btn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel('Something happened,is that OK?')
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)



class MainWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('My App')
        btn = QPushButton('Press me for a dialog')
        btn.clicked.connect(self.button_clicked)
        self.setCentralWidget(btn)
    
    def button_clicked(self,s) -> None:
        print('clicked ',s)
        dlg = CustomDialog()
        if dlg.exec_(): print('Success!')
        else: print('Cancel!')

class MainMessage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        btn = QPushButton('Press me for a dialog')
        btn.clicked.connect(self.button_clicked)
        self.setCentralWidget(btn)
    
    def button_clicked(self,s) -> None:
        dlg = QMessageBox(self)
        dlg.setWindowTitle('I have a question!')
        dlg.setText('This is a simple dialog')
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec_()
        if button == QMessageBox.Yes: print('Yes!')
        else: print('No!')


class MainMessageMethods(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        btn = QPushButton('Press me for a dialog')
        btn.clicked.connect(self.button_clicked)
        self.setCentralWidget(btn)
    
    def button_clicked(self,s) -> None:
        button = QMessageBox.question(self,'Question dialog','The longer message')
        if (button == QMessageBox.Yes): print('Yes!')
        else: print('No!')

class MainMesseageMethodsDefault(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My App')
        btn = QPushButton('Press me for a dialog')
        btn.clicked.connect(self.button_clicked)
        self.setCentralWidget(btn)
    
    def button_clicked(self) -> None:
        button = QMessageBox.critical(
            self,'Oh dear!','Something went very wrong',
            buttons = QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard)
        if (button == QMessageBox.Yes): print('Yes!')
        else: print('No!')

#==== Main ====#
app = QApplication(sys.argv)
#window = MainWidget()
#window = MainMessage()
#window = MainMessageMethods()
window = MainMesseageMethodsDefault()
window.show()
app.exec_()