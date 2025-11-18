@echo off
REM Go to root of the project
cd /d "%~dp0"

REM Activate the virtual environment
call sphinx_venv\Scripts\activate.bat

sphinx-build -b html -c ./source ../docs ../pfx_docs_build

IF %ERRORLEVEL% NEQ 0 (
    echo Build error.
    exit /b %ERRORLEVEL%
) ELSE (
    echo Build successfull.
)
pause