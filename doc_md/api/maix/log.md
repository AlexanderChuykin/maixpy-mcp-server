---
title: maix.log
---

maix.log module


> You can use `maix.log` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### LogLevel {#LogLevel}

Error log level enums

| item | describe |
| --- | --- |
| **values** | **LEVEL_NONE**: <br>**LEVEL_ERROR**: <br>**LEVEL_WARN**: <br>**LEVEL_INFO**: <br>**LEVEL_DEBUG**: <br>**LEVEL_MAX**: <br>
> C++ defination code:
> ```cpp
> enum class LogLevel
>     {
>         LEVEL_NONE  = 0,
>         LEVEL_ERROR,
>         LEVEL_WARN,
>         LEVEL_INFO,
>         LEVEL_DEBUG,
>         LEVEL_MAX
>     }
> ```


## Variable {#Variable}



## Function {#Function}

### set\_log\_level {#set\_log\_level}

```python
def set_log_level(level: LogLevel, color: bool) -> None
```
Set log level globally, by default log level is LEVEL_INFO.

| item | description |
| --- | --- |
| **param** | **level**: log level, @see maix.log.LogLevel<br>**color**: true to enable color, false to disable color<br>|

> C++ defination code:
> ```cpp
> void set_log_level(log::LogLevel level, bool color)
> ```
### get\_log\_level {#get\_log\_level}

```python
def get_log_level() -> LogLevel
```
Get current log level

| item | description |
| --- | --- |
| **return** | current log level |

> C++ defination code:
> ```cpp
> log::LogLevel get_log_level()
> ```
### get\_log\_use\_color {#get\_log\_use\_color}

```python
def get_log_use_color() -> bool
```
Get whether log use color

| item | description |
| --- | --- |
| **return** | true if log use color, else false |

> C++ defination code:
> ```cpp
> bool get_log_use_color()
> ```


## Class {#Class}

