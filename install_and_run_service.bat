@echo off

REM Install Elnotah POS Printers Server service
nssm install "Elnotah POS Printers Server" "C:\Users\Ahmed Elsherif\pos-fastapi\build\Elnotah POS Printers Server\launcher.exe"
REM Start the service
nssm start "Elnotah POS Printers Server"