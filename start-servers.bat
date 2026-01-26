@echo off
echo ========================================
echo Finance Dashboard - Starting Servers
echo ========================================
echo.

echo [1/2] Starting Backend (FastAPI)...
start "Backend Server" powershell -NoExit -Command "cd backend; C:/WORKSPACE_PULSE/copilot-example/.venv/Scripts/python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000"

echo Waiting for backend to initialize...
timeout /t 3 /nobreak >nul

echo.
echo [2/2] Starting Frontend (Vite)...
start "Frontend Server" powershell -NoExit -Command "cd frontend; npm run dev"

echo.
echo ========================================
echo Servers are starting...
echo ========================================
echo.
echo Backend:  http://127.0.0.1:8000
echo Frontend: http://localhost:5173
echo API Docs: http://127.0.0.1:8000/docs
echo.
echo Press any key to open frontend in browser...
pause >nul

start http://localhost:5173

echo.
echo Both servers are running in separate windows.
echo Close those windows to stop the servers.
echo.
pause
