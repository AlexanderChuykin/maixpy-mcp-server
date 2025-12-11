"""
Тестовый скрипт для проверки работы MCP сервера
"""

import asyncio
import json
from pathlib import Path

# Добавить родительскую директорию в путь
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from mcp_server.server import MaixPyDocServer


async def test_server():
    """Тест основных функций сервера"""
    
    server = MaixPyDocServer()
    
    print("=" * 60)
    print("Тестирование MCP сервера MaixPy Documentation")
    print("=" * 60)
    
    # Тест 1: Список модулей
    print("\n1. Тест: Список модулей")
    print("-" * 60)
    result = await server._list_modules()
    print(result[:500])  # Первые 500 символов
    
    # Тест 2: Поиск по документации
    print("\n2. Тест: Поиск 'camera'")
    print("-" * 60)
    result = await server._search_docs("camera", "all")
    print(result[:500])
    
    # Тест 3: Получение API документации
    print("\n3. Тест: API для модуля 'image'")
    print("-" * 60)
    result = await server._get_api_reference("image")
    print(result[:500])
    
    # Тест 4: Получение туториала
    print("\n4. Тест: Туториал по 'vision'")
    print("-" * 60)
    result = await server._get_tutorial("vision", "en")
    print(result[:500])
    
    # Тест 5: Чтение конкретного файла
    print("\n5. Тест: Чтение файла 'api/maix/camera.md'")
    print("-" * 60)
    result = await server._read_doc_file("api/maix/camera.md")
    print(result[:500])
    
    print("\n" + "=" * 60)
    print("Тестирование завершено!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(test_server())
