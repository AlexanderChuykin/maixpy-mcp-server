---
title: maix.ahrs
---

maix.ahrs module


> You can use `maix.ahrs` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}

### PI {#PI}

Math PI

| item | description |
| --- | --- |
| **value** | **3.14159265358979323846f** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const float PI = 3.14159265358979323846f
> ```
### RAD2DEG {#RAD2DEG}

angle unit radian to degree.

| item | description |
| --- | --- |
| **value** | **180.0f / PI** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const float RAD2DEG = 180.0f / PI
> ```
### DEG2RAD {#DEG2RAD}

angle unit degree to radian.

| item | description |
| --- | --- |
| **value** | **PI / 180.0f** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const float DEG2RAD = PI / 180.0f
> ```


## Function {#Function}



## Class {#Class}

### MahonyAHRS {#MahonyAHRS}

class MahonyAHRS for Attitude Estimation from IMU data, a Complementary Filter,\nsupport accelerometer, gyroscope and magnetometer fusion.


> C++ defination code:
> ```cpp
> class MahonyAHRS
> ```

#### kp {#kp}

P of PI controller, a larger P (proportional gain) leads to faster response,\nbut it increases the risk of overshoot and oscillation.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float kp
> ```
#### ki {#ki}

I of PI controller, a larger I (integral gain) helps to eliminate steady-state errors more quickly,\nbut it can accumulate error over time, potentially causing instability or slow drift.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float ki
> ```
#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, kp: float, ki: float) -> None
```
class MahonyAHRS constructor.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **kp**: P of PI controller, a larger P (proportional gain) leads to faster response,<br>but it increases the risk of overshoot and oscillation.<br>**ki**: I of PI controller, a larger I (integral gain) helps to eliminate steady-state errors more quickly,<br>but it can accumulate error over time, potentially causing instability or slow drift.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> MahonyAHRS(float kp,float ki)
> ```
#### init {#init}

```python
def init(self, ax: float, ay: float, az: float, mx: float = 0, my: float = 0, mz: float = 0) -> None
```
Initialize by accelerometer and magnetometer(optional).\nIf you not call this method mannually, get_angle and update method will automatically call it.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ax**: z axis of accelerometer, unit is g or raw data.<br>**ay**: y axis of accelerometer, unit is g or raw data.<br>**mx**: x axis of magnetometer, unit is uT or raw data, mx, my, mz all 0 means not use magnetometer.<br>**my**: y axis of magnetometer, unit is uT or raw data, mx, my, mz all 0 means not use magnetometer.<br>**mz**: z axis of magnetometer, unit is uT or raw data, mx, my, mz all 0 means not use magnetometer.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void init(float ax, float ay, float az, float mx = 0, float my = 0, float mz = 0)
> ```
#### update {#update}

```python
def update(self, ax: float, ay: float, az: float, gx: float, gy: float, gz: float, mx: float, my: float, mz: float, dt: float) -> None
```
Update angles by accelerometer, gyroscope and magnetometer(optional).\nget_angle method will automatically call it.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ax**: z axis of gyroscope, unit is rad/s.<br>**ay**: y axis of gyroscope, unit is rad/s.<br>**mx**: x axis of magnetometer, unit is uT or raw data, mx, my, mz all 0 means not use magnetometer.<br>**my**: y axis of magnetometer, unit is uT or raw data, mx, my, mz all 0 means not use magnetometer.<br>**mz**: z axis of magnetometer, unit is uT or raw data, mx, my, mz all 0 means not use magnetometer.<br>**dt**: Delta time between two times call update method.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void update(float ax, float ay, float az, float gx, float gy, float gz, float mx, float my, float mz, float dt)
> ```
#### get\_angle {#get\_angle}

```python
def get_angle(self, acc: maix.tensor.Vector3f, gyro: maix.tensor.Vector3f, mag: maix.tensor.Vector3f, dt: float, radian: bool = False) -> maix.tensor.Vector3f
```
Get angle by mahony complementary filter, will automatically call update method,\nand automatically call init in first time.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **acc**: accelerometer data, unit is g or raw data. maix.vector.Vector3f type.<br>**gyro**: gyroscope data, unit can be rad/s or degree/s, if rad/s, arg radian should be true. maix.vector.Vector3f type.<br>**mag**: magnetometer data, optional, if no magnetometer, set all value to 0. maix.vector.Vector3f type.<br>**dt**: delta T of two time call get_anle, unit is second, float type.<br>**radian**: if gyro's unit is rad/s, set this arg to true, degree/s set to false.<br>|
| **return** | rotation angle data, maix.vector.Vector3f type. |
| **static** | False |

> C++ defination code:
> ```cpp
> tensor::Vector3f get_angle(tensor::Vector3f acc, tensor::Vector3f gyro, tensor::Vector3f mag, float dt, bool radian = false)
> ```
#### reset {#reset}

```python
def reset(self) -> None
```
reset to not initialized status.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void reset()
> ```
