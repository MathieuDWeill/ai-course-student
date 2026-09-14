@echo off
setlocal
cd /d "%~dp0"

set "PY="

for %%V in (3.12 3.11 3.10) do (
  if not defined PY (
    py -%%V --version >nul 2>nul
    if not errorlevel 1 set "PY=py -%%V"
  )
)

if not defined PY (
  python --version >nul 2>nul
  if not errorlevel 1 set "PY=python"
)

echo ==^> Using Python
%PY% --version
if errorlevel 1 (
  echo Python introuvable ou version non compatible.
  echo Installez Python 3.11 depuis https://www.python.org/downloads/
  echo Cochez "Add python.exe to PATH", puis relancez setup.bat.
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
