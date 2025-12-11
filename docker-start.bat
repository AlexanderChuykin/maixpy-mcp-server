@echo off
chcp 65001 >nul
echo ============================================================
echo Сборка и запуск Docker контейнера MaixPy MCP Server
echo ============================================================
echo.

echo [1/3] Сборка Docker образа...
docker-compose build

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Ошибка сборки Docker образа!
    pause
    exit /b 1
)

echo.
echo [2/3] Запуск контейнера...
docker-compose up -d

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Ошибка запуска контейнера!
    pause
    exit /b 1
)

echo.
echo [3/3] Проверка статуса...
timeout /t 3 /nobreak >nul
docker-compose ps

echo.
echo ============================================================
echo ✅ MCP сервер запущен!
echo ============================================================
echo.
echo 🌐 URL: http://localhost:8000
echo 📡 SSE Endpoint: http://localhost:8000/sse
echo.
echo Команды управления:
echo   docker-compose logs -f      - просмотр логов
echo   docker-compose stop         - остановка
echo   docker-compose restart      - перезапуск
echo   docker-compose down         - остановка и удаление
echo.
echo Следующий шаг:
echo Добавьте в VS Code settings.json:
echo   "github.copilot.chat.mcp.servers": {
echo     "maixpy-docs": {
echo       "url": "http://localhost:8000/sse"
echo     }
echo   }
echo.
pause
