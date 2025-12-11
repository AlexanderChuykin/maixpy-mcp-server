---
title: maix.touchscreen
---

maix.touchscreen module


> You can use `maix.touchscreen` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### TouchScreen {#TouchScreen}

TouchScreen class


> C++ defination code:
> ```cpp
> class TouchScreen
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, device: str = '', open: bool = True) -> None
```
Construct a new TouchScreen object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **device**: touchscreen device path, you can get devices by list_devices method, by default(value is NULL(None in MaixPy)) means the first device<br>**open**: If true, touchscreen will automatically call open() after creation. default is true.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> TouchScreen(const std::string &device = "", bool open = true)
> ```
#### open {#open}

```python
def open(self) -> maix.err.Err
```
open touchscreen device

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err open()
> ```
#### close {#close}

```python
def close(self) -> maix.err.Err
```
close touchscreen device

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err close()
> ```
#### read {#read}

```python
def read(self) -> list[int]
```
read touchscreen device

| item | description |
| --- | --- |
| **type** | func |
| **attention** | This method will discard same event in buffer, that is:<br>if too many move event in buffer when call this method, it will only return the last one,<br>and if read pressed or released event, it will return immediately. |
| **return** | Returns a list include x, y, pressed state |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> read()
> ```
#### read0 {#read0}

```python
def read0(self) -> list[int]
```
read touchscreen device

| item | description |
| --- | --- |
| **type** | func |
| **attention** | This method will return immediately if have event, so it's better to use available() to check if have more event in buffer,<br>or too much event in buffer when your program call this read() interval is too long will make your program slow. |
| **return** | Returns a list include x, y, pressed state |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> read0()
> ```
#### available {#available}

```python
def available(self, timeout: int = 0) -> bool
```
If we need to read from touchscreen, for event driven touchscreen means have event or not

| item | description |
| --- | --- |
| **type** | func |
| **param** | **timeout**: -1 means block, 0 means no block, >0 means timeout, default is 0, unit is ms.<br>|
| **return** | true if need to read(have event), false if not |
| **static** | False |

> C++ defination code:
> ```cpp
> bool available(int timeout = 0)
> ```
#### is\_opened {#is\_opened}

```python
def is_opened(self) -> bool
```
Check if touchscreen is opened

| item | description |
| --- | --- |
| **type** | func |
| **return** | true if touchscreen is opened, false if not |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_opened()
> ```
#### clear {#clear}

```python
def clear(self) -> None
```
Clear touchscreen event buffer

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void clear()
> ```
