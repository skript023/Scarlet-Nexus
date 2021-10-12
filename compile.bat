@echo off
cd "%~dp0\"
pyinstaller --exclude-module _bootlocale -n "Scarlet Nexus" -F -y --clean -i "C:\dbase\tugas\New folder\Ellohim Project\Ellohim.ico" "%~dp0\gui.py"
pause