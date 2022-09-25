@echo off
REM displays ipconfig every 5 seconds
REM VERSION HISTORY: netinfo_console v0.1 Windows-only CMD/Powershell compatible
color 0a

:show
  ipconfig
  timeout /t 5
goto show
