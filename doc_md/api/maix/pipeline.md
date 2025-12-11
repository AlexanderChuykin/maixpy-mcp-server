---
title: maix.pipeline
---

maix.pipeline module, video stream processing via pipeline


> You can use `maix.pipeline` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### Stream {#Stream}

Stream class, saved the video stream data


> C++ defination code:
> ```cpp
> class Stream
> ```

#### data\_count {#data\_count}

```python
def data_count(self) -> int
```
Since a single stream may contain multiple pieces of data, this returns the number of data segments present.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int data_count()
> ```
#### data {#data}

```python
def data(*args, **kwargs)
```
Get the data stream at index

| item | description |
| --- | --- |
| **type** | func |
| **param** | **idx**: data index, must be less than data_count().<br>|
| **return** | Returns the data at index. Note: when using C++, you need to manually release the memory. |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *data(int idx)
> ```
#### data\_size {#data\_size}

```python
def data_size(self, idx: int) -> int
```
Get the data size at index

| item | description |
| --- | --- |
| **type** | func |
| **param** | **idx**: data index, must be less than data_count().<br>|
| **return** | Returns the data size at index. |
| **static** | False |

> C++ defination code:
> ```cpp
> int data_size(int idx)
> ```
#### get\_sps\_frame {#get\_sps\_frame}

```python
def get_sps_frame(*args, **kwargs)
```
Get the SPS frame data; if the frame does not exist, return null.

| item | description |
| --- | --- |
| **type** | func |
| **return** | SPS frame data. |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *get_sps_frame()
> ```
#### get\_pps\_frame {#get\_pps\_frame}

```python
def get_pps_frame(*args, **kwargs)
```
Get the PPS frame data; if the frame does not exist, return null.

| item | description |
| --- | --- |
| **type** | func |
| **return** | PPS frame data. |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *get_pps_frame()
> ```
#### get\_i\_frame {#get\_i\_frame}

```python
def get_i_frame(*args, **kwargs)
```
Get the I frame data; if the frame does not exist, return null.

| item | description |
| --- | --- |
| **type** | func |
| **return** | I frame data. |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *get_i_frame()
> ```
#### get\_p\_frame {#get\_p\_frame}

```python
def get_p_frame(*args, **kwargs)
```
Get the PTS(Presentation Timestamp) of the stream.

| item | description |
| --- | --- |
| **type** | func |
| **return** | P frame data. |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *get_p_frame()
> ```
#### has\_pps\_frame {#has\_pps\_frame}

```python
def has_pps_frame(self) -> bool
```
Check if the stream has PPS frame.

| item | description |
| --- | --- |
| **type** | func |
| **return** | PPS frame data. |
| **static** | False |

> C++ defination code:
> ```cpp
> bool has_pps_frame()
> ```
#### has\_sps\_frame {#has\_sps\_frame}

```python
def has_sps_frame(self) -> bool
```
Check if the stream has SPS frame.

| item | description |
| --- | --- |
| **type** | func |
| **return** | SPS frame data. |
| **static** | False |

> C++ defination code:
> ```cpp
> bool has_sps_frame()
> ```
#### has\_i\_frame {#has\_i\_frame}

```python
def has_i_frame(self) -> bool
```
Check if the stream has I frame.

| item | description |
| --- | --- |
| **type** | func |
| **return** | True if the stream has I frame, otherwise false. |
| **static** | False |

> C++ defination code:
> ```cpp
> bool has_i_frame()
> ```
#### has\_p\_frame {#has\_p\_frame}

```python
def has_p_frame(self) -> bool
```
Check if the stream has P frame.

| item | description |
| --- | --- |
| **type** | func |
| **return** | True if the stream has P frame, otherwise false. |
| **static** | False |

> C++ defination code:
> ```cpp
> bool has_p_frame()
> ```
#### pts {#pts}

```python
def pts(self) -> int
```
Get the pts(Presentation Timestamp) of the stream

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the pts of the stream. |
| **static** | False |

> C++ defination code:
> ```cpp
> size_t pts()
> ```
### Frame {#Frame}

Frame class, saved the image data


> C++ defination code:
> ```cpp
> class Frame
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, frame: capsule, auto_delete: bool = False, from: str = '') -> None
```
Construct a new Frame object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **frame**: frame handle<br>**auto_delete**: auto delete frame when object is destroyed<br>**from**: When releasing the object, the 'from' parameter will be referenced to determine the release method.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Frame(void *frame, bool auto_delete = false, std::string from = "")
> ```
#### width {#width}

```python
def width(self) -> int
```
Get the width of the frame

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the width of the frame. |
| **static** | False |

> C++ defination code:
> ```cpp
> int width()
> ```
#### height {#height}

```python
def height(self) -> int
```
Get the height of the frame

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the height of the frame. |
| **static** | False |

> C++ defination code:
> ```cpp
> int height()
> ```
#### format {#format}

```python
def format(self) -> maix.image.Format
```
Get the format of the frame

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the format of the frame. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format format()
> ```
#### to\_image {#to\_image}

```python
def to_image(self) -> maix.image.Image
```
Convert the frame to an image

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns an image object. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *to_image()
> ```
#### stride {#stride}

```python
def stride(self, idx: int) -> int
```
Get the stride of the plane. Stride represents the number of bytes occupied in memory by each row of image data.\nIt is usually greater than or equal to the number of bytes actually used by the pixels in that row.\nIn image processing, different image formats are divided into multiple planes.\nTypically, RGB images have only one valid plane, while NV21/NV12 images have two valid planes.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **idx**: plane index.<br>|
| **return** | Returns the stride of the frame. |
| **static** | False |

> C++ defination code:
> ```cpp
> int stride(int idx)
> ```
#### virtual\_address {#virtual\_address}

```python
def virtual_address(self, idx: int) -> int
```
Get the virtual address of the plane. In image processing, different image formats are divided into multiple planes.\nTypically, RGB images have only one valid plane, while NV21/NV12 images have two valid planes.

| item | description |
| --- | --- |
| **type** | func |
| **note** | You can read image data from this address, but you need to be very careful.<br>If the current object has been released, operating on this address is prohibited. |
| **param** | **idx**: plane index.<br>|
| **return** | Returns the virtual address of the frame. |
| **static** | False |

> C++ defination code:
> ```cpp
> uint64_t virtual_address(int idx)
> ```
#### physical\_address {#physical\_address}

```python
def physical_address(self, idx: int) -> int
```
Get the physical address of the plane. In image processing, different image formats are divided into multiple planes.\nTypically, RGB images have only one valid plane, while NV21/NV12 images have two valid planes.

| item | description |
| --- | --- |
| **type** | func |
| **note** | Don’t operate on this address. |
| **param** | **idx**: plane index.<br>|
| **return** | Returns the physical address of the frame. |
| **static** | False |

> C++ defination code:
> ```cpp
> uint64_t physical_address(int idx)
> ```
