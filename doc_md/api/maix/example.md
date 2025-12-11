---
title: maix.example
---

example module, this will be maix.example module in MaixPy, maix::example namespace in MaixCDK


> You can use `maix.example` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### Kind {#Kind}

Example enum(not recommend! See Kind2)

| item | describe |
| --- | --- |
| **values** | **KIND_NONE**: Kind none, value always 0, other enum value will auto increase<br>**KIND_DOG**: Kind dog<br>**KIND_CAT**: Kind cat, value is auto generated according to KING_DOG<br>**KIND_BIRD**: <br>**KIND_MAX**: Max Kind quantity<br>You can get max Kind value by KIND_MAX - 1<br>
> C++ defination code:
> ```cpp
> enum Kind
>         {
>             KIND_NONE = 0, /** Kind none, value always 0, other enum value will auto increase */
>             KIND_DOG,      /** Kind dog*/
>             KIND_CAT,      // Kind cat, value is auto generated according to KING_DOG
>             KIND_BIRD,
>             KIND_MAX /* Max Kind quantity,
>                         You can get max Kind value by KIND_MAX - 1
>                      */
>         }
> ```
### Kind2 {#Kind2}

Example enum class(recommend!)

| item | describe |
| --- | --- |
| **values** | **NONE**: Kind none, value always 0, other enum value will auto increase<br>**DOG**: Kind dog<br>**CAT**: Kind cat, value is auto generated according to KING_DOG<br>**BIRD**: <br>**MAX**: Max Kind quantity<br>You can get max Kind value by KIND_MAX - 1<br>
> C++ defination code:
> ```cpp
> enum class Kind2
>         {
>             NONE = 0, /** Kind none, value always 0, other enum value will auto increase */
>             DOG,      /** Kind dog*/
>             CAT,      // Kind cat, value is auto generated according to KING_DOG
>             BIRD,
>             MAX       /* Max Kind quantity,
>                          You can get max Kind value by KIND_MAX - 1
>                       */
>         }
> ```


## Variable {#Variable}

### var1 {#var1}

Example module variable

| item | description |
| --- | --- |
| **attention** | It's a copy of this variable in MaixPy,<br>so change it in C++ (e.g. update var in hello function) will not take effect the var inMaixPy.<br>So we add const for this var to avoid this mistake. |
| **value** | **"Sipeed"** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const std::string var1 = "Sipeed"
> ```
### list\_var {#list\_var}

Tensor data type size in bytes

| item | description |
| --- | --- |
| **attention** | **1**. DO NOT use C/C++ array directly for python API, the python wrapper not support it.<br>Use std::vector instead.<br>**2**. It's a copy of this variable in MaixPy,<br>so change it in C++ (e.g. update var in hello function) will not take effect the var inMaixPy.<br>So we add const for this var to avoid this mistake.<br>|
| **value** | **{<br>            0, 1, 2, 3, 4, 5, 6, 7, 8, 9}** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const std::vector<int> list_var = {
>             0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
> ```
### test\_var {#test\_var}

Example module variable test_var

| item | description |
| --- | --- |
| **attention** | It's a copy of this variable in MaixPy, so if you change it in C++, it will not take effect in MaixPy.<br>And change it in MaixPy will not take effect in C++ as well !!!<br>If you want to use vars shared between C++ and MaixPy, you can create a class and use its member. |
| **value** | **100** |
| **readonly**| False |

> C++ defination code:
> ```cpp
> int test_var = 100
> ```


## Function {#Function}

### hello {#hello}

```python
def hello(name: str) -> str
```
say hello to someone

| item | description |
| --- | --- |
| **param** | **name**: direction [in], name of someone, string type<br>|
| **return** | string type, content is hello + name |

> C++ defination code:
> ```cpp
> std::string hello(std::string name)
> ```
### change\_arg\_name {#change\_arg\_name}

```python
def change_arg_name(e: Example) -> Example
```
Change arg name example

| item | description |
| --- | --- |
| **param** | **e**: Example object<br>|
| **return** | same as arg |

> C++ defination code:
> ```cpp
> example::Example *change_arg_name(example::Example *e)
> ```
### change\_arg\_name2 {#change\_arg\_name2}

```python
def change_arg_name2(e: Example) -> None
```
Change arg name example

| item | description |
| --- | --- |
| **param** | **e**: Example object<br>|

> C++ defination code:
> ```cpp
> void change_arg_name2(example::Example &e)
> ```


## Class {#Class}

### Test {#Test}

Test class


> C++ defination code:
> ```cpp
> class Test
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self) -> None
```
Test constructor

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> Test()
> ```
### Example {#Example}

Example class\nthis class will be export to MaixPy as maix.example.Example


> C++ defination code:
> ```cpp
> class Example
> ```

#### \_\_init\_\_ {#\_\_init\_\_-2}

```python
def __init__(self, name: str, age: int = 18, pet: Kind = ...) -> None
```
Example constructor\nthis constructor will be export to MaixPy as maix.example.Example.__init__

| item | description |
| --- | --- |
| **type** | func |
| **param** | **name**: direction [in], name of Example, string type<br>**age**: direction [in], age of Example, int type, default is 18, value range is [0, 100]<br>|
| **attention** | to make auto generate code work, param Kind should with full namespace name `example::Kind` instead of `Kind`,<br>namespace `maix` can be ignored. |
| **static** | False |

> C++ defination code:
> ```cpp
> Example(std::string &name, int age = 18, example::Kind pet = example::KIND_NONE)
> ```
#### get\_name {#get\_name}

```python
def get_name(self) -> str
```
get name of Example\nyou can also get name by property `name`.

| item | description |
| --- | --- |
| **type** | func |
| **return** | name of Example, string type |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string get_name()
> ```
#### get\_age {#get\_age}

```python
def get_age(self) -> int
```
get age of Example

| item | description |
| --- | --- |
| **type** | func |
| **return** | age of Example, int type, value range is [0, 100] |
| **static** | False |

> C++ defination code:
> ```cpp
> int get_age()
> ```
#### set\_name {#set\_name}

```python
def set_name(self, name: str) -> None
```
set name of Example

| item | description |
| --- | --- |
| **type** | func |
| **param** | **name**: name of Example, string type<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_name(std::string name)
> ```
#### set\_age {#set\_age}

```python
def set_age(self, age: int) -> None
```
set age of Example

| item | description |
| --- | --- |
| **type** | func |
| **param** | **age**: age of Example, int type, value range is [0, 100]<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_age(int age)
> ```
#### set\_pet {#set\_pet}

```python
def set_pet(self, pet: Kind) -> None
```
Example enum member

| item | description |
| --- | --- |
| **type** | func |
| **attention** |  |
| **static** | False |

> C++ defination code:
> ```cpp
> void set_pet(example::Kind pet)
> ```
#### get\_pet {#get\_pet}

```python
def get_pet(self) -> Kind
```
Example enum member

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> example::Kind get_pet()
> ```
#### get\_list {#get\_list}

```python
def get_list(self, in: list[int]) -> list[int]
```
get list example

| item | description |
| --- | --- |
| **type** | func |
| **param** | **in**: direction [in], input list, items are int type.<br>In MaixPy, you can pass list or tuple to this API<br>|
| **return** | list, items are int type, content is [1, 2, 3] + in. Alloc item, del in MaixPy will auto free memory. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> *get_list(std::vector<int> in)
> ```
#### get\_dict {#get\_dict}

```python
def get_dict(self, in: dict[str, int]) -> dict[str, int]
```
Example dict API

| item | description |
| --- | --- |
| **type** | func |
| **param** | **in**: direction [in], input dict, key is string type, value is int type.<br>In MaixPy, you can pass `dict` to this API<br>|
| **return** | dict, key is string type, value is int type, content is {"a": 1} + in<br>In MaixPy, return type is `dict` object |
| **static** | False |

> C++ defination code:
> ```cpp
> std::map<std::string, int> get_dict(std::map<std::string, int> &in)
> ```
#### hello {#hello-2}

```python
def hello(name: str) -> str
```
say hello to someone

| item | description |
| --- | --- |
| **type** | func |
| **param** | **name**: name of someone, string type<br>|
| **return** | string type, content is Example::hello_str + name |
| **static** | True |

> C++ defination code:
> ```cpp
> static std::string hello(std::string name)
> ```
#### hello\_bytes {#hello\_bytes}

```python
def hello_bytes(*args, **kwargs)
```
param is bytes example

| item | description |
| --- | --- |
| **type** | func |
| **param** | **bytes**: bytes type param<br>|
| **return** | bytes type, return value is bytes changed value |
| **static** | True |

> C++ defination code:
> ```cpp
> static Bytes *hello_bytes(Bytes &bytes)
> ```
#### callback {#callback}

```python
def callback(cb: typing.Callable[[int, int], int]) -> int
```
Callback example

| item | description |
| --- | --- |
| **type** | func |
| **param** | **cb**: callback function, param is two int type, return is int type<br>|
| **return** | int type, return value is cb's return value. |
| **static** | True |

> C++ defination code:
> ```cpp
> static int callback(std::function<int(int, int)> cb)
> ```
#### callback2 {#callback2}

```python
def callback2(cb: typing.Callable[[list[int], int], int]) -> int
```
Callback example

| item | description |
| --- | --- |
| **type** | func |
| **param** | **cb**: callback function, param is a int list type and int type, return is int type<br>|
| **return** | int type, return value is cb's return value. |
| **static** | True |

> C++ defination code:
> ```cpp
> static int callback2(std::function<int(std::vector<int>, int)> cb)
> ```
#### hello\_dict {#hello\_dict}

```python
def hello_dict(dict: dict[str, int]) -> dict[str, int]
```
Dict param example

| item | description |
| --- | --- |
| **type** | func |
| **param** | **dict**: dict type param, key is string type, value is int type<br>|
| **static** | True |

> C++ defination code:
> ```cpp
> static std::map<std::string, int> *hello_dict(std::map<std::string, int> *dict)
> ```
#### name {#name}

name member of Example

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string name
> ```
#### age {#age}

age member of Example, value range should be [0, 100]

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int age
> ```
#### hello\_str {#hello\_str}

hello_str member of Example, default value is \"hello \"

| item | description |
| --- | --- |
| **type** | var |
| **static** | True |
| **readonly** | False |

> C++ defination code:
> ```cpp
> static std::string hello_str
> ```
#### var1 {#var1-2}

Example module readonly variable

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | True |

> C++ defination code:
> ```cpp
> const std::string var1 = "Example.var1"
> ```
#### var2 {#var2}

Example module readonly variable

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | True |

> C++ defination code:
> ```cpp
> std::string var2 = "Example.var2"
> ```
#### dict\_test {#dict\_test}

```python
def dict_test() -> dict[str, Test]
```
dict_test, return dict type, and element is pointer type(alloc in C++).\nHere when the returned Tensor object will auto delete by Python GC.

| item | description |
| --- | --- |
| **type** | func |
| **static** | True |

> C++ defination code:
> ```cpp
> static std::map<std::string, example::Test *> *dict_test()
> ```
