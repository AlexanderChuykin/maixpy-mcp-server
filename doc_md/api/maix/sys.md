---
title: maix.sys
---

maix.sys module


> You can use `maix.sys` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### Feature {#Feature}

Special features enumerate for sys.is_support to query platform support feature or not.

| item | describe |
| --- | --- |
| **values** | **AI_ISP**: <br>**MAX**: <br>
> C++ defination code:
> ```cpp
> enum class Feature
>     {
>         AI_ISP = 0,
>         MAX
>     }
> ```


## Variable {#Variable}



## Function {#Function}

### os\_version {#os\_version}

```python
def os_version() -> str
```
Get system version

| item | description |
| --- | --- |
| **return** | version string, e.g. "maixcam-2024-08-13-maixpy-v4.4.20" |

> C++ defination code:
> ```cpp
> std::string os_version()
> ```
### maixpy\_version {#maixpy\_version}

```python
def maixpy_version() -> str
```
Get MaixPy version, if get failed will return empty string.

| item | description |
| --- | --- |
| **return** | version  string, e.g. "4.4.21" |

> C++ defination code:
> ```cpp
> std::string maixpy_version()
> ```
### runtime\_version {#runtime\_version}

```python
def runtime_version() -> str
```
Get runtime version

| item | description |
| --- | --- |
| **return** | current runtime version |

> C++ defination code:
> ```cpp
> std::string runtime_version()
> ```
### device\_configs {#device\_configs}

```python
def device_configs(cache: bool = True) -> dict[str, str]
```
Get device configs, we also say board configs. e.g. for MaixCAM it read form /boot/board

| item | description |
| --- | --- |
| **param** | **cache**: read config from cache(if exists, or will call device_configs first internally) if true,<br>if false, always read fron config file.<br>|
| **return** | device config,json format |
| **throw** | If board config file error will throw out exception(err.Exception) |

> C++ defination code:
> ```cpp
> std::map<std::string, std::string> device_configs(bool cache = true)
> ```
### device\_id {#device\_id}

```python
def device_id(cache: bool = True) -> str
```
Get device id

| item | description |
| --- | --- |
| **param** | **cache**: read id from cache(if exists, or will call device_configs first internally) if true,<br>if false, always read fron config file.<br>|
| **return** | device id, e.g. "maixcam" "maixcam_pro" |

> C++ defination code:
> ```cpp
> std::string device_id(bool cache = true)
> ```
### device\_name {#device\_name}

```python
def device_name(cache: bool = True) -> str
```
Get device name

| item | description |
| --- | --- |
| **param** | **cache**: read id from cache(if exists, or will call device_configs first internally) if true,<br>if false, always read fron config file.<br>|
| **return** | device name, e.g. "MaixCAM" "MaixCAM-Pro" |

> C++ defination code:
> ```cpp
> std::string device_name(bool cache = true)
> ```
### host\_name {#host\_name}

```python
def host_name() -> str
```
Get host name

| item | description |
| --- | --- |
| **return** | host name, e.g. "maixcam-2f9f" |

> C++ defination code:
> ```cpp
> std::string host_name()
> ```
### host\_domain {#host\_domain}

```python
def host_domain() -> str
```
Get host domain

| item | description |
| --- | --- |
| **return** | host domain, e.g. "maixcam-2f9f.local" |

> C++ defination code:
> ```cpp
> std::string host_domain()
> ```
### ip\_address {#ip\_address}

```python
def ip_address() -> dict[str, str]
```
Get ip address

| item | description |
| --- | --- |
| **return** | ip address, dict type, e.g. {"eth0": "192.168.0.195", "wlan0": "192.168.0.123", "usb0": "10.47.159.1"} |

> C++ defination code:
> ```cpp
> std::map<std::string, std::string> ip_address()
> ```
### mac\_address {#mac\_address}

```python
def mac_address() -> dict[str, str]
```
Get mac address

| item | description |
| --- | --- |
| **return** | mac address, dict type, e.g. {"eth0": "00:0c:29:2f:9f:00", "wlan0": "00:0c:29:2f:9f:01", "usb0": "00:0c:29:2f:9f:02"} |

> C++ defination code:
> ```cpp
> std::map<std::string, std::string> mac_address()
> ```
### device\_key {#device\_key}

```python
def device_key() -> str
```
Get device key, can be unique id of device

| item | description |
| --- | --- |
| **return** | device key, 32 bytes hex string, e.g. "1234567890abcdef1234567890abcdef" |

> C++ defination code:
> ```cpp
> std::string device_key()
> ```
### memory\_info {#memory\_info}

```python
def memory_info() -> dict[str, int]
```
Get memory info

| item | description |
| --- | --- |
| **return** | memory info, dict type, e.g. {"total": 1024, "used": 512, "hw_total": 256*1024*1024}<br>total: total memory size in Byte.<br>used: used memory size in Byte.<br>hw_total: total memory size in Byte of hardware, the total <= hw_total，<br>OS kernel may reserve some memory for some hardware like camera, npu, display etc.<br>cmm_total: Board or Chip custom memory management area, we call them cmm memory here. For example, for MaixCAM is IOA, for MaixCAM2 is CMM.<br>cmm_used: Board or Chip custom memory management area used size, we call them cmm memory here.<br>cma_total: Contiguous Memory Allocator (Linux CMA standard) total size in Byte.<br>cma_used: Contiguous Memory Allocator (Linux CMA standard) used size in Byte. |

> C++ defination code:
> ```cpp
> std::map<std::string, int64_t> memory_info()
> ```
### bytes\_to\_human {#bytes\_to\_human}

```python
def bytes_to_human(bytes: int, precision: int = 2, base: int = 1024, units: list[str] = [], sep: str = ' ') -> str
```
Bytes to human readable string

| item | description |
| --- | --- |
| **param** | **bytes:**: bytes size，e.g. 1234B = 1234/1024 = 1.205 KB<br>**precision:**: decimal precision, default 2<br>**base:**: base number, default 1024<br>**unit:**: unit string, e.g. "B"<br>**sep:**: separator string, e.g. " "<br>|
| **return** | human readable string, e.g. "1.21 KB" |

> C++ defination code:
> ```cpp
> std::string bytes_to_human(unsigned long long bytes, int precision = 2, int base = 1024, const std::vector<std::string> &units = std::vector<std::string>(), const std::string &sep = " ")
> ```
### cpu\_freq {#cpu\_freq}

```python
def cpu_freq() -> dict[str, int]
```
Get CPU frequency

| item | description |
| --- | --- |
| **return** | CPU frequency, dict type, e.g. {"cpu0": 1000000000, "cpu1": 1000000000} |

> C++ defination code:
> ```cpp
> std::map<std::string, unsigned long> cpu_freq()
> ```
### cpu\_temp {#cpu\_temp}

```python
def cpu_temp() -> dict[str, float]
```
Get CPU temperature

| item | description |
| --- | --- |
| **return** | CPU temperature, unit dgree, dict type, e.g. {"cpu": 50.0, "cpu0": 50, "cpu1": 50} |

> C++ defination code:
> ```cpp
> std::map<std::string, float> cpu_temp()
> ```
### cpu\_usage {#cpu\_usage}

```python
def cpu_usage() -> dict[str, float]
```
Get CPU usage

| item | description |
| --- | --- |
| **return** | CPU usage, dict type, e.g. {"cpu": 50.0, "cpu0": 50, "cpu1": 50} |

> C++ defination code:
> ```cpp
> std::map<std::string, float> cpu_usage()
> ```
### npu\_freq {#npu\_freq}

```python
def npu_freq() -> dict[str, int]
```
Get NPU frequency

| item | description |
| --- | --- |
| **return** | NPU frequency, dict type, e.g. {"npu0": 500000000}, value -1 means not support query on this platform.<br>If get from system failed, will return last time value. |

> C++ defination code:
> ```cpp
> std::map<std::string, unsigned long> npu_freq()
> ```
### npu\_usage {#npu\_usage}

```python
def npu_usage() -> dict[str, float]
```
Get NPU usage

| item | description |
| --- | --- |
| **return** | NPU usage, dict type, e.g. {"npu": 50.0, "npu0": 50, "npu1": 50} |

> C++ defination code:
> ```cpp
> std::map<std::string, float> npu_usage()
> ```
### disk\_usage {#disk\_usage}

```python
def disk_usage(path: str = '/') -> dict[str, int]
```
Get disk usage

| item | description |
| --- | --- |
| **param** | **path:**: disk path, default "/"<br>|
| **return** | disk usage, dict type, e.g. {"total": 1024, "used": 512} |

> C++ defination code:
> ```cpp
> std::map<std::string, unsigned long long> disk_usage(const std::string &path = "/")
> ```
### disk\_partitions {#disk\_partitions}

```python
def disk_partitions(only_disk: bool = True) -> list[dict[str, str]]
```
Get disk partition and mount point info

| item | description |
| --- | --- |
| **param** | **only_disk**: only return real disk, tempfs sysfs etc. not return, default true.<br>|
| **return** | disk partition and mount point info, list type, e.g. [{"device": "/dev/mmcblk0p1", "mountpoint": "/mnt/sdcard", "fstype": "vfat"}] |

> C++ defination code:
> ```cpp
> std::vector<std::map<std::string, std::string>> disk_partitions(bool only_disk = true)
> ```
### register\_default\_signal\_handle {#register\_default\_signal\_handle}

register default signal handle


> C++ defination code:
> ```cpp
> void register_default_signal_handle()
> ```
### poweroff {#poweroff}

```python
def poweroff() -> None
```
Power off device


> C++ defination code:
> ```cpp
> void poweroff()
> ```
### reboot {#reboot}

```python
def reboot() -> None
```
Power off device and power on


> C++ defination code:
> ```cpp
> void reboot()
> ```
### is\_support {#is\_support}

```python
def is_support(feature: Feature) -> bool
```
Query is board support special feature or not.

| item | description |
| --- | --- |
| **param** | **feature**: which feature you want to query, see sys.Feature enumerate.<br>|

> C++ defination code:
> ```cpp
> bool is_support(sys::Feature feature)
> ```


## Class {#Class}

