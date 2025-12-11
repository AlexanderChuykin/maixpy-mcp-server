---
title: maix.rtsp
---

maix.rtsp module


> You can use `maix.rtsp` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### RtspStreamType {#RtspStreamType}

The stream type of rtsp

| item | describe |
| --- | --- |
| **values** | **RTSP_STREAM_NONE**: format invalid<br>**RTSP_STREAM_H264**: <br>**RTSP_STREAM_H265**: <br>
> C++ defination code:
> ```cpp
> enum RtspStreamType
>     {
>         RTSP_STREAM_NONE = 0,  // format invalid
>         RTSP_STREAM_H264,
>         RTSP_STREAM_H265,
>     }
> ```


## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### Region {#Region}

Region class


> C++ defination code:
> ```cpp
> class Region
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, x: int, y: int, width: int, height: int, format: maix.image.Format, camera: maix.camera.Camera) -> None
```
Construct a new Region object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: region coordinate x<br>**y**: region coordinate y<br>**width**: region width<br>**height**: region height<br>**format**: region format<br>**camera**: bind region to camera<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Region(int x, int y, int width, int height, image::Format format, camera::Camera *camera)
> ```
#### get\_canvas {#get\_canvas}

```python
def get_canvas(self) -> maix.image.Image
```
Return an image object from region

| item | description |
| --- | --- |
| **type** | func |
| **return** | image object |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *get_canvas()
> ```
#### update\_canvas {#update\_canvas}

```python
def update_canvas(self) -> maix.err.Err
```
Update canvas

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err update_canvas()
> ```
### Rtsp {#Rtsp}

Rtsp class


> C++ defination code:
> ```cpp
> class Rtsp
> ```

#### \_\_init\_\_ {#\_\_init\_\_-2}

```python
def __init__(self, ip: str = '', port: int = 8554, fps: int = 30, stream_type: RtspStreamType = ..., bitrate: int = 3000000) -> None
```
Construct a new Video object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **ip**: rtsp ip<br>**port**: rtsp port<br>**fps**: rtsp fps<br>**stream_type**: rtsp stream type<br>**bitrate**: rtsp bitrate<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Rtsp(std::string ip = std::string(), int port = 8554, int fps = 30, rtsp::RtspStreamType stream_type = rtsp::RtspStreamType::RTSP_STREAM_H264, int bitrate = 3000 * 1000)
> ```
#### start {#start}

```python
def start(self) -> maix.err.Err
```
start rtsp

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err start()
> ```
#### stop {#stop}

```python
def stop(self) -> maix.err.Err
```
stop rtsp

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err stop()
> ```
#### bind\_camera {#bind\_camera}

```python
def bind_camera(self, camera: maix.camera.Camera) -> maix.err.Err
```
Bind camera

| item | description |
| --- | --- |
| **type** | func |
| **param** | **camera**: camera object<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err bind_camera(camera::Camera *camera)
> ```
#### bind\_audio\_recorder {#bind\_audio\_recorder}

```python
def bind_audio_recorder(self, recorder: maix.audio.Recorder) -> maix.err.Err
```
Bind audio recorder

| item | description |
| --- | --- |
| **type** | func |
| **note** | If the audio_recorder object is bound, the audio_recorder object cannot be used elsewhere. |
| **param** | **recorder**: audio_recorder object<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err bind_audio_recorder(audio::Recorder *recorder)
> ```
#### write {#write}

```python
def write(self, frame: maix.video.Frame) -> maix.err.Err
```
Write data to rtsp(This function will be removed in the future)

| item | description |
| --- | --- |
| **type** | func |
| **param** | **frame**: video frame data<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err write(video::Frame &frame)
> ```
#### get\_url {#get\_url}

```python
def get_url(self) -> str
```
Get url of rtsp

| item | description |
| --- | --- |
| **type** | func |
| **return** | url of rtsp |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string get_url()
> ```
#### get\_urls {#get\_urls}

```python
def get_urls(self) -> list[str]
```
Get url list of rtsp

| item | description |
| --- | --- |
| **type** | func |
| **return** | url list of rtsp |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::string> get_urls()
> ```
#### to\_camera {#to\_camera}

```python
def to_camera(self) -> maix.camera.Camera
```
Get camera object from rtsp

| item | description |
| --- | --- |
| **type** | func |
| **return** | camera object |
| **static** | False |

> C++ defination code:
> ```cpp
> camera::Camera *to_camera()
> ```
#### add\_region {#add\_region}

```python
def add_region(self, x: int, y: int, width: int, height: int, format: maix.image.Format = ...) -> Region
```
return a region object, you can draw image on the region.(This function will be removed in the future)

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: region coordinate x<br>**y**: region coordinate y<br>**width**: region width<br>**height**: region height<br>**format**: region format, support Format::FMT_BGRA8888 only<br>|
| **return** | the reigon object |
| **static** | False |

> C++ defination code:
> ```cpp
> rtsp::Region *add_region(int x, int y, int width, int height, image::Format format = image::Format::FMT_BGRA8888)
> ```
#### update\_region {#update\_region}

```python
def update_region(self, region: Region) -> maix.err.Err
```
update and show region(This function will be removed in the future)

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err update_region(rtsp::Region &region)
> ```
#### del\_region {#del\_region}

```python
def del_region(self, region: Region) -> maix.err.Err
```
del region(This function will be removed in the future)

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err del_region(rtsp::Region *region)
> ```
#### draw\_rect {#draw\_rect}

```python
def draw_rect(self, id: int, x: int, y: int, width: int, height: int, color: maix.image.Color, thickness: int = 1) -> maix.err.Err
```
Draw a rectangle on the canvas(This function will be removed in the future)

| item | description |
| --- | --- |
| **type** | func |
| **param** | **id**: region id<br>**x**: rectangle coordinate x<br>**y**: rectangle coordinate y<br>**width**: rectangle width<br>**height**: rectangle height<br>**color**: rectangle color<br>**thickness**: rectangle thickness. If you set it to -1, the rectangle will be filled.<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err draw_rect(int id, int x, int y, int width, int height, image::Color color, int thickness = 1)
> ```
#### draw\_string {#draw\_string}

```python
def draw_string(self, id: int, x: int, y: int, str: str, color: maix.image.Color, size: int = 16, thickness: int = 1) -> maix.err.Err
```
Draw a string on the canvas(This function will be removed in the future)

| item | description |
| --- | --- |
| **type** | func |
| **param** | **id**: region id<br>**x**: string coordinate x<br>**y**: string coordinate y<br>**str**: string<br>**color**: string color<br>**size**: string size<br>**thickness**: string thickness<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err draw_string(int id, int x, int y, const char *str, image::Color color, int size = 16, int thickness = 1)
> ```
