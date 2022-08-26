@echo off

:a
	ipconfig
	timeout(5)
goto a

REM // # runs ipconfig in your window, refreshing every 5 seconds
