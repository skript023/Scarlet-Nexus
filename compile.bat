@echo off
cd "%~dp0\"
pyinstaller --key 030023 -n "Scarlet Nexus" -F -y --clean -i "C:\dbase\tugas\New folder\Ellohim Project\Ellohim.ico" "%~dp0\scarlet_nexus_trainer.py"
pause