---
title: maix.peripheral.i2c
---

maix.peripheral.i2c module


> You can use `maix.peripheral.i2c` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### AddrSize {#AddrSize}

Address size enum

| item | describe |
| --- | --- |
| **values** | **SEVEN_BIT**: 7-bit address mode<br>**TEN_BIT**: 10-bit address mode<br>
> C++ defination code:
> ```cpp
> enum AddrSize
>     {
>         SEVEN_BIT = 7,   // 7-bit address mode
>         TEN_BIT   = 10   // 10-bit address mode
>     }
> ```
### Mode {#Mode}

I2C mode enum

| item | describe |
| --- | --- |
| **values** | **MASTER**: master mode<br>**SLAVE**: slave mode<br>
> C++ defination code:
> ```cpp
> enum Mode
>     {
>         MASTER = 0x00, // master mode
>         SLAVE = 0x01   // slave mode
>     }
> ```


## Variable {#Variable}



## Function {#Function}

### list\_devices {#list\_devices}

```python
def list_devices() -> list[int]
```
Get supported i2c bus devices.

| item | description |
| --- | --- |
| **return** | i2c bus devices list, int type, is the i2c bus id. |

> C++ defination code:
> ```cpp
> std::vector<int> list_devices()
> ```


## Class {#Class}

### I2C {#I2C}

Peripheral i2c class


> C++ defination code:
> ```cpp
> class I2C
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, id: int, mode: Mode, freq: int = 100000, addr_size: AddrSize = ...) -> None
```
I2C Device constructor\nthis constructor will be export to MaixPy as _maix.example.Example.__init__

| item | description |
| --- | --- |
| **type** | func |
| **param** | **id**: direction [in], i2c bus id, int type, e.g. 0, 1, 2<br>**freq**: direction [in], i2c clock, int type, default is 100000(100kbit/s), will auto set fast mode if freq > 100000.<br>**mode**: direction [in], mode of i2c, i2c.Mode.SLAVE or i2c.Mode.MASTER.<br>**addr_size**: direction [in], address length of i2c, i2c.AddrSize.SEVEN_BIT or i2c.AddrSize.TEN_BIT.<br>|
| **throw** | err::Exception if open i2c device failed. |
| **static** | False |

> C++ defination code:
> ```cpp
> I2C(int id, i2c::Mode mode, int freq = 100000, i2c::AddrSize addr_size = i2c::AddrSize::SEVEN_BIT)
> ```
#### scan {#scan}

```python
def scan(self, addr: int = -1) -> list[int]
```
scan all i2c salve address on the bus

| item | description |
| --- | --- |
| **type** | func |
| **param** | **addr**: If -1, only scan this addr, or scan from 0x08~0x77, default -1.<br>|
| **return** | the list of i2c slave address, int list type. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> scan(int addr = -1)
> ```
#### writeto {#writeto}

```python
def writeto(self, addr: int, data: maix.Bytes(bytes)) -> int
```
write data to i2c slave

| item | description |
| --- | --- |
| **type** | func |
| **param** | **addr**: direction [in], i2c slave address, int type<br>**data**: direction [in], data to write, bytes type.<br>Note: The range of value should be in [0,255].<br>|
| **return** | if success, return the length of written data, error occurred will return -err::Err. |
| **static** | False |

> C++ defination code:
> ```cpp
> int writeto(int addr, const Bytes &data)
> ```
#### readfrom {#readfrom}

```python
def readfrom(*args, **kwargs)
```
read data from i2c slave

| item | description |
| --- | --- |
| **type** | func |
| **param** | **addr**: direction [in], i2c slave address, int type<br>**len**: direction [in], data length to read, int type<br>|
| **return** | the list of data read from i2c slave, bytes type, you should delete it after use in C++.<br>If read failed, return nullptr in C++, None in MaixPy. |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes* readfrom(int addr, int len)
> ```
#### writeto\_mem {#writeto\_mem}

```python
def writeto_mem(self, addr: int, mem_addr: int, data: maix.Bytes(bytes), mem_addr_size: int = 8, mem_addr_le: bool = False) -> int
```
write data to i2c slave's memory address

| item | description |
| --- | --- |
| **type** | func |
| **param** | **addr**: direction [in], i2c slave address, int type<br>**mem_addr**: direction [in], memory address want to write, int type.<br>**data**: direction [in], data to write, bytes type.<br>**mem_addr_size**: direction [in], memory address size, default is 8.<br>**mem_addr_le**: direction [in], memory address little endian, default is false, that is send high byte first.<br>|
| **return** | data length written if success, error occurred will return -err::Err. |
| **static** | False |

> C++ defination code:
> ```cpp
> int writeto_mem(int addr, int mem_addr, const Bytes &data, int mem_addr_size = 8, bool mem_addr_le = false)
> ```
#### readfrom\_mem {#readfrom\_mem}

```python
def readfrom_mem(*args, **kwargs)
```
read data from i2c slave

| item | description |
| --- | --- |
| **type** | func |
| **param** | **addr**: direction [in], i2c slave address, int type<br>**mem_addr**: direction [in], memory address want to read, int type.<br>**len**: direction [in], data length to read, int type<br>**mem_addr_size**: direction [in], memory address size, default is 8.<br>**mem_addr_le**: direction [in], memory address little endian, default is false, that is send high byte first.<br>|
| **return** | the list of data read from i2c slave, bytes type, you should delete it after use in C++.<br>If read failed, return nullptr in C++, None in MaixPy. |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes* readfrom_mem(int addr, int mem_addr, int len, int mem_addr_size = 8, bool mem_addr_le = false)
> ```
