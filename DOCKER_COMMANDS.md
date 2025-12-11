# 🐳 Шпаргалка по Docker командам

## Быстрый запуск

```powershell
# Автоматический запуск (Windows)
.\docker-start.bat

# Автоматический запуск (Linux/macOS)
./docker-start.sh

# Вручную
docker-compose up -d
```

---

## Основные команды

### Управление контейнером

```powershell
# Запуск
docker-compose up -d

# Остановка
docker-compose stop

# Перезапуск
docker-compose restart

# Остановка и удаление
docker-compose down

# Проверка статуса
docker-compose ps

# Статистика использования ресурсов
docker stats maixpy-mcp-server
```

### Просмотр логов

```powershell
# Все логи
docker-compose logs

# Последние 100 строк
docker-compose logs --tail=100

# В реальном времени
docker-compose logs -f

# Только сервис maixpy-mcp
docker-compose logs -f maixpy-mcp
```

### Сборка и обновление

```powershell
# Пересборка образа
docker-compose build

# Пересборка без кеша
docker-compose build --no-cache

# Пересборка и перезапуск
docker-compose up -d --build

# Остановка, пересборка, запуск
docker-compose down
docker-compose build
docker-compose up -d
```

---

## Отладка

### Вход в контейнер

```powershell
# Открыть shell в контейнере
docker exec -it maixpy-mcp-server /bin/bash

# Запустить команду в контейнере
docker exec -it maixpy-mcp-server python --version

# Проверить Python модули
docker exec -it maixpy-mcp-server pip list
```

### Проверка работы

```powershell
# Проверка endpoint
curl http://localhost:8000/sse

# Windows PowerShell
Invoke-WebRequest http://localhost:8000/sse

# Проверка внутри контейнера
docker exec -it maixpy-mcp-server curl localhost:8000/sse
```

### Просмотр файлов

```powershell
# Список файлов в контейнере
docker exec -it maixpy-mcp-server ls -la /app

# Проверка документации
docker exec -it maixpy-mcp-server ls -la /app/doc_md

# Просмотр файла
docker exec -it maixpy-mcp-server cat /app/mcp_server/server.py
```

---

## Работа с образами

```powershell
# Список образов
docker images | findstr maixpy

# Удаление образа
docker rmi maixpy_mcp-maixpy-mcp

# Удаление неиспользуемых образов
docker image prune

# Информация об образе
docker inspect maixpy_mcp-maixpy-mcp
```

---

## Работа с volumes

```powershell
# Список volumes
docker volume ls

# Информация о volume
docker volume inspect maixpy_mcp_doc_volume

# Удаление неиспользуемых volumes
docker volume prune
```

---

## Очистка

```powershell
# Остановить и удалить все
docker-compose down

# Удалить также volumes
docker-compose down -v

# Полная очистка системы Docker
docker system prune -a

# Очистка с volumes
docker system prune -a --volumes
```

---

## Мониторинг

```powershell
# Использование ресурсов
docker stats maixpy-mcp-server

# Информация о контейнере
docker inspect maixpy-mcp-server

# Процессы в контейнере
docker top maixpy-mcp-server

# Health check
docker exec -it maixpy-mcp-server python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/sse')"
```

---

## Порты

```powershell
# Изменить порт в docker-compose.yml
ports:
  - "8080:8000"  # localhost:8080 -> container:8000

# Проверить используемые порты
docker port maixpy-mcp-server

# Windows: проверить что занимает порт
netstat -ano | findstr :8000
```

---

## Обновление документации

Документация монтирована как volume, изменения применяются сразу:

```powershell
# 1. Обновите файлы в ./doc_md/

# 2. Перезапустите контейнер (пересборка не нужна!)
docker-compose restart

# 3. Проверьте логи
docker-compose logs -f
```

---

## Переменные окружения

### В docker-compose.yml

```yaml
environment:
  - MCP_HOST=0.0.0.0
  - MCP_PORT=8000
  - DEBUG=true  # если добавите поддержку
```

### При запуске

```powershell
# Переопределить порт
MCP_PORT=8080 docker-compose up -d

# Linux/macOS
export MCP_PORT=8080
docker-compose up -d
```

---

## Резервное копирование

```powershell
# Экспорт образа
docker save maixpy_mcp-maixpy-mcp > maixpy-mcp-backup.tar

# Импорт образа
docker load < maixpy-mcp-backup.tar

# Копирование файлов из контейнера
docker cp maixpy-mcp-server:/app/logs ./backup_logs/
```

---

## Полезные алиасы (PowerShell)

Добавьте в профиль PowerShell (`$PROFILE`):

```powershell
# MaixPy MCP Docker алиасы
function mcp-start { docker-compose up -d }
function mcp-stop { docker-compose stop }
function mcp-restart { docker-compose restart }
function mcp-logs { docker-compose logs -f }
function mcp-status { docker-compose ps }
function mcp-shell { docker exec -it maixpy-mcp-server /bin/bash }
function mcp-rebuild { docker-compose down; docker-compose build; docker-compose up -d }
```

---

## Troubleshooting

### Контейнер не запускается

```powershell
# 1. Проверить логи
docker-compose logs

# 2. Проверить порт
netstat -ano | findstr :8000

# 3. Пересобрать без кеша
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Изменения не применяются

```powershell
# 1. Остановить
docker-compose down

# 2. Пересобрать
docker-compose build --no-cache

# 3. Запустить
docker-compose up -d
```

### Проблемы с сетью

```powershell
# Пересоздать сеть
docker network rm maixpy_mcp_mcp-network
docker-compose up -d

# Проверить сети
docker network ls
```

---

## Быстрая справка

| Команда | Описание |
|---------|----------|
| `docker-compose up -d` | Запустить в фоне |
| `docker-compose down` | Остановить и удалить |
| `docker-compose logs -f` | Логи в реальном времени |
| `docker-compose ps` | Статус контейнеров |
| `docker-compose restart` | Перезапустить |
| `docker-compose build` | Пересобрать образ |
| `docker exec -it maixpy-mcp-server bash` | Войти в контейнер |

---

**См. также:**
- [DOCKER_QUICKSTART.md](DOCKER_QUICKSTART.md) - полная инструкция
- [docker-compose.yml](docker-compose.yml) - конфигурация
- [Dockerfile](Dockerfile) - описание образа
