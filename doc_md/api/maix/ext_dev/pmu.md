---
title: maix.ext_dev.pmu
---

maix.ext_dev.pmu module


> You can use `maix.ext_dev.pmu` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### ChargerStatus {#ChargerStatus}

charger status

| item | describe |
| --- | --- |
| **values** | **CHG_TRI_STATE**: tri_charge<br>**CHG_PRE_STATE**: pre_charge<br>**CHG_CC_STATE**: constant charge<br>**CHG_CV_STATE**: constant voltage<br>**CHG_DONE_STATE**: charge done<br>**CHG_STOP_STATE**: not charge<br>
> C++ defination code:
> ```cpp
> enum class ChargerStatus {
>     CHG_TRI_STATE,   //tri_charge
>     CHG_PRE_STATE,   //pre_charge
>     CHG_CC_STATE,    //constant charge
>     CHG_CV_STATE,    //constant voltage
>     CHG_DONE_STATE,  //charge done
>     CHG_STOP_STATE,  //not charge
> }
> ```
### PowerChannel {#PowerChannel}

power channel

| item | describe |
| --- | --- |
| **values** | **DCDC1**: <br>**DCDC2**: <br>**DCDC3**: <br>**DCDC4**: <br>**DCDC5**: <br>**ALDO1**: <br>**ALDO2**: <br>**ALDO3**: <br>**ALDO4**: <br>**BLDO1**: <br>**BLDO2**: <br>**DLDO1**: <br>**DLDO2**: <br>**VBACKUP**: <br>**CPULDO**: <br>
> C++ defination code:
> ```cpp
> enum class PowerChannel {
>         DCDC1,
>         DCDC2,
>         DCDC3,
>         DCDC4,
>         DCDC5,
>         ALDO1,
>         ALDO2,
>         ALDO3,
>         ALDO4,
>         BLDO1,
>         BLDO2,
>         DLDO1,
>         DLDO2,
>         VBACKUP,
>         CPULDO,
> }
> ```


## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### PMU {#PMU}

PMU driver class


> C++ defination code:
> ```cpp
> class PMU
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, driver: str = '', i2c_bus: int = -1, addr: int = 52) -> None
```
Construct a new PMU object, will open PMU.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **driver**: driver name, support "axp2101" "maixcam2", default empty means use default.<br>**i2c_bus**: i2c bus number. Automatically selects the on-board pmu when -1 is passed in.<br>**addr**: PMU i2c addr.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> PMU(std::string driver = "", int i2c_bus = -1, int addr = 0x34)
> ```
#### poweroff {#poweroff}

```python
def poweroff(self) -> maix.err.Err
```
Poweroff immediately.

| item | description |
| --- | --- |
| **type** | func |
| **return** | err::Err type, if init success, return err::ERR_NONE. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err poweroff()
> ```
#### is\_bat\_connect {#is\_bat\_connect}

```python
def is_bat_connect(self) -> bool
```
Is the battery connected.

| item | description |
| --- | --- |
| **type** | func |
| **return** | bool type, if battery is connected, return true. |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_bat_connect()
> ```
#### is\_vbus\_in {#is\_vbus\_in}

```python
def is_vbus_in(self) -> bool
```
Is the power adapter connected.

| item | description |
| --- | --- |
| **type** | func |
| **return** | bool type, if power adapter is connected, return true. |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_vbus_in()
> ```
#### is\_charging {#is\_charging}

```python
def is_charging(self) -> bool
```
Is bat charging.

| item | description |
| --- | --- |
| **type** | func |
| **return** | bool type, if bat is charging, return true. |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_charging()
> ```
#### get\_bat\_percent {#get\_bat\_percent}

```python
def get_bat_percent(self) -> int
```
Get the battery percentage.

| item | description |
| --- | --- |
| **type** | func |
| **return** | int type, return battery percentage. |
| **static** | False |

> C++ defination code:
> ```cpp
> int get_bat_percent()
> ```
#### get\_charger\_status {#get\_charger\_status}

```python
def get_charger_status(self) -> ChargerStatus
```
Get the battery charging status.

| item | description |
| --- | --- |
| **type** | func |
| **return** | int type, return battery charging status. |
| **static** | False |

> C++ defination code:
> ```cpp
> ext_dev::pmu::ChargerStatus get_charger_status()
> ```
#### get\_bat\_vol {#get\_bat\_vol}

```python
def get_bat_vol(self) -> int
```
Get the battery voltage.

| item | description |
| --- | --- |
| **type** | func |
| **return** | uint16_t type, return battery voltage. |
| **static** | False |

> C++ defination code:
> ```cpp
> uint16_t get_bat_vol()
> ```
#### clean\_irq {#clean\_irq}

```python
def clean_irq(self) -> maix.err.Err
```
Clear interrupt flag.

| item | description |
| --- | --- |
| **type** | func |
| **return** | err::Err type, if clean success, return err::ERR_NONE. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err clean_irq()
> ```
#### set\_bat\_charging\_cur {#set\_bat\_charging\_cur}

```python
def set_bat_charging_cur(self, current: int) -> maix.err.Err
```
Set the battery charging current.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **current**: The current to be set.<br>|
| **return** | err::Err type, if set success, return err::ERR_NONE. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_bat_charging_cur(int current)
> ```
#### get\_bat\_charging\_cur {#get\_bat\_charging\_cur}

```python
def get_bat_charging_cur(self) -> int
```
Get the battery charging current.

| item | description |
| --- | --- |
| **type** | func |
| **return** | int, return the currently set charging current. |
| **static** | False |

> C++ defination code:
> ```cpp
> int get_bat_charging_cur()
> ```
#### set\_vol {#set\_vol}

```python
def set_vol(self, channel: PowerChannel, voltage: int) -> maix.err.Err
```
Set the PMU channel voltage.\nYou can retrieve the available channel from ext_dev.pmu.PowerChannel.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **voltage**: The voltage to be set.<br>|
| **return** | int, return the channel voltage. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_vol(ext_dev::pmu::PowerChannel channel, int voltage)
> ```
#### get\_vol {#get\_vol}

```python
def get_vol(self, channel: PowerChannel) -> int
```
Get the PMU channel voltage.\nYou can retrieve the available channel from ext_dev.pmu.PowerChannel.

| item | description |
| --- | --- |
| **type** | func |
| **return** | err::Err type, if set success, return err::ERR_NONE. |
| **static** | False |

> C++ defination code:
> ```cpp
> int get_vol(ext_dev::pmu::PowerChannel channel)
> ```
