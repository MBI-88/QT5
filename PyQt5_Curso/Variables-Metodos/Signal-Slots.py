"""
@author: MBI
Descripcion: Descripcion del uso de las señales y los puertos.
"""
#%%==== Package ====#
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5.QtCore import Qt
import  sys,random
#%%==== Clases ====#
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle('My App')
        self.button = QPushButton('Press Me!')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print('Clicked!')

    def the_button_was_toggled(self,checked):
        print('Clicked?',checked)
        self.button_is_checked = checked

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
#%%
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')

        self.button = QPushButton('Press Me!')
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText('You already clicked me.')
        self.button.setEnabled(False)
        self.setWindowTitle('My Oneshot App')

    def the_button_was_toggled(self, checked):
        print('Clicked?', checked)
        self.button_is_checked = checked

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
#%%
window_titles = [
    'My App','Still My App','What on earth','This  is surprising','Something went wrong'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.setWindowTitle('My App')
        self.button = QPushButton('Press Me!')
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print('Clicked')
        new_window_title = random.choice(window_titles)
        print('Setting title: %s'% new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self,window_title):
        print('Window title changed: %s'% window_title)
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()