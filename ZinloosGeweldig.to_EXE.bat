@echo off
cls

cd C:\Users\gebruiker\AppData\Local\Programs\Python\Python37\scripts

pyinstaller      --onefile --clean^
		 --distpath C:\Users\gebruiker\Desktop\MyAppJar\exe^
		 --noconsole C:\Users\gebruiker\Desktop\MyAppJar\ZinloosGeweldig.py

cd C:\Users\gebruiker\Desktop\MyAppJar\exe

echo ""
echo ""
echo  "Wait this file is scanned by Aliens before launced!"
echo ""
echo ""

ZinloosGeweldig.exe



