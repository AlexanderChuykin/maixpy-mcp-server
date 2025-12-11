---
title: maix.thread
---

maix.thread module


> You can use `maix.thread` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### Thread {#Thread}

thread class


> C++ defination code:
> ```cpp
> class Thread
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, func: typing.Callable[[capsule], None], args: capsule = None) -> None
```
create thread

| item | description |
| --- | --- |
| **type** | func |
| **param** | **func**: direction [in], thread function, one `args` parameter, void* type, no return value<br>**args**: direction [in], thread function parameter<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Thread(std::function<void(void *)> func, void *args = nullptr)
> ```
#### join {#join}

```python
def join(self) -> None
```
wait thread exit

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void join()
> ```
#### detach {#detach}

```python
def detach(self) -> None
```
detach thread, detach will auto start thread and you can't use join anymore.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void detach()
> ```
#### joinable {#joinable}

```python
def joinable(self) -> bool
```
Check if thread is joinable

| item | description |
| --- | --- |
| **type** | func |
| **return** | true if thread is joinable |
| **static** | False |

> C++ defination code:
> ```cpp
> bool joinable()
> ```
