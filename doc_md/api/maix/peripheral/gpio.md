---
title: maix.peripheral.gpio
---

maix.peripheral.gpio module


> You can use `maix.peripheral.gpio` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### Mode {#Mode}

GPIO mode

| item | describe |
| --- | --- |
| **values** | **IN**: input mode<br>**OUT**: output mode<br>**OUT_OD**: output open drain mode<br>**MODE_MAX**: <br>
> C++ defination code:
> ```cpp
> enum Mode
>     {
>         IN     = 0x01,     // input mode
>         OUT    = 0x02,     // output mode
>         OUT_OD = 0x03,     // output open drain mode
>         MODE_MAX
>     }
> ```
### Pull {#Pull}

GPIO pull mode

| item | describe |
| --- | --- |
| **values** | **PULL_NONE**: pull none mode<br>**PULL_UP**: pull up mode<br>**PULL_DOWN**: pull down mode<br>**PULL_MAX**: <br>
> C++ defination code:
> ```cpp
> enum Pull
>     {
>         PULL_NONE = 0x00,  // pull none mode
>         PULL_UP   = 0x01,  // pull up mode
>         PULL_DOWN = 0x02,  // pull down mode
>         PULL_MAX
>     }
> ```


## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### GPIO {#GPIO}

Peripheral gpio class


> C++ defination code:
> ```cpp
> class GPIO
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, pin: str, mode: Mode = ..., pull: Pull = ...) -> None
```
GPIO constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **pin**: direction [in], gpio pin name, string type the same as board's pin name, e.g. "B14" or "GPIOB14", or number string like "10" if board no gpiochipe name.<br>**mode**: direction [in], gpio mode. gpio.Mode type, default is gpio.Mode.IN (input) mode.<br>**pull**: direction [in], gpio pull. gpio.Pull type, default is gpio.Pull.PULL_NONE (pull none) mode.<br>For input mode, this will set gpio default status(value), if set to gpio.Pull.PULL_NONE, gpio value will be floating.<br>For output mode, this will set gpio default status(value), if set to gpio.Pull.PULL_UP, gpio value will be 1, else 0.<br>|
| **throw** | err::Exception if open gpio device failed. |
| **static** | False |

> C++ defination code:
> ```cpp
> GPIO(std::string pin, gpio::Mode mode = gpio::Mode::IN, gpio::Pull pull = gpio::Pull::PULL_NONE)
> ```
#### value {#value}

```python
def value(self, value: int = -1) -> int
```
set and get gpio value

| item | description |
| --- | --- |
| **type** | func |
| **param** | **value**: direction [in], gpio value. int type.<br>0, means write gpio to low level<br>1, means write gpio to high level<br>-1, means read gpio value, not set<br>|
| **return** | int type, return gpio value, can be 0 or 1 |
| **static** | False |

> C++ defination code:
> ```cpp
> int value(int value = -1)
> ```
#### high {#high}

```python
def high(self) -> None
```
set gpio high (value to 1)

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void high()
> ```
#### low {#low}

```python
def low(self) -> None
```
set gpio low (value to 0)

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void low()
> ```
#### toggle {#toggle}

```python
def toggle(self) -> None
```
gpio toggle

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void toggle()
> ```
#### get\_mode {#get\_mode}

```python
def get_mode(self) -> Mode
```
gpio get mode

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> gpio::Mode get_mode()
> ```
#### get\_pull {#get\_pull}

```python
def get_pull(self) -> Pull
```
get gpio pull

| item | description |
| --- | --- |
| **type** | func |
| **return** | gpio::Pull type |
| **static** | False |

> C++ defination code:
> ```cpp
> gpio::Pull get_pull()
> ```
#### reset {#reset}

```python
def reset(self, mode: Mode, pull: Pull) -> maix.err.Err
```
reset gpio

| item | description |
| --- | --- |
| **type** | func |
| **param** | **mode**: direction [in], gpio mode. gpio.Mode type<br>**pull**: direction [in], gpio pull. gpio.Pull type<br>For input mode, this will set gpio default status(value), if set to gpio.Pull.PULL_NONE, gpio value will be floating.<br>For output mode, this will set gpio default status(value), if set to gpio.Pull.PULL_UP, gpio value will be 1, else 0.<br>|
| **return** | err::Err type |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err reset(gpio::Mode mode, gpio::Pull pull)
> ```
