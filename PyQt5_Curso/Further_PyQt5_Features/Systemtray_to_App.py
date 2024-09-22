"""
@autor: MBI
Description: Script to add a system tray icon to an App

Reason Value                             Description
QSystemTrayIcon.Unknown 0                Unknown reason.
QSystemTrayIcon.Context 1                Context menu requested (single click macOS, right-click Windows).
QSystemTrayIcon.DoubleClick 2            Icon double clicked. On macOS double-click only fires if no context
                                         menu is set, as the menu opens with a single click.
QSystemTrayIcon.Trigger 3                Icon clicked once.
QSystemTrayIcon.MiddleClick 4            Icon clicked with the middle mouse
button

"""
#==== Package ====#
from PyQt5.QtWidgets import (QApplication, QMainWindow,QSystemTrayIcon,QMenu,
                            QTextEdit,QAction)
from PyQt5.QtGui import QIcon
import sys

#==== Class ====#

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

icon = QIcon('Further_PyQt5_Features\\smiley-lol.png')

tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        menu = self.menuBar()
        file_menu = menu.addMenu('&File')

        self.quit = QAction('&Quit')
        self.quit.triggered.connect(app.quit)
        file_menu.addAction(self.quit)

        self.editor = QTextEdit()
        self.load()

        self.setCentralWidget(self.editor)
        self.setWindowTitle('Note')
    
    def load(self) -> None:
        with open('Further_PyQt5_Features\\note.txt','r') as f:
            text = f.read()
        self.editor.setPlainText(text)
    
    def save(self) -> None:
        text = self.editor.toPlainText()
        with open('Further_PyQt5_Features\\note.txt','w')  as f:
            f.write(text)

    def activate(self,reason) -> None:
        if reason == QSystemTrayIcon.Trigger:
            if self.isVisible():
                self.hide()
            else: self.show()


#==== Main ====#
window = MainWindow()
tray.activated.connect(window.activate)
app.aboutToQuit.connect(window.save)
app.exec_()
