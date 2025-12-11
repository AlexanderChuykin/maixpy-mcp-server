---
title: maix.err
---

maix.err module


> You can use `maix.err` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### Err {#Err}

Maix Error code

| item | describe |
| --- | --- |
| **values** | **ERR_NONE**: No error<br>**ERR_ARGS**: Invalid arguments<br>**ERR_NO_MEM**: No memory<br>**ERR_NOT_IMPL**: Not implemented<br>**ERR_NOT_READY**: Not ready<br>**ERR_NOT_INIT**: Not initialized<br>**ERR_NOT_OPEN**: Not opened<br>**ERR_NOT_PERMIT**: Not permitted<br>**ERR_REOPEN**: Re-open<br>**ERR_BUSY**: Busy<br>**ERR_READ**: Read error<br>**ERR_WRITE**: Write error<br>**ERR_TIMEOUT**: Timeout<br>**ERR_RUNTIME**: Runtime error<br>**ERR_IO**: IO error<br>**ERR_NOT_FOUND**: Not found<br>**ERR_ALREAY_EXIST**: Already exist<br>**ERR_BUFF_FULL**: Buffer full<br>**ERR_BUFF_EMPTY**: Buffer empty<br>**ERR_CANCEL**: Cancel<br>**ERR_OVERFLOW**: Overflow<br>**ERR_MAX**: <br>
> C++ defination code:
> ```cpp
> enum Err
>     {
>         // !!! fixed error code, DO NOT change number already defined, only append new error code
>         ERR_NONE        = 0,   // No error
>         ERR_ARGS           ,   // Invalid arguments
>         ERR_NO_MEM         ,   // No memory
>         ERR_NOT_IMPL       ,   // Not implemented
>         ERR_NOT_READY      ,   // Not ready
>         ERR_NOT_INIT       ,   // Not initialized
>         ERR_NOT_OPEN       ,   // Not opened
>         ERR_NOT_PERMIT     ,   // Not permitted
>         ERR_REOPEN         ,   // Re-open
>         ERR_BUSY           ,   // Busy
>         ERR_READ           ,   // Read error
>         ERR_WRITE          ,   // Write error
>         ERR_TIMEOUT        ,   // Timeout
>         ERR_RUNTIME        ,   // Runtime error
>         ERR_IO             ,   // IO error
>         ERR_NOT_FOUND      ,   // Not found
>         ERR_ALREAY_EXIST   ,   // Already exist
>         ERR_BUFF_FULL      ,   // Buffer full
>         ERR_BUFF_EMPTY     ,   // Buffer empty
>         ERR_CANCEL         ,   // Cancel
>         ERR_OVERFLOW       ,   // Overflow
>         ERR_MAX,
>     }
> ```


## Variable {#Variable}



## Function {#Function}

### to\_str {#to\_str}

```python
def to_str(e: Err) -> str
```
Error code to string

| item | description |
| --- | --- |
| **param** | **e**: direction [in], error code, err::Err type<br>|
| **return** | error string |

> C++ defination code:
> ```cpp
> std::string to_str(err::Err e)
> ```
### get\_error {#get\_error}

```python
def get_error() -> str
```
get last error string

| item | description |
| --- | --- |
| **return** | error string |

> C++ defination code:
> ```cpp
> std::string& get_error()
> ```
### set\_error {#set\_error}

```python
def set_error(str: str) -> None
```
set last error string

| item | description |
| --- | --- |
| **param** | **str**: direction [in], error string<br>|

> C++ defination code:
> ```cpp
> void set_error(const std::string &str)
> ```
### check\_raise {#check\_raise}

```python
def check_raise(e: Err, msg: str = '') -> None
```
Check error code, if not ERR_NONE, raise err.Exception

| item | description |
| --- | --- |
| **param** | **e**: direction [in], error code, err::Err type<br>**msg**: direction [in], error message<br>|

> C++ defination code:
> ```cpp
> void check_raise(err::Err e, const std::string &msg = "")
> ```
### check\_bool\_raise {#check\_bool\_raise}

```python
def check_bool_raise(ok: bool, msg: str = '') -> None
```
Check condition, if false, raise err.Exception

| item | description |
| --- | --- |
| **param** | **ok**: direction [in], condition, if true, do nothing, if false, raise err.Exception<br>**msg**: direction [in], error message<br>|

> C++ defination code:
> ```cpp
> void check_bool_raise(bool ok, const std::string &msg = "")
> ```
### check\_null\_raise {#check\_null\_raise}

```python
def check_null_raise(ptr: capsule, msg: str = '') -> None
```
Check NULL pointer, if NULL, raise exception

| item | description |
| --- | --- |
| **param** | **ptr**: direction [in], pointer<br>**msg**: direction [in], error message<br>|

> C++ defination code:
> ```cpp
> void check_null_raise(void *ptr, const std::string &msg = "")
> ```


## Class {#Class}

### Exception {#Exception}

Maix Exception


> C++ defination code:
> ```cpp
> class Exception : public std::exception
> ```

