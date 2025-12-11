---
title: maix.peripheral.wdt
---

maix.peripheral.wdt module


> You can use `maix.peripheral.wdt` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### WDT {#WDT}

Peripheral wdt class


> C++ defination code:
> ```cpp
> class WDT
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, id: int, feed_ms: int) -> None
```
WDT constructor, after construct, the wdt will auto start.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **id**: direction [in], id of wdt, int type<br>**feed_ms**: direction [in], feed interval, int type, unit is ms, you must feed wdt in this interval, or system will restart.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> WDT(int id, int feed_ms)
> ```
#### feed {#feed}

```python
def feed(self) -> int
```
feed wdt

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code, if feed success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> int feed()
> ```
#### stop {#stop}

```python
def stop(self) -> int
```
stop wdt

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int stop()
> ```
#### restart {#restart}

```python
def restart(self) -> int
```
restart wdt, stop and start watchdog timer.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int restart()
> ```
