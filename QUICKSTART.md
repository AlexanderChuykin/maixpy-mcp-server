# Быстрый старт MaixPy MCP Server

## 1. Установка (уже выполнено ✅)

```powershell
pip install -r requirements.txt
```

## 2. Настройка VS Code

### Вариант A: Автоматическая настройка

Скопируйте содержимое файла `vscode_mcp_config.json` в ваш файл настроек VS Code.

**Путь к файлу настроек:**
- Windows: `%APPDATA%\Code\User\settings.json`
- macOS: `~/Library/Application Support/Code/User/settings.json`
- Linux: `~/.config/Code/User/settings.json`

### Вариант B: Ручная настройка

1. Откройте VS Code
2. Нажмите `Ctrl+,` (настройки)
3. Нажмите иконку файла в правом верхнем углу (откроется settings.json)
4. Добавьте:

```json
{
  "github.copilot.chat.mcp.servers": {
    "maixpy-docs": {
      "command": "python",
      "args": [
        "c:\\dev\\maixpy_mcp\\mcp_server\\server.py"
      ]
    }
  }
}
```

**⚠️ ВАЖНО:** Замените путь на актуальный для вашей системы!

## 3. Перезапустите VS Code

Полностью закройте и откройте VS Code заново.

## 4. Проверка работы

Откройте GitHub Copilot Chat и попробуйте:

```
@workspace Список всех модулей MaixPy v4
```

или

```
@workspace Как использовать камеру в MaixPy?
```

## ✅ Готово!

Теперь вы можете использовать актуальную документацию MaixPy v4 через GitHub Copilot!

---

## Дополнительные ресурсы

- **Примеры использования:** См. `USAGE_EXAMPLES.md`
- **Детальная инструкция:** См. `SETUP_INSTRUCTIONS.md`
- **Тестирование:** `python tests\test_server.py`

## Возможности сервера

✅ Поиск по документации
✅ API справочник модулей
✅ Учебные пособия
✅ Примеры кода
✅ Поддержка русского и английского языков

## Команды для проверки

```powershell
# Проверка установки
pip list | findstr mcp

# Тестовый запуск сервера
python mcp_server\server.py

# Запуск тестов
python tests\test_server.py
```
