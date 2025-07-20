@echo off

REM Stop and remove existing service if present
nssm stop "Elnotah POS Printers Server"
nssm remove "Elnotah POS Printers Server" confirm

REM Install Elnotah POS Printers Server service
nssm install "Elnotah POS Printers Server" "C:\Elnotah POS Printers Server\launcher.exe"
REM Start the service
nssm start "Elnotah POS Printers Server"

echo.
echo Press any key to close...
pause >nul