# Справочник команд MaixPy MCP Server

## Команды установки

```powershell
# Установка зависимостей
pip install -r requirements.txt

# Проверка установки
pip show mcp

# Обновление MCP SDK
pip install --upgrade mcp
```

## Команды тестирования

```powershell
# Запуск всех тестов
python tests\test_server.py

# Или через bat-файл (для Windows)
.\run_tests.bat

# Проверка версии Python
python --version

# Список установленных пакетов
pip list
pip list | findstr mcp
```

## Команды запуска

```powershell
# Ручной запуск сервера (для отладки)
python mcp_server\server.py

# Примечание: Сервер ждет ввода через stdio
# Используйте Ctrl+C для выхода

# В продакшене сервер запускается автоматически через VS Code
```

## Команды проверки

```powershell
# Проверка структуры документации
Get-ChildItem doc_md\api\maix -Recurse -Filter *.md | Measure-Object

# Проверка путей Python
where python

# Проверка переменных окружения
$env:PATH -split ';' | Select-String Python
```

## Конфигурация VS Code

### Найти файл настроек

**Windows:**
```powershell
# Открыть папку с настройками
explorer %APPDATA%\Code\User

# Или прямо файл
notepad %APPDATA%\Code\User\settings.json
```

**Или через VS Code:**
1. `Ctrl + ,` (открыть настройки)
2. Нажать иконку файла справа сверху (открыть settings.json)

### Содержимое конфигурации

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

**Примечания:**
- Используйте двойные обратные слеши `\\` для путей Windows
- Замените путь на актуальный для вашей системы
- Можно указать полный путь к Python, если он не в PATH

## Примеры запросов в Copilot

### Базовые запросы

```
@workspace Список всех модулей MaixPy v4

@workspace Покажи API для модуля camera

@workspace Как использовать image модуль?

@workspace Найди информацию о детекции объектов
```

### Поиск по темам

```
@workspace Как работать с нейронными сетями в MaixPy?

@workspace Покажи примеры работы с WiFi

@workspace Как настроить GPIO в MaixPy v4?

@workspace Примеры работы с дисплеем
```

### Создание кода

```
@workspace Создай скрипт для захвата изображения с камеры

@workspace Напиши код детекции объектов с YOLOv5

@workspace Как подключиться к WiFi и отправить HTTP запрос?
```

## Отладка

### Просмотр логов VS Code

1. `View → Output` (или `Ctrl+Shift+U`)
2. Выбрать `GitHub Copilot Chat` в выпадающем списке
3. Искать сообщения от `maixpy-docs` сервера

### Типичные ошибки

**"Cannot find module mcp"**
```powershell
pip install mcp
```

**"Python not found"**
```json
// В settings.json укажите полный путь:
"command": "C:\\Python312\\python.exe"
```

**"Server connection failed"**
1. Проверьте путь к server.py в settings.json
2. Перезапустите VS Code
3. Проверьте логи в Output панели

### Ручная проверка сервера

```powershell
# Запуск сервера для проверки
python mcp_server\server.py

# Если сервер запускается без ошибок - он работает корректно
# Ctrl+C для выхода
```

## Структура файлов

```
c:\dev\maixpy_mcp\
│
├── mcp_server\
│   ├── __init__.py         # Модуль
│   └── server.py           # Основной код (запускать этот файл)
│
├── tests\
│   └── test_server.py      # Тесты
│
├── doc_md\                 # Документация MaixPy
│   ├── api\
│   └── doc\
│
├── requirements.txt        # Зависимости
├── pyproject.toml         # Конфигурация
├── README.md              # Основная документация
└── ...
```

## Полезные ссылки

**Локальная документация:**
- README.md - основная документация
- QUICKSTART.md - быстрый старт
- CHECKLIST.md - чеклист установки
- USAGE_EXAMPLES.md - примеры использования
- ARCHITECTURE.md - архитектура системы

**Внешние ресурсы:**
- [MaixPy Wiki](https://wiki.sipeed.com/maixpy/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Быстрая справка по инструментам сервера

| Инструмент | Описание | Пример |
|------------|----------|--------|
| `search_docs` | Поиск по документации | Найти "camera" в api |
| `get_api_reference` | API модуля | Получить API для "image" |
| `list_modules` | Список модулей | Все доступные модули |
| `get_tutorial` | Учебные пособия | Туториал по "vision" |
| `read_doc_file` | Чтение файла | Прочитать "api/maix/camera.md" |

## Горячие клавиши VS Code

| Действие | Клавиши |
|----------|---------|
| Открыть настройки | `Ctrl + ,` |
| Открыть Copilot Chat | `Ctrl + Alt + I` |
| Открыть Output панель | `Ctrl + Shift + U` |
| Открыть терминал | `` Ctrl + ` `` |
| Команда палитра | `Ctrl + Shift + P` |

## Обновление сервера

Если вы внесли изменения в код сервера:

1. Сохраните изменения
2. Перезапустите VS Code
3. MCP сервер будет использовать новую версию

Нет необходимости переустанавливать зависимости, если они не изменились.

---

**Нужна помощь?** Проверьте CHECKLIST.md для полного списка шагов установки.
