@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo .venv absent. Lancez d'abord setup.bat
  exit /b 1
)

echo ==^> Starting Jupyter Lab...
".venv\Scripts\python.exe" -m jupyterlab
