#!/usr/bin/python3
import os.path
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from configparser import ConfigParser

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

config_file = "/var/cache/busylight/config.conf"
config = ConfigParser()

# Icons
icons = {
    "off" : QIcon.fromTheme("busylight-off"),
    "red" : QIcon.fromTheme("busylight-red"),
    "green" : QIcon.fromTheme("busylight-green"),
    "blue" : QIcon.fromTheme("busylight-blue"),
    "yellow" : QIcon.fromTheme("busylight-yellow"),
    "white" : QIcon.fromTheme("busylight-white")
    }
    
# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icons["off"])
tray.setVisible(True)
 
# Creating the options
menu = QMenu()
option1 = QAction(icons["green"], "Frei")
option2 = QAction(icons["red"], "Am Telefon")
option3 = QAction(icons["blue"], "In Fernwartung")
option4 = QAction(icons["yellow"], "Beschäftigt")
option1.triggered.connect(lambda: color(icons["green"], 0, 255, 0))
option2.triggered.connect(lambda: color(icons["red"], 255, 0, 0))
option3.triggered.connect(lambda: color(icons["blue"], 0, 0, 255))
option4.triggered.connect(lambda: color(icons["yellow"], 255, 255, 0))
menu.addAction(option1)
menu.addAction(option2)
menu.addAction(option3)
menu.addAction(option4)

menu.addSeparator()

# Farben
submenu = QMenu("Farben")
suboption1 = QAction(icons["green"], "Grün")
suboption2 = QAction(icons["red"], "Rot")
suboption3 = QAction(icons["blue"], "Blau")
suboption4 = QAction(icons["yellow"], "Gelb")
suboption5 = QAction(icons["white"], "Weiß")
suboption1.triggered.connect(lambda: color(icons["green"], 0, 255, 0))
suboption2.triggered.connect(lambda: color(icons["red"], 255, 0, 0))
suboption3.triggered.connect(lambda: color(icons["blue"], 0, 0, 255))
suboption4.triggered.connect(lambda: color(icons["yellow"], 255, 255, 0))
suboption5.triggered.connect(lambda: color(icons["white"], 255, 255, 255))
submenu.addAction(suboption1)
submenu.addAction(suboption2)
submenu.addAction(suboption3)
submenu.addAction(suboption4)
submenu.addAction(suboption5)
menu.addMenu(submenu)
  
menu.addSeparator()  

# Aus
optionOff = QAction(icons["off"], "Aus")
menu.addAction(optionOff)
optionOff.triggered.connect(lambda: color(optionOff.icon))

# To quit the app
optionquit = QAction("Beenden")
optionquit.triggered.connect(lambda: quit())
menu.addAction(optionquit)
  
# Adding options to the System Tray
tray.setContextMenu(menu)

# Function to exit app
def quit():
    if os.path.isfile(config_file):
            config.read(config_file)
            rgb = config["RGB"]
            rgb["red"] = 0
            rgb["green"] = 0
            rgb["blue"] = 0
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Service not running")
        msg.setInformativeText("The background servive that is needed is not running")
        msg.setWindowTitle("ERROR")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()
    app.quit()

# Function to change color
def color(icon=icons["off"], red=0, green=0, blue=0):
    tray.setIcon(QIcon(icon))
    if os.path.isfile(config_file):
            config.read(config_file)
            rgb = config["RGB"]
            rgb["red"] = red
            rgb["green"] = green
            rgb["blue"] = blue
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Service not running")
        msg.setInformativeText("The background servive that is needed is not running")
        msg.setWindowTitle("ERROR")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()

app.exec_()