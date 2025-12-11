---
title: maix.rtmp
---

maix.rtmp module


> You can use `maix.rtmp` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### TagType {#TagType}

Video type

| item | describe |
| --- | --- |
| **values** | **TAG_NONE**: <br>**TAG_VIDEO**: <br>**TAG_AUDIO**: <br>**TAG_SCRIPT**: <br>
> C++ defination code:
> ```cpp
> enum TagType
>     {
>         TAG_NONE,
>         TAG_VIDEO,
>         TAG_AUDIO,
>         TAG_SCRIPT,
>     }
> ```


## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### Rtmp {#Rtmp}

Rtmp class


> C++ defination code:
> ```cpp
> class Rtmp
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, host: str = 'localhost', port: int = 1935, app: str = '', stream: str = '', bitrate: int = 1000000) -> None
```
Construct a new Video object

| item | description |
| --- | --- |
| **type** | func |
| **note** | Rtmp url : rtmp://host:prot/app/stream<br>example:<br>r = Rtmp("localhost", 1935, "live", "stream")<br>means rtmp url is rtmp://localhost:1935/live/stream |
| **param** | **host**: rtmp ip<br>**port**: rtmp port, default is 1935.<br>**app**: rtmp app name<br>**stream**: rtmp stream name<br>**bitrate**: rtmp bitrate, default is 1000 * 1000<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Rtmp(std::string host = "localhost", int port = 1935, std::string app = std::string(), std::string stream = std::string(), int bitrate = 1000 * 1000)
> ```
#### bitrate {#bitrate}

```python
def bitrate(self) -> int
```
Get bitrate

| item | description |
| --- | --- |
| **type** | func |
| **return** | bitrate |
| **static** | False |

> C++ defination code:
> ```cpp
> int bitrate()
> ```
#### bind\_camera {#bind\_camera}

```python
def bind_camera(self, cam: maix.camera.Camera) -> maix.err.Err
```
Bind camera

| item | description |
| --- | --- |
| **type** | func |
| **note** | If the cam object is bound, the cam object cannot be used elsewhere. |
| **param** | **cam**: camera object<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err bind_camera(camera::Camera *cam)
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
#### bind\_display {#bind\_display}

```python
def bind_display(self, display: maix.display.Display) -> maix.err.Err
```
Bind display

| item | description |
| --- | --- |
| **type** | func |
| **note** | If the display object is bound, the display object cannot be used elsewhere. |
| **param** | **disaply**: display object<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err bind_display(display::Display *display)
> ```
#### get\_camera {#get\_camera}

```python
def get_camera(self) -> maix.camera.Camera
```
If you bind a camera, return the camera object.

| item | description |
| --- | --- |
| **type** | func |
| **return** | Camera object |
| **static** | False |

> C++ defination code:
> ```cpp
> camera::Camera *get_camera()
> ```
#### start {#start}

```python
def start(self, path: str = '') -> maix.err.Err
```
Start push stream

| item | description |
| --- | --- |
| **type** | func |
| **note** | only support flv file now |
| **param** | **path**: File path, if you passed file path, cyclic push the file, else if you bound camera, push the camera image.(This parameter has been deprecated)<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err start(std::string path = std::string())
> ```
#### stop {#stop}

```python
def stop(self) -> maix.err.Err
```
Stop push stream

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err stop()
> ```
#### get\_path {#get\_path}

```python
def get_path(self) -> str
```
Get the file path of the push stream

| item | description |
| --- | --- |
| **type** | func |
| **return** | file path |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string get_path()
> ```
#### is\_started {#is\_started}

```python
def is_started(self) -> bool
```
Check whether push streaming has started

| item | description |
| --- | --- |
| **type** | func |
| **return** | If rtmp thread is running, returns true |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_started()
> ```
