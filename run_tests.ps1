# Запуск MCP сервера для MaixPy Documentation

# Проверка версии Python
Write-Host "Проверка Python..." -ForegroundColor Cyan
python --version

# Проверка установки MCP
Write-Host "`nПроверка установки MCP..." -ForegroundColor Cyan
pip show mcp | Select-String "Version"

# Проверка структуры документации
Write-Host "`nПроверка документации..." -ForegroundColor Cyan
if (Test-Path "doc_md\api\maix") {
    $fileCount = (Get-ChildItem "doc_md\api\maix" -Recurse -Filter "*.md").Count
    Write-Host "Найдено $fileCount файлов документации в api/maix" -ForegroundColor Green
} else {
    Write-Host "ВНИМАНИЕ: Папка doc_md\api\maix не найдена!" -ForegroundColor Red
}

if (Test-Path "doc_md\doc\en") {
    $fileCount = (Get-ChildItem "doc_md\doc\en" -Recurse -Filter "*.md").Count
    Write-Host "Найдено $fileCount файлов документации в doc/en" -ForegroundColor Green
} else {
    Write-Host "ВНИМАНИЕ: Папка doc_md\doc\en не найдена!" -ForegroundColor Red
}

# Запуск тестов
Write-Host "`nЗапуск тестов..." -ForegroundColor Cyan
python tests\test_server.py

Write-Host "`n" + "="*60 -ForegroundColor Green
Write-Host "Сервер готов к использованию!" -ForegroundColor Green
Write-Host "="*60 -ForegroundColor Green
Write-Host ""
Write-Host "Следующие шаги:" -ForegroundColor Yellow
Write-Host "1. Добавьте конфигурацию в VS Code settings.json (см. QUICKSTART.md)"
Write-Host "2. Перезапустите VS Code"
Write-Host "3. Используйте @workspace в GitHub Copilot Chat"
Write-Host ""
Write-Host "Пример: @workspace Как использовать камеру в MaixPy?" -ForegroundColor Cyan
