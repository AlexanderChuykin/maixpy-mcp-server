---
title: maix.ext_dev.lsm6dsowtr
---

maix.ext_dev.lsm6dsowtr module


> You can use `maix.ext_dev.lsm6dsowtr` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### LSM6DSOWTR {#LSM6DSOWTR}

LSM6DSOWTR driver class


> C++ defination code:
> ```cpp
> class LSM6DSOWTR
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, mode: maix.ext_dev.imu.Mode = ..., acc_scale: maix.ext_dev.imu.AccScale = ..., acc_odr: maix.ext_dev.imu.AccOdr = ..., gyro_scale: maix.ext_dev.imu.GyroScale = ..., gyro_odr: maix.ext_dev.imu.GyroOdr = ..., block: bool = True) -> None
```
Construct a new LSM6DSOWTR object, will open LSM6DSOWTR

| item | description |
| --- | --- |
| **type** | func |
| **param** | **mode**: LSM6DSOWTR Mode: ACC_ONLY/GYRO_ONLY/DUAL<br>**acc_scale**: acc scale, see @imu::AccScale<br>**acc_odr**: acc output data rate, see @imu::AccOdr<br>**gyro_scale**: gyro scale, see @imu::GyroScale<br>**gyro_odr**: gyro output data rate, see @imu::GyroOdr<br>**block**: block or non-block, defalut is true<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> LSM6DSOWTR(
>             maix::ext_dev::imu::Mode mode=maix::ext_dev::imu::Mode::DUAL,
>             maix::ext_dev::imu::AccScale acc_scale=maix::ext_dev::imu::AccScale::ACC_SCALE_2G,
>             maix::ext_dev::imu::AccOdr acc_odr=maix::ext_dev::imu::AccOdr::ACC_ODR_8000,
>             maix::ext_dev::imu::GyroScale gyro_scale=maix::ext_dev::imu::GyroScale::GYRO_SCALE_16DPS,
>             maix::ext_dev::imu::GyroOdr gyro_odr=maix::ext_dev::imu::GyroOdr::GYRO_ODR_8000,
>             bool block=true)
> ```
#### read {#read}

```python
def read(self) -> list[float]
```
Read data from LSM6DSOWTR.

| item | description |
| --- | --- |
| **type** | func |
| **return** | list type. If only one of the outputs is initialized, only [x,y,z] of that output will be returned.<br>If all outputs are initialized, [acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z] is returned. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<float> read()
> ```
