# GUI-two-axis-tracker-controller

This is the current GUI version for the two axis controller

To run this program and activate the GUI, gui_wrapper.bat must be run

To change properties to view them on the GUI, go into gui_wrapper.py and change where the properties are defined, rerun the batch file

The batch file creates a virtual environment and installs the required packages, so it will take a minute or so the first run, then instantly on subsequent runs.

REQUIREMENTS:  
Python 3 must be installed on users computer and in Environment Variables  
  (To test: type "python --version" into command prompt to see if python is in environment variables)  
Pip must be installed on users computer and in Environment Variables  
  (To test: type "pip --version" into command prompt to see if Pip is in environment variables)  


None of the buttons have functionality yet, as the API/Controller code has not been set up by the rest of the team so the buttons have nothing to communicate with.

the properties are as follows (camel case for the QML file, snake case for python, ONLY edit in the python file)
currDate  
currTime  
timeServer  
siteLongitude  
siteLatitude  
timeZone  
currAz  
currEL  
currSunrise  
currSolarNoon  
currSunset  
currAirMass  
windPort  
tempPort  
auxPort  
windStatus  
tempStatus  
auxStatus  
windStowDelay  
tempStowDelay  
auxStowDelay  
windRecDelay  
tempRecDelay  
auxRecDelay  
currStatus  
comPosAz  
actPosAz  
posErrorAz  
offsetAz  
comPosEl  
actPosEl  
posErrorEl  
offsetEl  
minUpdate  
motorStatusAZ  
motorStatusEl  
limitSwitchStatusEaAZ  
limitSwitchStatusDnAZ  
limitSwitchStatusEaEl  
limitSwitchStatusDnEl  
