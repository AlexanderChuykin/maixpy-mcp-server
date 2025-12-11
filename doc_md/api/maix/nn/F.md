---
title: maix.nn.F
---

maix.nn.F module


> You can use `maix.nn.F` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}

### softmax {#softmax}

```python
def softmax(tensor: maix.tensor.Tensor, replace: bool) -> maix.tensor.Tensor
```
Softmax, only support 1D tensor, multi-dimension tensor will be treated as 1D tensor

| item | description |
| --- | --- |
| **param** | **tensor**: input tensor<br>**replace**: change input tensor data directly, if not, will create a new tensor<br>|
| **throw** | If arg error, will raise err.Exception error |
| **return** | output tensor, if arg replace is true, return the arg tensor's address.<br>If not replace, return a new object, so In C++, you should delete it manually in this case! |

> C++ defination code:
> ```cpp
> tensor::Tensor *softmax(tensor::Tensor *tensor, bool replace)
> ```


## Class {#Class}

