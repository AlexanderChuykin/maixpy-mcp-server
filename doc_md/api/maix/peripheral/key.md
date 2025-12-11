---
title: maix.peripheral.key
---

maix.peripheral.key module


> You can use `maix.peripheral.key` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### Keys {#Keys}

Keys enum, id the same as linux input.h(input-event-codes.h)

| item | describe |
| --- | --- |
| **values** | **KEY_NONE**: <br>**KEY_ESC**: <br>**KEY_SPACE**: <br>**KEY_LEFT**: <br>**KEY_RIGHT**: <br>**KEY_POWER**: <br>**KEY_OK**: <br>**KEY_OPTION**: <br>**KEY_NEXT**: <br>**KEY_PREV**: <br>
> C++ defination code:
> ```cpp
> enum Keys{
>         KEY_NONE   = 0x000,
>         KEY_ESC    = 0x001,
>         KEY_SPACE  = 0x039,
>         KEY_LEFT   = 0x069,
>         KEY_RIGHT  = 0x06a,
>         KEY_POWER  = 0x074,
>         KEY_OK     = 0x160,
>         KEY_OPTION = 0x165,
>         KEY_NEXT   = 0x197,
>         KEY_PREV   = 0x19c,
>     }
> ```
### State {#State}

Key state enum

| item | describe |
| --- | --- |
| **values** | **KEY_RELEASED**: <br>**KEY_PRESSED**: <br>**KEY_LONG_PRESSED**: <br>
> C++ defination code:
> ```cpp
> enum State{
>         KEY_RELEASED     = 0,
>         KEY_PRESSED      = 1,
>         KEY_LONG_PRESSED = 2,
>     }
> ```


## Variable {#Variable}



## Function {#Function}

### add\_default\_listener {#add\_default\_listener}

Add default listener, if you want to exit app when press ok button, you can just call this function.\nThis function is auto called in MaixPy' startup code, so you don't need to call it in MaixPy.\nCreate Key object will auto call rm_default_listener() to cancel the default ok button function.\nWhen ok button pressed, a SIGINT signal will be raise and call app.set_exit_flag(True).


> C++ defination code:
> ```cpp
> void add_default_listener()
> ```
### rm\_default\_listener {#rm\_default\_listener}

Remove default listener, if you want to cancel the default ok button function(exit app), you can just call this function.


> C++ defination code:
> ```cpp
> void rm_default_listener()
> ```


## Class {#Class}

### Key {#Key}

Key input class


> C++ defination code:
> ```cpp
> class Key
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, callback: typing.Callable[[int, int], None] = None, open: bool = True, device: str = '', long_press_time: int = 2000) -> None
```
Key Device constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **callback**: When key triggered and callback is not empty(empty In MaixPy is None, in C++ is nullptr),<br>callback will be called with args key(key.Keys) and value(key.State).<br>If set to null, you can get key value by read() function.<br>This callback called in a standalone thread, so you can block a while in callback, and you should be carefully when operate shared data.<br>**open**: auto open device in constructor, if false, you need call open() to open device.<br>**device**: Specifies the input device to use. The default initializes all keys,<br>for a specific device, provide the path (e.g., "/dev/input/device").<br>**long_press_time**: The duration (in milliseconds) from pressing the key to triggering the long press event. Default is 2000ms.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Key(std::function<void(int, int)> callback = nullptr, bool open = true, const string &device = "", int long_press_time = 2000)
> ```
#### open {#open}

```python
def open(self) -> maix.err.Err
```
Open(Initialize) key device, if already opened, will close first and then open.

| item | description |
| --- | --- |
| **type** | func |
| **return** | err::Err type, err.Err.ERR_NONE means success |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err open()
> ```
#### close {#close}

```python
def close(self) -> maix.err.Err
```
Close key device

| item | description |
| --- | --- |
| **type** | func |
| **return** | err::Err type, err.Err.ERR_NONE means success |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err close()
> ```
#### is\_opened {#is\_opened}

```python
def is_opened(self) -> bool
```
Check key device is opened

| item | description |
| --- | --- |
| **type** | func |
| **return** | bool type, true means opened, false means closed |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_opened()
> ```
#### read {#read}

```python
def read(self) -> tuple[int, int]
```
Read key input, and return key and value, if callback is set, DO NOT call this function manually.

| item | description |
| --- | --- |
| **type** | func |
| **return** | list type, first is key(maix.key.Keys), second is value(maix.key.State), if no key input, return [0, 0] |
| **throw** | If read failed, will throw maix.err.Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::pair<int, int> read()
> ```
#### long\_press\_time {#long\_press\_time}

```python
def long_press_time(self, press_time: int = -1) -> int
```
Sets and retrieves the key's long press time.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **press_time**: The long press time to set for the key.<br>Setting it to 0 will disable the long press event.<br>|
| **return** | int type, the current long press time for the key (in milliseconds). |
| **static** | False |

> C++ defination code:
> ```cpp
> int long_press_time(int press_time = -1)
> ```
