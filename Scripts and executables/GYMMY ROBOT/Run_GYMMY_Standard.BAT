echo --- Run_GYMMY_Standard.bat ---

@echo off
cd /d "C:\Users\Administrator\Documents\NetanelAndTal\GM\gymmy_Netanel_Tal"
echo --- Run_GYMMY_Standard.bat ---
echo --- Starting GYMMY (Using poppCodeNew) ---

:: הגדרת הנתיבים לסביבה החדשה שעובדת
SET ENV_DIR=C:\Users\Administrator\.conda\envs\poppCodeNew
SET ANACONDA_BASE=C:\ProgramData\Anaconda3

:: הזרקת ה-DLLs הנדרשים (פותר את שגיאת ה-SSL)
SET PATH=%ENV_DIR%;%ENV_DIR%\Library\bin;%ENV_DIR%\Scripts;%ANACONDA_BASE%\Library\bin;%PATH%

:: הרצת הפייתון מהנתיב המדויק שסימנת בתמונה
"%ENV_DIR%\python.exe" main.py

pause