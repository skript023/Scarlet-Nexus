@echo off
cd "%~dp0\"
pyinstaller --exclude-module _bootlocale -n "Scarlet Nexus" -F -y --clean -i "%~dp0\Ellohim.ico" "%~dp0\gui.py"
pause