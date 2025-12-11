---
title: maix.http
---

maix.http module


> You can use `maix.http` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### JpegStreamer {#JpegStreamer}

JpegStreamer class


> C++ defination code:
> ```cpp
> class JpegStreamer
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, host: str = '', port: int = 8000, client_number: int = 16) -> None
```
Construct a new jpeg streamer object

| item | description |
| --- | --- |
| **type** | func |
| **note** | You can get the picture stream through http://host:port/stream, you can also get it through http://ip:port, and you can add personal style through set_html() at this time |
| **param** | **host**: http host<br>**port**: http port, default is 8000<br>**client_number**: the max number of client<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> JpegStreamer(std::string host = std::string(), int port = 8000, int client_number = 16)
> ```
#### start {#start}

```python
def start(self) -> maix.err.Err
```
start jpeg streame

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err start()
> ```
#### stop {#stop}

```python
def stop(self) -> maix.err.Err
```
stop http

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err stop()
> ```
#### write {#write}

```python
def write(self, img: maix.image.Image) -> maix.err.Err
```
Write data to http

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image object<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err write(image::Image *img)
> ```
#### set\_html {#set\_html}

```python
def set_html(self, data: str) -> maix.err.Err
```
add your style in this api\ndefault is:\n<html>\n<body>\n<h1>JPG Stream</h1>\n<img src='/stream'>\n</body>\n</html>

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: html code<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_html(std::string data)
> ```
#### host {#host}

```python
def host(self) -> str
```
Get host

| item | description |
| --- | --- |
| **type** | func |
| **return** | host name |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string host()
> ```
#### port {#port}

```python
def port(self) -> int
```
Get port

| item | description |
| --- | --- |
| **type** | func |
| **return** | port |
| **static** | False |

> C++ defination code:
> ```cpp
> int port()
> ```
