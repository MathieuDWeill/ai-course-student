@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
  set "PY=py -3"
) else (
  set "PY=python"
)

echo ==^> Using Python
%PY% --version
if errorlevel 1 (
  echo Python introuvable. Installez Python 3.10+ depuis python.org puis relancez.
  exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
  echo ==^> Creating venv in .venv\
  %PY% -m venv .venv
  if errorlevel 1 exit /b 1
) else (
  echo ==^> venv already exists
)

echo ==^> Upgrading pip
".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 exit /b 1

echo ==^> Installing requirements
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 exit /b 1

echo OK Setup complete.
echo Next: run check.bat then run.bat
