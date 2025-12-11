#!/usr/bin/env python3
"""
MaixPy Documentation MCP Server

Предоставляет доступ к документации MaixPy v4 через Model Context Protocol.
Позволяет LLM моделям получать актуальную информацию о MaixPy API и модулях.
"""

import os
import json
import asyncio
from pathlib import Path
from typing import Any
import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Route
import uvicorn

# Путь к документации относительно корня проекта
DOC_ROOT = Path(__file__).parent.parent / "doc_md"


class MaixPyDocServer:
    """Сервер документации MaixPy"""
    
    def __init__(self):
        self.server = Server("maixpy-docs")
        self.doc_root = DOC_ROOT
        self._setup_handlers()
    
    def _setup_handlers(self):
        """Настройка обработчиков запросов"""
        
        @self.server.list_tools()
        async def list_tools() -> list[types.Tool]:
            """Список доступных инструментов"""
            return [
                types.Tool(
                    name="search_docs",
                    description="Поиск по документации MaixPy. Ищет в заголовках, названиях файлов и содержимом файлов. "
                               "Используйте для поиска модулей, классов, функций или концепций.",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Поисковый запрос (название модуля, функции или ключевое слово)"
                            },
                            "section": {
                                "type": "string",
                                "description": "Раздел для поиска: 'api', 'doc', 'all' (по умолчанию 'all')",
                                "enum": ["api", "doc", "all"]
                            }
                        },
                        "required": ["query"]
                    }
                ),
                types.Tool(
                    name="get_api_reference",
                    description="Получить полную API документацию для конкретного модуля MaixPy. "
                               "Возвращает детальное описание классов, методов и параметров.",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "module_name": {
                                "type": "string",
                                "description": "Название модуля (например: 'image', 'camera', 'nn', 'display')"
                            }
                        },
                        "required": ["module_name"]
                    }
                ),
                types.Tool(
                    name="list_modules",
                    description="Получить список всех доступных модулей MaixPy с кратким описанием",
                    inputSchema={
                        "type": "object",
                        "properties": {}
                    }
                ),
                types.Tool(
                    name="get_tutorial",
                    description="Получить руководство или учебное пособие по конкретной теме. "
                               "Используйте для изучения концепций, примеров использования и best practices.",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "topic": {
                                "type": "string",
                                "description": "Тема (например: 'basic', 'vision', 'audio', 'network', 'peripheral')"
                            },
                            "language": {
                                "type": "string",
                                "description": "Язык документации: 'en' или 'zh' (по умолчанию 'en')",
                                "enum": ["en", "zh"]
                            }
                        },
                        "required": ["topic"]
                    }
                ),
                types.Tool(
                    name="read_doc_file",
                    description="Прочитать конкретный файл документации по относительному пути",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "file_path": {
                                "type": "string",
                                "description": "Относительный путь к файлу (например: 'api/maix/image.md' или 'doc/en/vision/find_blobs.md')"
                            }
                        },
                        "required": ["file_path"]
                    }
                )
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: Any) -> list[types.TextContent]:
            """Вызов инструмента"""
            try:
                if name == "search_docs":
                    result = await self._search_docs(
                        arguments.get("query", ""),
                        arguments.get("section", "all")
                    )
                elif name == "get_api_reference":
                    result = await self._get_api_reference(arguments["module_name"])
                elif name == "list_modules":
                    result = await self._list_modules()
                elif name == "get_tutorial":
                    result = await self._get_tutorial(
                        arguments["topic"],
                        arguments.get("language", "en")
                    )
                elif name == "read_doc_file":
                    result = await self._read_doc_file(arguments["file_path"])
                else:
                    result = f"Неизвестный инструмент: {name}"
                
                return [types.TextContent(type="text", text=result)]
            except Exception as e:
                return [types.TextContent(type="text", text=f"Ошибка: {str(e)}")]
    
    async def _search_docs(self, query: str, section: str = "all") -> str:
        """Поиск по документации"""
        results = []
        query_lower = query.lower()
        
        search_paths = []
        if section in ["api", "all"]:
            search_paths.append(self.doc_root / "api")
        if section in ["doc", "all"]:
            search_paths.append(self.doc_root / "doc")
        
        for search_path in search_paths:
            if not search_path.exists():
                continue
                
            for md_file in search_path.rglob("*.md"):
                try:
                    # Проверка имени файла
                    if query_lower in md_file.stem.lower():
                        rel_path = md_file.relative_to(self.doc_root)
                        results.append({
                            "file": str(rel_path),
                            "match_type": "filename",
                            "preview": f"Файл: {md_file.stem}"
                        })
                        continue
                    
                    # Поиск в содержимом
                    content = md_file.read_text(encoding="utf-8", errors="ignore")
                    lines = content.split("\n")
                    
                    for i, line in enumerate(lines):
                        if query_lower in line.lower():
                            rel_path = md_file.relative_to(self.doc_root)
                            context_start = max(0, i - 1)
                            context_end = min(len(lines), i + 2)
                            context = "\n".join(lines[context_start:context_end])
                            
                            results.append({
                                "file": str(rel_path),
                                "match_type": "content",
                                "line": i + 1,
                                "preview": context[:200]
                            })
                            break  # Один результат на файл для краткости
                
                except Exception as e:
                    continue
        
        if not results:
            return f"Ничего не найдено по запросу: '{query}'"
        
        # Форматирование результатов
        output = [f"Найдено результатов: {len(results)}\n"]
        for i, r in enumerate(results[:10], 1):  # Ограничиваем 10 результатами
            output.append(f"\n{i}. {r['file']}")
            if r['match_type'] == "content":
                output.append(f"   Строка {r['line']}: {r['preview']}")
            else:
                output.append(f"   {r['preview']}")
        
        if len(results) > 10:
            output.append(f"\n... и еще {len(results) - 10} результатов")
        
        return "\n".join(output)
    
    async def _get_api_reference(self, module_name: str) -> str:
        """Получить API документацию модуля"""
        # Поиск в api/maix/
        module_path = self.doc_root / "api" / "maix" / f"{module_name}.md"
        
        if not module_path.exists():
            # Поиск в подпапках
            api_dir = self.doc_root / "api" / "maix"
            for subdir in api_dir.iterdir():
                if subdir.is_dir():
                    potential_path = subdir / f"{module_name}.md"
                    if potential_path.exists():
                        module_path = potential_path
                        break
        
        if not module_path.exists():
            return f"Модуль '{module_name}' не найден. Используйте list_modules для просмотра доступных модулей."
        
        try:
            content = module_path.read_text(encoding="utf-8")
            rel_path = module_path.relative_to(self.doc_root)
            return f"# API Documentation: {module_name}\n\nПуть: {rel_path}\n\n{content}"
        except Exception as e:
            return f"Ошибка чтения файла: {str(e)}"
    
    async def _list_modules(self) -> str:
        """Список всех модулей"""
        api_dir = self.doc_root / "api" / "maix"
        
        if not api_dir.exists():
            return "API директория не найдена"
        
        modules = []
        
        # Модули в корне api/maix/
        for md_file in api_dir.glob("*.md"):
            if md_file.name not in ["README.md", "README2.md"]:
                modules.append({
                    "name": md_file.stem,
                    "path": f"api/maix/{md_file.name}"
                })
        
        # Модули в поддиректориях
        for subdir in api_dir.iterdir():
            if subdir.is_dir():
                for md_file in subdir.glob("*.md"):
                    if md_file.name != "README.md":
                        modules.append({
                            "name": f"{subdir.name}.{md_file.stem}",
                            "path": f"api/maix/{subdir.name}/{md_file.name}"
                        })
        
        modules.sort(key=lambda x: x["name"])
        
        output = ["# Доступные модули MaixPy v4\n"]
        for mod in modules:
            output.append(f"- **{mod['name']}** ({mod['path']})")
        
        return "\n".join(output)
    
    async def _get_tutorial(self, topic: str, language: str = "en") -> str:
        """Получить учебное пособие"""
        doc_path = self.doc_root / "doc" / language / topic
        
        if not doc_path.exists():
            # Попробуем найти точный файл
            doc_file = self.doc_root / "doc" / language / f"{topic}.md"
            if doc_file.exists():
                content = doc_file.read_text(encoding="utf-8")
                return f"# {topic}\n\n{content}"
            
            return f"Тема '{topic}' не найдена. Доступные разделы: basic, vision, audio, network, peripheral, comm, gui, video"
        
        # Если это директория, показываем список файлов
        if doc_path.is_dir():
            files = list(doc_path.glob("*.md"))
            if not files:
                return f"В разделе '{topic}' нет файлов"
            
            output = [f"# Раздел: {topic}\n\nДоступные руководства:\n"]
            for f in sorted(files):
                output.append(f"- {f.stem} (используйте read_doc_file: 'doc/{language}/{topic}/{f.name}')")
            
            # Если есть README, показываем его
            readme = doc_path / "README.md"
            if readme.exists():
                output.append(f"\n## Обзор раздела:\n")
                output.append(readme.read_text(encoding="utf-8"))
            
            return "\n".join(output)
        
        return f"Путь '{doc_path}' не найден"
    
    async def _read_doc_file(self, file_path: str) -> str:
        """Прочитать файл документации"""
        full_path = self.doc_root / file_path
        
        if not full_path.exists():
            return f"Файл не найден: {file_path}"
        
        if not full_path.is_file():
            return f"Путь не является файлом: {file_path}"
        
        try:
            content = full_path.read_text(encoding="utf-8")
            return f"# {file_path}\n\n{content}"
        except Exception as e:
            return f"Ошибка чтения файла: {str(e)}"
    
    async def run_stdio(self):
        """Запуск сервера через stdio (для локального использования)"""
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )
    
    async def run_http(self, host: str = "0.0.0.0", port: int = 8000):
        """Запуск сервера через HTTP/SSE (для Docker)"""
        from starlette.routing import Mount
        
        sse = SseServerTransport("/messages")
        
        # ASGI приложение для SSE
        async def sse_app(scope, receive, send):
            if scope["path"] == "/sse":
                async with sse.connect_sse(scope, receive, send) as streams:
                    await self.server.run(
                        streams[0],
                        streams[1],
                        self.server.create_initialization_options()
                    )
            elif scope["path"] == "/messages" and scope["method"] == "POST":
                await sse.handle_post_message(scope, receive, send)
            else:
                # 404 для неизвестных путей
                await send({
                    'type': 'http.response.start',
                    'status': 404,
                    'headers': [[b'content-type', b'text/plain']],
                })
                await send({
                    'type': 'http.response.body',
                    'body': b'Not Found',
                })
        
        app = Starlette(
            routes=[
                Mount("/", app=sse_app),
            ]
        )
        
        config = uvicorn.Config(app, host=host, port=port, log_level="info")
        server = uvicorn.Server(config)
        await server.serve()


async def main():
    """Точка входа"""
    import sys
    
    server = MaixPyDocServer()
    
    # Определяем режим запуска
    if "--http" in sys.argv:
        # HTTP режим для Docker
        host = os.getenv("MCP_HOST", "0.0.0.0")
        port = int(os.getenv("MCP_PORT", "8000"))
        print(f"🚀 Запуск MCP сервера в HTTP режиме на {host}:{port}")
        await server.run_http(host, port)
    else:
        # Stdio режим для локального использования
        print("🚀 Запуск MCP сервера в stdio режиме", file=sys.stderr)
        await server.run_stdio()


if __name__ == "__main__":
    asyncio.run(main())
