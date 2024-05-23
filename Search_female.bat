@echo off
setlocal
echo ENTER ACTRESS NAME
set /p temp=
cd Data
cls
findstr /I %temp% album_details.csv
endlocal
pause