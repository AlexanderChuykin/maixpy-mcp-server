# Инструкция по настройке MCP сервера в VS Code

## Шаг 1: Найдите файл настроек VS Code

Откройте файл настроек пользователя VS Code:
- **Windows:** `%APPDATA%\Code\User\settings.json`
- **macOS:** `~/Library/Application Support/Code/User/settings.json`
- **Linux:** `~/.config/Code/User/settings.json`

## Шаг 2: Добавьте конфигурацию MCP

Добавьте или объедините следующую конфигурацию в ваш `settings.json`:

```json
{
  "github.copilot.chat.mcp.servers": {
    "maixpy-docs": {
      "command": "python",
      "args": [
        "c:\\dev\\maixpy_mcp\\mcp_server\\server.py"
      ],
      "env": {}
    }
  }
}
```

**ВАЖНО:** Убедитесь, что путь `c:\\dev\\maixpy_mcp\\mcp_server\\server.py` соответствует вашей системе!

## Шаг 3: Перезапустите VS Code

После добавления конфигурации полностью перезапустите VS Code.

## Шаг 4: Проверка работы

Откройте GitHub Copilot Chat и попробуйте:

```
@workspace Как использовать camera в MaixPy?
```

или

```
@workspace Покажи API для модуля image
```

Copilot должен использовать ваш MCP сервер для получения актуальной документации MaixPy v4.

## Альтернативный способ: через интерфейс VS Code

1. Откройте VS Code
2. Нажмите `Ctrl+,` (или `Cmd+,` на macOS) для открытия настроек
3. Нажмите на иконку файла в правом верхнем углу для открытия `settings.json`
4. Добавьте конфигурацию выше

## Устранение проблем

### Python не найден

Если VS Code не может найти Python:
1. Убедитесь что Python установлен и доступен в PATH
2. Используйте полный путь к Python:
   ```json
   "command": "C:\\Python312\\python.exe"
   ```

### Сервер не запускается

1. Проверьте логи в Output panel (View → Output → GitHub Copilot Chat)
2. Убедитесь что установлены зависимости: `pip list | findstr mcp`
3. Попробуйте запустить сервер вручную: `python mcp_server\server.py`
