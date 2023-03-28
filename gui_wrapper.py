# Set up virtual environment for 1st Time users
import os
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QTimer, QObject
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from datetime import datetime

TIME_SERVER = "00:00:00"
SITE_LONGITUDE = 105.19
SITE_LATITUDE = 39.74
TIME_ZONE = '7'

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('Screen02.qml')

# Variables Changed and Running on a Time Loop
# Used for Time, Date, curr_AZ, curr_EL, command_AZ
# command_El, command_AZ
def update_time_and_date_az_el():
    # Time and Date
    curr_date = "1/1/2023"
    curr_time = "00:00:00"
    engine.rootObjects()[0].setProperty('currDate', curr_date)
    engine.rootObjects()[0].setProperty('currTime', curr_time)
    
    # Azimuth and Elevation
    currAz = 0.0
    currEl = 0.0
    engine.rootObjects()[0].setProperty('currAz', '%0.6f' % currAz)
    engine.rootObjects()[0].setProperty('currEl', '%0.6f' % currEl)


timer = QTimer()
timer.setInterval(500)  # msecs 100 = 1/10th sec
timer.timeout.connect(update_time_and_date_az_el)
timer.start()

# All non-updating properties in top box
engine.rootObjects()[0].setProperty('timeServer', str(TIME_SERVER))
engine.rootObjects()[0].setProperty('siteLongitude', str(SITE_LONGITUDE))
engine.rootObjects()[0].setProperty('siteLatitude', str(SITE_LATITUDE))
engine.rootObjects()[0].setProperty('timeZone', str(TIME_ZONE))

# All other properties
# TODO: Set properties in loop that are needed to recieve JSON
# Packages, Currently just strings of 0s until controller code can run
currSunrise = "00.00"
currSolarNoon = "00.00"
currSunset = "00.00"
currAirMass = "00.00"
windPort = "00.00"
tempPort = "00.00"
auxPort = "00.00"
windStatus = "00.00"
tempStatus = "00.00"
auxStatus = "00.00"
windStowDelay = "00.00"
tempStowDelay = "00.00"
auxStowDelay = "00.00"
windRecDelay = "00.00"
tempRecDelay = "00.00"
auxRecDelay = "00.00"
currStatus = "00.00"
comPosAz = "00.00"
actPosAz = "00.00"
posErrorAz = "00.00"
offsetAz = "00.00"
comPosEl = "00.00"
actPosEl = "00.00"
posErrorEl = "00.00"
offsetEl = "00.00"
minUpdate = "00.00"
motorStatusAZ = "00.00"
motorStatusEl = "00.00"
limitSwitchStatusEaAZ = "00.00"
limitSwitchStatusDnAZ = "00.00"
limitSwitchStatusEaEl = "00.00"
limitSwitchStatusDnEl = "00.00"

# Set Properties in QML
engine.rootObjects()[0].setProperty('currSunrise', currSunrise)
engine.rootObjects()[0].setProperty('currSolarNoon', currSolarNoon)
engine.rootObjects()[0].setProperty('currSunset', currSunset)
engine.rootObjects()[0].setProperty('currAirMass', currAirMass)
engine.rootObjects()[0].setProperty('windPort', windPort)
engine.rootObjects()[0].setProperty('tempPort', tempPort)
engine.rootObjects()[0].setProperty('auxPort', auxPort)
engine.rootObjects()[0].setProperty('windStatus', windStatus)
engine.rootObjects()[0].setProperty('tempStatus', tempStatus)
engine.rootObjects()[0].setProperty('auxStatus', auxStatus)
engine.rootObjects()[0].setProperty('windStowDelay', windStowDelay)
engine.rootObjects()[0].setProperty('tempStowDelay', tempStowDelay)
engine.rootObjects()[0].setProperty('auxStowDelay', auxStowDelay)
engine.rootObjects()[0].setProperty('windRecDelay', windRecDelay)
engine.rootObjects()[0].setProperty('tempRecDelay', tempRecDelay)
engine.rootObjects()[0].setProperty('auxRecDelay', auxRecDelay)
engine.rootObjects()[0].setProperty('currStatus', currStatus)
engine.rootObjects()[0].setProperty('comPosAz', comPosAz)
engine.rootObjects()[0].setProperty('actPosAz', actPosAz)
engine.rootObjects()[0].setProperty('posErrorAz', posErrorAz)
engine.rootObjects()[0].setProperty('offsetAz', offsetAz)
engine.rootObjects()[0].setProperty('comPosEl', comPosEl)
engine.rootObjects()[0].setProperty('actPosEl', actPosEl)
engine.rootObjects()[0].setProperty('posErrorEl', posErrorEl)
engine.rootObjects()[0].setProperty('offsetEl', offsetEl)
engine.rootObjects()[0].setProperty('minUpdate', minUpdate)
engine.rootObjects()[0].setProperty('motorStatusAZ', motorStatusAZ)
engine.rootObjects()[0].setProperty('motorStatusEl', motorStatusEl)
engine.rootObjects()[0].setProperty('limitSwitchStatusEaAZ', limitSwitchStatusEaAZ)
engine.rootObjects()[0].setProperty('limitSwitchStatusDnAZ', limitSwitchStatusDnAZ)
engine.rootObjects()[0].setProperty('limitSwitchStatusEaEl', limitSwitchStatusEaEl)
engine.rootObjects()[0].setProperty('limitSwitchStatusDnEl', limitSwitchStatusDnEl)

#################################
# Button Functionality
#################################

# Emergency Wind Stow
def emergencyWindStow():
    print('Emergency Wind Stow')
    
win = engine.rootObjects()[0]

emergency_wind_stow = win.findChild(QObject, "emergency_wind_stow")
emergency_wind_stow.messageRequired.connect(emergencyWindStow)

# Run Command Button
def runCommand():
    print("Running Command...")
    
run_command = win.findChild(QObject, "run_command_button")
run_command.messageRequired.connect(runCommand)

# Upload Batch File Button
def uploadBatchFile():
    print("Uploading Batch File...")
    
upload_batch_file = win.findChild(QObject, "upload_batch_file")
upload_batch_file.messageRequired.connect(uploadBatchFile)

# Run Batch File Button
def runBatchFile():
    print("Running Batch File...")
    
run_batch_file = win.findChild(QObject, "run_batch_file")
run_batch_file.messageRequired.connect(runBatchFile)

sys.exit(app.exec()) 