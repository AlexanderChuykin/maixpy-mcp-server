---
title: maix.tracker
---

maix.tracker module


> You can use `maix.tracker` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### ByteTracker {#ByteTracker}

tracker.ByteTracker class


> C++ defination code:
> ```cpp
> class ByteTracker
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, max_lost_buff_num: int = 60, track_thresh: float = 0.5, high_thresh: float = 0.6, match_thresh: float = 0.8, max_history: int = 20) -> None
```
tracker.ByteTracker class constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **max_lost_buff_num**: the frames for keep lost tracks.<br>**track_thresh**: tracking confidence threshold.<br>**high_thresh**: threshold to add to new track.<br>**match_thresh**: matching threshold for tracking, e.g. one object in two frame iou < match_thresh we think they are the same obj.<br>**max_history**: max tack's position history length.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> ByteTracker(const int &max_lost_buff_num = 60,
>                     const float &track_thresh = 0.5,
>                     const float &high_thresh = 0.6,
>                     const float &match_thresh = 0.8,
>                     const int &max_history = 20)
> ```
#### update {#update}

```python
def update(self, objs: list[...]) -> list[...]
```
update tracks according to current detected objects.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<tracker::Track> update(const std::vector<tracker::Object> &objs)
> ```
### Object {#Object}

tracker.Object class


> C++ defination code:
> ```cpp
> class Object
> ```

#### \_\_init\_\_ {#\_\_init\_\_-2}

```python
def __init__(self, x: int, y: int, w: int, h: int, class_id: int, score: float) -> None
```
tracker.Object class constructor

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> Object(const int &x, const int &y, const int &w, const int &h, const int &class_id, const float &score)
> ```
#### x {#x}

position x attribute.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int x
> ```
#### y {#y}

position y attribute.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int y
> ```
#### w {#w}

position rectangle width.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int w
> ```
#### h {#h}

position rectangle height.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int h
> ```
#### class\_id {#class\_id}

object class id, int type.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int class_id
> ```
#### score {#score}

object score(prob).

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float score
> ```
### Track {#Track}

tracker.Track class


> C++ defination code:
> ```cpp
> class Track
> ```

#### \_\_init\_\_ {#\_\_init\_\_-3}

```python
def __init__(self, id: int, score: float, lost: bool, start_frame_id: int, frame_id: int) -> None
```
tracker.Track class constructor

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> Track(const size_t &id, const float &score, const bool &lost, const size_t &start_frame_id, const size_t &frame_id)
> ```
#### id {#id}

track id.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> size_t id
> ```
#### score {#score-2}

track score(prob).

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float score
> ```
#### lost {#lost}

whether this track lost.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool lost
> ```
#### start\_frame\_id {#start\_frame\_id}

track start frame id.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> size_t start_frame_id
> ```
#### frame\_id {#frame\_id}

track current frame id.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> size_t frame_id
> ```
#### history {#history}

track position history, the last one is latest position.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::deque<tracker::Object> history
> ```
