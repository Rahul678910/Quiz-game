@echo off
title QuizMaster Launcher
echo Starting QuizMaster GUI Game...

where python3.11 >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    python3.11 quiz_game.py
    goto end
)

where py >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    py quiz_game.py
    goto end
)

where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    python quiz_game.py
    goto end
)

echo Python was not found in PATH!
pause

:end
