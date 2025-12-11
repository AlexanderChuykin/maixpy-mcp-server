---
title: maix.comm
---

maix.comm module


> You can use `maix.comm` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

| module | brief |
| --- | --- |
| [modbus](./comm/modbus.md) | maix.comm.modbus module |


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}

### add\_default\_comm\_listener {#add\_default\_comm\_listener}

Add default CommProtocol listener.\nWhen the application uses this port, the listening thread will immediately\nrelease the port resources and exit. If you need to start the default listening thread again,\nplease release the default port resources and then call this function.


> C++ defination code:
> ```cpp
> void add_default_comm_listener()
> ```
### rm\_default\_comm\_listener {#rm\_default\_comm\_listener}

Remove default CommProtocol listener.

| item | description |
| --- | --- |
| **return** | bool type. |

> C++ defination code:
> ```cpp
> bool rm_default_comm_listener()
> ```


## Class {#Class}

### CommProtocol {#CommProtocol}

Class for communication protocol


> C++ defination code:
> ```cpp
> class CommProtocol
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, buff_size: int = 1024, header: int = 3148663466, method_none_raise: bool = False) -> None
```
Construct a new CommProtocol object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **buff_size**: buffer size, default to 1024 bytes<br>**header**: Customize header, default is maix.protocol.HEADER<br>**method_none_raise**: If method set to "none", raise err.Exception() if method_none_raise is true. Default false,<br>if method is "none" and this arg is false, valid() function will return false and get_msg() always return none.<br>|
| **throw** | Initialize failed will raise err::Exception() |
| **static** | False |

> C++ defination code:
> ```cpp
> CommProtocol(int buff_size = 1024, uint32_t header=maix::protocol::HEADER, bool method_none_raise = false)
> ```
#### get\_msg {#get\_msg}

```python
def get_msg(self, timeout: int = 0) -> ...
```
Read data to buffer, and try to decode it as maix.protocol.MSG object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **timeout**: unit ms, 0 means return immediatly, -1 means block util have msg, >0 means block until have msg or timeout.<br>|
| **return** | decoded data, if nullptr, means no valid frame found.<br>Attentioin, delete it after use in C++. |
| **static** | False |

> C++ defination code:
> ```cpp
> protocol::MSG *get_msg(int timeout = 0)
> ```
#### resp\_ok {#resp\_ok}

```python
def resp_ok(self, cmd: int, body: maix.Bytes(bytes) = None) -> maix.err.Err
```
Send response ok(success) message

| item | description |
| --- | --- |
| **type** | func |
| **param** | **cmd**: CMD value<br>**body**: response body, can be null<br>|
| **return** | encoded data, if nullptr, means error, and the error code is -err.Err.<br>Attentioin, delete it after use in C++. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err resp_ok(uint8_t cmd, Bytes *body = nullptr)
> ```
#### report {#report}

```python
def report(self, cmd: int, body: maix.Bytes(bytes) = None) -> maix.err.Err
```
Send report message

| item | description |
| --- | --- |
| **type** | func |
| **param** | **cmd**: CMD value<br>**body**: report body, can be null<br>|
| **return** | encoded data, if nullptr, means error, and the error code is -err.Err.<br>Attentioin, delete it after use in C++. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err report(uint8_t cmd, Bytes *body = nullptr)
> ```
#### resp\_err {#resp\_err}

```python
def resp_err(self, cmd: int, code: maix.err.Err, msg: str) -> maix.err.Err
```
Encode response error message to buffer

| item | description |
| --- | --- |
| **type** | func |
| **param** | **cmd**: CMD value<br>**code**: error code<br>**msg**: error message<br>|
| **return** | encoded data, if nullptr, means error, and the error code is -err.Err.<br>Attentioin, delete it after use in C++. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err resp_err(uint8_t cmd, err::Err code, const std::string &msg)
> ```
#### valid {#valid}

```python
def valid(self) -> bool
```
Is CommProtocol valid, only not valid when method not set to \"none\".

| item | description |
| --- | --- |
| **type** | func |
| **return** | false if commprotocol method is "none". |
| **static** | False |

> C++ defination code:
> ```cpp
> bool valid()
> ```
#### set\_method {#set\_method}

```python
def set_method(method: str) -> maix.err.Err
```
Set CommProtocol method. Static method, can be called directly without instance.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **method**: Can be "uart" or "none", "none" means not use CommProtocol.<br>|
| **static** | True |

> C++ defination code:
> ```cpp
> static err::Err set_method(const std::string &method)
> ```
#### get\_method {#get\_method}

```python
def get_method() -> str
```
Get CommProtocol method. Static method, can be called directly without instance.

| item | description |
| --- | --- |
| **type** | func |
| **return** | method Can be "uart" or "none", "none" means not use CommProtocol. |
| **static** | True |

> C++ defination code:
> ```cpp
> static std::string get_method()
> ```
#### get\_uart\_port {#get\_uart\_port}

```python
def get_uart_port() -> list[str]
```
Get CommProtocol method uart's port name. Static method, can be called directly without instance.

| item | description |
| --- | --- |
| **type** | func |
| **return** | uart [port name, device path], e.g. ["uart0", "/dev/ttyS0"].<br>If no valid uart port, return empty list !! |
| **static** | True |

> C++ defination code:
> ```cpp
> static std::vector<std::string> get_uart_port()
> ```
#### get\_uart\_ports {#get\_uart\_ports}

```python
def get_uart_ports() -> list[list[str]]
```
Get all CommProtocol method uart supported ports. Static method, can be called directly without instance.

| item | description |
| --- | --- |
| **type** | func |
| **return** | uart [[port name, device path]], e.g. [["uart0", "/dev/ttyS0"], ...]. |
| **static** | True |

> C++ defination code:
> ```cpp
> static std::vector<std::vector<std::string>> get_uart_ports()
> ```
