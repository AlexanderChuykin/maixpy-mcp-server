---
title: maix.network.wifi
---

maix.network.wifi module


> You can use `maix.network.wifi` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}

### list\_devices {#list\_devices}

```python
def list_devices() -> list[str]
```
List WiFi interfaces

| item | description |
| --- | --- |
| **return** | WiFi interface list, string type |

> C++ defination code:
> ```cpp
> std::vector<std::string> list_devices()
> ```


## Class {#Class}

### AP\_Info {#AP\_Info}

WiFi AP info


> C++ defination code:
> ```cpp
> class AP_Info
> ```

#### ssid {#ssid}

WiFi AP info SSID

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<uint8_t> ssid
> ```
#### bssid {#bssid}

WiFi AP info BSSID

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string bssid
> ```
#### security {#security}

WiFi AP info security

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string security
> ```
#### channel {#channel}

WiFi AP info channel

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int channel
> ```
#### frequency {#frequency}

WiFi AP info frequency

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int frequency
> ```
#### rssi {#rssi}

WiFi AP info rssi

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int rssi
> ```
#### ssid\_str {#ssid\_str}

```python
def ssid_str(self) -> str
```
WiFi AP info ssid_str

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string ssid_str()
> ```
### Wifi {#Wifi}

Wifi class


> C++ defination code:
> ```cpp
> class Wifi
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, iface: str = 'wlan0') -> None
```
Wifi class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **iface**: wifi interface name, default is wlan0<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Wifi(std::string iface = "wlan0")
> ```
#### get\_ip {#get\_ip}

```python
def get_ip(self) -> str
```
Get current WiFi ip

| item | description |
| --- | --- |
| **type** | func |
| **return** | ip, string type, if network not connected, will return empty string. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string get_ip()
> ```
#### get\_mac {#get\_mac}

```python
def get_mac(self) -> str
```
Get current WiFi MAC address

| item | description |
| --- | --- |
| **type** | func |
| **return** | ip, string type. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string get_mac()
> ```
#### get\_ssid {#get\_ssid}

```python
def get_ssid(self, from_cache: bool = True) -> str
```
Get current WiFi SSID

| item | description |
| --- | --- |
| **type** | func |
| **param** | **from_cache**: if true, will not read config from file, direct use ssid in cache.<br>attention, first time call this method will auto matically read config from file, and if call connect method will set cache.<br>|
| **return** | SSID, string type. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string get_ssid(bool from_cache = true)
> ```
#### get\_gateway {#get\_gateway}

```python
def get_gateway(self) -> str
```
Get current WiFi ip

| item | description |
| --- | --- |
| **type** | func |
| **return** | ip, string type, if network not connected, will return empty string. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string get_gateway()
> ```
#### start\_scan {#start\_scan}

```python
def start_scan(self) -> maix.err.Err
```
WiFi start scan AP info around in background.

| item | description |
| --- | --- |
| **type** | func |
| **return** | If success, return err.Err.ERR_NONE, else means failed. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err start_scan()
> ```
#### get\_scan\_result {#get\_scan\_result}

```python
def get_scan_result(self) -> list[AP_Info]
```
Get WiFi scan AP info.

| item | description |
| --- | --- |
| **type** | func |
| **return** | wifi.AP_Info list. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<network::wifi::AP_Info> get_scan_result()
> ```
#### stop\_scan {#stop\_scan}

```python
def stop_scan(self) -> None
```
Stop WiFi scan AP info.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void stop_scan()
> ```
#### connect {#connect}

```python
def connect(self, ssid: str, password: str, wait: bool = True, timeout: int = 60) -> maix.err.Err
```
Connect to WiFi AP.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ssid**: SSID of AP<br>**password**: password of AP, if no password, leave it empty.<br>**wait**: wait for got IP or failed or timeout.<br>**timeout**: connect timeout internal, unit second.<br>|
| **return** | If success, return err.Err.ERR_NONE, else means failed. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err connect(const std::string &ssid, const std::string &password, bool wait = true, int timeout = 60)
> ```
#### disconnect {#disconnect}

```python
def disconnect(self) -> maix.err.Err
```
Disconnect from WiFi AP.

| item | description |
| --- | --- |
| **type** | func |
| **return** | If success, return err.Err.ERR_NONE, else means failed. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err disconnect()
> ```
#### is\_connected {#is\_connected}

```python
def is_connected(self) -> bool
```
See if WiFi is connected to AP.

| item | description |
| --- | --- |
| **type** | func |
| **return** | If connected return true, else false. |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_connected()
> ```
#### start\_ap {#start\_ap}

```python
def start_ap(self, ssid: str, password: str, mode: str = 'g', channel: int = 0, ip: str = '192.168.66.1', netmask: str = '255.255.255.0', hidden: bool = False) -> maix.err.Err
```
Start WiFi AP.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ssid**: SSID of AP.<br>**password**: password of AP, if no password, leave it empty.<br>**ip**: ip address of hostap, default empty string means auto generated one according to hardware.<br>**netmask**: netmask, default 255.255.255.0, now only support 255.255.255.0 .<br>**mode**: WiFi mode, default g(IEEE 802.11g (2.4 GHz)), a = IEEE 802.11a (5 GHz), b = IEEE 802.11b (2.4 GHz).<br>**channel**: WiFi channel number, 0 means auto select. MaixCAM not support auto, will default channel 1.<br>**hidden**: hidden SSID or not.<br>|
| **return** | If success, return err.Err.ERR_NONE, else means failed. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err start_ap(const std::string &ssid, const std::string &password,
>                           std::string mode = "g", int channel = 0,
>                           const std::string &ip = "192.168.66.1", const std::string &netmask = "255.255.255.0",
>                           bool hidden = false)
> ```
#### stop\_ap {#stop\_ap}

```python
def stop_ap(self) -> maix.err.Err
```
Stop WiFi AP.

| item | description |
| --- | --- |
| **type** | func |
| **return** | If success, return err.Err.ERR_NONE, else means failed. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err stop_ap()
> ```
#### is\_ap\_mode {#is\_ap\_mode}

```python
def is_ap_mode(self) -> bool
```
Whether WiFi is AP mode

| item | description |
| --- | --- |
| **type** | func |
| **return** | True if AP mode now, or False. |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_ap_mode()
> ```
