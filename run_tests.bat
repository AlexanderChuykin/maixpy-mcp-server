@echo off
chcp 65001 >nul
echo ============================================================
echo Проверка MCP сервера для MaixPy Documentation
echo ============================================================
echo.

echo Проверка Python...
python --version
echo.

echo Проверка установки MCP...
pip show mcp | findstr "Version"
echo.

echo Запуск тестов...
python tests\test_server.py

echo.
echo ============================================================
echo Сервер готов к использованию!
echo ============================================================
echo.
echo Следующие шаги:
echo 1. Добавьте конфигурацию в VS Code settings.json (см. QUICKSTART.md)
echo 2. Перезапустите VS Code
echo 3. Используйте @workspace в GitHub Copilot Chat
echo.
echo Пример: @workspace Как использовать камеру в MaixPy?
echo.
pause
