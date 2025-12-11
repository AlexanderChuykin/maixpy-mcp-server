---
title: maix.camera
---

maix.camera module, access camera device and get image from it


> You can use `maix.camera` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### AeMode {#AeMode}

Auto exposure mode

| item | describe |
| --- | --- |
| **values** | **Invalid**: <br>**Auto**: <br>**Manual**: <br>
> C++ defination code:
> ```cpp
> enum class AeMode {
>         Invalid = -1,
>         Auto = 0,
>         Manual = 1
>     }
> ```
### AwbMode {#AwbMode}

Auto white balance mode

| item | describe |
| --- | --- |
| **values** | **Invalid**: <br>**Auto**: <br>**Manual**: <br>
> C++ defination code:
> ```cpp
> enum class AwbMode {
>         Invalid = -1,
>         Auto = 0,
>         Manual = 1
>     }
> ```


## Variable {#Variable}



## Function {#Function}

### list\_devices {#list\_devices}

```python
def list_devices() -> list[str]
```
List all supported camera devices.

| item | description |
| --- | --- |
| **return** | Returns the path to the camera device. |

> C++ defination code:
> ```cpp
> std::vector<std::string> list_devices()
> ```
### set\_regs\_enable {#set\_regs\_enable}

```python
def set_regs_enable(enable: bool = True) -> None
```
Enable set camera registers, default is false, if set to true, will not set camera registers, you can manually set registers by write_reg API.

| item | description |
| --- | --- |
| **param** | **enable**: enable/disable set camera registers<br>|

> C++ defination code:
> ```cpp
> void set_regs_enable(bool enable = true)
> ```
### get\_device\_name {#get\_device\_name}

```python
def get_device_name() -> str
```
Get device name. Most of the time, the returned name is the name of the sensor.


> C++ defination code:
> ```cpp
> std::string get_device_name()
> ```
### get\_sensor\_size {#get\_sensor\_size}

```python
def get_sensor_size() -> list[int]
```
Get sensor size

| item | description |
| --- | --- |
| **return** | Return a list of sensor sizes, the format is [w, h]. |

> C++ defination code:
> ```cpp
> std::vector<int> get_sensor_size()
> ```


## Class {#Class}

### Camera {#Camera}

Camera class


> C++ defination code:
> ```cpp
> class Camera
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, width: int = -1, height: int = -1, format: maix.image.Format = ..., device: str = None, fps: float = -1, buff_num: int = 3, open: bool = True, raw: bool = False) -> None
```
Construct a new Camera object.\nMaximum resolution support 2560x1440.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **width**: camera width, default is -1, means auto, mostly means max width of camera support<br>**height**: camera height, default is -1, means auto, mostly means max height of camera support<br>**format**: camera output format, default is image.Format.FMT_RGB888<br>**device**: camera device path, you can get devices by list_devices method, by default(value is NULL(None in MaixPy)) means the first device<br>**fps**: camera fps, default is -1, means auto, mostly means max fps of camera support<br>**buff_num**: camera buffer number, default is 3, means 3 buffer, one used by user, one used for cache the next frame,<br>more than one buffer will accelerate image read speed, but will cost more memory.<br>**open**: If true, camera will automatically call open() after creation. default is true.<br>**raw**: If true, you can use read_raw() to capture the raw image output from the sensor.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Camera(int width = -1, int height = -1, image::Format format = image::FMT_RGB888, const char *device = nullptr, double fps = -1, int buff_num = 3, bool open = true, bool raw = false)
> ```
#### get\_ch\_nums {#get\_ch\_nums}

```python
def get_ch_nums(self) -> int
```
Get the number of channels supported by the camera.

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the maximum number of channels. |
| **static** | False |

> C++ defination code:
> ```cpp
> int get_ch_nums()
> ```
#### open {#open}

```python
def open(self, width: int = -1, height: int = -1, format: maix.image.Format = ..., fps: float = -1, buff_num: int = -1) -> maix.err.Err
```
Open camera and run

| item | description |
| --- | --- |
| **type** | func |
| **param** | **width**: camera width, default is -1, means auto, mostly means max width of camera support<br>**height**: camera height, default is -1, means auto, mostly means max height of camera support<br>**format**: camera output format, default same as the constructor's format argument<br>**fps**: camera fps, default is -1, means auto, mostly means max fps of camera support<br>**buff_num**: camera buffer number, default is 3, means 3 buffer, one used by user, one used for cache the next frame,<br>more than one buffer will accelerate image read speed, but will cost more memory.<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err open(int width = -1, int height = -1, image::Format format = image::FMT_INVALID, double fps = -1, int buff_num = -1)
> ```
#### read {#read}

```python
def read(self, block: bool = True, block_ms: int = -1) -> maix.image.Image
```
Get one frame image from camera buffer, must call open method before read.\nIf open method not called, will call it automatically, if open failed, will throw exception!\nSo call open method before read is recommended.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **block**: block read, default is true, means block util read image successfully,<br>if set to false, will return nullptr if no image in buffer<br>**block_ms**: block read timeout<br>For the MaixCam, due to some issues with the platform’s interface, setting block_ms too low may result in duplicate frames being output.<br>|
| **return** | image::Image object, if failed, return nullptr, you should delete if manually in C++ |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *read(bool block = true, int block_ms = -1)
> ```
#### read\_raw {#read\_raw}

```python
def read_raw(self) -> maix.image.Image
```
Read the raw image and obtain the width, height, and format of the raw image through the returned Image object.

| item | description |
| --- | --- |
| **type** | func |
| **note** | The raw image is in a Bayer format, and its width and height are affected by the driver. Modifying the size and format is generally not allowed. |
| **return** | image::Image object, if failed, return nullptr, you should delete if manually in C++ |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *read_raw()
> ```
#### clear\_buff {#clear\_buff}

```python
def clear_buff(self) -> None
```
Clear buff to ensure the next read image is the latest image

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void clear_buff()
> ```
#### skip\_frames {#skip\_frames}

```python
def skip_frames(self, num: int) -> None
```
Read some frames and drop, this is usually used avoid read not stable image when camera just opened.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **num**: number of frames to read and drop<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void skip_frames(int num)
> ```
#### close {#close}

```python
def close(self) -> None
```
Close camera

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void close()
> ```
#### add\_channel {#add\_channel}

```python
def add_channel(self, width: int = -1, height: int = -1, format: maix.image.Format = ..., fps: float = -1, buff_num: int = 3, open: bool = True) -> Camera
```
Add a new channel and return a new Camera object, you can use close() to close this channel.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **width**: camera width, default is -1, means auto, mostly means max width of camera support<br>**height**: camera height, default is -1, means auto, mostly means max height of camera support<br>**format**: camera output format, default is RGB888<br>**fps**: camera fps, default is -1, means auto, mostly means max fps of camera support<br>**buff_num**: camera buffer number, default is 3, means 3 buffer, one used by user, one used for cache the next frame,<br>more than one buffer will accelerate image read speed, but will cost more memory.<br>**open**: If true, camera will automatically call open() after creation. default is true.<br>|
| **return** | new Camera object |
| **static** | False |

> C++ defination code:
> ```cpp
> camera::Camera *add_channel(int width = -1, int height = -1, image::Format format = image::FMT_RGB888, double fps = -1, int buff_num = 3, bool open = true)
> ```
#### is\_opened {#is\_opened}

```python
def is_opened(self) -> bool
```
Check if camera is opened

| item | description |
| --- | --- |
| **type** | func |
| **return** | true if camera is opened, false if not |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_opened()
> ```
#### is\_closed {#is\_closed}

```python
def is_closed(self) -> bool
```
check camera device is closed or not

| item | description |
| --- | --- |
| **type** | func |
| **return** | closed or not, bool type |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_closed()
> ```
#### width {#width}

```python
def width(self) -> int
```
Get camera width

| item | description |
| --- | --- |
| **type** | func |
| **return** | camera width |
| **static** | False |

> C++ defination code:
> ```cpp
> int width()
> ```
#### height {#height}

```python
def height(self) -> int
```
Get camera height

| item | description |
| --- | --- |
| **type** | func |
| **return** | camera height |
| **static** | False |

> C++ defination code:
> ```cpp
> int height()
> ```
#### fps {#fps}

```python
def fps(self) -> float
```
Get camera fps

| item | description |
| --- | --- |
| **type** | func |
| **return** | camera fps |
| **static** | False |

> C++ defination code:
> ```cpp
> double fps()
> ```
#### format {#format}

```python
def format(self) -> maix.image.Format
```
Get camera output format

| item | description |
| --- | --- |
| **type** | func |
| **return** | camera output format, image::Format object |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format format()
> ```
#### buff\_num {#buff\_num}

```python
def buff_num(self) -> int
```
Get camera buffer number

| item | description |
| --- | --- |
| **type** | func |
| **return** | camera buffer number |
| **static** | False |

> C++ defination code:
> ```cpp
> int buff_num()
> ```
#### hmirror {#hmirror}

```python
def hmirror(self, value: int = -1) -> int
```
Set/Get camera horizontal mirror

| item | description |
| --- | --- |
| **type** | func |
| **return** | camera horizontal mirror |
| **static** | False |

> C++ defination code:
> ```cpp
> int hmirror(int value = -1)
> ```
#### vflip {#vflip}

```python
def vflip(self, value: int = -1) -> int
```
Set/Get camera vertical flip

| item | description |
| --- | --- |
| **type** | func |
| **return** | camera vertical flip |
| **static** | False |

> C++ defination code:
> ```cpp
> int vflip(int value = -1)
> ```
#### device {#device}

```python
def device(self) -> str
```
Get camera device path

| item | description |
| --- | --- |
| **type** | func |
| **return** | camera device path |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string device()
> ```
#### write\_reg {#write\_reg}

```python
def write_reg(self, addr: int, data: int, bit_width: int = 8) -> maix.err.Err
```
Write camera register

| item | description |
| --- | --- |
| **type** | func |
| **param** | **addr**: register address<br>**data**: register data<br>**bit_width**: register data bit width, default is 8<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err write_reg(int addr, int data, int bit_width = 8)
> ```
#### read\_reg {#read\_reg}

```python
def read_reg(self, addr: int, bit_width: int = 8) -> int
```
Read camera register

| item | description |
| --- | --- |
| **type** | func |
| **param** | **addr**: register address<br>**bit_width**: register data bit width, default is 8<br>|
| **return** | register data, -1 means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> int read_reg(int addr, int bit_width = 8)
> ```
#### show\_colorbar {#show\_colorbar}

```python
def show_colorbar(self, enable: bool) -> maix.err.Err
```
Camera output color bar image for test

| item | description |
| --- | --- |
| **type** | func |
| **param** | **enable**: enable/disable color bar<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err show_colorbar(bool enable)
> ```
#### get\_channel {#get\_channel}

```python
def get_channel(self) -> int
```
Get channel of camera

| item | description |
| --- | --- |
| **type** | func |
| **return** | channel number |
| **static** | False |

> C++ defination code:
> ```cpp
> int get_channel()
> ```
#### set\_resolution {#set\_resolution}

```python
def set_resolution(self, width: int, height: int) -> maix.err.Err
```
Set camera resolution

| item | description |
| --- | --- |
| **type** | func |
| **param** | **width**: new width<br>**height**: new height<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_resolution(int width, int height)
> ```
#### set\_fps {#set\_fps}

```python
def set_fps(self, fps: float) -> maix.err.Err
```
Set camera fps

| item | description |
| --- | --- |
| **type** | func |
| **param** | **fps**: new fps<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_fps(double fps)
> ```
#### exposure {#exposure}

```python
def exposure(self, value: int = -1) -> int
```
Set/Get camera exposure

| item | description |
| --- | --- |
| **type** | func |
| **attention** | This method will affect the isp and thus the image, so please be careful with it. |
| **param** | **value**: exposure time. unit: us<br>If value == -1, return exposure time.<br>If value != 0, set and return exposure time.<br>|
| **return** | camera exposure time |
| **static** | False |

> C++ defination code:
> ```cpp
> int exposure(int value = -1)
> ```
#### gain {#gain}

```python
def gain(self, value: int = -1) -> int
```
Set/Get camera gain

| item | description |
| --- | --- |
| **type** | func |
| **attention** | This method will affect the isp and thus the image, so please be careful with it. |
| **param** | **value**: camera gain.<br>If value == -1, returns camera gain.<br>If value != 0, set and return camera gain.<br>|
| **return** | camera gain |
| **static** | False |

> C++ defination code:
> ```cpp
> int gain(int value = -1)
> ```
#### iso {#iso}

```python
def iso(self, value: int = -1) -> int
```
Set/Get camera iso

| item | description |
| --- | --- |
| **type** | func |
| **attention** | This method will affect the isp and thus the image, so please be careful with it. |
| **param** | **value**: camera iso.<br>If value == -1, returns camera iso.<br>If value != 0, set and return camera iso.<br>|
| **return** | camera iso |
| **static** | False |

> C++ defination code:
> ```cpp
> int iso(int value = -1)
> ```
#### luma {#luma}

```python
def luma(self, value: int = -1) -> int
```
Set/Get camera luma

| item | description |
| --- | --- |
| **type** | func |
| **attention** | This method will affect the isp and thus the image, so please be careful with it. |
| **param** | **value**: luma value, range is [0, 100]<br>If value == -1, returns luma value.<br>If value != 0, set and return luma value.<br>|
| **return** | returns luma value |
| **static** | False |

> C++ defination code:
> ```cpp
> int luma(int value = -1)
> ```
#### constrast {#constrast}

```python
def constrast(self, value: int = -1) -> int
```
Set/Get camera constrast

| item | description |
| --- | --- |
| **type** | func |
| **attention** | This method will affect the isp and thus the image, so please be careful with it. |
| **param** | **value**: constrast value, range is [0, 100]<br>If value == -1, returns constrast value.<br>If value != 0, set and return constrast value.<br>|
| **return** | returns constrast value |
| **static** | False |

> C++ defination code:
> ```cpp
> int constrast(int value = -1)
> ```
#### saturation {#saturation}

```python
def saturation(self, value: int = -1) -> int
```
Set/Get camera saturation

| item | description |
| --- | --- |
| **type** | func |
| **attention** | This method will affect the isp and thus the image, so please be careful with it. |
| **param** | **value**: saturation value, range is [0, 100]<br>If value == -1, returns saturation value.<br>If value != 0, set and return saturation value.<br>|
| **return** | returns saturation value |
| **static** | False |

> C++ defination code:
> ```cpp
> int saturation(int value = -1)
> ```
#### awb\_mode {#awb\_mode}

```python
def awb_mode(self, value: AwbMode = ...) -> AwbMode
```
Set/Get white balance mode (deprecated interface)

| item | description |
| --- | --- |
| **type** | func |
| **attention** | This method will affect the isp and thus the image, so please be careful with it.<br>This interface may be deprecated in the future, and there may be incompatibilities in the definition of the parameters of the new interface |
| **param** | **value**: value = 0, means set white balance to auto mode, value = 1, means set white balance to manual mode, default is auto mode.<br>|
| **return** | returns awb mode |
| **static** | False |

> C++ defination code:
> ```cpp
> camera::AwbMode awb_mode(camera::AwbMode value = camera::AwbMode::Invalid)
> ```
#### set\_awb {#set\_awb}

```python
def set_awb(self, mode: int = -1) -> int
```
Set/Get white balance mode (deprecated interface)

| item | description |
| --- | --- |
| **type** | func |
| **attention** | This method will affect the isp and thus the image, so please be careful with it. |
| **param** | **value**: value = 0, means set white balance to manual mode, value = 1, means set white balance to auto mode, default is auto mode.<br>|
| **return** | returns awb mode |
| **static** | False |

> C++ defination code:
> ```cpp
> int set_awb(int mode = -1)
> ```
#### set\_wb\_gain {#set\_wb\_gain}

```python
def set_wb_gain(self, gains: list[float] = []) -> list[float]
```
This interface is used to manually set the white balance gains and disable auto white balance, you can re-enable auto white balance using awb_mode().

| item | description |
| --- | --- |
| **type** | func |
| **note** | MaixCam can only manually set white balance by adjusting the gain. |
| **param** | **gains**: This is a float array representing the gains for r, gr, gb, and b respectively, with a value range of 0 to 1.0.<br>For MaixCam, the recommended initial values are [0.134, 0.0625, 0.0625, 0.1239]<br>For MaixCam2, the recommended initial values are[0.0682, 0, 0, 0.04897]<br>If no parameters are passed, the current gain values will be returned.<br>|
| **return** | Returns the current gain values. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<float> set_wb_gain(std::vector<float> gains = std::vector<float>())
> ```
#### exp\_mode {#exp\_mode}

```python
def exp_mode(self, value: AeMode = ...) -> AeMode
```
Set/Get exposure mode (deprecated interface)

| item | description |
| --- | --- |
| **type** | func |
| **attention** | This method will affect the isp and thus the image, so please be careful with it.<br>This interface may be deprecated in the future, and there may be incompatibilities in the definition of the parameters of the new interface |
| **param** | **value**: value = 0, means set exposure to auto mode, value = 1, means set exposure to manual mode, default is auto mode.<br>|
| **return** | returns exposure mode |
| **static** | False |

> C++ defination code:
> ```cpp
> camera::AeMode exp_mode(camera::AeMode value = camera::AeMode::Invalid)
> ```
#### set\_windowing {#set\_windowing}

```python
def set_windowing(self, roi: list[int]) -> maix.err.Err
```
Set window size of camera

| item | description |
| --- | --- |
| **type** | func |
| **param** | **roi**: Support two input formats, [x,y,w,h] set the coordinates and size of the window;<br>[w,h] set the size of the window, when the window is centred.<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_windowing(std::vector<int> roi)
> ```
#### get\_sensor\_size {#get\_sensor\_size-2}

```python
def get_sensor_size(self) -> list[int]
```
Get sensor size

| item | description |
| --- | --- |
| **type** | func |
| **return** | Return a list of sensor sizes, the format is [w, h]. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> get_sensor_size()
> ```
