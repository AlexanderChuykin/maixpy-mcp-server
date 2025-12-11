---
title: maix.protocol
---

maix.protocol module


> You can use `maix.protocol` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### CMD {#CMD}

protocol cmd, more doc see MaixCDK document's convention doc

| item | describe |
| --- | --- |
| **note** | max app custom CMD value should < CMD_APP_MAX |
| **values** | **CMD_APP_MAX**: 200, max app custom CMD value should < CMD_APP_MAX<br>**CMD_SET_REPORT**: set auto upload data mode<br>**CMD_APP_LIST**: <br>**CMD_START_APP**: <br>**CMD_EXIT_APP**: <br>**CMD_CUR_APP_INFO**: <br>**CMD_APP_INFO**: <br>**CMD_KEY**: <br>**CMD_TOUCH**: <br>
> C++ defination code:
> ```cpp
> enum CMD
>         {
>             CMD_APP_MAX = 0xC8,     //  200, max app custom CMD value should < CMD_APP_MAX
> 
>             CMD_SET_REPORT   = 0xF8, // set auto upload data mode
>             CMD_APP_LIST     = 0xF9,
>             CMD_START_APP    = 0xFA,
>             CMD_EXIT_APP     = 0xFB,
>             CMD_CUR_APP_INFO = 0xFC,
>             CMD_APP_INFO     = 0xFD,
>             CMD_KEY          = 0xFE,
>             CMD_TOUCH        = 0xFF,
>         }
> ```
### FLAGS {#FLAGS}

protocol flags, more doc see MaixCDK document's convention doc

| item | describe |
| --- | --- |
| **values** | **FLAG_REQ**: <br>**FLAG_RESP**: <br>**FLAG_IS_RESP_MASK**: <br>**FLAG_RESP_OK**: <br>**FLAG_RESP_ERR**: <br>**FLAG_RESP_OK_MASK**: <br>**FLAG_REPORT**: <br>**FLAG_REPORT_MASK**: <br>**FLAG_VERSION_MASK**: <br>
> C++ defination code:
> ```cpp
> enum FLAGS
>         {
>             FLAG_REQ = 0x00,
>             FLAG_RESP = 0x80,
>             FLAG_IS_RESP_MASK = 0x80,
> 
>             FLAG_RESP_OK = 0x40,
>             FLAG_RESP_ERR = 0x00,
>             FLAG_RESP_OK_MASK = 0x40,
> 
>             FLAG_REPORT = 0x20,
>             FLAG_REPORT_MASK = 0x20,
> 
>             FLAG_VERSION_MASK = 0x03
>         }
> ```


## Variable {#Variable}

### VERSION {#VERSION}

protocol version

| item | description |
| --- | --- |
| **value** | **1** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const uint8_t VERSION = 1
> ```
### HEADER {#HEADER}

protocol header

| item | description |
| --- | --- |
| **readonly**| False |

> C++ defination code:
> ```cpp
> extern uint32_t HEADER
> ```


## Function {#Function}

### crc16\_IBM {#crc16\_IBM}

```python
def crc16_IBM(data: maix.Bytes(bytes)) -> int
```
CRC16-IBM

| item | description |
| --- | --- |
| **param** | **data**: data, bytes type.<br>|
| **return** | CRC16-IBM value, uint16_t type. |

> C++ defination code:
> ```cpp
> uint16_t crc16_IBM(const Bytes *data)
> ```


## Class {#Class}

### MSG {#MSG}

protocol msg


> C++ defination code:
> ```cpp
> class MSG
> ```

#### version {#version-2}

protocol version

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint8_t version
> ```
#### resp\_ok {#resp\_ok}

Indicate response message type, true means CMD valid and the CMD processed correctly, (only for response msg)

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint8_t resp_ok
> ```
#### has\_been\_replied {#has\_been\_replied}

Flag whether CMD has been processed and responded to CMD sender.\nE.g. CMD CMD_START_APP will be automatically processed in CommProtocol.get_msg function,\nso the return msg will set this flag to true.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool has_been_replied{false}
> ```
#### cmd {#cmd-2}

CMD value

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint8_t cmd
> ```
#### is\_resp {#is\_resp}

message is response or not, contrast with is_req

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool is_resp
> ```
#### is\_req {#is\_req}

message is request or not, contrast with is_resp

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool is_req
> ```
#### is\_report {#is\_report}

message is request or not, contrast with is_resp

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool is_report
> ```
#### body\_len {#body\_len}

Message body length, read only, use set_body() to update

| item | description |
| --- | --- |
| **type** | var |
| **attention** | DO NOT manually change this value |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int body_len
> ```
#### encode\_resp\_ok {#encode\_resp\_ok}

```python
def encode_resp_ok(*args, **kwargs)
```
Encode response ok(success) message

| item | description |
| --- | --- |
| **type** | func |
| **param** | **body**: response body, can be null<br>|
| **return** | encoded data, if nullptr, means error, and the error code is -err.Err |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *encode_resp_ok(Bytes *body = nullptr)
> ```
#### encode\_report {#encode\_report}

```python
def encode_report(*args, **kwargs)
```
Encode proactively report message

| item | description |
| --- | --- |
| **type** | func |
| **param** | **body**: report body, can be null<br>|
| **return** | encoded data, if nullptr, means error, and the error code is -err.Err |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *encode_report(Bytes *body = nullptr)
> ```
#### encode\_resp\_err {#encode\_resp\_err}

```python
def encode_resp_err(*args, **kwargs)
```
Encode response error message

| item | description |
| --- | --- |
| **type** | func |
| **param** | **code**: error code<br>**msg**: error message<br>|
| **return** | encoded data, if nullptr, means error, and the error code is -err.Err |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *encode_resp_err(err::Err code, const std::string &msg)
> ```
#### set\_body {#set\_body}

```python
def set_body(self, body_new: maix.Bytes(bytes)) -> None
```
Update message body

| item | description |
| --- | --- |
| **type** | func |
| **param** | **body_new**: new body data<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_body(Bytes *body_new)
> ```
#### get\_body {#get\_body}

```python
def get_body(*args, **kwargs)
```
Get message body

| item | description |
| --- | --- |
| **type** | func |
| **return** | message body, bytes type |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *get_body()
> ```
### Protocol {#Protocol}

Communicate protocol


> C++ defination code:
> ```cpp
> class Protocol
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, buff_size: int = 1024, header: int = 3148663466) -> None
```
Construct a new Protocol object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **buff_size**: Data queue buffer size<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Protocol(int buff_size = 1024, uint32_t header=maix::protocol::HEADER)
> ```
#### buff\_size {#buff\_size}

```python
def buff_size(self) -> int
```
Data queue buffer size

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int buff_size()
> ```
#### push\_data {#push\_data}

```python
def push_data(self, new_data: maix.Bytes(bytes)) -> maix.err.Err
```
Add data to data queue

| item | description |
| --- | --- |
| **type** | func |
| **param** | **new_data**: new data<br>|
| **return** | error code, maybe err.Err.ERR_BUFF_FULL |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err push_data(const Bytes *new_data)
> ```
#### decode {#decode}

```python
def decode(self, new_data: maix.Bytes(bytes) = None) -> MSG
```
Decode data in data queue and return a message

| item | description |
| --- | --- |
| **type** | func |
| **param** | **new_data**: new data add to data queue, if null, only decode.<br>|
| **return** | decoded message, if nullptr, means no message decoded. |
| **static** | False |

> C++ defination code:
> ```cpp
> protocol::MSG *decode(const Bytes *new_data = nullptr)
> ```
#### encode\_resp\_ok {#encode\_resp\_ok-2}

```python
def encode_resp_ok(*args, **kwargs)
```
Encode response ok(success) message to buffer

| item | description |
| --- | --- |
| **type** | func |
| **param** | **cmd**: CMD value<br>**body**: response body, can be null<br>|
| **return** | encoded data, if nullptr, means error, and the error code is -err.Err |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *encode_resp_ok(uint8_t cmd, Bytes *body = nullptr)
> ```
#### encode\_report {#encode\_report-2}

```python
def encode_report(*args, **kwargs)
```
Encode proactively report message to buffer

| item | description |
| --- | --- |
| **type** | func |
| **param** | **cmd**: CMD value<br>**body**: report body, can be null<br>|
| **return** | encoded data, if nullptr, means error, and the error code is -err.Err |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *encode_report(uint8_t cmd, Bytes *body = nullptr)
> ```
#### encode\_resp\_err {#encode\_resp\_err-2}

```python
def encode_resp_err(*args, **kwargs)
```
Encode response error message to buffer

| item | description |
| --- | --- |
| **type** | func |
| **param** | **cmd**: CMD value<br>**code**: error code<br>**msg**: error message<br>|
| **return** | encoded data, if nullptr, means error, and the error code is -err.Err |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *encode_resp_err(uint8_t cmd, err::Err code, const std::string &msg)
> ```
