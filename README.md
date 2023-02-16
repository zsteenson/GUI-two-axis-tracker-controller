# GUI-two-axis-tracker-controller

This is the current GUI version for the two axis controller

To run this program and activate the GUI, gui_wrapper.bat must be run

To change properties to view them on the GUI, go into gui_wrapper.py and change where the properties are defined, rerun the batch file

The batch file creates a virtual environment and installs the required packages, so it will take a minute or so the first run, then instantly on subsequent runs.

REQUIREMENTS:
Python 3 must be installed on users computer and in Environment Variables
  (To test: type "python --version" into command prompt to see if python is in environment variables)
Pip must be installed on users computer and in Environment Variables
  (To test: type "pip --version" into command prompt to see if python is in environment variables)


None of the buttons have functionality yet, as the API/Controller code has not been set up by the rest of the team so the buttons have nothing to communicate with.

the properties are as follows (camel case for the QML file, snake case for python, ONLY edit in the python file)
currDate\n
currTime\n
timeServer\n
siteLongitude\n
siteLatitude\n
timeZone\n
currAz\n
currEL\n
currSunrise\n
currSolarNoon\n
currSunset\n
currAirMass\n
windPort\n
tempPort\n
auxPort\n
windStatus\n
tempStatus\n
auxStatus\n
windStowDelay\n
tempStowDelay\n
auxStowDelay\n
windRecDelay\n
tempRecDelay\n
auxRecDelay\n
currStatus\n
comPosAz\n
actPosAz\n
posErrorAz\n
offsetAz\n
comPosEl\n
actPosEl\n
posErrorEl\n
offsetEl\n
minUpdate\n
motorStatusAZ\n
motorStatusEl\n
limitSwitchStatusEaAZ\n
limitSwitchStatusDnAZ\n
limitSwitchStatusEaEl\n
limitSwitchStatusDnEl\n
\n
