@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo .venv absent. Lancez d'abord setup.bat
  exit /b 1
)

".venv\Scripts\python.exe" scripts\check_environment.py
if errorlevel 1 exit /b 1
