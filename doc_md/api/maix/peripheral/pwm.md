---
title: maix.peripheral.pwm
---

maix.peripheral.pwm module


> You can use `maix.peripheral.pwm` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### PWM {#PWM}

Peripheral pwm class


> C++ defination code:
> ```cpp
> class PWM
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, id: int, freq: int = 1000, duty: float = 0, enable: bool = True, duty_val: int = -1) -> None
```
PWM constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **pin**: direction [in], pwm id, int type, like 0, 1, 2 etc.<br>**freq**: direction [in], pwm frequency, unit: Hz. int type. default is 1000<br>**duty**: direction [in], pwm duty. double type. range is [0, 100], default is 0.<br>**enable**: direction [in], enable pwm output right now. bool type. default is true, if false, you need to call enable() to enable pwm output.<br>**duty_val**: direction [in], pwm duty value, int type. default -1 means not set and auto calculate by freq and duty.<br>This arg directly set pwm duty value, if set, will ignore duty arg.<br>duty_val = duty / 100 * T_ns, T_ns = 1 / freq * 1000000000.<br>|
| **throw** | If args error or init pwm failed, will throw err::Exception |
| **static** | False |

> C++ defination code:
> ```cpp
> PWM(int id, int freq = 1000, double duty = 0, bool enable = true, int duty_val = -1)
> ```
#### duty {#duty}

```python
def duty(self, duty: float = -1) -> float
```
get or set pwm duty

| item | description |
| --- | --- |
| **type** | func |
| **param** | **duty**: direction [in], pwm duty, double type, value in [0, 100], default -1 means only read.<br>|
| **return** | current duty, float type, if set and set failed will return -err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> double duty(double duty = -1)
> ```
#### duty\_val {#duty\_val}

```python
def duty_val(self, duty_val: int = -1) -> int
```
set pwm duty value

| item | description |
| --- | --- |
| **type** | func |
| **param** | **duty_val**: direction [in], pwm duty value. int type. default is -1<br>duty_val > 0 means set duty_val<br>duty_val == -1 or not set, return current duty_val<br>|
| **return** | int type<br>when get duty_val, return current duty_val, else return -err::Err code. |
| **static** | False |

> C++ defination code:
> ```cpp
> int duty_val(int duty_val = -1)
> ```
#### freq {#freq}

```python
def freq(self, freq: int = -1) -> int
```
get or set pwm frequency

| item | description |
| --- | --- |
| **type** | func |
| **param** | **freq**: direction [in], pwm frequency. int type. default is -1<br>freq >= 0, set freq<br>freq == -1 or not set, return current freq<br>|
| **return** | int type, current freq, if set and set failed will return -err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> int freq(int freq = -1)
> ```
#### enable {#enable}

```python
def enable(self) -> maix.err.Err
```
set pwm enable

| item | description |
| --- | --- |
| **type** | func |
| **return** | err::Err type, err.Err.ERR_NONE means success |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err enable()
> ```
#### disable {#disable}

```python
def disable(self) -> maix.err.Err
```
set pwm disable

| item | description |
| --- | --- |
| **type** | func |
| **return** | err::Err type, err.Err.ERR_NONE means success |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err disable()
> ```
#### is\_enabled {#is\_enabled}

```python
def is_enabled(self) -> bool
```
get pwm enable status

| item | description |
| --- | --- |
| **type** | func |
| **return** | bool type, true means enable, false means disable |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_enabled()
> ```
