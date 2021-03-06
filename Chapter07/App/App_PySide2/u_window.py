# -*- coding: utf-8 -*-         #   PYTHON 2   #
from PySide2 import QtWidgets, QtCore, QtGui   # Import of the PySide2.
from u_style import UWin, UWid, UMBar, USBar, UMenu, UTWid


class UWindow(UWin):                           # Create the Main Window.
    
    def __init__(self, parent=None):           # Constructor of the class.
        super(UWindow, self).__init__(parent)  # Initialization of the class.
        self.menubar = UMBar()                 # Menu Bar for main window.
        self.mb1 = UMenu(self.menubar)         # First Menu for Menu Bar.
        self.mb1.addAction("Open")             # Menu, that will create,
        self.mb1.addAction("Save")             # open and save files used
        self.mb1.setTitle("&File")             # in the application.
        self.mb2 = UMenu(self.menubar)         # Second Menu for Menu Bar.
        self.mb2.addAction("Cut")              # Adding of the elements of
        self.mb2.addAction("Copy")             # the Menu that will edit
        self.mb2.addAction("Paste")            # some documents created with
        self.mb2.setTitle("&Edit")             # this app, and set title.
        self.mb3 = UMenu(self.menubar)         # Third Menu for Menu Bar.
        self.mb3.addAction("Settings")         # Add elements to provide 
        self.mb3.addAction("Run")              # some settings, run and
        self.mb3.addAction("Configuration")    # configure some parameters
        self.mb3.setTitle("&Options")          # of the app as some options.
        self.mb4 = UMenu(self.menubar)         # Fourth Menu for Menu Bar.
        self.mb4.addAction("Online Help")      # Provides links to online
        self.mb4.addAction("Documentation")    # help and other docs that
        self.mb4.setTitle("&Help")             # will related to this app.
        self.menubar.addMenu(self.mb1)         # Add first menu to menu bar.
        self.menubar.addMenu(self.mb2)         # Add second menu to menu bar.
        self.menubar.addMenu(self.mb3)         # Add third menu to menu bar.
        self.menubar.addMenu(self.mb4)         # Add fourth menu to menu bar.
        self.setMenuBar(self.menubar)          # And set menu bar to window.
        self.tabwid = UTWid()                  # Tab Widget for main window.
        self.twid1 = UWid()                    # First widget for tab widget.
        self.twid2 = UWid()                    # Second widget for tab.
        self.twid3 = UWid()                    # Third widget for tab widget.
        self.tabwid.addTab(self.twid1, "Applications")
        self.tabwid.addTab(self.twid2, "Visualization")
        self.tabwid.addTab(self.twid3, "Documents")
        self.setCentralWidget(self.tabwid)     # Central widget for tab
        self.stat_bar = USBar()                # widget. Create status bar
        self.setStatusBar(self.stat_bar)       # object. Set status bar.
