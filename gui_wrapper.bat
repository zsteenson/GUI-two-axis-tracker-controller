@ECHO OFF

ECHO Path of current working directory for GUI: %~dp0
cd %~dp0

ECHO Creating virtual Environment:

pip install virtualenv
python -m venv venv && (
  ECHO virtual environment created
) || (
  ECHO venv creation failed
)

cd venv
cd Scripts
call activate.bat

cd %~dp0
pip install -r requirements.txt && (
  ECHO required packages installed
) || (
  ECHO installing required packages failed
)


PAUSE

ECHO Press any key to run GUI

python gui_wrapper.py

PAUSE