@echo off
cls
set PATH=%PATH%;C:\Python27\
:my_loop
IF %1=="" GOTO completed
  python C:\Python27\work\Subscene-subtitle\subsceneSub.py %1
  SHIFT
  GOTO my_loop
:completed
