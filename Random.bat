@echo off
:random
set /A rand=%random%
if %rand% leq 540 (echo %rand% && color 0a) else (echo %rand% && goto random)
pause