# -*- coding: utf-8 -*-         #   PYTHON 2   #
from PySide2 import QtWidgets, QtCore, QtGui   # Importing PySide2 modules.

color = ["rgba(0,41,59,140)", "rgba(0,41,59,255)", 
         "rgba(1,255,217,140)", "rgba(1,255,217,255)"]


class UFonts(object):                          # Will change the fonts.
    
    def __init__(self, parent=None, ls=2.0, ws=2.0, family="Verdana",
                 size=12, weight=34):          # Parameters of the fonts.
        self.font1 = QtGui.QFont()             # Sets fonts to widgets.
        self.font1.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, ls)
        self.font1.setWordSpacing(ws)          # Set spacing between letters
        self.font1.setFamily(family)           # and words, sets font family,
        self.font1.setPixelSize(size)          # sets font size in the pixels
        self.font1.setWeight(weight)           # and font weight of the text.


class UWin(QtWidgets.QMainWindow):             # Class for Main Window.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UWin, self).__init__(parent)     # initialization.
        self.setWindowTitle("U App")           # Title of the application
        win_icon = QtGui.QIcon("Icons/python1.png")
        self.setWindowIcon(win_icon)           # Sets icon.
        self.setWindowOpacity(1)               # Sets widget opacity.
        self.setAnimated(True)                 # Set property  enabled.
        self.setAcceptDrops(True)              # Accept drop event.
        self.setMouseTracking(True)            # Mouse tracking enabled.
        self.setUpdatesEnabled(True)           # Updates enabled.
        self.setAutoFillBackground(True)       # Auto fill of the background.
        self.setStyleSheet("background-color: %s;" % (color[0],))


class UMBar(QtWidgets.QMenuBar):               # Class for Menu Bar.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UMBar, self).__init__(parent)    # initialization.
        self.setStyleSheet("background-color: %s;" % (color[2],))


class UMenu(QtWidgets.QMenu):                  # Class for Menu.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UMenu, self).__init__(parent)    # initialization.
        self.setStyleSheet("background-color: %s;" % (color[2],))


class UTWid(QtWidgets.QTabWidget):             # Class for Tab Widget.

    def __init__(self, parent=None, twbdr=3, twbdw=0.5, twbbg=color[1],
                 tbpad=7, tbsize=140, tbbg=color[0], tbc=color[2],
                 tbcs=color[3]):               # Constructor with parameters.
        super(UTWid, self).__init__(parent)    # initialization of ab widget.
        font = UFonts()                        # Fonts with default params.
        self.setFont(font.font1)               # Sets font to the tab widget.
        self.twbdr = twbdr                     # Parameters of the __init__
        self.twbdw = twbdw                     # function of the class,
        self.twbbg = twbbg                     # that will be used in the
        self.tbsize = tbsize                   # functions of this class to
        self.tbpad = tbpad                     # styling. Parameters of the 
        self.tbbg = tbbg                       # borders size, background
        self.tbc = tbc                         # colors, text colors, size of
        self.tbcs = tbcs                       # the tabs in the tab bar. Set
        self.setStyleSheet(                    # parameters with StyleSheet. 
                """QTabWidget::pane {border-style: solid; border-radius: %spx;
                   border-width: %spx; border-color: %s;}
                   QTabBar::tab {width: %spx; margin: 0px; padding: %spx;
                   background-color: %s; color: %s; border-style: solid;
                   border-top-right-radius: 10px; border-width: %spx;
                   border-bottom-width: 0px; border-color: %s;}
                   QTabBar::tab:selected {background-color: %s; color: %s;}
                   QTabBar::tab:!selected {margin-top: 5px;}
                   QTabBar QToolButton {color: %s;}"""
                   % (self.twbdr, self.twbdw, self.twbbg, self.tbsize,
                      self.tbpad, self.tbbg, self.tbc, self.twbdw, self.tbbg,
                      self.twbbg, self.tbcs, self.tbcs))


class USBar(QtWidgets.QStatusBar):             # Class for Status Bar.

    def __init__(self, parent=None):           # Constructor of the class and
        super(USBar, self).__init__(parent)    # initialization.
        self.setStyleSheet("background-color: %s;" % (color[2],))


class UWid(QtWidgets.QWidget):                 # Class for Widget.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UWid, self).__init__(parent)     # initialization.
        self.setWindowTitle("U App")           # Title of the application
        win_icon = QtGui.QIcon("Icons/python1.png")
        self.setWindowIcon(win_icon)           # Sets icon.
        self.setWindowOpacity(0.95)            # Sets widget opacity.
        self.setAcceptDrops(True)              # Accept drop event.
        self.setMouseTracking(True)            # Mouse tracking is enabled.
        self.setUpdatesEnabled(True)           # Updates enabled.
        self.setAutoFillBackground(True)       # Auto fill of the background.
        self.setStyleSheet("background-color: %s;" % (color[0],))


class UFrame(QtWidgets.QFrame):                # Class for Frame.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UFrame, self).__init__(parent)   # initialization of the frame.
        self.setStyleSheet("background-color: %s;" % (color[2],))


class ULabel(QtWidgets.QLabel):                # Class for Label.

    def __init__(self, parent=None):           # Constructor of the class and
        super(ULabel, self).__init__(parent)   # initialization of the label.
        font = UFonts(ls=3.0, size=14, weight=59)
        self.setFont(font.font1)               # Sets font with params.
        self.setStyleSheet(                    # Styling of the Label,
                """background-color: %s; color: %s;""" 
                % (color[0], color[3]))        # background and text colors.


class ULineEd(QtWidgets.QLineEdit):            # Class for Line Edit field.

    def __init__(self, parent=None, tmrgl=10, tmrgt=10, tmrgr=10, tmrgb=10,
                 drg=True, bdr=5, bdw=1, bdc=color[3]):
        super(ULineEd, self).__init__(parent)  # initialization of the field.
        self.setClearButtonEnabled(True)       # Button to clear input.
        self.setDragEnabled(drg)               # Set drag enabled and text 
        self.setTextMargins(tmrgl, tmrgt, tmrgr, tmrgb)  # margins to each
        self.bdr = bdr                         # side from params of the 
        self.bdw = bdw                         # __init__, such as border
        self.bdc = bdc                         # radius, width and color.
        font = UFonts(size=14, weight=59)      # The class for font changes.
        self.setFont(font.font1)               # Sets font with params.
        self.setStyleSheet(                    # Styling of the Line Edit,
                """background-color: %s; color: %s; border-radius: %spx;
                border-width: %spx; border-color: %s;""" 
                % (color[0], color[3], self.bdr, self.bdw, self.bdc))


class UTextEd(QtWidgets.QTextEdit):            # Class for Text Edit field.

    def __init__(self, parent=None, bgcolor=color[0], sbh=7, sbv=7,
                 sbc=color[1], tepad=7, tebgcolor=color[1], tetxc=color[3],
                 lh=14, bdr=5, bdw=1, bdc=color[3]):
        super(UTextEd, self).__init__(parent)  # initialization of the field.
        self.setAcceptRichText(True)           # Rich text will accepted.
        self.setUndoRedoEnabled(True)          # undoes and redoes enabled.
        self.bgcolor = bgcolor                 # Properties from __init__
        self.sbh = sbh                         # function to set style for:
        self.sbv = sbv                         # background color of the 
        self.sbc = sbc                         # widget, width, height and
        self.tepad = tepad                     # background color for scroll
        self.tebgcolor = tebgcolor             # bars of the text field, 
        self.tetxc = tetxc                     # padding for text field from 
        self.lh = lh                           # text field frame to texts,
        self.bdr = bdr                         # text color, background color
        self.bdw = bdw                         # of the field, line height of
        self.bdc = bdc                         # the text and field borders.
        font = UFonts(size=14, weight=59)      # The class for font changes.
        self.setFont(font.font1)               # Sets font with parameters.
        self.setStyleSheet(                    # Styling of the Text Edit.
                """QWidget {background-color: %s;}
                   QScrollBar:horizontal {width: %spx; height: %spx;
                                          background-color: %s;}
                   QScrollBar:vertical {width: %spx; height: %spx;
                                        background-color: %s;}
                   QTextEdit {padding: %spx; background-color: %s;
                              color: %s; line-height: %spx;
                              border-style: solid; border-radius: %spx;
                              border-width: %spx; border-color: %s;}"""
                              % (self.bgcolor, self.sbh, self.sbv, self.sbc,
                                 self.sbh, self.sbv, self.sbc, self.tepad,
                                 self.tebgcolor, self.tetxc, self.lh,
                                 self.bdr, self.bdw, self.bdc))
