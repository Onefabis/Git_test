@echo off
setlocal enabledelayedexpansion

echo Checking for Python 3 installation...

REM --- Try to find Python 3 executable from system PATH ---
set "PYTHON_CMD="

for %%P in (python.exe py.exe python3.exe) do (
    for /f "tokens=2 delims= " %%V in ('%%P --version 2^>^&1') do (
        echo Found %%P version %%V
        echo %%V | findstr /b "3." >nul
        if !errorlevel! == 0 (
            set "PYTHON_CMD=%%P"
            goto :FoundPython3
        )
    )
)

REM --- No Python 3 found ---
echo.
echo Python 3 not found. Please install it from the official website.
start https://www.python.org/downloads/
pause
exit /b 1

:FoundPython3
echo Using !PYTHON_CMD! for virtual environments.
echo.

REM --- Go to the Sphinx directory ---
cd sphinx
IF ERRORLEVEL 1 (
    echo Failed to navigate to sphinx
    pause
    exit /b 1
)

REM --- Create Python virtual environment for Sphinx ---
!PYTHON_CMD! -m venv sphinx_venv
IF ERRORLEVEL 1 (
    echo Failed to create Sphinx virtual environment
    pause
    exit /b 1
)

REM --- Upgrade pip and install Sphinx requirements ---
sphinx_venv\Scripts\python.exe -m pip install --upgrade pip
sphinx_venv\Scripts\python.exe -m pip install -r requirements.txt

REM --- Go to Myst-Editor directory ---
cd ..\myst-editor
IF ERRORLEVEL 1 (
    echo Failed to navigate to myst-editor
    pause
    exit /b 1
)

REM --- Create Python virtual environment for Myst-Editor ---
!PYTHON_CMD! -m venv myst_venv
IF ERRORLEVEL 1 (
    echo Failed to create Myst-Editor virtual environment
    pause
    exit /b 1
)

REM --- Upgrade pip and install Myst-Editor requirements ---
myst_venv\Scripts\python.exe -m pip install --upgrade pip
myst_venv\Scripts\python.exe -m pip install -r requirements.txt

echo.
echo Setup complete!

REM --- Launch the Sphinx WYSIWYG editor server ---
call launch_myst_editor_server.bat

pause
