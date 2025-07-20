@echo off

REM Stop and remove existing service if present
nssm stop"Elnotah Python POS Printers Python Server"
nssm remove "Elnotah Python POS Printers Python Server" confirm


REM Install the service with a name including "Python"
nssm install "Elnotah Python POS Printers Python Server" "C:\Users\Ahmed Elsherif\pos-fastapi\.venv\Scripts\python.exe" launcher.py

REM Set the startup directory (recommended)
nssm set "Elnotah Python POS Printers Python Server" AppDirectory "C:\Users\Ahmed Elsherif\pos-fastapi"

REM Start the service
nssm start "Elnotah Python POS Printers Python Server"



echo.
echo Press any key to close...
pause >nul