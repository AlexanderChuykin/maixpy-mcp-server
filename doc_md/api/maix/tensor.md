---
title: maix.tensor
---

maix.tensor module


> You can use `maix.tensor` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### DType {#DType}

Tensor data types

| item | describe |
| --- | --- |
| **values** | **UINT8**: <br>**INT8**: <br>**UINT16**: <br>**INT16**: <br>**UINT32**: <br>**INT32**: <br>**FLOAT16**: <br>**FLOAT32**: <br>**FLOAT64**: <br>**BOOL**: <br>**DTYPE_MAX**: <br>
> C++ defination code:
> ```cpp
> enum DType
>         {
>             UINT8 = 0,
>             INT8,
>             UINT16,
>             INT16,
>             UINT32,
>             INT32,
>             FLOAT16,
>             FLOAT32,
>             FLOAT64,
>             BOOL,
>             // STRING,
>             // OBJECT,
>             DTYPE_MAX
>         }
> ```


## Variable {#Variable}

### dtype\_size {#dtype\_size}

Tensor data type size in bytes

| item | description |
| --- | --- |
| **attention** | It's a copy of this variable in MaixPy,<br>so change it in C++ (e.g. update var in hello function) will not take effect the var inMaixPy.<br>So we add const for this var to avoid this mistake. |
| **value** | **{<br>            1, // UINT8<br>            1, // INT8<br>            2, // UINT16<br>            2, // INT16<br>            4, // UINT32<br>            4, // INT32<br>            2, // FLOAT16<br>            4, // FLOAT32<br>            8, // FLOAT64<br>            1, // BOOL<br>            // 1, // STRING<br>            // 1, // OBJECT<br>            0<br>        }** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const std::vector<int> dtype_size = {
>             1, // UINT8
>             1, // INT8
>             2, // UINT16
>             2, // INT16
>             4, // UINT32
>             4, // INT32
>             2, // FLOAT16
>             4, // FLOAT32
>             8, // FLOAT64
>             1, // BOOL
>             // 1, // STRING
>             // 1, // OBJECT
>             0
>         }
> ```
### dtype\_name {#dtype\_name}

Tensor data type name

| item | description |
| --- | --- |
| **value** | **{<br>            "uint8",<br>            "int8",<br>            "uint16",<br>            "int16",<br>            "uint32",<br>            "int32",<br>            "float16",<br>            "float32",<br>            "float64",<br>            "bool",<br>            // "string",<br>            // "object",<br>            "invalid"<br>        }** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const std::vector<std::string> dtype_name = {
>             "uint8",
>             "int8",
>             "uint16",
>             "int16",
>             "uint32",
>             "int32",
>             "float16",
>             "float32",
>             "float64",
>             "bool",
>             // "string",
>             // "object",
>             "invalid"
>         }
> ```


## Function {#Function}

### tensor\_from\_numpy\_float32 {#tensor\_from\_numpy\_float32}

```python
def tensor_from_numpy_float32(array: numpy.ndarray[numpy.float32], copy: bool = True) -> Tensor
```
float32 type numpy ndarray object to tensor.Tensor object.

| item | description |
| --- | --- |
| **param** | **array**: numpy array object.<br>**copy**: if true, will alloc new buffer and copy data, else will directly use array's data buffer, default true.<br>Use this arg carefully, when set to false, ther array MUST keep alive until we don't use the return tensor of this func, or will cause program crash.<br>|
| **return** | tensor.Tensor object. |

> C++ defination code:
> ```cpp
> tensor::Tensor *tensor_from_numpy_float32(py::array_t<float, py::array::c_style> array, bool copy = true)
> ```
### tensor\_from\_numpy\_uint8 {#tensor\_from\_numpy\_uint8}

```python
def tensor_from_numpy_uint8(array: numpy.ndarray[numpy.uint8], copy: bool = True) -> Tensor
```
uint8 type numpy ndarray object to tensor.Tensor object.

| item | description |
| --- | --- |
| **param** | **array**: numpy array object.<br>**copy**: if true, will alloc new buffer and copy data, else will directly use array's data buffer, default true.<br>Use this arg carefully, when set to false, ther array MUST keep alive until we don't use the return tensor of this func, or will cause program crash.<br>|
| **return** | tensor.Tensor object. |

> C++ defination code:
> ```cpp
> tensor::Tensor *tensor_from_numpy_uint8(py::array_t<uint8_t, py::array::c_style> array, bool copy = true)
> ```
### tensor\_from\_numpy\_int8 {#tensor\_from\_numpy\_int8}

```python
def tensor_from_numpy_int8(array: numpy.ndarray[numpy.int8], copy: bool = True) -> Tensor
```
int8 type numpy ndarray object to tensor.Tensor object.

| item | description |
| --- | --- |
| **param** | **array**: numpy array object.<br>**copy**: if true, will alloc new buffer and copy data, else will directly use array's data buffer, default true.<br>Use this arg carefully, when set to false, ther array MUST keep alive until we don't use the return tensor of this func, or will cause program crash.<br>|
| **return** | tensor.Tensor object. |

> C++ defination code:
> ```cpp
> tensor::Tensor *tensor_from_numpy_int8(py::array_t<int8_t, py::array::c_style> array, bool copy = true)
> ```
### tensor\_to\_numpy\_float32 {#tensor\_to\_numpy\_float32}

```python
def tensor_to_numpy_float32(t: Tensor, copy: bool = True) -> numpy.ndarray[numpy.float32]
```
tensor.Tensor object to float32 type numpy ndarray object.

| item | description |
| --- | --- |
| **param** | **t**: tensor.Tensor object.<br>**copy**: Whether alloc new Tensor and copy data or not,<br>if not copy, array object will directly use arg's data buffer, will faster but change array will affect arg's data, default true.<br>|
| **return** | numpy array object |

> C++ defination code:
> ```cpp
> py::array_t<float, py::array::c_style> tensor_to_numpy_float32(tensor::Tensor *t, bool copy = true)
> ```
### tensor\_to\_numpy\_uint8 {#tensor\_to\_numpy\_uint8}

```python
def tensor_to_numpy_uint8(t: Tensor, copy: bool = True) -> numpy.ndarray[numpy.uint8]
```
tensor.Tensor object to int8 type numpy ndarray object.

| item | description |
| --- | --- |
| **param** | **t**: tensor.Tensor object.<br>**copy**: Whether alloc new Tensor and copy data or not,<br>if not copy, array object will directly use arg's data buffer, will faster but change array will affect arg's data, default true.<br>|
| **return** | numpy array object |

> C++ defination code:
> ```cpp
> py::array_t<uint8_t, py::array::c_style> tensor_to_numpy_uint8(tensor::Tensor *t, bool copy = true)
> ```
### tensor\_to\_numpy\_int8 {#tensor\_to\_numpy\_int8}

```python
def tensor_to_numpy_int8(t: Tensor, copy: bool = True) -> numpy.ndarray[numpy.int8]
```
tensor.Tensor object to int8 type numpy ndarray object.

| item | description |
| --- | --- |
| **param** | **t**: tensor.Tensor object.<br>**copy**: Whether alloc new Tensor and copy data or not,<br>if not copy, array object will directly use arg's data buffer, will faster but change array will affect arg's data, default true.<br>|
| **return** | numpy array object |

> C++ defination code:
> ```cpp
> py::array_t<int8_t, py::array::c_style> tensor_to_numpy_int8(tensor::Tensor *t, bool copy = true)
> ```


## Class {#Class}

### Tensor {#Tensor}

Tensor class


> C++ defination code:
> ```cpp
> class Tensor
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, shape: list[int], dtype: DType) -> None
```
Tensor constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **shape**: tensor shape, a int list<br>**dtype**: tensor element data type, see DType of this module<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Tensor(std::vector<int> shape, tensor::DType dtype)
> ```
#### to\_str {#to\_str}

```python
def to_str(self) -> str
```
To string

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string to_str()
> ```
#### \_\_str\_\_ {#\_\_str\_\_}

```python
def __str__(self) -> str
```
To string

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string __str__()
> ```
#### shape {#shape}

```python
def shape(self) -> list[int]
```
get tensor shape

| item | description |
| --- | --- |
| **type** | func |
| **return** | tensor shape, a int list |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> shape()
> ```
#### expand\_dims {#expand\_dims}

```python
def expand_dims(self, axis: int) -> None
```
expand tensor shape

| item | description |
| --- | --- |
| **type** | func |
| **param** | **axis**: axis to expand<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void expand_dims(int axis)
> ```
#### reshape {#reshape}

```python
def reshape(self, shape: list[int]) -> None
```
reshape tensor shape, if size not match, it will throw an err::Exception

| item | description |
| --- | --- |
| **type** | func |
| **param** | **shape**: new shape<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void reshape(std::vector<int> shape)
> ```
#### flatten {#flatten}

```python
def flatten(self) -> None
```
Flatten tensor shape to 1D

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void flatten()
> ```
#### dtype {#dtype-2}

```python
def dtype(self) -> DType
```
get tensor data type

| item | description |
| --- | --- |
| **type** | func |
| **return** | tensor data type, see DType of this module |
| **static** | False |

> C++ defination code:
> ```cpp
> tensor::DType  dtype()
> ```
#### to\_float\_list {#to\_float\_list}

```python
def to_float_list(self) -> list[float]
```
get tensor data and return a list

| item | description |
| --- | --- |
| **type** | func |
| **return** | list type data |
| **static** | False |

> C++ defination code:
> ```cpp
> std::valarray<float>* to_float_list()
> ```
#### argmax {#argmax}

```python
def argmax(self, axis: int = 65535) -> Tensor
```
argmax of tensor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **axis**: By default, the index is into the flattened array, otherwise along the specified axis., wrong axis will throw an err::Exception<br>|
| **return** | argmax result, you need to delete it after use in C++. |
| **static** | False |

> C++ defination code:
> ```cpp
> tensor::Tensor *argmax(int axis = 0xffff)
> ```
#### argmax1 {#argmax1}

```python
def argmax1(self) -> int
```
argmax1, flattened data max index

| item | description |
| --- | --- |
| **type** | func |
| **return** | argmax result, int type |
| **static** | False |

> C++ defination code:
> ```cpp
> int argmax1()
> ```
### Tensors {#Tensors}

Tensors


> C++ defination code:
> ```cpp
> class Tensors
> ```

#### \_\_init\_\_ {#\_\_init\_\_-2}

```python
def __init__(self) -> None
```
Constructor of Tensors

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> Tensors()
> ```
#### add\_tensor {#add\_tensor}

```python
def add_tensor(self, key: str, tensor: Tensor, copy: bool, auto_delete: bool) -> None
```
Add tensor

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void add_tensor(const std::string &key, tensor::Tensor *tensor, bool copy, bool auto_delete)
> ```
#### rm\_tensor {#rm\_tensor}

```python
def rm_tensor(self, key: str) -> None
```
Remove tensor

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void rm_tensor(const std::string &key)
> ```
#### clear {#clear}

```python
def clear(self) -> None
```
Clear tensors

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void clear()
> ```
#### get\_tensor {#get\_tensor}

```python
def get_tensor(self, key: str) -> Tensor
```
Get tensor by key

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> tensor::Tensor &get_tensor(const std::string &key)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_}

```python
def __getitem__(self, key: str) -> Tensor
```
Operator []

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> tensor::Tensor &operator[](const std::string &key)
> ```
#### \_\_len\_\_ {#\_\_len\_\_}

```python
def __len__(self) -> int
```
Size

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> size_t size()
> ```
#### keys {#keys}

```python
def keys(self) -> list[str]
```
Get names

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::string> keys()
> ```
#### tensors {#tensors-2}

Tensors data, dict type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::map<std::string, tensor::Tensor*> tensors
> ```
### Vector3f {#Vector3f}

Vector3 float type.


> C++ defination code:
> ```cpp
> class Vector3f : public Vector3<float> // we use class for we want to generate maixpy API, and the tool not suppoort using yet.
> ```

#### \_\_init\_\_ {#\_\_init\_\_-3}

```python
def __init__(self, x0: float, y0: float, z0: float) -> None
```
Construct Vector3f with 3 variables.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> Vector3f(float x0, float y0, float z0)
> ```
#### x {#x}

member x.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float x
> ```
#### y {#y}

member y.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float y
> ```
#### z {#z}

member z.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float z
> ```
### Vector3i32 {#Vector3i32}

Vector3 int32_t type.


> C++ defination code:
> ```cpp
> class Vector3i32 : public Vector3<int32_t> // we use class for we want to generate maixpy API, and the tool not suppoort using yet.
> ```

#### \_\_init\_\_ {#\_\_init\_\_-4}

```python
def __init__(self, x0: int, y0: int, z0: int) -> None
```
Construct Vector3i32 with 3 variables.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> Vector3i32(int32_t x0, int32_t y0, int32_t z0)
> ```
#### x {#x-2}

member x.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int32_t x
> ```
#### y {#y-2}

member y.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int32_t y
> ```
#### z {#z-2}

member z.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int32_t z
> ```
### Vector3u32 {#Vector3u32}

Vector3 uint32_t type.


> C++ defination code:
> ```cpp
> class Vector3u32 : public Vector3<uint32_t> // we use class for we want to generate maixpy API, and the tool not suppoort using yet.
> ```

#### \_\_init\_\_ {#\_\_init\_\_-5}

```python
def __init__(self, x0: int, y0: int, z0: int) -> None
```
Construct Vector3u32 with 3 variables.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> Vector3u32(uint32_t x0, uint32_t y0, uint32_t z0)
> ```
#### x {#x-3}

member x.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint32_t x
> ```
#### y {#y-3}

member y.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint32_t y
> ```
#### z {#z-3}

member z.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint32_t z
> ```
### Vector3i16 {#Vector3i16}

Vector3 int16 type.


> C++ defination code:
> ```cpp
> class Vector3i16 : public Vector3<int16_t> // we use class for we want to generate maixpy API, and the tool not suppoort using yet.
> ```

#### \_\_init\_\_ {#\_\_init\_\_-6}

```python
def __init__(self, x0: int, y0: int, z0: int) -> None
```
Construct Vector3i16 with 3 variables.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> Vector3i16(int16_t x0, int16_t y0, int16_t z0)
> ```
#### x {#x-4}

member x.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int16_t x
> ```
#### y {#y-4}

member y.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int16_t y
> ```
#### z {#z-4}

member z.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int16_t z
> ```
### Vector3u16 {#Vector3u16}

Vector3 uint16 type.


> C++ defination code:
> ```cpp
> class Vector3u16 : public Vector3<uint16_t> // we use class for we want to generate maixpy API, and the tool not suppoort using yet.
> ```

#### \_\_init\_\_ {#\_\_init\_\_-7}

```python
def __init__(self, x0: int, y0: int, z0: int) -> None
```
Construct Vector3u16 with 3 variables.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> Vector3u16(uint16_t x0, uint16_t y0, uint16_t z0)
> ```
#### x {#x-5}

member x.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint16_t x
> ```
#### y {#y-5}

member y.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint16_t y
> ```
#### z {#z-5}

member z.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint16_t z
> ```
