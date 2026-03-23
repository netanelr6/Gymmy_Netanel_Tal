echo --- Update_To_Tal_Test.bat ---

@echo off
cd /d "C:\Users\Administrator\Documents\NetanelAndTal\GM\Gymmy_Tal"
echo --- Updating Tal Branch ---
git fetch origin Tal_Test
git reset --hard origin/Tal_Test
pause