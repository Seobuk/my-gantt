@echo off
REM WBS Gantt launcher - Python 3.14
REM run.py installs Flask if missing, starts the server, opens the browser.
REM Stop: press Ctrl+C in this window.

cd /d "%~dp0"

py -3.14 run.py
if errorlevel 1 (
  echo.
  echo [ERROR] Failed to run. Check Python 3.14 is installed: py -0p
)

echo.
pause
