echo --- Update_To_Main.bat ---

@echo off
cd /d "C:\Users\Administrator\Documents\NetanelAndTal\GM\gymmy_Netanel_Tal"
echo --- Updating Robot to MAIN Branch ---
git checkout main
git fetch origin
git reset --hard origin/main
echo --- System Updated to Main (Official) ---
pause