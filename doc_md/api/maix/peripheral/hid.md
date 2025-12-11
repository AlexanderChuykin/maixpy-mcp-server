---
title: maix.peripheral.hid
---

maix.peripheral.hid module


> You can use `maix.peripheral.hid` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### DeviceType {#DeviceType}

Device enum of hid

| item | describe |
| --- | --- |
| **values** | **DEVICE_MOUSE**: <br>**DEVICE_KEYBOARD**: <br>**DEVICE_TOUCHPAD**: <br>
> C++ defination code:
> ```cpp
> enum DeviceType {
>         DEVICE_MOUSE = 0,
>         DEVICE_KEYBOARD,
>         DEVICE_TOUCHPAD
>     }
> ```


## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### Hid {#Hid}

Hid class


> C++ defination code:
> ```cpp
> class Hid
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, device_type: DeviceType, open: bool = True) -> None
```
Hid Device constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **device_type**: Device type, used to select mouse, keyboard, or touchpad.<br>**open**: auto open device in constructor, if false, you need call open() to open device<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Hid(hid::DeviceType device_type, bool open = true)
> ```
#### open {#open}

```python
def open(self) -> maix.err.Err
```
Open hid device

| item | description |
| --- | --- |
| **type** | func |
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err open()
> ```
#### close {#close}

```python
def close(self) -> maix.err.Err
```
Close hid device

| item | description |
| --- | --- |
| **type** | func |
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err close()
> ```
#### write {#write}

```python
def write(self, data: list[int]) -> maix.err.Err
```
Write data to hid device

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: data to write<br>For the keyboard, 8 bytes of data need to be written, with the format as follows:<br>data =      [0x00,   #<br>0x00,   #<br>0x00,   # Key value. Refer to the "Universal Serial Bus HID Usage Tables" section of the official documentation(https://www.usb.org).<br>0x00,   #<br>0x00,   #<br>0x00,   #<br>0x00,   #<br>0x00]   #<br>For the mouse, 4 bytes of data need to be written, with the format as follows:<br>data =       [0x00,  # Button state<br>0x00: no button pressed<br>0x01: press left button<br>0x02: press right button<br>0x04: press middle button<br>x,      # X-axis relative coordinates. Signed number, positive values for x indicate movement to the right<br>y,      # Y-axis relative coordinates. Signed number, positive values for y indicate movement downward<br>0x00]   # Wheel movement. Signed number, positive values indicate downward movement.<br>For the touchpad, 6 bytes of data need to be written, with the format as follows:<br>data =      [0x00,   # Button state (0: no button pressed, 0x01: press left button, 0x10, press right button.)<br>x & 0xFF, (x >> 8) & 0xFF,  # X-axis absolute coordinate, 0 means unused.<br>Note: You must map the target position to the range [0x1, 0x7FFF]. This means x value = <position_to_move> * 0x7FFF / <actual_screen_width><br>y & 0xFF, (y >> 8) & 0xFF,  # Y-axis absolute coordinate, 0 means unused.<br>Note: You must map the target position to the range [0x1, 0x7FFF]. This means y value = <position_to_move> * 0x7FFF / <actual_screen_height><br>0x00,   # Wheel movement. Signed number, positive values indicate downward movement.<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err write(std::vector<int> &data)
> ```
#### is\_opened {#is\_opened}

```python
def is_opened(self) -> bool
```
Check if hid device is opened

| item | description |
| --- | --- |
| **type** | func |
| **return** | bool |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_opened()
> ```
