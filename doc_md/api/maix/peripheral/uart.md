---
title: maix.peripheral.uart
---

maix uart peripheral driver


> You can use `maix.peripheral.uart` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### PARITY {#PARITY}

uart parity enum

| item | describe |
| --- | --- |
| **values** | **PARITY_NONE**: no parity<br>**PARITY_ODD**: odd parity<br>**PARITY_EVEN**: even parity<br>**PARITY_MAX**: <br>
> C++ defination code:
> ```cpp
> enum PARITY
>     {
>         PARITY_NONE = 0x00,  // no parity
>         PARITY_ODD  = 0x01,  // odd parity
>         PARITY_EVEN = 0x02,  // even parity
>         PARITY_MAX
>     }
> ```
### STOP {#STOP}

uart stop bits

| item | describe |
| --- | --- |
| **values** | **STOP_1**: 1 stop bit<br>**STOP_2**: 2 stop bits<br>**STOP_1_5**: 1.5 stop bits<br>**STOP_MAX**: <br>
> C++ defination code:
> ```cpp
> enum STOP
>     {
>         STOP_1   = 0x01,  // 1 stop bit
>         STOP_2   = 0x02,  // 2 stop bits
>         STOP_1_5 = 0x03,  // 1.5 stop bits
>         STOP_MAX
>     }
> ```
### BITS {#BITS}

uart stop bits

| item | describe |
| --- | --- |
| **values** | **BITS_5**: 5 data bits<br>**BITS_6**: 6 data bits<br>**BITS_7**: 7 data bits<br>**BITS_8**: 8 data bits<br>**BITS_MAX**: <br>
> C++ defination code:
> ```cpp
> enum BITS
>     {
>         BITS_5 = 5,  // 5 data bits
>         BITS_6 = 6,  // 6 data bits
>         BITS_7 = 7,  // 7 data bits
>         BITS_8 = 8,  // 8 data bits
>         BITS_MAX
>     }
> ```
### FLOW\_CTRL {#FLOW\_CTRL}

uart flow control

| item | describe |
| --- | --- |
| **values** | **FLOW_CTRL_NONE**: no flow control<br>**FLOW_CTRL_HW**: hardware flow control<br>**FLOW_CTRL_MAX**: <br>
> C++ defination code:
> ```cpp
> enum FLOW_CTRL
>     {
>         FLOW_CTRL_NONE = 0,  // no flow control
>         FLOW_CTRL_HW   = 1,  // hardware flow control
>         FLOW_CTRL_MAX
>     }
> ```


## Variable {#Variable}



## Function {#Function}

### list\_devices {#list\_devices}

```python
def list_devices() -> list[str]
```
Get supported uart ports.

| item | description |
| --- | --- |
| **return** | uart ports list, string type. |

> C++ defination code:
> ```cpp
> std::vector<std::string> list_devices()
> ```


## Class {#Class}

### UART {#UART}

maix uart peripheral driver


> C++ defination code:
> ```cpp
> class UART : public comm::CommBase
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, port: str = '', baudrate: int = 115200, databits: BITS = ..., parity: PARITY = ..., stopbits: STOP = ..., flow_ctrl: FLOW_CTRL = ...) -> None
```
UART constructor. You need to call open() to open the device.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **port**: uart port. string type, can get it by uart.list_devices().<br>If empty, will not open device in constructor, default empty.<br>if not empty, will auto open device in constructor, open fail will throw err.Exception.<br>**baudrate**: baudrate of uart. int type, default 115200.<br>**databits**: databits, values @see uart.DATA_BITS<br>**parity**: parity, values @see uart.PARITY<br>**stopbits**: stopbits, values @see uart.STOP_BITS<br>**flow_control**: flow_control, values @see uart.FLOW_CTRL<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> UART(const std::string &port = "", int baudrate = 115200, uart::BITS databits = uart::BITS_8,
>             uart::PARITY parity = uart::PARITY_NONE, uart::STOP stopbits = uart::STOP_1,
>             uart::FLOW_CTRL flow_ctrl = uart::FLOW_CTRL_NONE)
> ```
#### set\_port {#set\_port}

```python
def set_port(self, port: str) -> maix.err.Err
```
Set port

| item | description |
| --- | --- |
| **type** | func |
| **param** | **port**: uart port. string type, can get it by uart.list_devices().<br>|
| **return** | set port error code, err.Err type. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_port(const std::string &port)
> ```
#### get\_port {#get\_port}

```python
def get_port(self) -> str
```
Get port

| item | description |
| --- | --- |
| **type** | func |
| **return** | uart port, string type. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string get_port()
> ```
#### set\_baudrate {#set\_baudrate}

```python
def set_baudrate(self, baudrate: int) -> maix.err.Err
```
Set baud rate

| item | description |
| --- | --- |
| **type** | func |
| **param** | **baudrate**: baudrate of uart. int type, default 115200.<br>|
| **return** | set baud rate error code, err.Err type. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_baudrate(int baudrate)
> ```
#### get\_baudrate {#get\_baudrate}

```python
def get_baudrate(self) -> int
```
Get baud rate

| item | description |
| --- | --- |
| **type** | func |
| **return** | baud rate, int type. |
| **static** | False |

> C++ defination code:
> ```cpp
> int get_baudrate()
> ```
#### open {#open}

```python
def open(self) -> maix.err.Err
```
Open uart device, before open, port must be set in constructor or by set_port().\nIf already opened, do nothing and return err.ERR_NONE.

| item | description |
| --- | --- |
| **type** | func |
| **return** | open device error code, err.Err type. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err open()
> ```
#### is\_open {#is\_open}

```python
def is_open(self) -> bool
```
Check if device is opened.

| item | description |
| --- | --- |
| **type** | func |
| **return** | true if opened, false if not opened. |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_open()
> ```
#### close {#close}

```python
def close(self) -> maix.err.Err
```
Close uart device, if already closed, do nothing and return err.ERR_NONE.

| item | description |
| --- | --- |
| **type** | func |
| **return** | close device error code, err.Err type. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err close()
> ```
#### set\_received\_callback {#set\_received\_callback}

```python
def set_received_callback(self, callback: typing.Callable[[UART, maix.Bytes(bytes)], None]) -> None
```
Set received callback function

| item | description |
| --- | --- |
| **type** | func |
| **param** | **callback**: function to call when received data<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_received_callback(std::function<void(uart::UART&, Bytes&)> callback)
> ```
#### write\_str {#write\_str}

```python
def write_str(self, str: str) -> int
```
Send string data

| item | description |
| --- | --- |
| **type** | func |
| **param** | **str**: string data<br>|
| **return** | sent data length, < 0 means error, value is -err.Err. |
| **static** | False |

> C++ defination code:
> ```cpp
> int write_str(const std::string &str)
> ```
#### write {#write}

```python
def write(self, data: maix.Bytes(bytes)) -> int
```
Send data to uart

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: direction [in], data to send, bytes type. If you want to send str type, use str.encode() to convert.<br>|
| **return** | sent length, int type, if < 0 means error, value is -err.Err. |
| **static** | False |

> C++ defination code:
> ```cpp
> int write(Bytes &data)
> ```
#### available {#available}

```python
def available(self, timeout: int = 0) -> int
```
Check if data available or wait data available.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **timeout**: unit ms, timeout to wait data, default 0.<br>0 means check data available and return immediately,<br>> 0 means wait until data available or timeout.<br>- 1 means wait until data available.<br>|
| **return** | available data number, 0 if timeout or no data, <0 if error, value is -err.Err, can be err::ERR_IO， err::ERR_CANCEL, err::ERR_NOT_OPEN. |
| **throw** | err.Exception if fatal error. |
| **static** | False |

> C++ defination code:
> ```cpp
> int available(int timeout = 0)
> ```
#### read {#read}

```python
def read(*args, **kwargs)
```
Recv data from uart

| item | description |
| --- | --- |
| **type** | func |
| **param** | **len**: max data length want to receive, default -1.<br>-1 means read data in uart receive buffer.<br>>0 means read len data want to receive.<br>other values is invalid.<br>**timeout**: unit ms, timeout to receive data, default 0.<br>0 means read data in uart receive buffer and return immediately,<br>-1 means block until read len data,<br>>0 means block until read len data or timeout.<br>|
| **return** | received data, bytes type.<br>Attention, you need to delete the returned object yourself in C++. |
| **throw** | Read failed will raise err.Exception error. |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *read(int len = -1, int timeout = 0)
> ```
#### readline {#readline}

```python
def readline(*args, **kwargs)
```
Read line from uart, that is read until '\n' or '\r\n'.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **timeout**: unit ms, timeout to receive data, default -1 means block until read '\n' or '\r\n'.<br>> 0 means block until read '\n' or '\r\n' or timeout.<br>|
| **return** | received data, bytes type. If timeout will return the current received data despite not read '\n' or '\r\n'.<br>e.g. If we want to read b'123\n', but when we only read b'12', timeout, then return b'12'. |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *readline(int timeout = -1)
> ```
