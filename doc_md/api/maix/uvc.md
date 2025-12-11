---
title: maix.uvc
---

maix.uvc module


> You can use `maix.uvc` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}

### helper\_fill\_mjpg\_image {#helper\_fill\_mjpg\_image}

```python
def helper_fill_mjpg_image(buf: capsule, size: int, img: maix.image.Image) -> int
```
helper_fill_mjpg_image

| item | description |
| --- | --- |
| **param** | **buf**: to be filled<br>**size**: to be set<br>**img**: image::Image<br>|
| **return** | int |

> C++ defination code:
> ```cpp
> int helper_fill_mjpg_image(void* buf, uint32_t* size, image::Image *img)
> ```


## Class {#Class}

### UvcServer {#UvcServer}

UvcServer class


> C++ defination code:
> ```cpp
> class UvcServer
> ```

#### set\_cb {#set\_cb}

```python
def set_cb(self, cb: typing.Callable[[capsule, int], int]) -> None
```
set UvcServer's cb

| item | description |
| --- | --- |
| **type** | func |
| **param** | **cb**: callback function<br>|
| **return** | void |
| **static** | False |

> C++ defination code:
> ```cpp
> void set_cb(std::function<int(void* buf, uint32_t* size)> cb)
> ```
#### run {#run}

```python
def run(self) -> None
```
run UvcServer

| item | description |
| --- | --- |
| **type** | func |
| **return** | void |
| **static** | False |

> C++ defination code:
> ```cpp
> void run()
> ```
#### stop {#stop}

```python
def stop(self) -> None
```
stop UvcServer

| item | description |
| --- | --- |
| **type** | func |
| **return** | void |
| **static** | False |

> C++ defination code:
> ```cpp
> void stop()
> ```
#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, cb: typing.Callable[[capsule, int], int] = None) -> None
```
Construct a new jpeg server object

| item | description |
| --- | --- |
| **type** | func |
| **note** | You can get the picture stream through http://host:port/stream, you can also get it through http://ip:port, and you can add personal style through set_html() at this time |
| **static** | False |

> C++ defination code:
> ```cpp
> UvcServer(std::function<int(void* buf, uint32_t* size)> cb = nullptr)
> ```
### UvcStreamer {#UvcStreamer}

UvcStreamer class


> C++ defination code:
> ```cpp
> class UvcStreamer
> ```

#### \_\_init\_\_ {#\_\_init\_\_-2}

```python
def __init__(self) -> None
```
Construct a new jpeg streamer object

| item | description |
| --- | --- |
| **type** | func |
| **note** | You can get the picture stream through http://host:port/stream, you can also get it through http://ip:port, and you can add personal style through set_html() at this time |
| **static** | False |

> C++ defination code:
> ```cpp
> UvcStreamer()
> ```
#### show {#show}

```python
def show(self, img: maix.image.Image) -> maix.err.Err
```
Write data to uvc

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image object<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err show(image::Image *img)
> ```
#### use\_mjpg {#use\_mjpg}

```python
def use_mjpg(self, b: int = 1) -> None
```
use mjpg on uvc

| item | description |
| --- | --- |
| **type** | func |
| **param** | **b**: using mjpg: 0 for NOT, others to use<br>|
| **return** | void |
| **static** | False |

> C++ defination code:
> ```cpp
> void use_mjpg(uint32_t b=1)
> ```
