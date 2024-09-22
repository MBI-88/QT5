"""
@autor:  MBI
Description: Script for development of skeleton palette
"""
#==== Packages ====#
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QMainWindow,QLabel,QPushButton,QWidget
from PyQt5.QtGui import QPalette,QColor
from PyQt5.QtCore import Qt
import sys
#==== App skeleton ====#
darkPalette = QPalette()
darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
darkPalette.setColor(QPalette.WindowText, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
darkPalette.setColor(QPalette.ToolTipText, Qt.white)
darkPalette.setColor(QPalette.Text, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
darkPalette.setColor(QPalette.ButtonText, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
darkPalette.setColor(QPalette.BrightText, Qt.red)
darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
darkPalette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80))
darkPalette.setColor(QPalette.HighlightedText, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127))

#==== Main ====#
app = QApplication(sys.argv)
app.setPalette(darkPalette)
app.setStyle('Fusion')

window = QMainWindow()  # Replace with your QMainWindow instance.
label = QLabel()
label.setText('Hi we\'re testing a skeleton Palette')
btn = QPushButton()
btn.setText('Push')
layout = QHBoxLayout()
layout.addWidget(label)
layout.addWidget(btn)
widget = QWidget()
widget.setLayout(layout)
window.setCentralWidget(widget)
window.show()
app.exec_()