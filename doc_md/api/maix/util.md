---
title: maix.util
---

maix.util module


> You can use `maix.util` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}

### init\_before\_main {#init\_before\_main}

```python
def init_before_main() -> None
```
Initialize before main\nThe function is used to add preparatory operations that need to be executed before the main program runs.


> C++ defination code:
> ```cpp
> void init_before_main()
> ```
### do\_exit\_function {#do\_exit\_function}

```python
def do_exit_function() -> None
```
exec all of exit function


> C++ defination code:
> ```cpp
> void do_exit_function()
> ```
### register\_atexit {#register\_atexit}

```python
def register_atexit() -> None
```
Registering default processes that need to be executed on exit


> C++ defination code:
> ```cpp
> void register_atexit()
> ```
### str\_strip {#str\_strip}

```python
def str_strip(s: str) -> str
```
strip string, and return new striped string, will alloc new string.


> C++ defination code:
> ```cpp
> std::string str_strip(std::string &s)
> ```


## Class {#Class}

