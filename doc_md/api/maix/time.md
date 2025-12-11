---
title: maix.time
---

maix.time module


> You can use `maix.time` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}

### time {#time}

```python
def time() -> float
```
Get current time in s

| item | description |
| --- | --- |
| **return** | current time in s, double type |
| **attention** | If board have no RTC battery, when bootup and connect to network,<br>system will automatically sync time by NTP, will cause time() have big change,<br>e.g. before NTP: 10(s), after: 1718590639.5149617(s).<br>If you want to calculate time interval, please use ticks_s(). |

> C++ defination code:
> ```cpp
> double time()
> ```
### time\_ms {#time\_ms}

```python
def time_ms() -> int
```
Get current time in ms

| item | description |
| --- | --- |
| **return** | current time in ms, uint64_t type |
| **attention** | If board have no RTC battery, when bootup and connect to network,<br>system will automatically sync time by NTP, will cause time() have big change,<br>e.g. before NTP: 10000(ms), after: 1718590639000(ms)<br>If you want to calculate time interval, please use ticks_ms(). |

> C++ defination code:
> ```cpp
> uint64_t time_ms()
> ```
### time\_s {#time\_s}

```python
def time_s() -> int
```
Get current time in s

| item | description |
| --- | --- |
| **return** | current time in s, uint64_t type |
| **attention** | If board have no RTC battery, when bootup and connect to network,<br>system will automatically sync time by NTP, will cause time() have big change,<br>e.g. before NTP: 10(s), after: 1718590639(s) |

> C++ defination code:
> ```cpp
> uint64_t time_s()
> ```
### time\_us {#time\_us}

```python
def time_us() -> int
```
Get current time in us

| item | description |
| --- | --- |
| **return** | current time in us, uint64_t type |
| **attention** | If board have no RTC battery, when bootup and connect to network,<br>system will automatically sync time by NTP, will cause time() have big change,<br>e.g. before NTP: 10000000(us), after: 1718590639000000(s)<br>If you want to calculate time interval, please use ticks_us(). |

> C++ defination code:
> ```cpp
> uint64_t time_us()
> ```
### time\_diff {#time\_diff}

```python
def time_diff(last: float, now: float = -1) -> float
```
Calculate time difference in s.

| item | description |
| --- | --- |
| **param** | **last**: last time<br>**now**: current time, can be -1 if use current time<br>|
| **return** | time difference |
| **attention** | If board have no RTC battery, when bootup and connect to network,<br>system will automatically sync time by NTP, will cause time() have big change, and lead to big value.<br>e.g. before NTP: 1(s), after: 1718590500(s)<br>If you want to calculate time interval, please use ticks_diff(). |

> C++ defination code:
> ```cpp
> double time_diff(double last, double now = -1)
> ```
### ticks\_s {#ticks\_s}

```python
def ticks_s() -> float
```
Get current time in s since bootup

| item | description |
| --- | --- |
| **return** | current time in s, double type |

> C++ defination code:
> ```cpp
> double ticks_s()
> ```
### ticks\_ms {#ticks\_ms}

```python
def ticks_ms() -> int
```
Get current time in ms since bootup

| item | description |
| --- | --- |
| **return** | current time in ms, uint64_t type |

> C++ defination code:
> ```cpp
> uint64_t ticks_ms()
> ```
### ticks\_us {#ticks\_us}

```python
def ticks_us() -> int
```
Get current time in us since bootup

| item | description |
| --- | --- |
| **return** | current time in us, uint64_t type |

> C++ defination code:
> ```cpp
> uint64_t ticks_us()
> ```
### ticks\_diff {#ticks\_diff}

```python
def ticks_diff(last: float, now: float = -1) -> float
```
Calculate time difference in s.

| item | description |
| --- | --- |
| **param** | **last**: last time<br>**now**: current time, can be -1 if use current time<br>|
| **return** | time difference |

> C++ defination code:
> ```cpp
> double ticks_diff(double last, double now = -1)
> ```
### sleep {#sleep}

Sleep seconds

| item | description |
| --- | --- |
| **param** | **s**: seconds, double type<br>|

> C++ defination code:
> ```cpp
> void sleep(double s)
> ```
### sleep\_ms {#sleep\_ms}

Sleep milliseconds

| item | description |
| --- | --- |
| **param** | **ms**: milliseconds, uint64_t type<br>|

> C++ defination code:
> ```cpp
> void sleep_ms(uint64_t ms)
> ```
### sleep\_us {#sleep\_us}

Sleep microseconds

| item | description |
| --- | --- |
| **param** | **us**: microseconds, uint64_t type<br>|

> C++ defination code:
> ```cpp
> void sleep_us(uint64_t us)
> ```
### fps {#fps}

```python
def fps() -> float
```
Calculate FPS since last call this method.\nAttention, this method is not multi thread safe, only call this method in one threads.\nIf you want to use in multi threads, please use time.FPS class.\nFPS is average value of recent n(buff_len) times, and you can call fps_set_buff_len(10) to change buffer length, default is 20.\nMultiple invoke this function will calculate fps between two invoke, and you can also call fps_start() fisrt to manually assign fps calulate start point.

| item | description |
| --- | --- |
| **return** | float type, current fps since last call this method |

> C++ defination code:
> ```cpp
> float fps()
> ```
### fps\_start {#fps\_start}

```python
def fps_start() -> None
```
Manually set fps calculation start point, then you can call fps() function to calculate fps between fps_start() and fps().


> C++ defination code:
> ```cpp
> void fps_start()
> ```
### fps\_set\_buff\_len {#fps\_set\_buff\_len}

```python
def fps_set_buff_len(len: int) -> None
```
Set fps method buffer length, by default the buffer length is 10.

| item | description |
| --- | --- |
| **param** | **len**: Buffer length to store recent fps value.<br>|

> C++ defination code:
> ```cpp
> void fps_set_buff_len(int len)
> ```
### now {#now}

```python
def now() -> DateTime
```
Get current UTC date and time

| item | description |
| --- | --- |
| **return** | current date and time, DateTime type |

> C++ defination code:
> ```cpp
> time::DateTime *now()
> ```
### localtime {#localtime}

```python
def localtime() -> DateTime
```
Get local time

| item | description |
| --- | --- |
| **return** | local time, DateTime type |

> C++ defination code:
> ```cpp
> time::DateTime *localtime()
> ```
### strptime {#strptime}

```python
def strptime(str: str, format: str) -> DateTime
```
DateTime from string

| item | description |
| --- | --- |
| **param** | **str**: date time string<br>**format**: date time format<br>|
| **return** | DateTime |

> C++ defination code:
> ```cpp
> time::DateTime *strptime(const std::string &str, const std::string &format)
> ```
### gmtime {#gmtime}

```python
def gmtime(timestamp: float) -> DateTime
```
timestamp to DateTime(time zone is UTC (value 0))

| item | description |
| --- | --- |
| **param** | **timestamp**: double timestamp<br>|
| **return** | DateTime |

> C++ defination code:
> ```cpp
> time::DateTime *gmtime(double timestamp)
> ```
### timezone {#timezone}

```python
def timezone(timezone: str = '') -> str
```
Set or get timezone

| item | description |
| --- | --- |
| **param** | **timezone**: string type, can be empty and default to empty, if empty, only return crrent timezone, a "region/city" string, e.g. Asia/Shanghai, Etc/UTC, you can get all by list_timezones function.<br>|
| **return** | string type, return current timezone setting. |
| **attention** | when set new timezone, time setting not take effect in this process for some API, so you need to restart program. |

> C++ defination code:
> ```cpp
> std::string timezone(const std::string &timezone = "")
> ```
### timezone2 {#timezone2}

```python
def timezone2(region: str = '', city: str = '') -> list[str]
```
Set or get timezone

| item | description |
| --- | --- |
| **param** | **region**: string type, which region to set, can be empty means only get current, default empty.<br>**city**: string type, which city to set, can be empty means only get current, default empty.<br>|
| **return** | list type, return current timezone setting, first is region, second is city. |
| **attention** | when set new timezone, time setting not take effect in this process for some API, so you need to restart program. |

> C++ defination code:
> ```cpp
> std::vector<std::string> timezone2(const std::string &region = "", const std::string &city = "")
> ```
### list\_timezones {#list\_timezones}

```python
def list_timezones() -> dict[str, list[str]]
```
List all timezone info

| item | description |
| --- | --- |
| **return** | A dict with key are regions, and value are region's cities. |

> C++ defination code:
> ```cpp
> std::map<std::string, std::vector<std::string>> list_timezones()
> ```
### ntp\_timetuple {#ntp\_timetuple}

```python
def ntp_timetuple(host: str, port: int = -1, retry: int = 3, timeout_ms: int = 0) -> list[int]
```
Retrieves time from an NTP server\nThis function fetches the current time from the specified NTP server and port,\nreturning a tuple containing the time details.

| item | description |
| --- | --- |
| **param** | **host**: The hostname or IP address of the NTP server.<br>**port**: The port number of the NTP server. Use -1 for the default port 123.<br>**retry**: The number of retry attempts. Must be at least 1.<br>**timeout_ms**: The timeout duration in milliseconds. Must be non-negative.<br>|
| **return** | A list of 6 elements: [year, month, day, hour, minute, second] |

> C++ defination code:
> ```cpp
> std::vector<int> ntp_timetuple(std::string host, int port=-1, uint8_t retry=3, int timeout_ms=0)
> ```
### ntp\_timetuple\_with\_config {#ntp\_timetuple\_with\_config}

```python
def ntp_timetuple_with_config(path: str) -> list[int]
```
Retrieves time from an NTP server using a configuration file\nThis function reads the configuration from a YAML file to fetch the current time\nfrom a list of specified NTP servers, returning a tuple containing the time details.

| item | description |
| --- | --- |
| **param** | **path**: The path to the YAML configuration file, which should include:<br>- Config:<br>- retry: Number of retry attempts (must be at least 1)<br>- total_timeout_ms: Total timeout duration in milliseconds (must be non-negative)<br>- NtpServers:<br>- host: Hostname or IP address of the NTP server<br>- port: Port number of the NTP server (use 123 for default)<br>Example YAML configuration:<br>Config:<br>- retry: 3<br>- total_timeout_ms: 10000<br>NtpServers:<br>- host: "pool.ntp.org"<br>port: 123<br>- host: "time.nist.gov"<br>port: 123<br>- host: "time.windows.com"<br>port: 123<br>|
| **return** | A list of 6 elements: [year, month, day, hour, minute, second] |

> C++ defination code:
> ```cpp
> std::vector<int> ntp_timetuple_with_config(std::string path)
> ```
### ntp\_sync\_sys\_time {#ntp\_sync\_sys\_time}

```python
def ntp_sync_sys_time(host: str, port: int = -1, retry: int = 3, timeout_ms: int = 0) -> list[int]
```
Retrieves time from an NTP server and synchronizes the system time\nThis function fetches the current time from the specified NTP server and port,\nthen synchronizes the system time with the retrieved time.

| item | description |
| --- | --- |
| **param** | **host**: The hostname or IP address of the NTP server.<br>**port**: The port number of the NTP server. Use 123 for the default port.<br>**retry**: The number of retry attempts. Must be at least 1.<br>**timeout_ms**: The timeout duration in milliseconds. Must be non-negative.<br>|
| **return** | A list of 6 elements: [year, month, day, hour, minute, second] |

> C++ defination code:
> ```cpp
> std::vector<int> ntp_sync_sys_time(std::string host, int port=-1, uint8_t retry=3, int timeout_ms=0)
> ```
### ntp\_sync\_sys\_time\_with\_config {#ntp\_sync\_sys\_time\_with\_config}

```python
def ntp_sync_sys_time_with_config(path: str) -> list[int]
```
Retrieves time from an NTP server using a configuration file and synchronizes the system time\nThis function reads the configuration from a YAML file to fetch the current time\nfrom a list of specified NTP servers, then synchronizes the system time with the retrieved time.

| item | description |
| --- | --- |
| **param** | **path**: The path to the YAML configuration file, which should include:<br>- Config:<br>- retry: Number of retry attempts (must be at least 1)<br>- total_timeout_ms: Total timeout duration in milliseconds (must be non-negative)<br>- NtpServers:<br>- host: Hostname or IP address of the NTP server<br>- port: Port number of the NTP server (use 123 for default)<br>Example YAML configuration:<br>Config:<br>- retry: 3<br>- total_timeout_ms: 10000<br>NtpServers:<br>- host: "pool.ntp.org"<br>port: 123<br>- host: "time.nist.gov"<br>port: 123<br>- host: "time.windows.com"<br>port: 123<br>|
| **return** | A vector of integers containing the time details: [year, month, day, hour, minute, second] |

> C++ defination code:
> ```cpp
> std::vector<int> ntp_sync_sys_time_with_config(std::string path)
> ```


## Class {#Class}

### FPS {#FPS-2}

FPS class to use average filter to calculate FPS.


> C++ defination code:
> ```cpp
> class FPS
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, buff_len: int = 20) -> None
```
FPS class constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **buff_len**: Average buffer length, default 20, that is, fps() function will return the average fps in recent buff_len times fps.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> FPS(int buff_len = 20)
> ```
#### start {#start}

```python
def start(self) -> None
```
Manually set fps calculation start point, then you can call fps() function to calculate fps between start() and fps().

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void start()
> ```
#### fps {#fps-3}

```python
def fps(self) -> float
```
The same as end function.

| item | description |
| --- | --- |
| **type** | func |
| **return** | float type, current fps since last call this method |
| **static** | False |

> C++ defination code:
> ```cpp
> float fps()
> ```
#### end {#end}

```python
def end(self) -> float
```
Calculate FPS since last call this method.\nFPS is average value of recent n(buff_len) times, and you can call fps_set_buff_len(10) to change buffer length, default is 20.\nMultiple invoke this function will calculate fps between two invoke, and you can also call fps_start() fisrt to manually assign fps calulate start point.

| item | description |
| --- | --- |
| **type** | func |
| **return** | float type, current fps since last call this method |
| **static** | False |

> C++ defination code:
> ```cpp
> float end()
> ```
#### set\_buff\_len {#set\_buff\_len}

```python
def set_buff_len(self, len: int) -> None
```
Set fps method buffer length, by default the buffer length is 10.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **len**: Buffer length to store recent fps value.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_buff_len(int len)
> ```
### DateTime {#DateTime}

Date and time class


> C++ defination code:
> ```cpp
> class DateTime
> ```

#### year {#year}

Year

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int year
> ```
#### month {#month}

Month, 1~12

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int month
> ```
#### day {#day}

Day

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int day
> ```
#### hour {#hour}

Hour

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int hour
> ```
#### minute {#minute}

Minute

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int minute
> ```
#### second {#second}

Second

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int second
> ```
#### microsecond {#microsecond}

Microsecond

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int microsecond
> ```
#### yearday {#yearday}

Year day

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int yearday
> ```
#### weekday {#weekday}

Weekday, 0 is Monday, 6 is Sunday

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int weekday
> ```
#### zone {#zone}

Time zone

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float zone
> ```
#### zone\_name {#zone\_name}

Time zone name

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string zone_name
> ```
#### \_\_init\_\_ {#\_\_init\_\_-2}

```python
def __init__(self, year: int = 0, month: int = 0, day: int = 0, hour: int = 0, minute: int = 0, second: int = 0, microsecond: int = 0, yearday: int = 0, weekday: int = 0, zone: int = 0) -> None
```
Constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **year**: year<br>**month**: month<br>**day**: day<br>**hour**: hour<br>**minute**: minute<br>**second**: second<br>**microsecond**: microsecond<br>**yearday**: year day<br>**weekday**: weekday<br>**zone**: time zone<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> DateTime(int year = 0, int month = 0, int day = 0, int hour = 0, int minute = 0, int second = 0, int microsecond = 0, int yearday = 0, int weekday = 0, int zone = 0)
> ```
#### strftime {#strftime}

```python
def strftime(self, format: str) -> str
```
Convert to string

| item | description |
| --- | --- |
| **type** | func |
| **return** | date time string |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string strftime(const std::string &format)
> ```
#### timestamp {#timestamp}

```python
def timestamp(self) -> float
```
Convert to float timestamp

| item | description |
| --- | --- |
| **type** | func |
| **return** | float timestamp |
| **static** | False |

> C++ defination code:
> ```cpp
> double timestamp()
> ```
