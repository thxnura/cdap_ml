@echo off

rem Define the path to your virtual environment
set VENV_PATH=C:\Users\thxnura\Downloads\py\api\myenv

rem Activate the virtual environment
call %VENV_PATH%\Scripts\activate

rem Run your Python script (index.py)
python index.py

rem Deactivate the virtual environment
deactivate
