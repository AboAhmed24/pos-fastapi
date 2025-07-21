@echo off

REM Stop and remove existing service if present
nssm stop "Elnotah POS Printers Server"
nssm remove "Elnotah POS Printers Server" confirm

echo.
echo Press any key to close...
pause >nul