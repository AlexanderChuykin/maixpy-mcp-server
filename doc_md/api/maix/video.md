---
title: maix.video
---

maix.video module


> You can use `maix.video` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### VideoType {#VideoType}

Video type

| item | describe |
| --- | --- |
| **values** | **VIDEO_NONE**: format invalid<br>**VIDEO_ENC_H265_CBR**: Deprecated<br>**VIDEO_ENC_MP4_CBR**: Deprecated<br>**VIDEO_DEC_H265_CBR**: Deprecated<br>**VIDEO_DEC_MP4_CBR**: Deprecated<br>**VIDEO_H264_CBR**: Deprecated<br>**VIDEO_H265_CBR**: Deprecated<br>**VIDEO_H264_CBR_MP4**: Deprecated<br>**VIDEO_H265_CBR_MP4**: Deprecated<br>**VIDEO_H264**: <br>**VIDEO_H264_MP4**: <br>**VIDEO_H264_FLV**: <br>**VIDEO_H265**: <br>**VIDEO_H265_MP4**: <br>
> C++ defination code:
> ```cpp
> enum VideoType
>     {
>         VIDEO_NONE = 0,  // format invalid
>         VIDEO_ENC_H265_CBR,     // Deprecated
>         VIDEO_ENC_MP4_CBR,      // Deprecated
>         VIDEO_DEC_H265_CBR,     // Deprecated
>         VIDEO_DEC_MP4_CBR,      // Deprecated
>         VIDEO_H264_CBR,         // Deprecated
>         VIDEO_H265_CBR,         // Deprecated
>         VIDEO_H264_CBR_MP4,     // Deprecated
>         VIDEO_H265_CBR_MP4,     // Deprecated
> 
>         VIDEO_H264,
>         VIDEO_H264_MP4,
>         VIDEO_H264_FLV,
>         VIDEO_H265,
>         VIDEO_H265_MP4,
>     }
> ```
### MediaType {#MediaType}

Video type

| item | describe |
| --- | --- |
| **values** | **MEDIA_TYPE_UNKNOWN**: Represents an unknown media type, which is usually treated as AVMEDIA_TYPE_DATA.<br>**MEDIA_TYPE_VIDEO**: Represents a video stream, such as video content encoded in H.264, MPEG-4, etc.<br>**MEDIA_TYPE_AUDIO**: Represents an audio stream, such as audio content encoded in AAC, MP3, etc.<br>**MEDIA_TYPE_DATA**: Represents opaque data streams that are usually continuous. This type of stream is not necessarily audio or video and may be used for other data purposes.<br>**MEDIA_TYPE_SUBTITLE**: Represents a subtitle stream used for displaying text or subtitle information, such as SRT, ASS, etc.<br>**MEDIA_TYPE_ATTACHMENT**: Represents attachment streams that are usually sparse. Attachment streams can include images, fonts, or other files that need to be bundled with the media.<br>**MEDIA_TYPE_NB**: Represents the number of media types (count) and indicates the total number of media types defined in this enumeration. It is not a media type itself but is used for counting enumeration items.<br>
> C++ defination code:
> ```cpp
> enum MediaType
>     {
>         MEDIA_TYPE_UNKNOWN = -1,    // Represents an unknown media type, which is usually treated as AVMEDIA_TYPE_DATA.
>         MEDIA_TYPE_VIDEO,           // Represents a video stream, such as video content encoded in H.264, MPEG-4, etc.
>         MEDIA_TYPE_AUDIO,           // Represents an audio stream, such as audio content encoded in AAC, MP3, etc.
>         MEDIA_TYPE_DATA,            // Represents opaque data streams that are usually continuous. This type of stream is not necessarily audio or video and may be used for other data purposes.
>         MEDIA_TYPE_SUBTITLE,        // Represents a subtitle stream used for displaying text or subtitle information, such as SRT, ASS, etc.
>         MEDIA_TYPE_ATTACHMENT,      // Represents attachment streams that are usually sparse. Attachment streams can include images, fonts, or other files that need to be bundled with the media.
>         MEDIA_TYPE_NB               // Represents the number of media types (count) and indicates the total number of media types defined in this enumeration. It is not a media type itself but is used for counting enumeration items.
>     }
> ```


## Variable {#Variable}



## Function {#Function}

### timebase\_to\_us {#timebase\_to\_us}

```python
def timebase_to_us(timebase: list[int], value: int) -> float
```
Convert a value in timebase units to microseconds. value * 1000000 / (timebase[1] / timebase[0])

| item | description |
| --- | --- |
| **param** | **timebse**: Time base, used as the unit for calculating playback time. It must be an array containing two parameters,<br>in the format [num, den], where the first parameter is the numerator of the time base, and the second parameter is the denominator of the time base.<br>**value**: Input value<br>|
| **return** | Return the result in microseconds. |

> C++ defination code:
> ```cpp
> double timebase_to_us(std::vector<int> timebase, uint64_t value)
> ```
### timebase\_to\_ms {#timebase\_to\_ms}

```python
def timebase_to_ms(timebase: list[int], value: int) -> float
```
Convert a value in timebase units to milliseconds.

| item | description |
| --- | --- |
| **param** | **timebse**: Time base, used as the unit for calculating playback time. It must be an array containing two parameters,<br>in the format [num, den], where the first parameter is the numerator of the time base, and the second parameter is the denominator of the time base.<br>**value**: Input value<br>|
| **return** | Return the result in milliseconds. |

> C++ defination code:
> ```cpp
> double timebase_to_ms(std::vector<int> timebase, uint64_t value)
> ```


## Class {#Class}

### Context {#Context}

Context class


> C++ defination code:
> ```cpp
> class Context
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, media_type: MediaType, timebase: list[int]) -> None
```
Construct a new Context object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **media_type**: enable capture, if true, you can use capture() function to get an image object<br>**timebase**: Time base, used as the unit for calculating playback time. It must be an array containing two parameters,<br>in the format [num, den], where the first parameter is the numerator of the time base, and the second parameter is the denominator of the time base.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Context(video::MediaType media_type, std::vector<int> timebase)
> ```
#### audio\_sample\_rate {#audio\_sample\_rate}

```python
def audio_sample_rate(self) -> int
```
Get sample rate of audio (only valid in the context of audio)

| item | description |
| --- | --- |
| **type** | func |
| **return** | sample rate |
| **static** | False |

> C++ defination code:
> ```cpp
> int audio_sample_rate()
> ```
#### audio\_channels {#audio\_channels}

```python
def audio_channels(self) -> int
```
Get channels of audio (only valid in the context of audio)

| item | description |
| --- | --- |
| **type** | func |
| **return** | channels |
| **static** | False |

> C++ defination code:
> ```cpp
> int audio_channels()
> ```
#### audio\_format {#audio\_format}

```python
def audio_format(self) -> maix.audio.Format
```
Get format of audio (only valid in the context of audio)

| item | description |
| --- | --- |
| **type** | func |
| **return** | audio format. @see audio::Format |
| **static** | False |

> C++ defination code:
> ```cpp
> audio::Format audio_format()
> ```
#### set\_pcm {#set\_pcm}

```python
def set_pcm(self, data: maix.Bytes(bytes), duration: int = 0, pts: int = 0, copy: bool = True) -> maix.err.Err
```
Set pcm data (only valid in the context of audio)

| item | description |
| --- | --- |
| **type** | func |
| **param** | **duration**: Duration of the current pcm. unit: timebase<br>**pts**: The start time of this pcm playback. If it is 0, it means this parameter is not supported. unit: timebase<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_pcm(maix::Bytes *data, int duration = 0, uint64_t pts = 0, bool copy = true)
> ```
#### get\_pcm {#get\_pcm}

```python
def get_pcm(*args, **kwargs)
```
Get pcm data (only valid in the context of audio)

| item | description |
| --- | --- |
| **type** | func |
| **attention** | Note that if you call this interface, you are responsible for releasing the memory of the data, and this interface cannot be called again. |
| **return** | Bytes |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *get_pcm()
> ```
#### image {#image}

```python
def image(self) -> maix.image.Image
```
Retrieve the image data to be played.

| item | description |
| --- | --- |
| **type** | func |
| **attention** | Note that if you call this interface, you are responsible for releasing the memory of the image, and this interface cannot be called again. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *image()
> ```
#### media\_type {#media\_type}

```python
def media_type(self) -> MediaType
```
Get the media type to determine whether it is video, audio, or another media type.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> video::MediaType media_type()
> ```
#### pts {#pts}

```python
def pts(self) -> int
```
Get the start time of the current playback., in units of time base.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> uint64_t pts()
> ```
#### last\_pts {#last\_pts}

```python
def last_pts(self) -> int
```
Get the start time of the previous playback, in units of time base.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> uint64_t last_pts()
> ```
#### timebase {#timebase}

```python
def timebase(self) -> list[int]
```
Get the time base.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> timebase()
> ```
#### duration {#duration}

```python
def duration(self) -> int
```
Duration of the current frame. unit: timebase

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int duration()
> ```
#### duration\_us {#duration\_us}

```python
def duration_us(self) -> int
```
Duration of the current frame. unit: us

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> uint64_t duration_us()
> ```
### Frame {#Frame}

Frame class


> C++ defination code:
> ```cpp
> class Frame
> ```

#### to\_bytes {#to\_bytes}

```python
def to_bytes(*args, **kwargs)
```
Get raw data of packet

| item | description |
| --- | --- |
| **type** | func |
| **param** | **copy**: if true, will alloc memory and copy data to new buffer<br>|
| **return** | raw data |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *to_bytes(bool copy = false)
> ```
#### size {#size}

```python
def size(self) -> int
```
Get raw data size of packet

| item | description |
| --- | --- |
| **type** | func |
| **return** | size of raw data |
| **static** | False |

> C++ defination code:
> ```cpp
> size_t size()
> ```
#### is\_valid {#is\_valid}

```python
def is_valid(self) -> bool
```
Check packet is valid

| item | description |
| --- | --- |
| **type** | func |
| **return** | true, packet is valid; false, packet is invalid |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_valid()
> ```
#### set\_pts {#set\_pts}

```python
def set_pts(self, pts: int) -> None
```
Set pts

| item | description |
| --- | --- |
| **type** | func |
| **param** | **pts**: presentation time stamp. unit: time_base<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_pts(uint64_t pts)
> ```
#### set\_dts {#set\_dts}

```python
def set_dts(self, dts: int) -> None
```
Set dts

| item | description |
| --- | --- |
| **type** | func |
| **param** | **dts**: decoding time stamp.  unit: time_base<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_dts(uint64_t dts)
> ```
#### set\_duration {#set\_duration}

```python
def set_duration(self, duration: int) -> None
```
Set duration

| item | description |
| --- | --- |
| **type** | func |
| **param** | **duration**: packet display time. unit: time_base<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_duration(uint64_t duration)
> ```
#### get\_pts {#get\_pts}

```python
def get_pts(self) -> int
```
Set pts

| item | description |
| --- | --- |
| **type** | func |
| **param** | **pts**: presentation time stamp. unit: time_base<br>|
| **return** | pts value |
| **static** | False |

> C++ defination code:
> ```cpp
> uint64_t get_pts()
> ```
#### get\_dts {#get\_dts}

```python
def get_dts(self) -> int
```
Set dts

| item | description |
| --- | --- |
| **type** | func |
| **param** | **dts**: decoding time stamp.  unit: time_base<br>|
| **return** | dts value |
| **static** | False |

> C++ defination code:
> ```cpp
> uint64_t get_dts()
> ```
#### get\_duration {#get\_duration}

```python
def get_duration(self) -> int
```
Get duration

| item | description |
| --- | --- |
| **type** | func |
| **return** | duration value |
| **static** | False |

> C++ defination code:
> ```cpp
> uint64_t get_duration()
> ```
#### type {#type}

```python
def type(self) -> VideoType
```
Get frame type

| item | description |
| --- | --- |
| **type** | func |
| **return** | video type. @see video::VideoType |
| **static** | False |

> C++ defination code:
> ```cpp
> video::VideoType type()
> ```
### Packet {#Packet}

Packet class


> C++ defination code:
> ```cpp
> class Packet
> ```

#### \_\_init\_\_ {#\_\_init\_\_-2}

```python
def __init__(self, data: int, len: int, pts: int = -1, dts: int = -1, duration: int = 0) -> None
```
Packet number (pair of numerator and denominator).

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: src data pointer, use pointers directly without copying.<br>Note: this object will try to free this memory<br>**len**: data len<br>**pts**: presentation time stamp. unit: time_base<br>**dts**: decoding time stamp. unit: time_base<br>**duration**: packet display time. unit: time_base<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Packet(uint8_t *data, int len, uint64_t pts = -1, uint64_t dts = -1, int64_t duration = 0)
> ```
#### get {#get}

```python
def get(self) -> list[int]
```
Get raw data of packet

| item | description |
| --- | --- |
| **type** | func |
| **return** | raw data |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint8_t> get()
> ```
#### data {#data}

```python
def data(self) -> int
```
Get raw data of packet

| item | description |
| --- | --- |
| **type** | func |
| **return** | raw data |
| **static** | False |

> C++ defination code:
> ```cpp
> uint8_t *data()
> ```
#### data\_size {#data\_size}

```python
def data_size(self) -> int
```
Get raw data size of packet

| item | description |
| --- | --- |
| **type** | func |
| **return** | size of raw data |
| **static** | False |

> C++ defination code:
> ```cpp
> size_t data_size()
> ```
#### is\_valid {#is\_valid-2}

```python
def is_valid(self) -> bool
```
Check packet is valid

| item | description |
| --- | --- |
| **type** | func |
| **return** | true, packet is valid; false, packet is invalid |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_valid()
> ```
#### set\_pts {#set\_pts-2}

```python
def set_pts(self, pts: int) -> None
```
Set pts

| item | description |
| --- | --- |
| **type** | func |
| **param** | **pts**: presentation time stamp. unit: time_base<br>|
| **return** | true, packet is valid; false, packet is invalid |
| **static** | False |

> C++ defination code:
> ```cpp
> void set_pts(uint64_t pts)
> ```
#### set\_dts {#set\_dts-2}

```python
def set_dts(self, dts: int) -> None
```
Set dts

| item | description |
| --- | --- |
| **type** | func |
| **param** | **dts**: decoding time stamp.  unit: time_base<br>|
| **return** | true, packet is valid; false, packet is invalid |
| **static** | False |

> C++ defination code:
> ```cpp
> void set_dts(uint64_t dts)
> ```
#### set\_duration {#set\_duration-2}

```python
def set_duration(self, duration: int) -> None
```
Set duration

| item | description |
| --- | --- |
| **type** | func |
| **param** | **duration**: packet display time. unit: time_base<br>|
| **return** | true, packet is valid; false, packet is invalid |
| **static** | False |

> C++ defination code:
> ```cpp
> void set_duration(uint64_t duration)
> ```
### Encoder {#Encoder}

Encode class


> C++ defination code:
> ```cpp
> class Encoder
> ```

#### \_\_init\_\_ {#\_\_init\_\_-3}

```python
def __init__(self, path: str = '', width: int = 2560, height: int = 1440, format: maix.image.Format = ..., type: VideoType = ..., framerate: int = 30, gop: int = 50, bitrate: int = 3000000, time_base: int = 1000, capture: bool = False, block: bool = True) -> None
```
Construct a new Video object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **width**: picture width. this value may be set automatically. default is 2560.<br>**height**: picture height. this value may be set automatically. default is 1440.<br>**format**: picture format. default is image::Format::FMT_YVU420SP. @see image::Format<br>**type**: video encode/decode type. default is ENC_H265_CBR. @see EncodeType<br>**framerate**: frame rate. framerate default is 30, means 30 frames per second<br>for video. 1/time_base is not the average frame rate if the frame rate is not constant.<br>**gop**: for h264/h265 encoding, the interval between two I-frames, default is 50.<br>**bitrate**: for h264/h265 encoding, used to limit the bandwidth used by compressed data, default is 3000kbps<br>**time_base**: frame time base. time_base default is 1000, means 1/1000 ms (not used)<br>**capture**: enable capture, if true, you can use capture() function to get an image object<br>**block**: This parameter determines whether encoding should block until it is complete.<br>If set to true, it will wait until encoding is finished before returning.<br>If set to false, it will return the current encoding result on the next call.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Encoder(std::string path = "", int width = 2560, int height = 1440, image::Format format = image::Format::FMT_YVU420SP, video::VideoType type = video::VideoType::VIDEO_H264, int framerate = 30, int gop = 50, int bitrate = 3000 * 1000, int time_base = 1000, bool capture = false, bool block = true)
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
#### encode {#encode}

```python
def encode(self, img: maix.image.Image = ..., pcm: maix.Bytes(bytes) = b'') -> Frame
```
Encode image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: the image will be encode.<br>if the img is NULL, this function will try to get image from camera, you must use bind_camera() function to bind the camera.<br>**pcm**: the pcm data will be encode.<br>|
| **return** | encode result |
| **static** | False |

> C++ defination code:
> ```cpp
> video::Frame *encode(image::Image *img = maix::video::Encoder::NoneImage, Bytes *pcm = maix::video::Encoder::NoneBytes)
> ```
#### push {#push}

```python
def push(self, frame: ...) -> maix.err.Err
```
Push a pipeline frame to encoder.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **frame**: the frame will be push.<br>|
| **return** | push result |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err push(pipeline::Frame *frame)
> ```
#### pop {#pop}

```python
def pop(self, block_ms: int = 1000) -> ...
```
Pop a frame from encoder.

| item | description |
| --- | --- |
| **type** | func |
| **note** | If encoder buffer is empty, it will return null. |
| **param** | **block_ms**: block read, if block_ms = -1, block indefinitely until an image is read; if block_ms = 0, do not block and return immediately<br>|
| **return** | pop result. @see pipeline::Stream |
| **static** | False |

> C++ defination code:
> ```cpp
> pipeline::Stream *pop(int block_ms = 1000)
> ```
#### capture {#capture}

```python
def capture(self) -> maix.image.Image
```
Capture image

| item | description |
| --- | --- |
| **type** | func |
| **attention** | Each time encode is called, the last captured image will be released. |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *capture()
> ```
#### width {#width}

```python
def width(self) -> int
```
Get video width

| item | description |
| --- | --- |
| **type** | func |
| **return** | video width |
| **static** | False |

> C++ defination code:
> ```cpp
> int width()
> ```
#### height {#height}

```python
def height(self) -> int
```
Get video height

| item | description |
| --- | --- |
| **type** | func |
| **return** | video height |
| **static** | False |

> C++ defination code:
> ```cpp
> int height()
> ```
#### format {#format}

```python
def format(self) -> maix.image.Format
```
Get video format

| item | description |
| --- | --- |
| **type** | func |
| **return** | video format |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format format()
> ```
#### type {#type-2}

```python
def type(self) -> VideoType
```
Get video encode type

| item | description |
| --- | --- |
| **type** | func |
| **return** | VideoType |
| **static** | False |

> C++ defination code:
> ```cpp
> video::VideoType type()
> ```
#### framerate {#framerate}

```python
def framerate(self) -> int
```
Get video encode framerate

| item | description |
| --- | --- |
| **type** | func |
| **return** | frame rate |
| **static** | False |

> C++ defination code:
> ```cpp
> int framerate()
> ```
#### gop {#gop}

```python
def gop(self) -> int
```
Get video encode gop

| item | description |
| --- | --- |
| **type** | func |
| **return** | gop value |
| **static** | False |

> C++ defination code:
> ```cpp
> int gop()
> ```
#### bitrate {#bitrate}

```python
def bitrate(self) -> int
```
Get video encode bitrate

| item | description |
| --- | --- |
| **type** | func |
| **return** | bitrate value |
| **static** | False |

> C++ defination code:
> ```cpp
> int bitrate()
> ```
#### time\_base {#time\_base}

```python
def time_base(self) -> int
```
Get video encode time base

| item | description |
| --- | --- |
| **type** | func |
| **return** | time base value |
| **static** | False |

> C++ defination code:
> ```cpp
> int time_base()
> ```
### Decoder {#Decoder}

Decoder class


> C++ defination code:
> ```cpp
> class Decoder
> ```

#### \_\_init\_\_ {#\_\_init\_\_-4}

```python
def __init__(self, path: str, format: maix.image.Format = ...) -> None
```
Construct a new decoder object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **path**: Path to the file to be decoded. Supports files with .264 and .mp4 extensions. Note that only mp4 files containing h.264 streams are supported.<br>**format**: Decoded output format, currently only support GRAYSCALE and YUV420SP<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Decoder(std::string path, image::Format format = image::Format::FMT_YVU420SP)
> ```
#### decode\_video {#decode\_video}

```python
def decode_video(self, block: bool = True) -> Context
```
Decode the video stream, returning the image of the next frame each time.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **block**: Whether it blocks or not. If true, it will wait for the decoding to complete and return the current frame.<br>If false, it will return the result of the previous frame's decoding. If the previous frame's decoding result is empty,<br>it will return an unknown Context, and you can use the media_type method of the Context to determine if a valid result exists.<br>default is true.<br>|
| **return** | Decoded context information. |
| **static** | False |

> C++ defination code:
> ```cpp
> video::Context * decode_video(bool block = true)
> ```
#### decode\_audio {#decode\_audio}

```python
def decode_audio(self) -> Context
```
Decode the video stream, returning the image of the next frame each time.

| item | description |
| --- | --- |
| **type** | func |
| **return** | Decoded context information. |
| **static** | False |

> C++ defination code:
> ```cpp
> video::Context * decode_audio()
> ```
#### decode {#decode}

```python
def decode(self, block: bool = True) -> Context
```
Decode the video and audio stream

| item | description |
| --- | --- |
| **type** | func |
| **param** | **block**: Whether it blocks or not. If true, it will wait for the decoding to complete and return the current frame.<br>If false, it will return the result of the previous frame's decoding. If the previous frame's decoding result is empty,<br>it will return an unknown Context, and you can use the media_type method of the Context to determine if a valid result exists.<br>default is true.<br>|
| **return** | Decoded context information. |
| **static** | False |

> C++ defination code:
> ```cpp
> video::Context * decode(bool block = true)
> ```
#### push {#push-2}

```python
def push(self, stream: ...) -> maix.err.Err
```
Push a pipeline frame to encoder.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **stream**: the frame will be push.<br>|
| **return** | push result |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err push(pipeline::Stream *stream)
> ```
#### pop {#pop-2}

```python
def pop(self, block_ms: int = 1000) -> ...
```
Pop a frame from encoder.

| item | description |
| --- | --- |
| **type** | func |
| **note** | If encoder buffer is empty, it will return null. |
| **param** | **block_ms**: block read, if block_ms = -1, block indefinitely until an image is read; if block_ms = 0, do not block and return immediately<br>|
| **return** | pop result. @see pipeline::Frame |
| **static** | False |

> C++ defination code:
> ```cpp
> pipeline::Frame *pop(int block_ms = 1000)
> ```
#### audio\_sample\_rate {#audio\_sample\_rate-2}

```python
def audio_sample_rate(self) -> int
```
Get sample rate of audio (only valid in the context of audio)

| item | description |
| --- | --- |
| **type** | func |
| **return** | sample rate |
| **static** | False |

> C++ defination code:
> ```cpp
> int audio_sample_rate()
> ```
#### audio\_channels {#audio\_channels-2}

```python
def audio_channels(self) -> int
```
Get channels of audio (only valid in the context of audio)

| item | description |
| --- | --- |
| **type** | func |
| **return** | channels |
| **static** | False |

> C++ defination code:
> ```cpp
> int audio_channels()
> ```
#### audio\_format {#audio\_format-2}

```python
def audio_format(self) -> maix.audio.Format
```
Get format of audio (only valid in the context of audio)

| item | description |
| --- | --- |
| **type** | func |
| **return** | audio format. @see audio::Format |
| **static** | False |

> C++ defination code:
> ```cpp
> audio::Format audio_format()
> ```
#### width {#width-2}

```python
def width(self) -> int
```
Get the video width

| item | description |
| --- | --- |
| **type** | func |
| **return** | video width |
| **static** | False |

> C++ defination code:
> ```cpp
> int width()
> ```
#### height {#height-2}

```python
def height(self) -> int
```
Get the video height

| item | description |
| --- | --- |
| **type** | func |
| **return** | video height |
| **static** | False |

> C++ defination code:
> ```cpp
> int height()
> ```
#### bitrate {#bitrate-2}

```python
def bitrate(self) -> int
```
Get the video bitrate

| item | description |
| --- | --- |
| **type** | func |
| **return** | bitrate value |
| **static** | False |

> C++ defination code:
> ```cpp
> int bitrate()
> ```
#### fps {#fps}

```python
def fps(self) -> int
```
Get the video fps

| item | description |
| --- | --- |
| **type** | func |
| **return** | fps value |
| **static** | False |

> C++ defination code:
> ```cpp
> int fps()
> ```
#### seek {#seek}

```python
def seek(self, time: float = -1) -> float
```
Seek to the required playback position

| item | description |
| --- | --- |
| **type** | func |
| **param** | **time**: timestamp value, unit: s<br>|
| **return** | return the current position, unit: s |
| **static** | False |

> C++ defination code:
> ```cpp
> double seek(double time = -1)
> ```
#### duration {#duration-2}

```python
def duration(self) -> float
```
Get the maximum duration of the video. If it returns 0, it means it cannot be predicted.

| item | description |
| --- | --- |
| **type** | func |
| **return** | duration value, unit: s |
| **static** | False |

> C++ defination code:
> ```cpp
> double duration()
> ```
#### timebase {#timebase-2}

```python
def timebase(self) -> list[int]
```
Get the time base.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> timebase()
> ```
#### has\_audio {#has\_audio}

```python
def has_audio(self) -> bool
```
If find audio data, return true

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> bool has_audio()
> ```
#### has\_video {#has\_video}

```python
def has_video(self) -> bool
```
If find video data, return true

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> bool has_video()
> ```
### Video {#Video}

Video class


> C++ defination code:
> ```cpp
> class Video
> ```

#### \_\_init\_\_ {#\_\_init\_\_-5}

```python
def __init__(self, path: str = '', width: int = 2560, height: int = 1440, format: maix.image.Format = ..., time_base: int = 30, framerate: int = 30, capture: bool = False, open: bool = True) -> None
```
Construct a new Video object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **path**: video path. the path determines the location where you load or save the file, if path is none, the video module will not save or load file.<br>xxx.h265 means video format is H265, xxx.mp4 means video format is MP4<br>**width**: picture width. this value may be set automatically. default is 2560.<br>**height**: picture height. this value may be set automatically. default is 1440.<br>**format**: picture pixel format. this value may be set automatically. default is FMT_YVU420SP.<br>**time_base**: frame time base. time_base default is 30, means 1/30 ms<br>**framerate**: frame rate. framerate default is 30, means 30 frames per second<br>for video. 1/time_base is not the average frame rate if the frame rate is not constant.<br>**capture**: enable capture, if true, you can use capture() function to get an image object<br>**open**: If true, video will automatically call open() after creation. default is true.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Video(std::string path = std::string(), int width = 2560, int height = 1440, image::Format format = image::Format::FMT_YVU420SP, int time_base = 30, int framerate = 30, bool capture = false, bool open = true)
> ```
#### open {#open}

```python
def open(self, path: str = '', fps: float = 30.0) -> maix.err.Err
```
Open video and run

| item | description |
| --- | --- |
| **type** | func |
| **param** | **path**: video path. the path determines the location where you load or save the file, if path is none, the video module will not save or load file.<br>xxx.h265 means video format is H265, xxx.mp4 means video format is MP4<br>**fps**: video fps<br>|
| **return** | error code, err::ERR_NONE means success, others means failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err open(std::string path = std::string(), double fps = 30.0)
> ```
#### close {#close}

```python
def close(self) -> None
```
Close video

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void close()
> ```
#### bind\_camera {#bind\_camera-2}

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
#### encode {#encode-2}

```python
def encode(self, img: maix.image.Image = ...) -> Packet
```
Encode image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: the image will be encode.<br>if the img is NULL, this function will try to get image from camera, you must use bind_camera() function to bind the camera.<br>|
| **return** | encode result |
| **static** | False |

> C++ defination code:
> ```cpp
> video::Packet *encode(image::Image *img = maix::video::Video::NoneImage)
> ```
#### decode {#decode-2}

```python
def decode(self, frame: Frame = None) -> maix.image.Image
```
Decode frame

| item | description |
| --- | --- |
| **type** | func |
| **param** | **frame**: the frame will be decode<br>|
| **return** | decode result |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *decode(video::Frame *frame = nullptr)
> ```
#### finish {#finish}

```python
def finish(self) -> maix.err.Err
```
Encode or decode finish

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err finish()
> ```
#### capture {#capture-2}

```python
def capture(self) -> maix.image.Image
```
Capture image

| item | description |
| --- | --- |
| **type** | func |
| **attention** | Each time encode is called, the last captured image will be released. |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *capture()
> ```
#### is\_recording {#is\_recording}

```python
def is_recording(self) -> bool
```
Check if video is recording

| item | description |
| --- | --- |
| **type** | func |
| **return** | true if video is recording, false if not |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_recording()
> ```
#### is\_opened {#is\_opened}

```python
def is_opened(self) -> bool
```
Check if video is opened

| item | description |
| --- | --- |
| **type** | func |
| **return** | true if video is opened, false if not |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_opened()
> ```
#### is\_closed {#is\_closed}

```python
def is_closed(self) -> bool
```
check video device is closed or not

| item | description |
| --- | --- |
| **type** | func |
| **return** | closed or not, bool type |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_closed()
> ```
#### width {#width-3}

```python
def width(self) -> int
```
Get video width

| item | description |
| --- | --- |
| **type** | func |
| **return** | video width |
| **static** | False |

> C++ defination code:
> ```cpp
> int width()
> ```
#### height {#height-3}

```python
def height(self) -> int
```
Get video height

| item | description |
| --- | --- |
| **type** | func |
| **return** | video height |
| **static** | False |

> C++ defination code:
> ```cpp
> int height()
> ```
### VideoRecorder {#VideoRecorder}

Video Recorder class. This module is not fully supported and may be deprecated in the future. You can use the camera, encoder, and audio modules to achieve similar functionality.


> C++ defination code:
> ```cpp
> class VideoRecorder
> ```

#### \_\_init\_\_ {#\_\_init\_\_-6}

```python
def __init__(self, open: bool = True) -> None
```
Construct a new VideoRecorder object. This is an object that integrates recording, video capturing, and display functions, which can be used to achieve high-resolution video input when needed.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **open**: If true, video will automatically call open() after creation. default is true.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> VideoRecorder(bool open = true)
> ```
#### lock {#lock}

```python
def lock(self, timeout: int = -1) -> maix.err.Err
```
lock video

| item | description |
| --- | --- |
| **type** | func |
| **param** | **timeout**: timeout in ms. unit:ms<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err lock(int64_t timeout = -1)
> ```
#### unlock {#unlock}

```python
def unlock(self) -> maix.err.Err
```
unlock video

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err unlock()
> ```
#### open {#open-2}

```python
def open(self) -> maix.err.Err
```
Start a thread to handle the input function.

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err open()
> ```
#### close {#close-2}

```python
def close(self) -> maix.err.Err
```
Stop the thread, and reset the object.

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err close()
> ```
#### is\_opened {#is\_opened-2}

```python
def is_opened(self) -> bool
```
Check whether the object is opened.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_opened()
> ```
#### bind\_display {#bind\_display}

```python
def bind_display(self, display: maix.display.Display, fit: maix.image.Fit = ...) -> maix.err.Err
```
Bind a Display object. if this object is not bound, it will not be displayed.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **display**: display object<br>**fit**: fit mode. It is recommended to fill in FIT_COVER or FIT_FILL. For maixcam, using FIT_CONTAIN may affect the<br>functionality of the second layer created by add_channel() in the Display. default is FIT_COVER.<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err bind_display(display::Display *display, image::Fit fit = image::FIT_COVER)
> ```
#### bind\_camera {#bind\_camera-3}

```python
def bind_camera(self, camera: maix.camera.Camera) -> maix.err.Err
```
Bind a Camera object. if this object is not bound, images cannot be captured.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **camera**: camera object<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err bind_camera(camera::Camera *camera)
> ```
#### bind\_audio {#bind\_audio}

```python
def bind_audio(self, audio: maix.audio.Recorder) -> maix.err.Err
```
Bind a AudioRecorder object. if this object is not bound, audio cannot be captured.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **audio**: audio recorder object<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err bind_audio(audio::Recorder *audio)
> ```
#### bind\_imu {#bind\_imu}

```python
def bind_imu(self, imu: capsule) -> maix.err.Err
```
Bind a IMU object. if this object is not bound, imu data cannot be captured.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **imu**: imu object<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err bind_imu(void *imu)
> ```
#### reset {#reset}

```python
def reset(self) -> maix.err.Err
```
Reset the video recorder.

| item | description |
| --- | --- |
| **type** | func |
| **note** | It will not reset the bound object; if you have already bound the display using bind_display(), there is no need to rebind the display after calling reset(). |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err reset()
> ```
#### config\_path {#config\_path}

```python
def config_path(self, path: str) -> maix.err.Err
```
The recorded video will be saved to this path, and this API cannot be called during runtime.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **path**: The path of the video file to be saved<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err config_path(std::string path)
> ```
#### get\_path {#get\_path}

```python
def get_path(self) -> str
```
Get the path of the video file to be saved

| item | description |
| --- | --- |
| **type** | func |
| **return** | path |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string get_path()
> ```
#### config\_snapshot {#config\_snapshot}

```python
def config_snapshot(self, enable: bool, resolution: list[int] = [], format: maix.image.Format = ...) -> maix.err.Err
```
Set the snapshot parameters

| item | description |
| --- | --- |
| **type** | func |
| **note** | Enabling snapshot functionality may result in some performance loss. |
| **param** | **enable**: enable or disable snapshot<br>**resolution**: image resolution of snapshot<br>**format**: image format of snapshot<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err config_snapshot(bool enable, std::vector<int> resolution = std::vector<int>(), image::Format format = image::Format::FMT_YVU420SP)
> ```
#### config\_resolution {#config\_resolution}

```python
def config_resolution(self, resolution: list[int]) -> maix.err.Err
```
Set the resolution of the video, and this API cannot be called during runtime.

| item | description |
| --- | --- |
| **type** | func |
| **note** | You must bind the camera first, and this interface will modify the camera's resolution. The width must be divisible by 32. |
| **param** | **resolution**: The resolution of the video<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err config_resolution(std::vector<int> resolution)
> ```
#### get\_resolution {#get\_resolution}

```python
def get_resolution(self) -> list[int]
```
Get the resolution of the video

| item | description |
| --- | --- |
| **type** | func |
| **return** | the resolution of the video |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> get_resolution()
> ```
#### config\_fps {#config\_fps}

```python
def config_fps(self, fps: int) -> maix.err.Err
```
Set the fps of the video, and this API cannot be called during runtime.

| item | description |
| --- | --- |
| **type** | func |
| **note** | This interface only affect the fps of the encoded file. |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err config_fps(int fps)
> ```
#### get\_fps {#get\_fps}

```python
def get_fps(self) -> int
```
Get the fps of the video.

| item | description |
| --- | --- |
| **type** | func |
| **return** | fps value |
| **static** | False |

> C++ defination code:
> ```cpp
> int get_fps()
> ```
#### config\_bitrate {#config\_bitrate}

```python
def config_bitrate(self, bitrate: int) -> maix.err.Err
```
Set the bitrate of the video, and this API cannot be called during runtime.

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err config_bitrate(int bitrate)
> ```
#### get\_bitrate {#get\_bitrate}

```python
def get_bitrate(self) -> int
```
Get the bitrate of the video.

| item | description |
| --- | --- |
| **type** | func |
| **return** | bitrate value |
| **static** | False |

> C++ defination code:
> ```cpp
> int get_bitrate()
> ```
#### mute {#mute}

```python
def mute(self, data: int = -1) -> int
```
Set/Get the mute of the video

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: If the parameter is true, mute; if false, unmute; if no parameter is provided, return the mute status.<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> int mute(int data = -1)
> ```
#### volume {#volume}

```python
def volume(self, data: int = -1) -> int
```
Set/Get the volume of the video

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: The volume of the video, the range is 0-100. if no parameter is provided, return the volume.<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> int volume(int data = -1)
> ```
#### seek {#seek-2}

```python
def seek(self) -> int
```
Get the current position of the video

| item | description |
| --- | --- |
| **type** | func |
| **return** | current position, unit: ms |
| **static** | False |

> C++ defination code:
> ```cpp
> int64_t seek()
> ```
#### record\_start {#record\_start}

```python
def record_start(self) -> maix.err.Err
```
Start recording

| item | description |
| --- | --- |
| **type** | func |
| **note** | You must bind the camera at a minimum during input. Additionally,<br>if you bind a display, the input image will be shown,<br>if you bind a audio, audio will be recorded,<br>if you bind a IMU, IMU data will be logged. |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err record_start()
> ```
#### snapshot {#snapshot}

```python
def snapshot(self) -> maix.image.Image
```
Take a snapshot

| item | description |
| --- | --- |
| **type** | func |
| **return** | image::Image |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *snapshot()
> ```
#### record\_finish {#record\_finish}

```python
def record_finish(self) -> maix.err.Err
```
Stop recording and save the video

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err record_finish()
> ```
#### draw\_rect {#draw\_rect}

```python
def draw_rect(self, id: int, x: int, y: int, w: int, h: int, color: maix.image.Color = ..., thickness: int = -1, hidden: bool = False) -> maix.err.Err
```
Draw a rect on the video

| item | description |
| --- | --- |
| **type** | func |
| **param** | **id**: id of the rect, range is [0, 15]<br>**x**: x coordinate<br>**y**: y coordinate<br>**w**: width<br>**h**: height<br>**color**: color<br>**tickness**: The line width of the rectangular box; if set to -1, it indicates that the rectangular box will be filled.<br>**hidden**: Hide or show the rectangular box<br>|
| **return** | error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err draw_rect(int id, int x, int y, int w, int h, image::Color color = image::COLOR_WHITE, int thickness = -1, bool hidden = false)
> ```
