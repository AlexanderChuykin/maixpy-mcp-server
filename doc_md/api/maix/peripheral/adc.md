---
title: maix.peripheral.adc
---

maix.peripheral.adc module


> You can use `maix.peripheral.adc` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}

### RES\_BIT\_8 {#RES\_BIT\_8}

8-bit resolution, supported by the actual hardware

| item | description |
| --- | --- |
| **value** | **8** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const int RES_BIT_8 = 8
> ```
### RES\_BIT\_10 {#RES\_BIT\_10}

10-bit resolution, supported by the actual hardware

| item | description |
| --- | --- |
| **value** | **10** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const int RES_BIT_10 = 10
> ```
### RES\_BIT\_12 {#RES\_BIT\_12}

12-bit resolution, supported by the actual hardware

| item | description |
| --- | --- |
| **value** | **12** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const int RES_BIT_12 = 12
> ```
### RES\_BIT\_16 {#RES\_BIT\_16}

16-bit resolution, supported by the actual hardware

| item | description |
| --- | --- |
| **value** | **16** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const int RES_BIT_16 = 16
> ```


## Function {#Function}



## Class {#Class}

### ADC {#ADC}

Peripheral adc class


> C++ defination code:
> ```cpp
> class ADC
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, id: int, resolution: int, vref: float = -1) -> None
```
ADC constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **id**: direction [in], adc id, int type, before use this ADC, you should use pinmap to ensure the coresponding pin is ADC function.<br>**resolution**: direction [in], adc resolution. default is -1, means use default resolution<br>option:<br>resolution = adc.RES_BIT_8, means 8-bit resolution<br>resolution = adc.RES_BIT_10, means 10-bit resolution<br>resolution = adc.RES_BIT_12, means 12-bit resolution<br>resolution = adc.RES_BIT_16, means 16-bit resolution<br>the default resolution is determined by actual hardware.<br>**vref**: direction [in], adc refer voltage. default is -1, means use default refer voltage.<br>the default vref is determined by actual hardware. range: [0.0, 10.0]<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> ADC(int id, int resolution, float vref = -1)
> ```
#### read {#read}

```python
def read(self) -> int
```
read adc value

| item | description |
| --- | --- |
| **type** | func |
| **return** | adc data, int type<br>if resolution is 8-bit, return value range is [0, 255]<br>if resolution is 10-bit, return value range is [0, 1023]<br>if resolution is 12-bit, return value range is [0, 4095]<br>if resolution is 16-bit, return value range is [0, 65535] |
| **static** | False |

> C++ defination code:
> ```cpp
> int read()
> ```
#### read\_vol {#read\_vol}

```python
def read_vol(self) -> float
```
read adc voltage

| item | description |
| --- | --- |
| **type** | func |
| **return** | adc voltage, float type。the range is [0.0, vref] |
| **static** | False |

> C++ defination code:
> ```cpp
> float read_vol()
> ```
