# importing the required libraries 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # this will hide the title bar 
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # set the title
        self.setWindowTitle("No Title")

        # setting the geometry of window
        self.setGeometry(100, 100, 400, 300)

        # creating a label widget
        self.label_1 = QLabel('No Title Bar', self)

        # moving position
        self.label_1.move(100, 100)

        # setting up border and background color
        self.label_1.setStyleSheet("background-color: green; border: 3px solid green; color: white; padding: 10px;")

        # Add a close button for better testing
        self.close_button = QPushButton("Close", self)
        self.close_button.setGeometry(150, 200, 100, 40)
        self.close_button.clicked.connect(self.close)
        
        # Ensure background color is set to avoid full transparency
        self.setStyleSheet("background-color: rgba(0, 0, 0, 50); border-radius: 10px;")

# Create PyQt5 app
App = QApplication(sys.argv)

# Create the instance of our Window
window = Window()  # Keep a persistent reference

App.setQuitOnLastWindowClosed(False)

# Adding an icon 
icon = QIcon("./logo.png")

# Adding item on the menu bar 
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Creating the options 
menu = QMenu()
option1 = QAction("Show Window")
option1.triggered.connect(window.show)  # Fix: Ensure persistent window reference
menu.addAction(option1)

# To quit the app 
quit_action = QAction("Quit")
quit_action.triggered.connect(App.quit)
menu.addAction(quit_action)

# Adding options to the System Tray 
tray.setContextMenu(menu)

# Start the app
App.exec_()
