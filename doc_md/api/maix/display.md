---
title: maix.display
---

maix.display module, control display device and show image on it


> You can use `maix.display` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}

### send\_to\_maixvision {#send\_to\_maixvision}

```python
def send_to_maixvision(img: maix.image.Image) -> None
```
Send image to MaixVision work station if connected.\nIf you want to debug your program an don't want to initialize display, use this method.

| item | description |
| --- | --- |
| **param** | **img**: image to send, image.Image object<br>|

> C++ defination code:
> ```cpp
> void send_to_maixvision(image::Image &img)
> ```
### set\_trans\_image\_quality {#set\_trans\_image\_quality}

```python
def set_trans_image_quality(value: int) -> None
```
Set image transport quality(only for JPEG)

| item | description |
| --- | --- |
| **param** | **quality**: default 95, value from 51 ~ 100<br>|

> C++ defination code:
> ```cpp
> void set_trans_image_quality(const int value)
> ```


## Class {#Class}

### Display {#Display}

Display class


> C++ defination code:
> ```cpp
> class Display
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, width: int = -1, height: int = -1, format: maix.image.Format = ..., device: str = '', open: bool = True) -> None
```
Construct a new Display object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **width**: display width, by default(value is -1) means auto detect,<br>if width > max device supported width, will auto set to max device supported width<br>**height**: display height, by default(value is -1) means auto detect,<br>if height > max device supported height, will auto set to max device supported height<br>**device**: display device name, you can get devices by list_devices method, by default(value is NULL(None in MaixPy)) means the first device<br>**open**: If true, display will automatically call open() after creation. default is true.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Display(int width = -1, int height = -1, image::Format format = image::FMT_RGB888, const std::string &device = "", bool open = true)
> ```
#### width {#width}

```python
def width(self) -> int
```
Get display width

| item | description |
| --- | --- |
| **type** | func |
| **return** | width |
| **static** | False |

> C++ defination code:
> ```cpp
> int width()
> ```
#### height {#height}

```python
def height(self) -> int
```
Get display height

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ch**: channel to get, by default(value is 0) means the first channel<br>|
| **return** | height |
| **static** | False |

> C++ defination code:
> ```cpp
> int height()
> ```
#### size {#size}

```python
def size(self) -> list[int]
```
Get display size

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ch**: channel to get, by default(value is 0) means the first channel<br>|
| **return** | size A list type in MaixPy, [width, height] |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> size()
> ```
#### format {#format}

```python
def format(self) -> maix.image.Format
```
Get display format

| item | description |
| --- | --- |
| **type** | func |
| **return** | format |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format format()
> ```
#### open {#open}

```python
def open(self, width: int = -1, height: int = -1, format: maix.image.Format = ...) -> maix.err.Err
```
open display device, if already opened, will return err.ERR_NONE.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **width**: display width, default is -1, means auto, mostly means max width of display support<br>**height**: display height, default is -1, means auto, mostly means max height of display support<br>**format**: display output format, default is RGB888<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err open(int width = -1, int height = -1, image::Format format = image::FMT_INVALID)
> ```
#### close {#close}

```python
def close(self) -> maix.err.Err
```
close display device

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err close()
> ```
#### add\_channel {#add\_channel}

```python
def add_channel(self, width: int = -1, height: int = -1, format: maix.image.Format = ..., open: bool = True) -> Display
```
Add a new channel and return a new Display object, you can use close() to close this channel.

| item | description |
| --- | --- |
| **type** | func |
| **attention** | If a new disp channel is created, it is recommended to set fit=image::FIT_COVER or fit=image::FIT_FILL when running show for the main channel,<br>otherwise the display of the new disp channel may be abnormal. |
| **param** | **width**: display width, default is -1, means auto, mostly means max width of display support. Maximum width must not exceed the main channel.<br>**height**: display height, default is -1, means auto, mostly means max height of display support. Maximum height must not exceed the main channel.<br>**format**: display output format, default is FMT_BGRA8888<br>**open**: If true, display will automatically call open() after creation. default is true.<br>|
| **return** | new Display object |
| **static** | False |

> C++ defination code:
> ```cpp
> display::Display *add_channel(int width = -1, int height = -1, image::Format format = image::FMT_BGRA8888, bool open = true)
> ```
#### is\_opened {#is\_opened}

```python
def is_opened(self) -> bool
```
check display device is opened or not

| item | description |
| --- | --- |
| **type** | func |
| **return** | opened or not, bool type |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_opened()
> ```
#### is\_closed {#is\_closed}

```python
def is_closed(self) -> bool
```
check display device is closed or not

| item | description |
| --- | --- |
| **type** | func |
| **return** | closed or not, bool type |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_closed()
> ```
#### show {#show}

```python
def show(self, img: maix.image.Image, fit: maix.image.Fit = ...) -> maix.err.Err
```
show image on display device, and will also send to MaixVision work station if connected.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image to show, image.Image object,<br>if the size of image smaller than display size, will show in the center of display;<br>if the size of image bigger than display size, will auto resize to display size and keep ratio, fill blank with black color.<br>**fit**: image in screen fit mode, by default(value is image.FIT_CONTAIN), @see image.Fit for more details<br>e.g. image.FIT_CONTAIN means resize image to fit display size and keep ratio, fill blank with black color.<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err show(image::Image &img, image::Fit fit = image::FIT_CONTAIN)
> ```
#### push {#push}

```python
def push(self, frame: ..., fit: maix.image.Fit = ...) -> maix.err.Err
```
push pipeline frame to display

| item | description |
| --- | --- |
| **type** | func |
| **param** | **frame**: pipeline frame<br>**fit**: image in screen fit mode, by default(value is image.FIT_CONTAIN), @see image.Fit for more details<br>e.g. image.FIT_CONTAIN means resize image to fit display size and keep ratio, fill blank with black color.<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err push(pipeline::Frame *frame, image::Fit fit = image::FIT_CONTAIN)
> ```
#### device {#device}

```python
def device(self) -> str
```
Get display device path

| item | description |
| --- | --- |
| **type** | func |
| **return** | display device path |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string device()
> ```
#### set\_backlight {#set\_backlight}

```python
def set_backlight(self, value: float) -> None
```
Set display backlight

| item | description |
| --- | --- |
| **type** | func |
| **param** | **value**: backlight value, float type, range is [0, 100]<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_backlight(float value)
> ```
#### get\_backlight {#get\_backlight}

```python
def get_backlight(self) -> float
```
Get display backlight

| item | description |
| --- | --- |
| **type** | func |
| **return** | value backlight value, float type, range is [0, 100] |
| **static** | False |

> C++ defination code:
> ```cpp
> float get_backlight()
> ```
#### set\_backlight\_on {#set\_backlight\_on}

```python
def set_backlight_on(self, ms: int = 500, wait: bool = False) -> None
```
Trun on display backlight in milliseconds

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ms**: time in milliseconds to turn on backlight, default 500ms, 0 means immediate<br>**wait**: If true, will wait until the backlight is turned on before returning, or will turn on in background. Default is false.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_backlight_on(int ms = 500, bool wait = false)
> ```
#### set\_backlight\_off {#set\_backlight\_off}

```python
def set_backlight_off(self, ms: int = 500, wait: bool = False) -> None
```
Trun off display backlight in milliseconds

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ms**: time in milliseconds to turn off backlight, default 500ms, 0 means immediate<br>**wait**: If true, will wait until the backlight is turned off before returning, or will turn off in background. Default is false.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_backlight_off(int ms = 500, bool wait = false)
> ```
#### set\_backlight\_toggle {#set\_backlight\_toggle}

```python
def set_backlight_toggle(self, ms: int = 500, wait: bool = False) -> None
```
Toggle display backlight state in milliseconds

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ms**: time in milliseconds to toggle backlight, default 500ms, 0 means immediate<br>**wait**: If true, will wait until the backlight is turned off before returning, or will turn off in background. Default is false.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_backlight_toggle(int ms = 500, bool wait = false)
> ```
#### is\_setting\_backlight {#is\_setting\_backlight}

```python
def is_setting_backlight(self) -> bool
```
Check if backlight is in setting status

| item | description |
| --- | --- |
| **type** | func |
| **return** | true if backlight is in setting status, false if backlight is stable(on or off) |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_setting_backlight()
> ```
#### set\_hmirror {#set\_hmirror}

```python
def set_hmirror(self, en: bool) -> maix.err.Err
```
Set display mirror

| item | description |
| --- | --- |
| **type** | func |
| **param** | **en**: enable/disable mirror<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_hmirror(bool en)
> ```
#### set\_vflip {#set\_vflip}

```python
def set_vflip(self, en: bool) -> maix.err.Err
```
Set display flip

| item | description |
| --- | --- |
| **type** | func |
| **param** | **en**: enable/disable flip<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_vflip(bool en)
> ```
