---
title: maix.comm.modbus
---

maix.comm.modbus module


> You can use `maix.comm.modbus` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### Mode {#Mode}

modbus mode

| item | describe |
| --- | --- |
| **values** | **RTU**: <br>**TCP**: <br>
> C++ defination code:
> ```cpp
> enum class Mode : unsigned char {
>         RTU,
>         TCP
>     }
> ```
### RequestType {#RequestType}

Modbus request types enumeration.\nThis enumeration defines the various Modbus request types,\nincluding functions for reading and writing coils, registers,\nas well as diagnostics and identification.

| item | describe |
| --- | --- |
| **values** | **READ_COILS**: < Read Coils<br>**READ_DISCRETE_INPUTS**: < Read Discrete Inputs<br>**READ_HOLDING_REGISTERS**: < Read Holding Registers<br>**READ_INPUT_REGISTERS**: < Read Input Registers<br>**WRITE_SINGLE_COIL**: < Write Single Coil<br>**WRITE_SINGLE_REGISTER**: < Write Single Register<br>**DIAGNOSTICS**: < Diagnostics (Serial Line only)<br>**GET_COMM_EVENT_COUNTER**: < Get Comm Event Counter (Serial Line only)<br>**WRITE_MULTIPLE_COILS**: < Write Multiple Coils<br>**WRITE_MULTIPLE_REGISTERS**: < Write Multiple Registers<br>**REPORT_SERVER_ID**: < Report Slave ID (Serial Line only)<br>**MASK_WRITE_REGISTER**: < Mask Write Register<br>**READ_WRITE_MULTIPLE_REGISTERS**: < Read/Write Multiple Registers<br>**READ_DEVICE_IDENTIFICATION**: < Read Device Identification<br>**UNKNOWN**: < Unknown Request Type<br>
> C++ defination code:
> ```cpp
> enum class RequestType : unsigned char {
>         READ_COILS                      = 0x01,     ///< Read Coils
>         READ_DISCRETE_INPUTS            = 0x02,     ///< Read Discrete Inputs
>         READ_HOLDING_REGISTERS          = 0x03,     ///< Read Holding Registers
>         READ_INPUT_REGISTERS            = 0x04,     ///< Read Input Registers
>         WRITE_SINGLE_COIL               = 0x05,     ///< Write Single Coil
>         WRITE_SINGLE_REGISTER           = 0x06,     ///< Write Single Register
>         DIAGNOSTICS                     = 0x08,     ///< Diagnostics (Serial Line only)
>         GET_COMM_EVENT_COUNTER          = 0x0B,     ///< Get Comm Event Counter (Serial Line only)
>         WRITE_MULTIPLE_COILS            = 0x0F,     ///< Write Multiple Coils
>         WRITE_MULTIPLE_REGISTERS        = 0x10,     ///< Write Multiple Registers
>         REPORT_SERVER_ID                = 0x11,     ///< Report Slave ID (Serial Line only)
>         MASK_WRITE_REGISTER             = 0x16,     ///< Mask Write Register
>         READ_WRITE_MULTIPLE_REGISTERS   = 0x17,     ///< Read/Write Multiple Registers
>         READ_DEVICE_IDENTIFICATION      = 0x2B,     ///< Read Device Identification
>         UNKNOWN                         = 0xFF      ///< Unknown Request Type
>     }
> ```


## Variable {#Variable}



## Function {#Function}

### set\_master\_debug {#set\_master\_debug}

```python
def set_master_debug(debug: bool) -> None
```
Set the master debug ON/OFF

| item | description |
| --- | --- |
| **param** | **debug**: True(ON) or False(OFF)<br>|

> C++ defination code:
> ```cpp
> void set_master_debug(bool debug)
> ```


## Class {#Class}

### Slave {#Slave}

Class for modbus Slave


> C++ defination code:
> ```cpp
> class Slave
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, mode: Mode, ip_or_device: str, coils_start: int = 0, coils_size: int = 0, discrete_start: int = 0, discrete_size: int = 0, holding_start: int = 0, holding_size: int = 0, input_start: int = 0, input_size: int = 0, rtu_baud: int = 115200, rtu_slave: int = 1, tcp_port: int = 502, debug: bool = False) -> None
```
Modbus Slave constructor.\nThis constructor initializes a Modbus Slave instance. Depending on the mode (RTU or TCP),\nit sets up the necessary parameters for communication and defines the register structure.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **mode**: Specifies the communication mode: RTU or TCP.<br>**ip_or_device**: The UART device name if using RTU mode.<br>If TCP mode is selected, this parameter is ignored.<br>**coils_start**: The starting address of the coils register.<br>**coils_size**: The number of coils to manage.<br>**discrete_start**: The starting address of the discrete inputs register.<br>**discrete_size**: The number of discrete inputs to manage.<br>**holding_start**: The starting address of the holding registers.<br>**holding_size**: The number of holding registers to manage.<br>**input_start**: The starting address of the input registers.<br>**input_size**: The number of input registers to manage.<br>**rtu_baud**: The baud rate for RTU communication.<br>Supported rates include: 110, 300, 600, 1200, 2400, 4800,<br>9600, 19200, 38400, 57600, 115200, 230400, 460800,<br>500000, 576000, 921600, 1000000, 1152000, 1500000,<br>2500000, 3000000, 3500000, 4000000.<br>Default is 115200. Ensure that the selected baud rate<br>is supported by the underlying hardware and libmodbus.<br>**rtu_slave**: The RTU slave address. Ignored in TCP mode. Default is 1.<br>**tcp_port**: The port used for TCP communication. Ignored in RTU mode. Default is 502.<br>**debug**: A boolean flag to enable or disable debug mode. Default is false.<br>|
| **see** | modbus.Mode for valid modes. |
| **static** | False |

> C++ defination code:
> ```cpp
> Slave(maix::comm::modbus::Mode mode, const std::string& ip_or_device,
>             uint32_t coils_start=0, uint32_t coils_size=0,
>             uint32_t discrete_start=0, uint32_t discrete_size=0,
>             uint32_t holding_start=0, uint32_t holding_size=0,
>             uint32_t input_start=0, uint32_t input_size=0,
>             int rtu_baud=115200, uint8_t rtu_slave=1,
>             int tcp_port=502, bool debug=false)
> ```
#### receive {#receive}

```python
def receive(self, timeout_ms: int = -1) -> maix.err.Err
```
Receives a Modbus request\nThis function is used to receive a Modbus request from the client. The behavior of the function\ndepends on the parameter `timeout_ms` provided, which dictates how long the function will wait\nfor a request before returning.

| item | description |
| --- | --- |
| **type** | func |
| **note** | This function gets and parses the request, it does not manipulate the registers. |
| **param** | **timeout_ms**: Timeout setting<br>-1   Block indefinitely until a request is received<br>0    Non-blocking mode; function returns immediately, regardless of whether a request is received<br>>0   Blocking mode; function will wait for the specified number of milliseconds for a request<br>|
| **return** | maix::err::Err type, @see maix::err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> ::maix::err::Err receive(const int timeout_ms=-1)
> ```
#### request\_type {#request\_type}

```python
def request_type(self) -> RequestType
```
Gets the type of the Modbus request that was successfully received\nThis function can be used to retrieve the type of the request received after a successful\ncall to `receive()`. The return value indicates the type of the Modbus request, allowing\nthe user to understand and process the received request appropriately.

| item | description |
| --- | --- |
| **type** | func |
| **return** | RequestType The type of the Modbus request that has been received. |
| **see** | modbus.RequestType |
| **static** | False |

> C++ defination code:
> ```cpp
> ::maix::comm::modbus::RequestType request_type()
> ```
#### reply {#reply}

```python
def reply(self) -> maix.err.Err
```
Processes the request and returns the corresponding data.\nThis function handles the requests received from the client. It retrieves any data that the client\nneeds to write to the registers and updates the registers accordingly. Additionally, it retrieves\nthe requested data from the registers and sends it back to the client in the response.\nThis function is essential for managing read and write operations in a Modbus Slave context.

| item | description |
| --- | --- |
| **type** | func |
| **note** | The function will modify the Slave's internal state based on the data received in the<br>request, and ensure that the appropriate data is returned to the client. |
| **return** | maix::err::Err type, @see maix::err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> ::maix::err::Err reply()
> ```
#### receive\_and\_reply {#receive\_and\_reply}

```python
def receive_and_reply(self, timeout_ms: int = -1) -> RequestType
```
Receives a request from the client and sends a response.\nThis function combines the operations of receiving a request and sending a corresponding\nresponse in a single call. It waits for a specified duration (defined by the `timeout_ms`\nparameter) to receive a request from the client. Upon successful receipt of the request,\nit processes the request and prepares the necessary data to be sent back to the client.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **timeout_ms**: The timeout duration for waiting to receive a request.<br>- A value of -1 makes the function block indefinitely until a request<br>is received.<br>- A value of 0 makes it non-blocking, returning immediately without<br>waiting for a request.<br>- A positive value specifies the maximum time (in milliseconds) to wait<br>for a request before timing out.<br>|
| **return** | RequestType The type of the Modbus request that has been received. |
| **see** | modbus.RequestType |
| **static** | False |

> C++ defination code:
> ```cpp
> ::maix::comm::modbus::RequestType receive_and_reply(const int timeout_ms=-1)
> ```
#### coils {#coils}

```python
def coils(self, data: list[int] = [], index: int = 0) -> list[int]
```
Reads from or writes to coils.\nThis function can be used to either read data from coils or write data to them.\nIf the `data` parameter is empty, the function performs a read operation.\nIf `data` is not empty, the function writes the contents of `data` to the coils\nstarting at the specified index.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: A vector of data to be written. If empty, a read operation is performed.<br>If not empty, the data will overwrite the coils from `index`.<br>**index**: The starting index for writing data. This parameter is ignored during read operations.<br>|
| **return** | std::vector<uint16_t> When the read operation is successful, return all data in the coils as a list.<br>When the write operation is successful, return a non-empty list; when it fails, return an empty list. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint8_t> coils(const std::vector<uint8_t>& data = std::vector<uint8_t>{}, const uint32_t index = 0)
> ```
#### discrete\_input {#discrete\_input}

```python
def discrete_input(self, data: list[int] = [], index: int = 0) -> list[int]
```
Reads from or writes to discrete input.\nThis function can be used to either read data from discrete input or write data to them.\nIf the `data` parameter is empty, the function performs a read operation.\nIf `data` is not empty, the function writes the contents of `data` to the discrete input\nstarting at the specified index.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: A vector of data to be written. If empty, a read operation is performed.<br>If not empty, the data will overwrite the discrete input from `index`.<br>**index**: The starting index for writing data. This parameter is ignored during read operations.<br>|
| **return** | std::vector<uint16_t> When the read operation is successful, return all data in the discrete input as a list.<br>When the write operation is successful, return a non-empty list; when it fails, return an empty list. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint8_t> discrete_input(const std::vector<uint8_t>& data = std::vector<uint8_t>{}, const uint32_t index = 0)
> ```
#### input\_registers {#input\_registers}

```python
def input_registers(self, data: list[int] = [], index: int = 0) -> list[int]
```
Reads from or writes to input registers.\nThis function can be used to either read data from input registers or write data to them.\nIf the `data` parameter is empty, the function performs a read operation.\nIf `data` is not empty, the function writes the contents of `data` to the input registers\nstarting at the specified index.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: A vector of data to be written. If empty, a read operation is performed.<br>If not empty, the data will overwrite the input registers from `index`.<br>**index**: The starting index for writing data. This parameter is ignored during read operations.<br>|
| **return** | std::vector<uint16_t> When the read operation is successful, return all data in the input registers as a list.<br>When the write operation is successful, return a non-empty list; when it fails, return an empty list. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint16_t> input_registers(const std::vector<uint16_t>& data = std::vector<uint16_t>{}, const uint32_t index = 0)
> ```
#### holding\_registers {#holding\_registers}

```python
def holding_registers(self, data: list[int] = [], index: int = 0) -> list[int]
```
Reads from or writes to holding registers.\nThis function can be used to either read data from holding registers or write data to them.\nIf the `data` parameter is empty, the function performs a read operation.\nIf `data` is not empty, the function writes the contents of `data` to the holding registers\nstarting at the specified index.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: A vector of data to be written. If empty, a read operation is performed.<br>If not empty, the data will overwrite the holding registers from `index`.<br>**index**: The starting index for writing data. This parameter is ignored during read operations.<br>|
| **return** | std::vector<uint16_t> When the read operation is successful, return all data in the holding registers as a list.<br>When the write operation is successful, return a non-empty list; when it fails, return an empty list. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint16_t> holding_registers(const std::vector<uint16_t>& data = std::vector<uint16_t>{}, const uint32_t index = 0)
> ```
### MasterRTU {#MasterRTU}

Class for modbus MasterRTU


> C++ defination code:
> ```cpp
> class MasterRTU final
> ```

#### \_\_init\_\_ {#\_\_init\_\_-2}

```python
def __init__(self, device: str = '', baudrate: int = 115200) -> None
```
Construct a new MasterRTU object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **device**: Default uart device.<br>**baudrate**: Default uart baudrate.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> MasterRTU(const std::string& device="", const int baudrate=115200)
> ```
#### read\_coils {#read\_coils}

```python
def read_coils(self, slave_id: int, addr: int, size: int, timeout_ms: int = -1, device: str = '', baudrate: int = -1) -> list[int]
```
Reads coils from the Modbus device.\nThis function reads a specified number of coils starting from a given address.\nIt includes timeout settings to define how long to wait for a response.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **slave_id**: The RTU slave address.<br>**addr**: The starting address for reading coils.<br>**size**: The number of coils to read.<br>**timeout_ms**: The timeout duration for waiting to receive a request.<br>- A value of -1 makes the function block indefinitely until a request<br>is received.<br>- A value of 0 makes it non-blocking, returning immediately without<br>waiting for a request.<br>- A positive value specifies the maximum time (in milliseconds) to wait<br>for a request before timing out.<br>**device**: The UART device to use. An empty string ("") indicates that the<br>default device from the constructor will be used.<br>**baudrate**: The UART baud rate. A value of -1 signifies that the default baud rate<br>from the constructor will be applied.<br>|
| **return** | std::vector<uint8_t>/list[int] A vector containing the read coil values. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint8_t> read_coils(const uint32_t slave_id, const uint32_t addr,
>                                         const uint32_t size, const int timeout_ms=-1,
>                                         const std::string& device="", const int baudrate=-1)
> ```
#### write\_coils {#write\_coils}

```python
def write_coils(self, slave_id: int, data: list[int], addr: int, timeout_ms: int = -1, device: str = '', baudrate: int = -1) -> int
```
Writes values to coils on the Modbus device.\nThis function writes the specified data to the coils starting from a given address.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **slave_id**: The RTU slave address.<br>**data**: A vector containing the coil values to write.<br>**addr**: The starting address for writing coils.<br>**timeout_ms**: The timeout duration for the write operation.<br>- A value of -1 makes the function block until the write is complete.<br>- A value of 0 makes it non-blocking.<br>- A positive value specifies the maximum time (in milliseconds) to wait.<br>**device**: The UART device to use. An empty string ("") indicates that the<br>default device from the constructor will be used.<br>**baudrate**: The UART baud rate. A value of -1 signifies that the default baud rate<br>from the constructor will be applied.<br>|
| **return** | int Returns the number of bytes written on success, or a value less than 0 on failure. |
| **static** | False |

> C++ defination code:
> ```cpp
> int write_coils(const uint32_t slave_id, const std::vector<uint8_t>& data,
>                         const uint32_t addr, const int timeout_ms=-1,
>                         const std::string& device="", const int baudrate=-1)
> ```
#### read\_discrete\_input {#read\_discrete\_input}

```python
def read_discrete_input(self, slave_id: int, addr: int, size: int, timeout_ms: int = -1, device: str = '', baudrate: int = -1) -> list[int]
```
Reads discrete inputs from the Modbus device.\nThis function reads a specified number of discrete inputs starting from a given address.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **slave_id**: The RTU slave address.<br>**addr**: The starting address for reading discrete inputs.<br>**size**: The number of discrete inputs to read.<br>**timeout_ms**: The timeout duration for the write operation.<br>- A value of -1 makes the function block until the write is complete.<br>- A value of 0 makes it non-blocking.<br>- A positive value specifies the maximum time (in milliseconds) to wait.<br>**device**: The UART device to use. An empty string ("") indicates that the<br>default device from the constructor will be used.<br>**baudrate**: The UART baud rate. A value of -1 signifies that the default baud rate<br>from the constructor will be applied.<br>|
| **return** | std::vector<uint8_t>/list[int] A vector containing the read discrete input values. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint8_t> read_discrete_input(const uint32_t slave_id, const uint32_t addr,
>                                                 const uint32_t size, const int timeout_ms=-1,
>                                                 const std::string& device="", const int baudrate=-1)
> ```
#### read\_input\_registers {#read\_input\_registers}

```python
def read_input_registers(self, slave_id: int, addr: int, size: int, timeout_ms: int = -1, device: str = '', baudrate: int = -1) -> list[int]
```
Reads input registers from the Modbus device.\nThis function reads a specified number of input registers starting from a given address.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **slave_id**: The RTU slave address.<br>**addr**: The starting address for reading input registers.<br>**size**: The number of input registers to read.<br>**timeout_ms**: The timeout duration for the write operation.<br>- A value of -1 makes the function block until the write is complete.<br>- A value of 0 makes it non-blocking.<br>- A positive value specifies the maximum time (in milliseconds) to wait.<br>**device**: The UART device to use. An empty string ("") indicates that the<br>default device from the constructor will be used.<br>**baudrate**: The UART baud rate. A value of -1 signifies that the default baud rate<br>from the constructor will be applied.<br>|
| **return** | std::vector<uint16_t>/list[int] A vector containing the read input register values. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint16_t> read_input_registers(const uint32_t slave_id, const uint32_t addr,
>                                                 const uint32_t size, const int timeout_ms=-1,
>                                                 const std::string& device="", const int baudrate=-1)
> ```
#### read\_holding\_registers {#read\_holding\_registers}

```python
def read_holding_registers(self, slave_id: int, addr: int, size: int, timeout_ms: int = -1, device: str = '', baudrate: int = -1) -> list[int]
```
Reads holding registers from the Modbus device.\nThis function reads a specified number of holding registers starting from a given address.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **slave_id**: The RTU slave address.<br>**addr**: The starting address for reading holding registers.<br>**size**: The number of holding registers to read.<br>**timeout_ms**: The timeout duration for the write operation.<br>- A value of -1 makes the function block until the write is complete.<br>- A value of 0 makes it non-blocking.<br>- A positive value specifies the maximum time (in milliseconds) to wait.<br>**device**: The UART device to use. An empty string ("") indicates that the<br>default device from the constructor will be used.<br>**baudrate**: The UART baud rate. A value of -1 signifies that the default baud rate<br>from the constructor will be applied.<br>|
| **return** | std::vector<uint16_t>/list[int] A vector containing the read holding register values. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint16_t> read_holding_registers(const uint32_t slave_id, const uint32_t addr,
>                                                     const uint32_t size, const int timeout_ms=-1,
>                                                     const std::string& device="", const int baudrate=-1)
> ```
#### write\_holding\_registers {#write\_holding\_registers}

```python
def write_holding_registers(self, slave_id: int, data: list[int], addr: int, timeout_ms: int = -1, device: str = '', baudrate: int = -1) -> int
```
Writes values to holding registers on the Modbus device.\nThis function writes the specified data to the holding registers starting from a given address.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **slave_id**: The RTU slave address.<br>**data**: A vector containing the values to write to holding registers.<br>**addr**: The starting address for writing holding registers.<br>**timeout_ms**: The timeout duration for the write operation.<br>- A value of -1 makes the function block until the write is complete.<br>- A value of 0 makes it non-blocking.<br>- A positive value specifies the maximum time (in milliseconds) to wait.<br>**device**: The UART device to use. An empty string ("") indicates that the<br>default device from the constructor will be used.<br>**baudrate**: The UART baud rate. A value of -1 signifies that the default baud rate<br>from the constructor will be applied.<br>|
| **return** | int Returns the number of bytes written on success, or a value less than 0 on failure. |
| **static** | False |

> C++ defination code:
> ```cpp
> int write_holding_registers(const uint32_t slave_id, const std::vector<uint16_t>& data,
>                                     const uint32_t addr, const int timeout_ms=-1,
>                                     const std::string& device="", const int baudrate=-1)
> ```
### MasterTCP {#MasterTCP}

Class for modbus Master


> C++ defination code:
> ```cpp
> class MasterTCP final
> ```

#### \_\_init\_\_ {#\_\_init\_\_-3}

```python
def __init__(self, port: int = 502) -> None
```
Construct a new MasterTCP object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **port**: Device tcp port.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> MasterTCP(const int port=502)
> ```
#### read\_coils {#read\_coils-2}

```python
def read_coils(self, ip: str, addr: int, size: int, timeout_ms: int = -1, port: int = -1) -> list[int]
```
Reads coils from the Modbus device.\nThis function reads a specified number of coils starting from a given address.\nIt includes timeout settings to define how long to wait for a response.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ip**: The TCP IP address.<br>**addr**: The starting address for reading coils.<br>**size**: The number of coils to read.<br>**timeout_ms**: The timeout duration for waiting to receive a request.<br>- A value of -1 makes the function block indefinitely until a request<br>is received.<br>- A value of 0 makes it non-blocking, returning immediately without<br>waiting for a request.<br>- A positive value specifies the maximum time (in milliseconds) to wait<br>for a request before timing out.<br>**port**: The TCP port. A value of -1 signifies that the default port<br>from the constructor will be applied.<br>|
| **return** | std::vector<uint8_t>/list[int] A vector containing the read coil values. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint8_t> read_coils(const std::string ip, const uint32_t addr,
>                                         const uint32_t size, const int timeout_ms=-1,
>                                         const int port=-1)
> ```
#### write\_coils {#write\_coils-2}

```python
def write_coils(self, ip: str, data: list[int], addr: int, timeout_ms: int = -1, port: int = -1) -> int
```
Writes values to coils on the Modbus device.\nThis function writes the specified data to the coils starting from a given address.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ip**: The TCP IP address.<br>**data**: A vector containing the coil values to write.<br>**addr**: The starting address for writing coils.<br>**timeout_ms**: The timeout duration for the write operation.<br>- A value of -1 makes the function block until the write is complete.<br>- A value of 0 makes it non-blocking.<br>- A positive value specifies the maximum time (in milliseconds) to wait.<br>**port**: The TCP port. A value of -1 signifies that the default port<br>from the constructor will be applied.<br>|
| **return** | int Returns the number of bytes written on success, or a value less than 0 on failure. |
| **static** | False |

> C++ defination code:
> ```cpp
> int write_coils(const std::string ip, const std::vector<uint8_t>& data,
>                         const uint32_t addr, const int timeout_ms=-1,
>                         const int port=-1)
> ```
#### read\_discrete\_input {#read\_discrete\_input-2}

```python
def read_discrete_input(self, ip: str, addr: int, size: int, timeout_ms: int = -1, port: int = -1) -> list[int]
```
Reads discrete inputs from the Modbus device.\nThis function reads a specified number of discrete inputs starting from a given address.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ip**: The TCP IP address.<br>**addr**: The starting address for reading discrete inputs.<br>**size**: The number of discrete inputs to read.<br>**timeout_ms**: The timeout duration for the write operation.<br>- A value of -1 makes the function block until the write is complete.<br>- A value of 0 makes it non-blocking.<br>- A positive value specifies the maximum time (in milliseconds) to wait.<br>**port**: The TCP port. A value of -1 signifies that the default port<br>from the constructor will be applied.<br>|
| **return** | std::vector<uint8_t>/list[int] A vector containing the read discrete input values. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint8_t> read_discrete_input(const std::string ip, const uint32_t addr,
>                                         const uint32_t size, const int timeout_ms=-1,
>                                         const int port=-1)
> ```
#### read\_input\_registers {#read\_input\_registers-2}

```python
def read_input_registers(self, ip: str, addr: int, size: int, timeout_ms: int = -1, port: int = -1) -> list[int]
```
Reads input registers from the Modbus device.\nThis function reads a specified number of input registers starting from a given address.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ip**: The TCP IP address.<br>**addr**: The starting address for reading input registers.<br>**size**: The number of input registers to read.<br>**timeout_ms**: The timeout duration for the write operation.<br>- A value of -1 makes the function block until the write is complete.<br>- A value of 0 makes it non-blocking.<br>- A positive value specifies the maximum time (in milliseconds) to wait.<br>**port**: The TCP port. A value of -1 signifies that the default port<br>from the constructor will be applied.<br>|
| **return** | std::vector<uint16_t>/list[int] A vector containing the read input register values. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint16_t> read_input_registers(const std::string ip, const uint32_t addr,
>                                         const uint32_t size, const int timeout_ms=-1,
>                                         const int port=-1)
> ```
#### read\_holding\_registers {#read\_holding\_registers-2}

```python
def read_holding_registers(self, ip: str, addr: int, size: int, timeout_ms: int = -1, port: int = -1) -> list[int]
```
Reads holding registers from the Modbus device.\nThis function reads a specified number of holding registers starting from a given address.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ip**: The TCP IP address.<br>**addr**: The starting address for reading holding registers.<br>**size**: The number of holding registers to read.<br>**timeout_ms**: The timeout duration for the write operation.<br>- A value of -1 makes the function block until the write is complete.<br>- A value of 0 makes it non-blocking.<br>- A positive value specifies the maximum time (in milliseconds) to wait.<br>**port**: The TCP port. A value of -1 signifies that the default port<br>from the constructor will be applied.<br>|
| **return** | std::vector<uint16_t>/list[int] A vector containing the read holding register values. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint16_t> read_holding_registers(const std::string ip, const uint32_t addr,
>                                         const uint32_t size, const int timeout_ms=-1,
>                                         const int port=-1)
> ```
#### write\_holding\_registers {#write\_holding\_registers-2}

```python
def write_holding_registers(self, ip: str, data: list[int], addr: int, timeout_ms: int = -1, port: int = -1) -> int
```
Writes values to holding registers on the Modbus device.\nThis function writes the specified data to the holding registers starting from a given address.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ip**: The TCP IP address.<br>**data**: A vector containing the values to write to holding registers.<br>**addr**: The starting address for writing holding registers.<br>**timeout_ms**: The timeout duration for the write operation.<br>- A value of -1 makes the function block until the write is complete.<br>- A value of 0 makes it non-blocking.<br>- A positive value specifies the maximum time (in milliseconds) to wait.<br>**port**: The TCP port. A value of -1 signifies that the default port<br>from the constructor will be applied.<br>|
| **return** | int Returns the number of bytes written on success, or a value less than 0 on failure. |
| **static** | False |

> C++ defination code:
> ```cpp
> int write_holding_registers(const std::string ip, const std::vector<uint16_t>& data,
>                                     const uint32_t addr, const int timeout_ms=-1,
>                                     const int port=-1)
> ```
