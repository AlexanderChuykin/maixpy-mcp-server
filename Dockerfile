FROM python:3.11-slim

# Установка рабочей директории
WORKDIR /app

# Копирование файлов зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода сервера
COPY mcp_server/ ./mcp_server/

# Копирование документации
COPY doc_md/ ./doc_md/

# Переменные окружения
ENV MCP_HOST=0.0.0.0
ENV MCP_PORT=8000
ENV PYTHONUNBUFFERED=1

# Открытие порта
EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/sse')" || exit 1

# Запуск сервера в HTTP режиме
CMD ["python", "-m", "mcp_server.server", "--http"]
