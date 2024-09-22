"""
@autor: MBI
Description: Script for development of Style Sheets

Styling Properties:

Property               Type                                     Description
Alignment              top | bottom | left |right | center      Horizontal and/or vertical                         alignment.
Attachment             scroll | fixed                           Scroll or fixed attachment.
Background             Brush | Url | Repeat | Alignment         Compound type of Brush, Url,Repeat,andAlignment.
Boolean                0 | 1                                    True (1) or False (0).
Border                 Border Style | Length | Brush            Shorthand border property.
Border Image           none | Url Number (stretch | repeat)     An image composed of nine parts (top left, top center, top right, center left, center, center right, bottom left, bottom center, and bottom right).
Border Style           dashed | dot-dash | dot-dot-dash |       The pattern used to draw a border.
                       dotted | double | groove |  inset | 
                       outset | ridge |  solid | none 
Box Colors             Brush                                    Up to four values ofBrush, specifying the top, right, bottom, and left edges of a box, respectively. If the left color omitted will copy right, if bottom omitted will copy top.
Box Lengths            Length                                   Up to four values of Length, specifying the top, right, bottom, and left edges of a box, respectively. If the left color omitted will copy right, if bottom omitted will copy top.
Brush                  Color | Gradient | PaletteRole           A Color, Gradient or an entry in the Palette.
Color                  rgb(r,g,b) | rgba(r,g,b,a) |             Specifies a color as RGB (red, green,blue), RGBA (red, green, blue, alpha),HSV (hue, saturation, value), HSVA (hue, saturation, value, alpha), HSL (hue, saturation, lightness), HSLA (hue, saturation, lightness, alpha) or a named color. Thergb()orrgba()syntax can be used with integer values between 0 and 255, or with percentages.
                       hsv(h,s,v) | hsva(h,s,v,a) | 
                       hsl(h,s,l)  | hsla(h,s,l,a) | 
                       #rrggbb  | Color Name
Font                   (Font Style | Font Weight)Font Size      Shorthand font property.
Font Size              Length                                   The size of a font.
Font Style             normal | italic | oblique                The style of a font.
Font Weight            normal | bold | 100 | 200… | 900         The weight of a font.
Gradient               qlineargradient | qradialgradient |      Lineargradients between start and end points. Radialgradients between a focal point and end points on a circle surrounding it. Conical gradients around a center point. See the QLinearGradient documentation for syntax.
                       qconicalgradient
Icon                   Url(disabled | active | normal |         A list of url,QIcon.ModeandQIcon.State. e.g. file-icon: url(file.png), url(file_selected.png) selected;
                       selected) 
                       (on | off)
Length                 Number(px | pt | em | ex)                A number followed by a measurement unit. If no unit is given, uses pixels in most contexts. One of px: pixels pt: the size of one point (i.e., 1/72 of an inch), em: the em `width of the font (i.e., the width of 'M'), ex: the ex width of the font (i.e., the height of 'x') 
Number                 A decimal integer or a real number       e.g. 123, or 12.2312
Origin                 margin | border | padding | content      See box model for more details.

PaletteRole           alternate-base | base |                   These values correspond theColor roles in the widget’sQPalette, e.g.  color: palette(dark);
                      bright-text | button |
                      button-text | dark |
                      highlight |
                      highlighted-text |
                      light | link | linkvisited | mid |
                      midlight | shadow |
                      text | window | window-text
Radius                Length                                    One or two occurrences of Length.
Repeat                repeat-x | repeat-y |                     repeat-x: Repeat horizontally. repeaty: Repeat vertically. repeat: Repeat horizontally and vertically. no-repeat: Don’t repeat.
                      repeat | no-repeat
Url                   url(filename)                             filenameis the name of a file on the local disk or stored usingThe Qt Resource System.


Text styles:

Property                    Type (Default)                             Description
color                       Brush (QPalette Foreground)                The color used to render text.
font                        Font                                       Shorthand notation for setting the text’s font. Equivalent to specifying font-family, font-size, font-style, and/or fontweight 
font-family                 String                                     The font family. 
font-size                   Font Size                                  The font size. In this version of Qt, only pt and px metrics are supported.
font-style                  normal | italic | oblique                  The font style.
font-weight                 Font Weight                                The weight of the font.
selection-backgroundcolor   Brush (QPalette Highlight)                 The background of selected text or items.
selection-color             Brush (Palette HighlightedText)            The foreground ofselected text or items.
text-align                  Alignment                                  The alignment of text and icon within the contents of the widget.
text-decoration             none | underline |overline | line-through  Additional text effects.

Backgrounds:

Property                    Type (Default)                             Description
background                  Background                                 Shorthand notation for setting the background.
                                                                       Equivalent to specifying background-color, background-image,background-repeat,
                                                                       and/or backgroundposition. See also background-origin, selection-backgroundcolor, background-clip,
                                                                       backgroundattachment and alternate-backgroundcolor.
background-color            Brush                                      The background color used for the widget.
background-image            Url                                        The background image used for the widget. Semi-transparent parts of the image let the
                                                                       background-color shine through.
background-repeat           Repeat (both)                              Whether and how the background image is repeated to fill the background-origin rectangle.
background-position         Alignment (top-left)                       The alignment of the background image within the backgroundorigin rectangle.
background-clip             Origin (border)                            The widget’s rectangle, in which the background is drawn.
background-origin           Origin (padding)                           The widget’s background rectangle, to use in conjunction with backgroundposition and background-image


Modify Boxes:

Property                    Type (Default)                             Description
border                      Border                                     Shorthand notation for setting the widget’s border. Equivalent to specifying border-color, border-style,
                                                                       and/or border-width. Also border-top, border-right, border-bottom and  border-left.
border-color                Box Colors (QPaletteForeground)            The color of all the border’s edges.Also border-top-color, border-rightcolor, border-bottom-color, borderleft-color for specific edges.
border-image                Border Image                               The image used to fill the border. The image is cut into nine parts and stretched appropriately if necessary.
border-radius               Radius                                     The radius (curve) of the border’s corners. Also border-top-left-radius, border-top-right-radius, borderbottom-right-radius and borderbottom-left-radius for specific corners.
border-style                Border Style (none)                        The style of all the border’s edges. Also border-top-style, border-rightstyle, border-bottom-style and borderleft-style for specific edges.
border-width                Box Lengths                                The width of the border. Also bordertop-width, border-right-width, borderbottom-width and border-left-width.
margin                      Box Lengths                                The widget’s margins. Also margin-top, margin-right, margin-bottom and margin-left.
outline                                                                The outline drawn around the object’s border.
outline-color               Color                                      The color of the outline. See also border-color
outline-offset              Length                                     The outline’s offset from the border of the widget.
outline-style                                                          Specifies the pattern used to draw the outline. See also border-style
outline-radius                                                         Adds rounded corners to the outline.
                                                                       Also outline-bottom-left-radius, outline-bottom-right-radius, outlinetop-left-radius and outline-topright-radius
padding                     Box Lengths                                The widget’s padding. Also paddingtop, padding-right, padding-bottom and padding-left.

Unints to use:

• px pixels
• pt the size of one point (i.e. 1/72 of an inch)
• em the em width of the font (i.e. the width of 'M')
• ex the ex width of the font (i.e. the height of 'x')

Sizing widget:

Property                  Type (Default)                               Description
max-height                Length                                       The widget’s or a subcontrol’s maximum height.
max-width                 Length                                       The widget’s or a subcontrol’s maximum width.
min-height                Length                                       The widget’s or a subcontrol’s minimum height.
min-width                 Length                                       The widget’s or a subcontrol’s minimum width

Widget specific style:

Property                                    Type (Default)                       Description
alternate-backgroundcolor                   Brush (QPalette AlternateBase)       The alternate background color used in QAbstractItemView subclasses.
background-attachment                       Attachment (scroll)                  Determines whether the background-image in a QAbstractScrollArea is scrolled or fixed with  respect to the viewport.
button-layout                               Number(SH_DialogButtonLayout)        The layout of buttons in a QDialogButtonBox or a QMessageBox. The possible values are 0 (Win), 1 (Mac), 2 (KDE), 3
                                                                                 (Gnome) and 5 (Android).
dialogbuttonbox-buttonshave-icons           Boolean                              Whether the buttons in a QDialogButtonBox show icons. If this property is set to 1, the buttons of a QDialogButtonBox show icons; if it is set to 0, the
                                                                                 icons are not shown.
gridline-color                              Color (SH_Table_GridLineColor)       The color of the grid line in a QTableView
icon                                        Url+                                 The widget icon. The only widget currently supporting this property is QPushButton.
icon-size                                   Length                               The width and height of the icon in a widget.
lineedit-password-character                 Number (SH_LineEdit_PasswordChar     The QLineEdit password character as a Unicode number.
                                            acter)

lineedit-password-mask-delay                Number (SH_LineEdit_PasswordMask     The QLineEdit password mask delay in milliseconds before lineedit-passwordcharacter is applied.
                                            Delay)
messagebox-textinteraction-flags            Number (SH_MessageBox_TextIntera     The interaction behavior for text in a message box.(from Qt.TextInteractionFlags)
                                            ctionFlags)
opacity                                     Number (SH_ToolTipLabel_Opacity)     The opacity for a widget (tooltips only) 0-255.
paint-alternating-rowcolors-for-empty-area  bool                                 Whether a QTreeView paints alternating rows past the end of the data.
show-decoration-selected                    Boolean (SH_ItemView_ShowDecorati    Controls whether selections in a QListView cover the entire row or just the extent of the text.
                                            onSelected)
titlebar-show-tooltipson-buttons            bool                                 Whether tool tips are shown on window title bar buttons.
widget-animationduration                    Number                               How long an animation should last (milliseconds)


Targeting:

Type                                        Example                              Description
Universal                                   *                                    Matches all widgets.
Type                                        QPushButton                          Instances of QPushButton or its subclasses.
Property                                    QPushButton[flat="false"]            Instances of QPushButton that are not flat. Can compare with any property that supports .toString(). Can also use class="classname"
Property contains                           QPushButton[property~="something"]   Instances of QPushButton orwhere property (a list of QString) does not contain the given value.
Class                                     `.QPushButton                          Instances of QPushButton but not subclasses.
ID                                          QPushButton#okButton                 A QPushButton instance whose object name is okButton.
Descendant                                  QDialog QPushButton                  Instances of QPushButton that are descendants (children, grandchildren, etc.) of a QDialog.
Child                                       QDialog > QPushButton                Instances of QPushButton that are immediate children of a QDialog.

Select type:
QAbstractButton {
background: orange;
}

Select all targets:
QWidget {
background: red;
}

Select only target:
.QWidget {
background: orange;
}

Select ID targeting:
combo.setObjectName('thecombo')
le.setObjectName('mylineedit')

Select Property [property="<value>"]:
QPushButton[text="Push me!"] {
background: red;
}

Select Descendant:
QMainWindow QComboBox {
background: yellow;
}
QMainWindow QWidget * {
background: yellow;
}

Select Child (dierct child):
QMainWindow > QWidget {
background: green;
}

Select Inheritance
QLineEdit#mylineedit {
background: blue;
}

Pseudo-selectors:

Pseudo-State                                        Description
:active                                             Widget is part of an active window.
:adjoins-item                                       The ::branch of a QTreeView is adjacent to an item.
:alternate                                          Set for every alternate row when painting the row of a QabstractItemView (QabstractItemView.alternatingRowColors() is True)
:bottom                                             Positioned at the bottom, e.g. a QTabBar that has its tabs at the bottom.
:checked                                            Item is checked, e.g. the checked state of QAbstractButton.
:closable                                           Items can be closed, e.g. a QDockWidget has QdockWidget.DockWidgetClosable enabled.
:closed                                             Item is in the closed state, e.g. an non-expanded item in a QtreeView
:default                                            Item is the default action, e.g. a default QPushButton or a default action in a QMenu.
:disabled                                           Item is disabled.
:editable                                           QcomboBox is editable.
:enabled                                            Item is enabled.
:exclusive                                          Item is part of an exclusive item group, e.g. a menu item in a exclusive QActionGroup.
:first                                              Item is the first in a list, e.g. the first tab in a QtabBar.
:flat                                               Item is flat, e.g. a flat QpushButton.
:floatable                                          Items can be floated, e.g. the QDockWidget has QDockWidget.DockWidgetFloatable enabled.
:focus                                              Item has input focus.
:has-children                                       Item has children, e.g. an item in a QTreeView with child items.
:has-siblings                                       Item has siblings, e.g. an item in a QTreeView with siblings.
:horizontal                                         Item has horizontal orientation
:hover                                              Mouse is hovering over the item.
:indeterminate                                      Item has indeterminate state, e.g. a QCheckBox or QRadioButton is partially checked.
:last                                               Item is the last (in a list), e.g. the last tab in a QTabBar.
:left                                               Item is positioned at the left, e.g. a QTabBar that has its tabs positioned at the left.
:maximized                                          Item is maximized, e.g. a maximized QMdiSubWindow.
:middle                                             Item is in the middle (in a list), e.g. a tab that is not in the beginning or the end in a QTabBar.
:minimized                                          Item is minimized, e.g. a minimized QMdiSubWindow.
:movable                                            Item can be moved around, e.g. the QDockWidget has QDockWidget.DockWidgetMovable enabled.
:no-frame                                           Item has no frame, e.g. a frameless QSpinBox or QLineEdit.
:non-exclusive                                      Item is part of a non-exclusive item group, e.g. a menu item in a non-exclusive QActionGroup.
:off                                                Items that can be toggled, this applies to items in the "off" state.
:on                                                 Items that can be toggled, this applies to widgets in the "on" state
:only-one                                           Item is the only one (in a list), e.g. a lone tab in a QTabBar.
:open                                               Item is in the open state, e.g. an expanded item in a QTreeView, or a QComboBox or` QPushButton` with an open menu.
:next-selected                                      Next item is selected, e.g. the selected tab of a QTabBar is next to this item.
:pressed                                            Item is being pressed using the mouse.
:previous-selected                                  Previous item is selected, e.g. a tab in a QTabBar that is next to the selected tab.
:read-only                                          Item is marked read only or non-editable, e.g. a read only QLineEdit or a non-editable QComboBox.
:right                                              Item is positioned at the right, e.g. a QTabBar that has its tabs positioned at the right.
:selected                                           Item is selected, e.g. the selected tab in a QTabBar or the selected item in a QMenu.
:top                                                Item is positioned at the top, e.g. a QTabBar that has its tabs positioned at the top.
:unchecked                                          Item is unchecked.
:vertical                                           Item has vertical orientation.
:window                                             Widget is a window (i.e a top level widget)


QPushButton:hover { //to a Button
background: red;
}
*:hover { //for all
background: red;
}
QPushButton:!hover { //The button is not yellow while hovering
background: yellow;
}
QCheckBox:checked:!hover {
background: green;
}
QCheckBox:checked:hover {
background: yellow;
}

Styling Widget Sub controls:

Sub-Control                                                       Description
::add-line                                                        Button to move to next line on a QScrollBar.
::add-page                                                        Space between the handle and the add-line of a QScrollBar.
::branch                                                          Branch indicator of a QTreeView.
::chunk                                                           Progress chunk of a QProgressBar.
::close-button                                                    Close button of a QDockWidget or tabs of QTabBar
::corner                                                          Corner between two scrollbars in a QAbstractScrollArea
::down-arrow                                                      Down arrow of a QComboBox, QHeaderView, QScrollBar or QSpinBox.
::down-button                                                     Down button of a QScrollBar or a QSpinBox.
::drop-down                                                       Drop-down button of a QComboBox.
::float-button                                                    Float button of a QDockWidget.
::groove                                                          Groove of a QSlider.
::indicator                                                       Indicator of a QAbstractItemView, a QCheckBox, a QRadioButton, a checkable QMenu item or a checkable QGroupBox.
::handle                                                          Handle of a QScrollBar, a QSplitter, or a QSlider.
::icon                                                            Icon of a QAbstractItemView or a QMenu.
::item                                                            Item of a QAbstractItemView, a QMenuBar, a QMenu, or a QStatusBar.
::left-arrow                                                      Left arrow of a QScrollBar.
::left-corner                                                     Left corner of a QTabWidget, e.g. control the left corner widget in a QTabWidget.
::menu-arrow                                                      Arrow of a QToolButton with a menu.
::menu-button                                                     Menu button of a QToolButton.
::menu-indicator                                                  Menu indicator of a QPushButton.
::right-arrow                                                     Right arrow of a QMenu or a QScrollBar.
::pane                                                            The pane (frame) of a QTabWidget.
::right-corner                                                    The right corner of a QTabWidget. For example, this control can be used to control the position the right corner widget in a QTabWidget.
::scroller                                                        The scroller of a QMenu or QTabBar.
::section                                                         The section of a QHeaderView.
::separator                                                       The separator of a QMenu or in a QMainWindow.
::sub-line                                                        The button to subtract a line of a QScrollBar.
::sub-page                                                        The region between the handle (slider) and the subline of a QScrollBar.
::tab                                                             The tab of a QTabBar or QToolBox.
::tab-bar                                                         The tab bar of a QTabWidget. This subcontrol exists only to control the position of the QTabBar inside the QTabWidget. To style the tabs using the ::tab subcontrol.
::tear                                                            The tear indicator of a QTabBar.
::tearoff                                                         The tear-off indicator of a QMenu.
::text                                                            The text of a QAbstractItemView.
::title                                                           The title of a QGroupBox or a QDockWidget.
::up-arrow                                                        The up arrow of a QHeaderView (sort indicator), QScrollBar or a QSpinBox.
::up-button                                                       The up button of a QSpinBox.

QComboBox::drop-down {
background: yellow;
image: url('puzzle.png')
}
QSpinBox::up-button {
background: green;
}
QSpinBox::down-button {
background: red;
}
QSpinBox::up-button:hover {
background: green;
}
QSpinBox::down-button:hover {
background: red;
}

Positioning Sub-controls:

Property                                   Type (Default)                    Description
position                                   relative | absolute (relative)    Whether offsets specified using left, right, top, and bottom are relative or absolute coordinates.
bottom                                     Length                            If position is relative (the default), moves a subcontrol by a certain
                                                                             offset up; specifying bottom: y is then equivalent to specifying top: -y. If position is absolute, the bottom property specifies the
                                                                             subcontrol’s bottom edge in relation to the parent’s bottom edge (see also subcontrolorigin).
left                                       Length                            If position=relative move a subcontrol right by the given offset (i.e. specifies additional space on the left). If position is absolute, specifies the
                                                                             distance from the left edge of the parent.
right                                      Length                            If position=relative move a subcontrol left by the given offset (i.e. specifies additional space on the right). 
                                                                             If position is  absolute, specifies the distance from the right edge of the parent. 
top                                       Length                             If position=relative move a subcontrol down the given offset (i.e. specifies additional space on the
                                                                             top). If position is absolute, specifies the distance from the top edge of the parent.

QSpinBox {
min-height: 100;
}
QSpinBox::up-button {
width: 50;
}
QSpinBox::down-button {
width: 50;
left: 5;
}

Subcontrol styles:

Property                                 Type (Default)                         Description
image                                    Url+                                   The image that is drawn in the contents rectangle of a subcontrol. Setting the image property on sub controls
                                                                                implicitly sets the width and height of the sub-control (unless the image in a SVG).
image-position                           alignment                              The alignment of the image
                                                                                image’s position can be specified using relative or absolute position. See relative and absolute for explanation. height Length The height of a subcontrol. If you want a widget with a
                                                                                fixed height, set the minheight and max-height to the same value.
spacing                                 Length                                  Internal spacing in the widget.
subcontrol-origin                       Origin (padding)                        The origin rectangle of the subcontrol within the parent element.
subcontrol-position                     Alignment                               The alignment of thesubcontrol within the origin rectangle specified by subcontrol-origin.
width                                   Length                                  The width of a subcontrol. If you want a widget with a fixed width , set the minwidth and max-width to the same value
"""
#==== Packages ====#
import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QColor,QPalette
from PyQt5.QtWidgets import (QApplication,QCheckBox,QComboBox,QLabel,QLineEdit,
QMainWindow,QPlainTextEdit,QPushButton,QSpinBox,QVBoxLayout,QWidget)
#==== Class ====#

class MainWindow(QMainWindow):
    def __init__(self) -> QMainWindow:
        super().__init__()
        self.setWindowTitle('QSS Tester')
        self.editor = QPlainTextEdit()
        self.editor.textChanged.connect(self.update_styles)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        cb = QCheckBox('Checkbox')
        layout.addWidget(cb)

        combo = QComboBox()
        combo.setObjectName('thecomob')
        combo.addItems(['Firt','Second','Third','Fourth'])
        layout.addWidget(combo)

        sb = QSpinBox()
        sb.setRange(0,9999)
        layout.addWidget(sb)

        l = QLabel('This is a label')
        layout.addWidget(l)

        le = QLineEdit()
        le.setObjectName('mylineedit')
        layout.addWidget(le)

        pb = QPushButton('Push me!')
        layout.addWidget(pb)

        self.container = QWidget()
        self.container.setLayout(layout)
        self.setCentralWidget(self.container)

    def update_styles(self) -> None:
        qss = self.editor.toPlainText()
        self.setStyleSheet(qss)

#==== Main ====#
app = QApplication(sys.argv)
app.setStyle('Fusion')
window = MainWindow()
window.show()
app.exec_()

