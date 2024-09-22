"""
@autor: MBI
Description: Script to use de System tray

Value             Ranges
#a2b3cc           00-FF
rgb(25, 28, 29)   0-255
hsv(14, 93, 199)  0-255

"""
#==== Packages ====#
from PyQt5.QtWidgets import QApplication,QSystemTrayIcon,QColorDialog,QMenu,QAction
from PyQt5.QtGui import QIcon
import sys

#==== Aplication ====#

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

icon = QIcon('Further_PyQt5_Features\\smiley-lol.png')

clipboard = QApplication.clipboard()
dialog = QColorDialog()

def copy_color_hex() -> None:
    if dialog.exec_():
        color = dialog.currentColor()
        clipboard.setText(color.name())

def copy_color_rgb() -> None:
    if dialog.exec_():
        color = dialog.currentColor()
        clipboard.setText("rgb(%d, %d, %d)"%(color.red(),color.green(),color.blue()))

def copy_color_hsv() -> None:
    if dialog.exec_():
        color = dialog.currentColor()
        clipboard.setText('hsv(%d, %d,%d)' % (color.hue(),color.saturation(),color.value()))


tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu  = QMenu()
action1 = QAction('Hex')
action1.triggered.connect(copy_color_hex)
menu.addAction(action1)

action2 = QAction('RGB')
action2.triggered.connect(copy_color_rgb)
menu.addAction(action2)

action3 = QAction('HSV')
action3.triggered.connect(copy_color_hsv)
menu.addAction(action3)

quit = QAction('Quit')
quit.triggered.connect(app.quit)
menu.addAction(quit)

tray.setContextMenu(menu)

app.exec_()