"""
@autor: MBI
Description: Script for development of Ui Styles and palettes.

Stayles:
To enable the style, call .setStyle() on the QApplication instance, passing in
the name of the style (in this case Fusion) as a string.

• Qt Modern provides a frameless window style, together with a dark mode
palette and custom window decorations to give a modern macOS-like look.

• Frameless Window Darkstyle provides a frameless window, dark mode
palette and Windows 10-like window decorations.

Palettes:

Constant                  Value    Description
QPalette.Window           10       Background color for windows.
QPalette.WindowText       0        Default text color for windows.
QPalette.Base             9        Background of text entry widgets, combobox drop down lists and toolbar handles. Usually white or light
QPalette.AlternateBase    16       Second Base color used in striped (alternating) rows — e.g. QAbstractItemView.setAlternatingRowColors()
QPalette.ToolTipBase      18       Background color for QToolTip and QWhatsThis hover indicators. Both tips use the Inactive group (see later) because they are not active windows.
QPalette.ToolTipText      19       Foreground color for QToolTip and QWhatsThis. Both tips use the Inactive group (see later) because they are not active windows.
QPalette.PlaceholderText  20       Color for placeholder text in widgets.
QPalette.Text             6        Text color for widgets colored with Base background. Must provide a good contrast with both Window and Base.
QPalette.Button           1        Default button background color. This can differ from Window but must provide good contrast with ButtonText.
QPalette.ButtonText       8        Text color used on buttons, must contrast with Button color.
QPalette.BrightText       7        Text color which is very different from WindowText, contrasts well with black. Used were other Text and WindowText colors would give poor contrast. Note: Not just used for text



There are also smaller sets of roles used for 3D beveling on widgets and
highlighting selected entries or links.

Constant                 Value     Description
QPalette.Light           2         Lighter than Button color.
QPalette.Midlight        3         Between Button and Light.
QPalette.Dark            4         Darker than Button.
QPalette.Mid             5         Between Button and Dark.
QPalette.Shadow          11        A very dark color. By default, the shadow color is Qt.black



Constant                 Value     Description
QPalette.Highlight       12        A color to indicate a selected item or the current item. By default, the highlight color is Qt.darkBlue.
QPalette.HighlightedText 13        A text color that contrasts with Highlight. By default, the highlighted text Qt.white.
QPalette.Link            14        A text color used for unvisited hyperlinks. By default, the link color is Qt.blue.
QPalette.LinkVisited     15        A text color used for already visited hyperlinks. By default, the link-visited color is Qt.magenta


For parts of the UI which change when a widget is active, inactive or disabled
you must set a color for each of these states. To do this, you can call
palette.setColor(group, role, color) passing additional group parameter. The
available groups are shown below — 

Constant                           Value
QPalette.Disabled                  1
QPalette.Active                    0
QPalette.Inactive                  2
QPalette.Normal synonym for Active 0

palette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.white)
"""
#==== Packages ====#
from PyQt5.QtWidgets import QApplication,QLabel, QStyle
from PyQt5.QtGui import QPalette,QColor
from PyQt5.QtCore import Qt 
import sys

#==== App ====#
app = QApplication(sys.argv)
palette = QPalette()
palette.setColor(QPalette.Window,QColor(0,128,255))
palette.setColor(QPalette.WindowText,Qt.white)
app.setStyle('Fusion')
app.setPalette(palette)
label = QLabel('Palette Test')
label.show()
app.exec_()


