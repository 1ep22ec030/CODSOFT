@echo off
title CODSOFT AI Tasks
cd /d "%~dp0"

set "PYTHON_CMD="
where python >nul 2>nul
if "%errorlevel%"=="0" set "PYTHON_CMD=python"

if "%PYTHON_CMD%"=="" (
    where py >nul 2>nul
    if "%errorlevel%"=="0" set "PYTHON_CMD=py"
)

if "%PYTHON_CMD%"=="" (
    echo Python was not found on this computer.
    echo Install Python 3.10 or newer from https://www.python.org/downloads/
    echo During installation, select "Add Python to PATH".
    pause
    exit /b 1
)

:menu
cls
echo ==============================
echo        CODSOFT AI Tasks
echo ==============================
echo.
echo 1. Task 1 - Rule-Based Chatbot
echo 2. Task 2 - Tic-Tac-Toe AI
echo 3. Task 4 - Recommendation System
echo 4. Exit
echo.
set /p choice=Choose an option from 1 to 4: 

if "%choice%"=="1" (
    cls
    %PYTHON_CMD% task1_chatbot\chatbot.py
    pause
    goto menu
)

if "%choice%"=="2" (
    cls
    %PYTHON_CMD% task2_tictactoe_ai\tictactoe.py
    pause
    goto menu
)

if "%choice%"=="3" (
    cls
    %PYTHON_CMD% task4_recommendation_system\recommender.py
    pause
    goto menu
)

if "%choice%"=="4" (
    exit
)

echo Invalid option. Please choose 1, 2, 3, or 4.
pause
goto menu
