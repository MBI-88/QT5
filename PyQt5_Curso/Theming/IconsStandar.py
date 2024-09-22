"""
@autor: MBI
Description: Script for development of Icons Standard


The icons are accessible through the current application style using
QStyle.standardIcon(name) or QStyle.<constant>. The full table of built-in icon names is shown below — 

SP_ArrowBack               SP_DirIcon                     SP_MediaSkipBackward
SP_ArrowDown               SP_DirLinkIcon                 SP_MediaSkipForward
SP_ArrowForward            SP_DirOpenIcon                 SP_MediaStop
SP_ArrowLeft               SP_DockWidgetCloseButton       SP_MediaVolume
SP_ArrowRight              SP_DriveCDIcon                 SP_MediaVolumeMuted
SP_ArrowUp                 SP_DriveDVDIcon                SP_MessageBoxCritical
SP_BrowserReload           SP_DriveFDIcon                 SP_MessageBoxInformation
SP_BrowserStop             SP_DriveHDIcon                 SP_MessageBoxQuestion
SP_CommandLink             SP_DriveNetIcon                SP_MessageBoxWarning
SP_ComputerIcon            SP_FileDialogBack              SP_TitleBarCloseButton
SP_CustomBase              SP_FileDialogContentsView      SP_TitleBarContextHelpButton
SP_DesktopIcon             SP_FileDialogDetailedView      SP_TitleBarMaxButton
SP_DialogApplyButton       SP_FileDialogEnd               SP_TitleBarMenuButton
SP_DialogCancelButton      SP_FileDialogInfoView          SP_TitleBarMinButton
SP_DialogCloseButton       SP_FileDialogListView          SP_TitleBarNormalButton
SP_DialogDiscardButton     SP_FileDialogNewFolder         SP_TitleBarShadeButton
SP_DialogHelpButton        SP_FileDialogStart             SP_TitleBarUnshadeButton
SP_DialogNoButton          SP_FileDialogToParent          SP_ToolBarHorizontalExtensionButton
SP_DialogOkButton          SP_FileIcon                    SP_ToolBarVerticalExtensionButton
SP_DialogResetButton       SP_FileLinkIcon                SP_TrashIcon
SP_DialogSaveButton        SP_MediaPause                  SP_VistaShield
SP_DialogYesButton         SP_MediaPlay                   SP_DirClosedIcon
SP_MediaSeekBackward       SP_DirHomeIcon                 SP_MediaSeekForward

You can access these icons directly via the QStyle namespace, as follows.
style = button.style() # Get the QStyle object from the widget.
icon = style.standardIcon(QStyle.SP_MessageBoxCritical)
button.setIcon(icon)

You can also use the style object from a specific widget. It doesn’t matter
which you use, since we’re only accessing the built-ins anyway.
style = button.style() # Get the QStyle object from the widget.
icon = style.standardIcon(style.SP_MessageBoxCritical)
button.setIcon(icon)

To get list of supported image formats on your own platform you can call 
QtGui.QImageReader.supportedImageFormats()
"""
#==== Packages ====#
from PyQt5.QtWidgets import QApplication,QPushButton
from PyQt5.QtGui import QIcon
import sys

#==== Main ====# 
app = QApplication(sys.argv)
button = QPushButton('Hello')
icon = QIcon.fromTheme('document-new') # Get icon from your self os.(Linux)
button.setIcon(icon)
button.show()
app.exec_()
