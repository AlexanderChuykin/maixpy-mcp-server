---
title: maix.peripheral.pinmap
---

maix.peripheral.pinmap module


> You can use `maix.peripheral.pinmap` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}

### get\_pins {#get\_pins}

```python
def get_pins() -> list[str]
```
Get all pins of devices

| item | description |
| --- | --- |
| **return** | pin name list, string type. |

> C++ defination code:
> ```cpp
> std::vector<std::string> get_pins()
> ```
### get\_pin\_functions {#get\_pin\_functions}

```python
def get_pin_functions(pin: str) -> list[str]
```
Get all function of a pin

| item | description |
| --- | --- |
| **param** | **pin**: pin name, string type.<br>|
| **return** | function list, function name is string type. |
| **throw** | If pin name error will throwout err.Err.ERR_ARGS error. |

> C++ defination code:
> ```cpp
> std::vector<std::string> get_pin_functions(const std::string &pin)
> ```
### set\_pin\_function {#set\_pin\_function}

```python
def set_pin_function(pin: str, func: str) -> maix.err.Err
```
Set function of a pin

| item | description |
| --- | --- |
| **param** | **pin**: pin name, string type.<br>**func**: which function should this pin use.<br>|
| **return** | if set ok, will return err.Err.ERR_NONE, else error occurs. |

> C++ defination code:
> ```cpp
> err::Err set_pin_function(const std::string &pin, const std::string &func)
> ```
### get\_pin\_function {#get\_pin\_function}

```python
def get_pin_function(pin: str) -> str
```
Get pin's current function

| item | description |
| --- | --- |
| **param** | **pin**: pin name, string type.<br>|
| **return** | pin's current funtion name. |
| **throw** | If pin name error will throwout err.Err.ERR_ARGS error,<br>if not implement for this pin, or read/write register failed, will throwout err.Err.Exception. |

> C++ defination code:
> ```cpp
> std::string get_pin_function(const std::string &pin)
> ```


## Class {#Class}

