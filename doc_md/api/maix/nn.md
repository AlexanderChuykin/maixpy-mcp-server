---
title: maix.nn
---

maix.nn module


> You can use `maix.nn` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

| module | brief |
| --- | --- |
| [F](./nn/F.md) | maix.nn.F module |


## Enum {#Enum}

### Layout {#Layout}

layer layout types

| item | describe |
| --- | --- |
| **values** | **NCHW**: [N, C, H, W]<br>**NHWC**: [N, H, W, C]<br>**UNKNOWN**: <br>
> C++ defination code:
> ```cpp
> enum class Layout
>     {
>         NCHW = 0,    // [N, C, H, W]
>         NHWC = 1,    // [N, H, W, C]
>         UNKNOWN = 4
>     }
> ```
### SpeechDevice {#SpeechDevice}

speech device

| item | describe |
| --- | --- |
| **values** | **DEVICE_NONE**: <br>**DEVICE_PCM**: <br>**DEVICE_MIC**: <br>**DEVICE_WAV**: <br>
> C++ defination code:
> ```cpp
> enum class SpeechDevice {
>     DEVICE_NONE = -1,
>     DEVICE_PCM,
>     DEVICE_MIC,
>     DEVICE_WAV,
> }
> ```
### SpeechDecoder {#SpeechDecoder}

speech decoder type

| item | describe |
| --- | --- |
| **values** | **DECODER_RAW**: <br>**DECODER_DIG**: <br>**DECODER_LVCSR**: <br>**DECODER_KWS**: <br>**DECODER_ALL**: <br>
> C++ defination code:
> ```cpp
> enum class SpeechDecoder {
>     DECODER_RAW   = 1,
>     DECODER_DIG   = 2,
>     DECODER_LVCSR = 4,
>     DECODER_KWS   = 8,
>     DECODER_ALL   = 65535,
> }
> ```


## Variable {#Variable}



## Function {#Function}



## Class {#Class}

### QwenResp {#QwenResp}

Qwen model response


> C++ defination code:
> ```cpp
> class QwenResp
> ```

#### msg {#msg}

Model response full message.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string msg
> ```
#### msg\_new {#msg\_new}

Model response new message.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string msg_new
> ```
#### err\_code {#err\_code}

Model response error code, maix.Err type, should be err.Err.ERR_NONE if no error.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> err::Err err_code
> ```
#### err\_msg {#err\_msg}

Model response error message.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string err_msg
> ```
### QwenPostConfig {#QwenPostConfig}

Qwen model post config


> C++ defination code:
> ```cpp
> class QwenPostConfig
> ```

#### enable\_temperature {#enable\_temperature}

Enable temperature sampling

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool enable_temperature
> ```
#### temperature {#temperature}

Temperature sampling value

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float temperature
> ```
#### enable\_repetition\_penalty {#enable\_repetition\_penalty}

Enable repetition penalty

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool enable_repetition_penalty
> ```
#### repetition\_penalty {#repetition\_penalty}

Repetition penalty value

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float repetition_penalty
> ```
#### penalty\_window {#penalty\_window}

Repetition penalty window

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int penalty_window
> ```
#### enable\_top\_p\_sampling {#enable\_top\_p\_sampling}

Enable diversity penalty

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool enable_top_p_sampling
> ```
#### top\_p {#top\_p}

Diversity penalty value

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float top_p
> ```
#### enable\_top\_k\_sampling {#enable\_top\_k\_sampling}

Enable top k sampling

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool enable_top_k_sampling
> ```
#### top\_k {#top\_k}

Top k sampling value

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int top_k
> ```
### Qwen {#Qwen}

Qwen model


> C++ defination code:
> ```cpp
> class Qwen
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, model: str) -> None
```
Qwen constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: direction [in], model file path, model format can be MUD(model universal describe file) file.<br>If model_path set, will load model from file, load failed will raise err.Exception.<br>If model_path not set, you can load model later by load function.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Qwen(const std::string &model)
> ```
#### load {#load}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: direction [in], model file path, model format can be MUD(model universal describe file) file.<br>|
| **return** | error code, if load success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const std::string &model)
> ```
#### unload {#unload}

```python
def unload(self) -> maix.err.Err
```
Unload model

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code, if unload success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err unload()
> ```
#### loaded {#loaded}

```python
def loaded(self) -> bool
```
Is model loaded

| item | description |
| --- | --- |
| **type** | func |
| **return** | true if model loaded, else false |
| **static** | False |

> C++ defination code:
> ```cpp
> bool loaded()
> ```
#### set\_system\_prompt {#set\_system\_prompt}

```python
def set_system_prompt(self, prompt: str) -> None
```
Set system prompt, will auto call clear_context.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **prompt**: system prompt<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_system_prompt(const std::string &prompt)
> ```
#### get\_system\_prompt {#get\_system\_prompt}

```python
def get_system_prompt(self) -> str
```
Get system prompt

| item | description |
| --- | --- |
| **type** | func |
| **return** | system prompt |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string get_system_prompt()
> ```
#### set\_log\_level {#set\_log\_level}

```python
def set_log_level(self, level: ..., color: bool) -> None
```
Set log level

| item | description |
| --- | --- |
| **type** | func |
| **param** | **level**: log level, @see maix.log.LogLevel<br>**color**: true to enable color, false to disable color<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_log_level(log::LogLevel level, bool color)
> ```
#### set\_reply\_callback {#set\_reply\_callback}

```python
def set_reply_callback(self, callback: typing.Callable[[Qwen, QwenResp], None] = None) -> None
```
Set reply callback

| item | description |
| --- | --- |
| **type** | func |
| **param** | **callback**: reply callback, when token(words) generated, this function will be called,<br>so you can get response message in real time in this callback funtion.<br>If set to None(nullptr in C++), you can get response after all response message generated.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_reply_callback(std::function<void(nn::Qwen &, const nn::QwenResp &)> callback = nullptr)
> ```
#### get\_reply\_callback {#get\_reply\_callback}

```python
def get_reply_callback(self) -> typing.Callable[[Qwen, QwenResp], None]
```
Get reply callback

| item | description |
| --- | --- |
| **type** | func |
| **return** | reply callback |
| **static** | False |

> C++ defination code:
> ```cpp
> std::function<void(nn::Qwen &, const nn::QwenResp &)> get_reply_callback()
> ```
#### send {#send}

```python
def send(self, msg: str) -> QwenResp
```
Send message to model

| item | description |
| --- | --- |
| **type** | func |
| **param** | **msg**: message to send<br>|
| **return** | model response |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::QwenResp send(const std::string &msg)
> ```
#### cancel {#cancel}

```python
def cancel(self) -> None
```
Cancel running

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void cancel()
> ```
#### clear\_context {#clear\_context}

```python
def clear_context(self) -> maix.err.Err
```
Clear context

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code, if clear success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err clear_context()
> ```
#### version {#version}

```python
def version(self) -> str
```
Get model version

| item | description |
| --- | --- |
| **type** | func |
| **return** | model version |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string version()
> ```
#### post\_config {#post\_config}

Qwen post config, default will read config from model mud file, you can also set it manually here.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> nn::QwenPostConfig post_config
> ```
### InternVLResp {#InternVLResp}

InternVL model response


> C++ defination code:
> ```cpp
> class InternVLResp
> ```

#### msg {#msg-2}

Model response full message.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string msg
> ```
#### msg\_new {#msg\_new-2}

Model response new message.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string msg_new
> ```
#### err\_code {#err\_code-2}

Model response error code, maix.Err type, should be err.Err.ERR_NONE if no error.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> err::Err err_code
> ```
#### err\_msg {#err\_msg-2}

Model response error message.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string err_msg
> ```
### InternVLPostConfig {#InternVLPostConfig}

InternVL model post config


> C++ defination code:
> ```cpp
> class InternVLPostConfig
> ```

#### enable\_temperature {#enable\_temperature-2}

Enable temperature sampling

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool enable_temperature
> ```
#### temperature {#temperature-2}

Temperature sampling value

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float temperature
> ```
#### enable\_repetition\_penalty {#enable\_repetition\_penalty-2}

Enable repetition penalty

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool enable_repetition_penalty
> ```
#### repetition\_penalty {#repetition\_penalty-2}

Repetition penalty value

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float repetition_penalty
> ```
#### penalty\_window {#penalty\_window-2}

Repetition penalty window

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int penalty_window
> ```
#### enable\_top\_p\_sampling {#enable\_top\_p\_sampling-2}

Enable diversity penalty

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool enable_top_p_sampling
> ```
#### top\_p {#top\_p-2}

Diversity penalty value

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float top_p
> ```
#### enable\_top\_k\_sampling {#enable\_top\_k\_sampling-2}

Enable top k sampling

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool enable_top_k_sampling
> ```
#### top\_k {#top\_k-2}

Top k sampling value

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int top_k
> ```
### InternVL {#InternVL}

InternVL model


> C++ defination code:
> ```cpp
> class InternVL
> ```

#### \_\_init\_\_ {#\_\_init\_\_-2}

```python
def __init__(self, model: str) -> None
```
InternVL constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: direction [in], model file path, model format can be MUD(model universal describe file) file.<br>If model_path set, will load model from file, load failed will raise err.Exception.<br>If model_path not set, you can load model later by load function.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> InternVL(const std::string &model)
> ```
#### load {#load-2}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: direction [in], model file path, model format can be MUD(model universal describe file) file.<br>|
| **return** | error code, if load success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const std::string &model)
> ```
#### unload {#unload-2}

```python
def unload(self) -> maix.err.Err
```
Unload model

| item | description |
| --- | --- |
| **type** | func |
| **return** | error code, if unload success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err unload()
> ```
#### loaded {#loaded-2}

```python
def loaded(self) -> bool
```
Is model loaded

| item | description |
| --- | --- |
| **type** | func |
| **return** | true if model loaded, else false |
| **static** | False |

> C++ defination code:
> ```cpp
> bool loaded()
> ```
#### set\_system\_prompt {#set\_system\_prompt-2}

```python
def set_system_prompt(self, prompt: str) -> None
```
Set system prompt

| item | description |
| --- | --- |
| **type** | func |
| **param** | **prompt**: system prompt<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_system_prompt(const std::string &prompt)
> ```
#### get\_system\_prompt {#get\_system\_prompt-2}

```python
def get_system_prompt(self) -> str
```
Get system prompt

| item | description |
| --- | --- |
| **type** | func |
| **return** | system prompt |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string get_system_prompt()
> ```
#### set\_log\_level {#set\_log\_level-2}

```python
def set_log_level(self, level: ..., color: bool) -> None
```
Set log level

| item | description |
| --- | --- |
| **type** | func |
| **param** | **level**: log level, @see maix.log.LogLevel<br>**color**: true to enable color, false to disable color<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_log_level(log::LogLevel level, bool color)
> ```
#### set\_reply\_callback {#set\_reply\_callback-2}

```python
def set_reply_callback(self, callback: typing.Callable[[InternVL, InternVLResp], None] = None) -> None
```
Set reply callback.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **callback**: reply callback, when token(words) generated, this function will be called,<br>so you can get response message in real time in this callback funtion.<br>If set to None(nullptr in C++), you can get response after all response message generated.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_reply_callback(std::function<void(nn::InternVL &, const nn::InternVLResp &)> callback = nullptr)
> ```
#### get\_reply\_callback {#get\_reply\_callback-2}

```python
def get_reply_callback(self) -> typing.Callable[[InternVL, InternVLResp], None]
```
Get reply callback

| item | description |
| --- | --- |
| **type** | func |
| **return** | reply callback |
| **static** | False |

> C++ defination code:
> ```cpp
> std::function<void(nn::InternVL &, const nn::InternVLResp &)> get_reply_callback()
> ```
#### input\_width {#input\_width}

```python
def input_width(self) -> int
```
Image input width

| item | description |
| --- | --- |
| **type** | func |
| **return** | input width. |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height}

```python
def input_height(self) -> int
```
Image input height

| item | description |
| --- | --- |
| **type** | func |
| **return** | input height. |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format}

```python
def input_format(self) -> maix.image.Format
```
Image input format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input format. |
| **static** | False |

> C++ defination code:
> ```cpp
> maix::image::Format input_format()
> ```
#### set\_image {#set\_image}

```python
def set_image(self, img: maix.image.Image, fit: maix.image.Fit = ...) -> maix.err.Err
```
Set image and will encode image.\nYou can set image once and call send multiple times.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: the image you want to use.<br>**fit**: Image resize fit method, only used when img size not equal to model input.<br>|
| **return** | err.Err return err.Err.ERR_NONE is no error happen. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_image(maix::image::Image &img, maix::image::Fit fit = maix::image::Fit::FIT_CONTAIN)
> ```
#### clear\_image {#clear\_image}

```python
def clear_image(self) -> None
```
Clear image, InternVL2.5 based on Qwen2.5, so you can clear image and only use LLM function.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void clear_image()
> ```
#### is\_image\_set {#is\_image\_set}

```python
def is_image_set(self) -> bool
```
Whether image set by set_image

| item | description |
| --- | --- |
| **type** | func |
| **return** | Return true if image set by set_image function, or return false. |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_image_set()
> ```
#### send {#send-2}

```python
def send(self, msg: str) -> InternVLResp
```
Send message to model

| item | description |
| --- | --- |
| **type** | func |
| **param** | **msg**: message to send<br>|
| **return** | model response |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::InternVLResp send(const std::string &msg)
> ```
#### cancel {#cancel-2}

```python
def cancel(self) -> None
```
Cancel running

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void cancel()
> ```
#### version {#version-2}

```python
def version(self) -> str
```
Get model version

| item | description |
| --- | --- |
| **type** | func |
| **return** | model version |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string version()
> ```
#### post\_config {#post\_config-2}

InternVL post config, default will read config from model mud file, you can also set it manually here.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> nn::InternVLPostConfig post_config
> ```
### DepthAnything {#DepthAnything}

DepthAnything


> C++ defination code:
> ```cpp
> class DepthAnything
> ```

#### \_\_init\_\_ {#\_\_init\_\_-3}

```python
def __init__(self, model: str = '', dual_buff: bool = True) -> None
```
Construct a new DepthAnything object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: MUD model path, if empty, will not load model, you can call load() later.<br>if not empty, will load model and will raise err::Exception if load failed.<br>**dual_buff**: direction [in], prepare dual input output buffer to accelarate forward, that is, when NPU is forwarding we not wait and prepare the next input buff.<br>If you want to ensure every time forward output the input's result, set this arg to false please.<br>Default true to ensure speed.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> DepthAnything(const string &model = "", bool dual_buff = true)
> ```
#### load {#load-3}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file, model format is .mud,\nMUD file should contain [extra] section, have key-values:\n- model_type: depth_anything_v2\n- input_type: rgb or bgr\n- mean: 123.675, 116.28, 103.53\n- scale: 0.017124753831663668, 0.01750700280112045, 0.017429193899782137\n- labels: imagenet_classes.txt

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: MUD model path<br>|
| **return** | error code, if load failed, return error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### get\_depth {#get\_depth}

```python
def get_depth(self, img: maix.image.Image, fit: maix.image.Fit = ...) -> maix.tensor.Tensor
```
Forward model and get raw image depth estimation data.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image, format should match model input_type， or will raise err.Exception<br>**fit**: image resize fit mode if input image not equal to model' input size,<br>will auto resize to model's input size then detect, and recover to image input size.<br>Default Fit.FIT_CONTAIN, see image.Fit.<br>|
| **throw** | If error occurred, will raise err::Exception, you can find reason in log, mostly caused by args error or hardware error. |
| **return** | result, a tensor.Tensor object. If in dual_buff mode, value can be None(in Python) or nullptr(in C++) when not ready. In C++, you need to delete it after use. |
| **static** | False |

> C++ defination code:
> ```cpp
> tensor::Tensor *get_depth(image::Image &img, image::Fit fit = image::FIT_CONTAIN)
> ```
#### get\_depth\_image {#get\_depth\_image}

```python
def get_depth_image(self, img: maix.image.Image, fit: maix.image.Fit = ..., cmap: maix.image.CMap = ...) -> maix.image.Image
```
Forward model and get image depth estimation data normlized to [0, 255] and as a image.Image object.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image, format should match model input_type， or will raise err.Exception<br>**fit**: image resize fit mode if input image not equal to model' input size,<br>will auto resize to model's input size then detect, and recover to image input size.<br>Default Fit.FIT_CONTAIN, see image.Fit.<br>**cmap**: Color map used convert grayscale distance estimation image to RGB image.<br>Diiferent cmap will influence finally image.<br>Default image.CMap.INFERNO.<br>|
| **throw** | If error occurred, will raise err::Exception, you can find reason in log, mostly caused by args error or hardware error. |
| **return** | result, a image::Image object. If in dual_buff mode, value can be None(in Python) or nullptr(in C++) when not ready. In C++, you need to delete it after use. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *get_depth_image(image::Image &img, image::Fit fit = image::FIT_CONTAIN, image::CMap cmap = image::CMap::INFERNO)
> ```
#### input\_size {#input\_size}

```python
def input_size(self) -> maix.image.Size
```
Get model input size, only for image input

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-2}

```python
def input_width(self) -> int
```
Get model input width, only for image input

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-2}

```python
def input_height(self) -> int
```
Get model input height, only for image input

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-2}

```python
def input_format(self) -> maix.image.Format
```
Get input image format, only for image input

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### input\_shape {#input\_shape}

```python
def input_shape(self) -> list[int]
```
Get input shape, if have multiple input, only return first input shape

| item | description |
| --- | --- |
| **type** | func |
| **return** | input shape, list type |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> input_shape()
> ```
#### mean {#mean}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
### MixFormerV2 {#MixFormerV2}

MixFormerV2 class


> C++ defination code:
> ```cpp
> class MixFormerV2
> ```

#### \_\_init\_\_ {#\_\_init\_\_-4}

```python
def __init__(self, model: str = '', update_interval: int = 200, lost_find_interval: int = 60) -> None
```
Constructor of MixFormerV2 class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>**update_interval**: update online template interval in framsed, default 200 frames<br>**lost_find_interval**: auto find lose target in global after lose target lost_find_interval frames, -1 means not use.<br>In some scene, this is useful to get back target, but if always find wrong target after target lost, you should disable this.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> MixFormerV2(const string &model = "", int update_interval = 200, int lost_find_interval = 60)
> ```
#### load {#load-4}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### init {#init}

```python
def init(self, img: maix.image.Image, x: int, y: int, w: int, h: int) -> None
```
Init tracker, give tacker first target image and target position.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Image want to detect, target should be in this image.<br>**x**: the target position left top coordinate x.<br>**y**: the target position left top coordinate y.<br>**w**: the target width.<br>**h**: the target height.<br>|
| **throw** | If image format not match model input format, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> void init(image::Image &img, int x, int y, int w, int h)
> ```
#### track {#track}

```python
def track(self, img: maix.image.Image, threshold: float = 0.5) -> ...
```
Track object acoording to last object position and the init function learned target feature.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image to detect object and track, can be any resolution, before detect it will crop a area according to last time target's position.<br>**threshold**: If score < threshold, will see this new detection is invalid, but remain return this new detecion,  default 0.9.<br>|
| **return** | object, attribute [x, y, w, h] and score are the predict target position and score, points attribute provide more info:<br>0~3  [ search_x, search_y, search_w, search_h ]: search area for this time track, based on last correct start position.<br>4~5  [ predict_cx, predict_cy]: predict center according to this time input.<br>6    [ search_size ]: search_area size based on last correct start position, center is (search_x - search_w / 2, search_y - search_h / 2).<br>7    [ predict_template_size ]: template size based on predict target, center is (predict_cx, predict_cy).<br>8~11 [ correct_cx, correct_cy, correct_w, correct_h]: latest correct (score > threshold) target position. |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::Object track(image::Image &img, float threshold = 0.5)
> ```
#### input\_size {#input\_size-2}

```python
def input_size(self) -> maix.image.Size
```
Get model input size

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-3}

```python
def input_width(self) -> int
```
Get model input width

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-3}

```python
def input_height(self) -> int
```
Get model input height

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-3}

```python
def input_format(self) -> maix.image.Format
```
Get input image format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### mean {#mean-2}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-2}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
#### frame\_id {#frame\_id}

Current frame_id

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint64_t frame_id
> ```
#### update\_interval {#update\_interval}

update online template interval in frames

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int update_interval
> ```
#### lost\_find\_interval {#lost\_find\_interval}

Auto find target after lost lost_find_interval frames, -1 means not auto find.\nIn some scene, this is useful to get back target, but if always find wrong target after target lost, you should disable this.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int lost_find_interval
> ```
### SelfLearnClassifier {#SelfLearnClassifier}

SelfLearnClassifier


> C++ defination code:
> ```cpp
> class SelfLearnClassifier
> ```

#### \_\_init\_\_ {#\_\_init\_\_-5}

```python
def __init__(self, model: str = '', dual_buff: bool = True) -> None
```
Construct a new SelfLearnClassifier object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: MUD model path, if empty, will not load model, you can call load_model() later.<br>if not empty, will load model and will raise err::Exception if load failed.<br>**dual_buff**: direction [in], prepare dual input output buffer to accelarate forward, that is, when NPU is forwarding we not wait and prepare the next input buff.<br>If you want to ensure every time forward output the input's result, set this arg to false please.<br>Default true to ensure speed.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> SelfLearnClassifier(const std::string &model = "", bool dual_buff = true)
> ```
#### load\_model {#load\_model}

```python
def load_model(self, model: str) -> maix.err.Err
```
Load model from file, model format is .mud,\nMUD file should contain [extra] section, have key-values:\n- model_type: classifier_no_top\n- input_type: rgb or bgr\n- mean: 123.675, 116.28, 103.53\n- scale: 0.017124753831663668, 0.01750700280112045, 0.017429193899782137

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: MUD model path<br>|
| **return** | error code, if load failed, return error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load_model(const string &model)
> ```
#### classify {#classify}

```python
def classify(self, img: maix.image.Image, fit: maix.image.Fit = ...) -> list[tuple[int, float]]
```
Classify image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image, format should match model input_type， or will raise err.Exception<br>**fit**: image resize fit mode, default Fit.FIT_COVER, see image.Fit.<br>|
| **throw** | If error occurred, will raise err::Exception, you can find reason in log, mostly caused by args error or hardware error. |
| **return** | result, a list of (idx, distance), smaller distance means more similar. In C++, you need to delete it after use. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::pair<int, float>> *classify(image::Image &img, image::Fit fit = image::FIT_COVER)
> ```
#### add\_class {#add\_class}

```python
def add_class(self, img: maix.image.Image, fit: maix.image.Fit = ...) -> None
```
Add a class to recognize

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Add a image as a new class<br>**fit**: image resize fit mode, default Fit.FIT_COVER, see image.Fit.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void add_class(image::Image &img, image::Fit fit = image::FIT_COVER)
> ```
#### class\_num {#class\_num}

```python
def class_num(self) -> int
```
Get class number

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int class_num()
> ```
#### rm\_class {#rm\_class}

```python
def rm_class(self, idx: int) -> maix.err.Err
```
Remove a class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **idx**: index, value from 0 to class_num();<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err rm_class(int idx)
> ```
#### add\_sample {#add\_sample}

```python
def add_sample(self, img: maix.image.Image, fit: maix.image.Fit = ...) -> None
```
Add sample, you should call learn method after add some samples to learn classes.\nSample image can be any of classes we already added.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Add a image as a new sample.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void add_sample(image::Image &img, image::Fit fit = image::FIT_COVER)
> ```
#### rm\_sample {#rm\_sample}

```python
def rm_sample(self, idx: int) -> maix.err.Err
```
Remove a sample

| item | description |
| --- | --- |
| **type** | func |
| **param** | **idx**: index, value from 0 to sample_num();<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err rm_sample(int idx)
> ```
#### sample\_num {#sample\_num}

```python
def sample_num(self) -> int
```
Get sample number

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int sample_num()
> ```
#### learn {#learn}

```python
def learn(self) -> int
```
Start auto learn class features from classes image and samples.\nYou should call this method after you add some samples.

| item | description |
| --- | --- |
| **type** | func |
| **return** | learn epoch(times), 0 means learn nothing. |
| **static** | False |

> C++ defination code:
> ```cpp
> int learn()
> ```
#### clear {#clear}

```python
def clear(self) -> None
```
Clear all class and samples

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void clear()
> ```
#### input\_size {#input\_size-3}

```python
def input_size(self) -> maix.image.Size
```
Get model input size, only for image input

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-4}

```python
def input_width(self) -> int
```
Get model input width, only for image input

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-4}

```python
def input_height(self) -> int
```
Get model input height, only for image input

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-4}

```python
def input_format(self) -> maix.image.Format
```
Get input image format, only for image input

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### input\_shape {#input\_shape-2}

```python
def input_shape(self) -> list[int]
```
Get input shape, if have multiple input, only return first input shape

| item | description |
| --- | --- |
| **type** | func |
| **return** | input shape, list type |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> input_shape()
> ```
#### save {#save}

```python
def save(self, path: str, labels: list[str] = []) -> maix.err.Err
```
Save features and labels to a binary file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **path**: file path to save, e.g. /root/my_classes.bin<br>**labels**: class labels, can be None, or length must equal to class num, or will return err::Err<br>|
| **return** | maix.err.Err if labels exists but length not equal to class num, or save file failed, or class num is 0. |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err save(const std::string &path, const std::vector<std::string> &labels = std::vector<std::string>())
> ```
#### load {#load-5}

```python
def load(self, path: str) -> list[str]
```
Load features info from binary file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **path**: feature info binary file path, e.g. /root/my_classes.bin<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::string> load(const std::string &path)
> ```
#### labels {#labels}

Labels list

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<string> labels
> ```
#### label\_path {#label\_path}

Label file path

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string label_path
> ```
#### mean {#mean-3}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-3}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
### YOLO11 {#YOLO11}

YOLO11 class


> C++ defination code:
> ```cpp
> class YOLO11
> ```

#### \_\_init\_\_ {#\_\_init\_\_-6}

```python
def __init__(self, model: str = '', dual_buff: bool = True) -> None
```
Constructor of YOLO11 class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>**dual_buff**: direction [in], prepare dual input output buffer to accelarate forward, that is, when NPU is forwarding we not wait and prepare the next input buff.<br>If you want to ensure every time forward output the input's result, set this arg to false please.<br>Default true to ensure speed.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> YOLO11(const string &model = "", bool dual_buff = true)
> ```
#### load {#load-6}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### detect {#detect}

```python
def detect(self, img: maix.image.Image, conf_th: float = 0.5, iou_th: float = 0.45, fit: maix.image.Fit = ..., keypoint_th: float = 0.5, sort: int = 0) -> ...
```
Detect objects from image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Image want to detect, if image's size not match model input's, will auto resize with fit method.<br>**conf_th**: Confidence threshold, default 0.5.<br>**iou_th**: IoU threshold, default 0.45.<br>**fit**: Resize method, default image.Fit.FIT_CONTAIN.<br>**keypoint_th**: keypoint threshold, default 0.5, only for yolo11-pose model.<br>**sort**: sort result according to object size, default 0 means not sort, 1 means bigger in front, -1 means smaller in front.<br>|
| **throw** | If image format not match model input format, will throw err::Exception. |
| **return** | Object list. In C++, you should delete it after use.<br>If model is yolo11-pose, object's points have value, and if points' value < 0 means that point is invalid(conf < keypoint_th). |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::Objects *detect(image::Image &img, float conf_th = 0.5, float iou_th = 0.45, maix::image::Fit fit = maix::image::FIT_CONTAIN, float keypoint_th = 0.5, int sort = 0)
> ```
#### input\_size {#input\_size-4}

```python
def input_size(self) -> maix.image.Size
```
Get model input size

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-5}

```python
def input_width(self) -> int
```
Get model input width

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-5}

```python
def input_height(self) -> int
```
Get model input height

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-5}

```python
def input_format(self) -> maix.image.Format
```
Get input image format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### draw\_pose {#draw\_pose}

```python
def draw_pose(self, img: maix.image.Image, points: list[int], radius: int = 4, color: maix.image.Color = ..., colors: list[maix.image.Color] = [], body: bool = True, close: bool = False) -> None
```
Draw pose keypoints on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image object, maix.image.Image type.<br>**points**: keypoits, int list type, [x, y, x, y ...]<br>**radius**: radius of points.<br>**color**: color of points.<br>**colors**: assign colors for points, list type, element is image.Color object.<br>**body**: true, if points' length is 17*2 and body is ture, will draw lines as human body, if set to false won't draw lines, default true.<br>**close**: connect all points to close a polygon, default false.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void draw_pose(image::Image &img, std::vector<int> points, int radius = 4, image::Color color = image::COLOR_RED, const std::vector<image::Color> &colors = std::vector<image::Color>(), bool body = true, bool close = false)
> ```
#### draw\_seg\_mask {#draw\_seg\_mask}

```python
def draw_seg_mask(self, img: maix.image.Image, x: int, y: int, seg_mask: maix.image.Image, threshold: int = 127) -> None
```
Draw segmentation on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image object, maix.image.Image type.<br>**seg_mask**: segmentation mask image by detect method, a grayscale image<br>**threshold**: only mask's value > threshold will be draw on image, value from 0 to 255.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void draw_seg_mask(image::Image &img, int x, int y, image::Image &seg_mask, int threshold = 127)
> ```
#### labels {#labels-2}

Labels list

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<string> labels
> ```
#### label\_path {#label\_path-2}

Label file path

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string label_path
> ```
#### mean {#mean-4}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-4}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
### Retinaface {#Retinaface}

Retinaface class


> C++ defination code:
> ```cpp
> class Retinaface
> ```

#### \_\_init\_\_ {#\_\_init\_\_-7}

```python
def __init__(self, model: str = '', dual_buff: bool = True) -> None
```
Constructor of Retinaface class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>**dual_buff**: direction [in], prepare dual input output buffer to accelarate forward, that is, when NPU is forwarding we not wait and prepare the next input buff.<br>If you want to ensure every time forward output the input's result, set this arg to false please.<br>Default true to ensure speed.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> Retinaface(const string &model = "", bool dual_buff = true)
> ```
#### load {#load-7}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### detect {#detect-2}

```python
def detect(self, img: maix.image.Image, conf_th: float = 0.4, iou_th: float = 0.45, fit: maix.image.Fit = ...) -> list[...]
```
Detect objects from image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Image want to detect, if image's size not match model input's, will auto resize with fit method.<br>**conf_th**: Confidence threshold, default 0.4.<br>**iou_th**: IoU threshold, default 0.45.<br>**fit**: Resize method, default image.Fit.FIT_CONTAIN.<br>|
| **throw** | If image format not match model input format, will throw err::Exception. |
| **return** | Object list. In C++, you should delete it after use. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<nn::Object> *detect(image::Image &img, float conf_th = 0.4, float iou_th = 0.45, maix::image::Fit fit = maix::image::FIT_CONTAIN)
> ```
#### input\_size {#input\_size-5}

```python
def input_size(self) -> maix.image.Size
```
Get model input size

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-6}

```python
def input_width(self) -> int
```
Get model input width

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-6}

```python
def input_height(self) -> int
```
Get model input height

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-6}

```python
def input_format(self) -> maix.image.Format
```
Get input image format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### mean {#mean-5}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-5}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
### Object {#Object}

Object for detect result


> C++ defination code:
> ```cpp
> class Object
> ```

#### \_\_init\_\_ {#\_\_init\_\_-8}

```python
def __init__(self, x: int = 0, y: int = 0, w: int = 0, h: int = 0, class_id: int = 0, score: float = 0, points: list[int] = [], angle: float = -9999) -> None
```
Constructor of Object for detect result

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: left top x<br>**y**: left top y<br>**w**: width<br>**h**: height<br>**class_id**: class id<br>**score**: score<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Object(int x = 0, int y = 0, int w = 0, int h = 0, int class_id = 0, float score = 0, std::vector<int> points = std::vector<int>(), float angle = -9999)
> ```
#### \_\_str\_\_ {#\_\_str\_\_}

```python
def __str__(self) -> str
```
Object info to string

| item | description |
| --- | --- |
| **type** | func |
| **return** | Object info string |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string to_str()
> ```
#### get\_obb\_points {#get\_obb\_points}

```python
def get_obb_points(self) -> list[int]
```
Get OBB(oriented bounding box) points, auto calculated according to x,y,w,h,angle

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> get_obb_points()
> ```
#### x {#x}

Object left top coordinate x

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

Object left top coordinate y

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

Object width

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

Object height

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

Object class id

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

Object score

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float score
> ```
#### points {#points}

keypoints

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<int> points
> ```
#### angle {#angle}

Rotate angle, -9999 means not set, value is a percentage, need to multiply 180 to get the real angle or multiply PI to get the radian.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float angle
> ```
#### seg\_mask {#seg\_mask}

segmentation mask, uint8 list type, shape is h * w but flattened to one dimension, value fron 0 to 255.

| item | description |
| --- | --- |
| **type** | var |
| **attention** | For efficiency, it's a pointer in C++, use this carefully! |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> image::Image *seg_mask
> ```
### ObjectFloat {#ObjectFloat}

Object for detect result


> C++ defination code:
> ```cpp
> class ObjectFloat
> ```

#### \_\_init\_\_ {#\_\_init\_\_-9}

```python
def __init__(self, x: float = 0, y: float = 0, w: float = 0, h: float = 0, class_id: float = 0, score: float = 0, points: list[float] = [], angle: float = -1) -> None
```
Constructor of Object for detect result

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: left top x<br>**y**: left top y<br>**w**: width<br>**h**: height<br>**class_id**: class id<br>**score**: score<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> ObjectFloat(float x = 0, float y = 0, float w = 0, float h = 0, float class_id = 0, float score = 0, std::vector<float> points = std::vector<float>(), float angle = -1)
> ```
#### \_\_str\_\_ {#\_\_str\_\_-2}

```python
def __str__(self) -> str
```
Object info to string

| item | description |
| --- | --- |
| **type** | func |
| **return** | Object info string |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string to_str()
> ```
#### x {#x-2}

Object left top coordinate x

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float x
> ```
#### y {#y-2}

Object left top coordinate y

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float y
> ```
#### w {#w-2}

Object width

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float w
> ```
#### h {#h-2}

Object height

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float h
> ```
#### class\_id {#class\_id-2}

Object class id

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float class_id
> ```
#### score {#score-2}

Object score

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float score
> ```
#### points {#points-2}

keypoints

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> points
> ```
#### angle {#angle-2}

Rotate angle

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float angle
> ```
### Objects {#Objects}

Objects Class for detect result


> C++ defination code:
> ```cpp
> class Objects
> ```

#### \_\_init\_\_ {#\_\_init\_\_-10}

```python
def __init__(self) -> None
```
Constructor of Objects class

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> Objects()
> ```
#### add {#add}

```python
def add(self, x: int = 0, y: int = 0, w: int = 0, h: int = 0, class_id: int = 0, score: float = 0, points: list[int] = [], angle: float = -1) -> Object
```
Add object to objects

| item | description |
| --- | --- |
| **type** | func |
| **throw** | Throw exception if no memory |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::Object &add(int x = 0, int y = 0, int w = 0, int h = 0, int class_id = 0, float score = 0, std::vector<int> points = std::vector<int>(), float angle = -1)
> ```
#### remove {#remove}

```python
def remove(self, idx: int) -> maix.err.Err
```
Remove object form objects

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err remove(int idx)
> ```
#### at {#at}

```python
def at(self, idx: int) -> Object
```
Get object item

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::Object &at(int idx)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_}

```python
def __getitem__(self, idx: int) -> Object
```
Get object item

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::Object &operator[](int idx)
> ```
#### \_\_len\_\_ {#\_\_len\_\_}

```python
def __len__(self) -> int
```
Get size

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> size_t size()
> ```
#### \_\_iter\_\_ {#\_\_iter\_\_}

```python
def __iter__(self) -> typing.Iterator
```
Begin

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<Object*>::iterator begin()
> ```
### FaceDetector {#FaceDetector}

FaceDetector class


> C++ defination code:
> ```cpp
> class FaceDetector
> ```

#### \_\_init\_\_ {#\_\_init\_\_-11}

```python
def __init__(self, model: str = '', dual_buff: bool = True) -> None
```
Constructor of FaceDetector class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>**dual_buff**: direction [in], prepare dual input output buffer to accelarate forward, that is, when NPU is forwarding we not wait and prepare the next input buff.<br>If you want to ensure every time forward output the input's result, set this arg to false please.<br>Default true to ensure speed.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> FaceDetector(const string &model = "", bool dual_buff = true)
> ```
#### load {#load-8}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### detect {#detect-3}

```python
def detect(self, img: maix.image.Image, conf_th: float = 0.5, iou_th: float = 0.45, fit: maix.image.Fit = ...) -> list[Object]
```
Detect objects from image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Image want to detect, if image's size not match model input's, will auto resize with fit method.<br>**conf_th**: Confidence threshold, default 0.5.<br>**iou_th**: IoU threshold, default 0.45.<br>**fit**: Resize method, default image.Fit.FIT_CONTAIN.<br>|
| **throw** | If image format not match model input format, will throw err::Exception. |
| **return** | Object list. In C++, you should delete it after use. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<nn::Object> *detect(image::Image &img, float conf_th = 0.5, float iou_th = 0.45, maix::image::Fit fit = maix::image::FIT_CONTAIN)
> ```
#### input\_size {#input\_size-6}

```python
def input_size(self) -> maix.image.Size
```
Get model input size

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-7}

```python
def input_width(self) -> int
```
Get model input width

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-7}

```python
def input_height(self) -> int
```
Get model input height

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-7}

```python
def input_format(self) -> maix.image.Format
```
Get input image format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### mean {#mean-6}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-6}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
### OCR\_Box {#OCR\_Box}

Object for OCR detect box


> C++ defination code:
> ```cpp
> class OCR_Box
> ```

#### \_\_init\_\_ {#\_\_init\_\_-12}

```python
def __init__(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0, x3: int = 0, y3: int = 0, x4: int = 0, y4: int = 0) -> None
```
OCR_Box constructor

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> OCR_Box(int x1 = 0, int y1 = 0, int x2 = 0, int y2 = 0, int x3 = 0, int y3 = 0, int x4 = 0, int y4 = 0)
> ```
#### x1 {#x1}

left top point of box

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int x1
> ```
#### y1 {#y1}

left top point of box

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int y1
> ```
#### x2 {#x2}

right top point of box

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int x2
> ```
#### y2 {#y2}

right top point of box

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int y2
> ```
#### x3 {#x3}

right bottom point of box

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int x3
> ```
#### y3 {#y3}

right bottom point of box

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int y3
> ```
#### x4 {#x4}

left bottom point of box

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int x4
> ```
#### y4 {#y4}

left bottom point of box

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int y4
> ```
#### to\_list {#to\_list}

```python
def to_list(self) -> list[int]
```
convert box point to a list type.

| item | description |
| --- | --- |
| **type** | func |
| **return** | list type, element is int type, value [x1, y1, x2, y2, x3, y3, x4, y4]. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> to_list()
> ```
### OCR\_Object {#OCR\_Object}

Object for OCR detect result


> C++ defination code:
> ```cpp
> class OCR_Object
> ```

#### \_\_init\_\_ {#\_\_init\_\_-13}

```python
def __init__(self, box: OCR_Box, idx_list: list[int], char_list: list[str], score: float = 0, char_pos: list[int] = []) -> None
```
Constructor of Object for OCR detect result

| item | description |
| --- | --- |
| **type** | func |
| **param** | **score**: score<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> OCR_Object(const nn::OCR_Box &box, const std::vector<int> &idx_list, const std::vector<std::string> &char_list, float score = 0, const std::vector<int> &char_pos = std::vector<int>())
> ```
#### box {#box}

OCR_Object box, 4 points box, first point at the left-top, clock-wise.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> nn::OCR_Box box
> ```
#### score {#score-3}

Object score

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float score
> ```
#### idx\_list {#idx\_list}

chars' idx list, element is int type.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<int> idx_list
> ```
#### char\_pos {#char\_pos}

Chars' position relative to left

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<int> char_pos
> ```
#### char\_str {#char\_str}

```python
def char_str(self) -> str
```
Get OCR_Object's charactors, return a string type.

| item | description |
| --- | --- |
| **type** | func |
| **return** | All charactors in string type. |
| **static** | False |

> C++ defination code:
> ```cpp
> const std::string &char_str()
> ```
#### char\_list {#char\_list}

```python
def char_list(self) -> list[str]
```
Get OCR_Object's charactors, return a list type.

| item | description |
| --- | --- |
| **type** | func |
| **return** | All charactors in list type. |
| **static** | False |

> C++ defination code:
> ```cpp
> const std::vector<std::string> &char_list()
> ```
#### update\_chars {#update\_chars}

```python
def update_chars(self, char_list: list[str]) -> None
```
Set OCR_Object's charactors

| item | description |
| --- | --- |
| **type** | func |
| **param** | **char_list**: All charactors in list type.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void update_chars(const std::vector<std::string> &char_list)
> ```
#### \_\_str\_\_ {#\_\_str\_\_-3}

```python
def __str__(self) -> str
```
OCR_Object info to string

| item | description |
| --- | --- |
| **type** | func |
| **return** | OCR_Object info string |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string to_str()
> ```
### OCR\_Objects {#OCR\_Objects}

OCR_Objects Class for detect result


> C++ defination code:
> ```cpp
> class OCR_Objects
> ```

#### \_\_init\_\_ {#\_\_init\_\_-14}

```python
def __init__(self) -> None
```
Constructor of OCR_Objects class

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> OCR_Objects()
> ```
#### add {#add-2}

```python
def add(self, box: OCR_Box, idx_list: list[int], char_list: list[str], score: float = 0, char_pos: list[int] = []) -> OCR_Object
```
Add object to objects

| item | description |
| --- | --- |
| **type** | func |
| **throw** | Throw exception if no memory |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::OCR_Object &add(const nn::OCR_Box &box, const std::vector<int> &idx_list, const std::vector<std::string> &char_list, float score = 0, const std::vector<int> &char_pos = std::vector<int>())
> ```
#### remove {#remove-2}

```python
def remove(self, idx: int) -> maix.err.Err
```
Remove object form objects

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err remove(int idx)
> ```
#### at {#at-2}

```python
def at(self, idx: int) -> OCR_Object
```
Get object item

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::OCR_Object &at(int idx)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-2}

```python
def __getitem__(self, idx: int) -> OCR_Object
```
Get object item

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::OCR_Object &operator[](int idx)
> ```
#### \_\_len\_\_ {#\_\_len\_\_-2}

```python
def __len__(self) -> int
```
Get size

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> size_t size()
> ```
#### \_\_iter\_\_ {#\_\_iter\_\_-2}

```python
def __iter__(self) -> typing.Iterator
```
Begin

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<OCR_Object*>::iterator begin()
> ```
### MeloTTS {#MeloTTS}

MeloTTS class


> C++ defination code:
> ```cpp
> class MeloTTS
> ```

#### \_\_init\_\_ {#\_\_init\_\_-15}

```python
def __init__(self, model: str = '', language: str = 'zh', speed: float = 0.800000011920929, noise_scale: float = 0.30000001192092896, noise_scale_w: float = 0.6000000238418579, sdp_ratio: float = 0.20000000298023224) -> None
```
Constructor of MeloTTS class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>**language**: language code, default "zh", supported language code: "zh"<br>**speed**: the speech rate of the audio is controlled by this value,lower values result in slower reading speed. default is 0.8<br>**noise_scale**: this parameter controls the randomness in speech. increasing the value results in more varied and less deterministic speech output.default is 0.3<br>**noise_scale_w**: this parameter controls the randomness in speech alignment. while a higher value can enhance naturalness, overly high values may introduce instability or distortion in the audio. default is 0.6<br>**sdp_ratio**: the higher the alignment weight, the more natural the speech sounds, but excessive values may result in instability. default is 0.2<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> MeloTTS(const string &model = "", std::string language = "zh", double speed = 0.8f, double noise_scale = 0.3f, double noise_scale_w = 0.6f, double sdp_ratio = 0.2f)
> ```
#### load {#load-9}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### infer {#infer}

```python
def infer(*args, **kwargs)
```
Text to speech

| item | description |
| --- | --- |
| **type** | func |
| **param** | **text**: input text<br>**path**: The output path of the voice file, the default sampling rate is 44100,<br>the number of channels is 1, and the number of sampling bits is 16. default is empty.<br>**output_pcm**: Enable or disable the output of raw PCM data. The default output sampling rate is 44100,<br>the number of channels is 1, and the sampling depth is 16 bits. default is false.<br>|
| **return** | raw PCM data |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *infer(std::string text, std::string path = "", bool output_pcm = false)
> ```
#### samplerate {#samplerate}

```python
def samplerate(self) -> int
```
Get pcm samplerate

| item | description |
| --- | --- |
| **type** | func |
| **return** | pcm samplerate |
| **static** | False |

> C++ defination code:
> ```cpp
> int samplerate()
> ```
#### speed {#speed}

```python
def speed(self) -> float
```
Get the speed of the text

| item | description |
| --- | --- |
| **type** | func |
| **return** | text speed |
| **static** | False |

> C++ defination code:
> ```cpp
> double speed()
> ```
### Whisper {#Whisper}

Whiper class


> C++ defination code:
> ```cpp
> class Whisper
> ```

#### \_\_init\_\_ {#\_\_init\_\_-16}

```python
def __init__(self, model: str = '', language: str = 'zh') -> None
```
Constructor of Whisper class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>**language**: language code, default "zh", supported language code: "zh", "en"<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> Whisper(const string &model = "", std::string language = "zh")
> ```
#### load {#load-10}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### transcribe {#transcribe}

```python
def transcribe(self, file: str) -> str
```
Transcribe audio file to text

| item | description |
| --- | --- |
| **type** | func |
| **note** | If the wav file has multiple channels, only the first channel will be used. |
| **param** | **file**: Pass in an audio file, supporting files in wav,pcm format.<br>|
| **return** | The output result after automatic speech recognition. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string transcribe(std::string &file)
> ```
#### transcribe\_raw {#transcribe\_raw}

```python
def transcribe_raw(self, pcm: maix.Bytes(bytes), sample_rate: int = 16000, channels: int = 1, bits_per_frame: int = 16) -> str
```
Transcribe pcm data to text

| item | description |
| --- | --- |
| **type** | func |
| **param** | **pcm**: RAW data<br>|
| **return** | The output result after automatic speech recognition. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string transcribe_raw(Bytes *pcm, int sample_rate = 16000, int channels = 1, int bits_per_frame = 16)
> ```
#### input\_pcm\_samplerate {#input\_pcm\_samplerate}

```python
def input_pcm_samplerate(self) -> int
```
Get input pcm samplerate

| item | description |
| --- | --- |
| **type** | func |
| **return** | input pcm samplerate |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_pcm_samplerate()
> ```
#### input\_pcm\_channels {#input\_pcm\_channels}

```python
def input_pcm_channels(self) -> int
```
Get input pcm channels

| item | description |
| --- | --- |
| **type** | func |
| **return** | input pcm channels |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_pcm_channels()
> ```
#### input\_pcm\_bits\_per\_frame {#input\_pcm\_bits\_per\_frame}

```python
def input_pcm_bits_per_frame(self) -> int
```
Get input pcm bits per frame

| item | description |
| --- | --- |
| **type** | func |
| **return** | input pcm bits per frame |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_pcm_bits_per_frame()
> ```
### MUD {#MUD}

MUD(model universal describe file) class


> C++ defination code:
> ```cpp
> class MUD
> ```

#### \_\_init\_\_ {#\_\_init\_\_-17}

```python
def __init__(self, model_path: str = '') -> None
```
MUD constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model_path**: direction [in], model file path, model format can be MUD(model universal describe file) file.<br>If model_path set, will load model from file, load failed will raise err.Exception.<br>If model_path not set, you can load model later by load function.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> MUD(const std::string &model_path = "")
> ```
#### load {#load-11}

```python
def load(self, model_path: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model_path**: direction [in], model file path, model format can be MUD(model universal describe file) file.<br>|
| **return** | error code, if load success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const std::string &model_path)
> ```
#### type {#type}

Model type, string type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string type
> ```
#### items {#items}

Model config items, different model type has different config items

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::map<std::string, std::map<std::string, std::string>> items
> ```
#### model\_path {#model\_path}

Model path

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string model_path
> ```
#### parse\_labels {#parse\_labels}

```python
def parse_labels(self, key: str = 'labels') -> list[str]
```
Please load() first, parse labels in items[\"extra\"][\"labels\"],\nif items[\"extra\"][\"labels\"] is a file path: will parse file, every one line is a label;\nif items[\"extra\"][\"labels\"] is a string, labels split by comma(\",\").\nExecute this method will replace items[\"extra\"][\"labels\"];

| item | description |
| --- | --- |
| **type** | func |
| **param** | **key**: parse from items[key], default "labels".<br>|
| **return** | parsed labels list. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::string> parse_labels(const std::string key = "labels")
> ```
### LayerInfo {#LayerInfo}

NN model layer info


> C++ defination code:
> ```cpp
> class LayerInfo
> ```

#### \_\_init\_\_ {#\_\_init\_\_-18}

```python
def __init__(self, name: str = '', dtype: maix.tensor.DType = ..., shape: list[int] = []) -> None
```
LayerInfo constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **name**: direction [in], layer name<br>**dtype**: direction [in], layer data type<br>**shape**: direction [in], layer shape<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> LayerInfo(const std::string &name =  "", tensor::DType dtype = tensor::DType::FLOAT32, std::vector<int> shape = std::vector<int>())
> ```
#### name {#name}

Layer name

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string   name
> ```
#### dtype {#dtype}

Layer data type

| item | description |
| --- | --- |
| **type** | var |
| **attention** | If model is quantized, this is the real quantized data type like int8 float16,<br>in most scene, inputs and outputs we actually use float32 in API like forward. |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> tensor::DType dtype
> ```
#### shape {#shape}

Layer shape

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<int> shape
> ```
#### layout {#layout-2}

If layer layout, if layout is chw, typically the shape is [N, C, H, W], hwc is [N, H, W, C].

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> nn::Layout layout = nn::Layout::UNKNOWN
> ```
#### shape\_int {#shape\_int}

```python
def shape_int(self) -> int
```
Shape as one int type, multiply all dims of shape

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int shape_int()
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
#### \_\_str\_\_ {#\_\_str\_\_-4}

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
### NN {#NN}

Neural network class


> C++ defination code:
> ```cpp
> class NN
> ```

#### \_\_init\_\_ {#\_\_init\_\_-19}

```python
def __init__(self, model: str = '', dual_buff: bool = False) -> None
```
Neural network constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: direction [in], model file path, model format can be MUD(model universal describe file) file.<br>If model_path set, will load model from file, load failed will raise err.Exception.<br>If model_path not set, you can load model later by load function.<br>**dual_buff**: direction [in], prepare dual input output buffer to accelarate forward, that is, when NPU is forwarding we not wait and prepare the next input buff.<br>If you want to ensure every time forward output the input's result, set this arg to false please.<br>Default false to ensure easy use.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> NN(const std::string &model = "", bool dual_buff = false)
> ```
#### load {#load-12}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: direction [in], model file path, model format can be MUD(model universal describe file) file.<br>|
| **return** | error code, if load success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const std::string &model)
> ```
#### loaded {#loaded-3}

```python
def loaded(self) -> bool
```
Is model loaded

| item | description |
| --- | --- |
| **type** | func |
| **return** | true if model loaded, else false |
| **static** | False |

> C++ defination code:
> ```cpp
> bool loaded()
> ```
#### set\_dual\_buff {#set\_dual\_buff}

```python
def set_dual_buff(self, enable: bool) -> None
```
Enable dual buff or disable dual buff

| item | description |
| --- | --- |
| **type** | func |
| **param** | **enable**: true to enable, false to disable<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void set_dual_buff(bool enable)
> ```
#### inputs\_info {#inputs\_info}

```python
def inputs_info(self) -> list[LayerInfo]
```
Get model input layer info

| item | description |
| --- | --- |
| **type** | func |
| **return** | input layer info |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<nn::LayerInfo> inputs_info()
> ```
#### outputs\_info {#outputs\_info}

```python
def outputs_info(self) -> list[LayerInfo]
```
Get model output layer info

| item | description |
| --- | --- |
| **type** | func |
| **return** | output layer info |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<nn::LayerInfo> outputs_info()
> ```
#### extra\_info {#extra\_info}

```python
def extra_info(self) -> dict[str, str]
```
Get model extra info define in MUD file

| item | description |
| --- | --- |
| **type** | func |
| **return** | extra info, dict type, key-value object, attention: key and value are all string type. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::map<std::string, std::string> extra_info()
> ```
#### extra\_info\_labels {#extra\_info\_labels}

```python
def extra_info_labels(self) -> list[str]
```
Get model parsed extra info labels define in MUD file

| item | description |
| --- | --- |
| **type** | func |
| **return** | labels list in extra info, string list type. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::string> extra_info_labels()
> ```
#### forward {#forward}

```python
def forward(self, inputs: maix.tensor.Tensors, copy_result: bool = True, dual_buff_wait: bool = False) -> maix.tensor.Tensors
```
forward run model, get output of model,\nthis is specially for MaixPy, not efficient, but easy to use in MaixPy

| item | description |
| --- | --- |
| **type** | func |
| **param** | **input**: direction [in], input tensor<br>**copy_result**: If set true, will copy result to a new variable; else will use a internal memory, you can only use it until to the next forward.<br>Default true to avoid problems, you can set it to false manually to make speed faster.<br>**dual_buff_wait**: bool type, only for dual_buff mode, if true, will inference this image and wait for result, default false.<br>|
| **return** | output tensor. In C++, you should manually delete tensors in return value and return value.<br>If dual_buff mode, it can be NULL(None in MaixPy) means not ready. |
| **throw** | if error ocurrs like no memory or arg error, will raise err.Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> tensor::Tensors *forward(tensor::Tensors &inputs, bool copy_result = true, bool dual_buff_wait = false)
> ```
#### forward\_image {#forward\_image}

```python
def forward_image(self, img: maix.image.Image, mean: list[float] = [], scale: list[float] = [], fit: maix.image.Fit = ..., copy_result: bool = True, dual_buff_wait: bool = False, chw: bool = True) -> maix.tensor.Tensors
```
forward model, param is image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: input image<br>**mean**: mean value, a list type, e.g. [0.485, 0.456, 0.406], default is empty list means not normalize.<br>**scale**: scale value, a list type, e.g. [1/0.229, 1/0.224, 1/0.225], default is empty list means not normalize.<br>**fit**: fit mode, if the image size of input not equal to model's input, it will auto resize use this fit method,<br>default is image.Fit.FIT_FILL for easy coordinate calculation, but for more accurate result, use image.Fit.FIT_CONTAIN is better.<br>**copy_result**: If set true, will copy result to a new variable; else will use a internal memory, you can only use it until to the next forward.<br>Default true to avoid problems, you can set it to false manually to make speed faster.<br>**dual_buff_wait**: bool type, only for dual_buff mode, if true, will inference this image and wait for result, default false.<br>**chw**: !!depracated!! This arg will be ignored!!! Please set extra.input_layout in mud file instead.<br>chw channel format, forward model with hwc format image input if set to false, default true(chw).<br>|
| **return** | output tensor. In C++, you should manually delete tensors in return value and return value.<br>If dual_buff mode, it can be NULL(None in MaixPy) means not ready. |
| **throw** | If error occurs, like arg error or alloc memory failed, will raise err.Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> tensor::Tensors *forward_image(image::Image &img, std::vector<float> mean = std::vector<float>(), std::vector<float> scale = std::vector<float>(), image::Fit fit = image::Fit::FIT_FILL, bool copy_result = true, bool dual_buff_wait = false, bool chw = true)
> ```
### YOLOv8 {#YOLOv8}

YOLOv8 class


> C++ defination code:
> ```cpp
> class YOLOv8 : public YOLO11
> ```

#### \_\_init\_\_ {#\_\_init\_\_-20}

```python
def __init__(self, model: str = '', dual_buff: bool = True) -> None
```
Constructor of YOLOv8 class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>**dual_buff**: direction [in], prepare dual input output buffer to accelarate forward, that is, when NPU is forwarding we not wait and prepare the next input buff.<br>If you want to ensure every time forward output the input's result, set this arg to false please.<br>Default true to ensure speed.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> YOLOv8(const string &model = "", bool dual_buff = true)
> ```
#### load {#load-13}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### detect {#detect-4}

```python
def detect(self, img: maix.image.Image, conf_th: float = 0.5, iou_th: float = 0.45, fit: maix.image.Fit = ..., keypoint_th: float = 0.5, sort: int = 0) -> Objects
```
Detect objects from image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Image want to detect, if image's size not match model input's, will auto resize with fit method.<br>**conf_th**: Confidence threshold, default 0.5.<br>**iou_th**: IoU threshold, default 0.45.<br>**fit**: Resize method, default image.Fit.FIT_CONTAIN.<br>**keypoint_th**: keypoint threshold, default 0.5, only for yolov8-pose model.<br>**sort**: sort result according to object size, default 0 means not sort, 1 means bigger in front, -1 means smaller in front.<br>|
| **throw** | If image format not match model input format, will throw err::Exception. |
| **return** | Object list. In C++, you should delete it after use.<br>If model is yolov8-pose, object's points have value, and if points' value < 0 means that point is invalid(conf < keypoint_th). |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::Objects *detect(image::Image &img, float conf_th = 0.5, float iou_th = 0.45, maix::image::Fit fit = maix::image::FIT_CONTAIN, float keypoint_th = 0.5, int sort = 0)
> ```
#### input\_size {#input\_size-7}

```python
def input_size(self) -> maix.image.Size
```
Get model input size

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-8}

```python
def input_width(self) -> int
```
Get model input width

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-8}

```python
def input_height(self) -> int
```
Get model input height

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-8}

```python
def input_format(self) -> maix.image.Format
```
Get input image format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### draw\_pose {#draw\_pose-2}

```python
def draw_pose(self, img: maix.image.Image, points: list[int], radius: int = 4, color: maix.image.Color = ..., colors: list[maix.image.Color] = [], body: bool = True, close: bool = False) -> None
```
Draw pose keypoints on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image object, maix.image.Image type.<br>**points**: keypoits, int list type, [x, y, x, y ...]<br>**radius**: radius of points.<br>**color**: color of points.<br>**colors**: assign colors for points, list type, element is image.Color object.<br>**body**: true, if points' length is 17*2 and body is ture, will draw lines as human body, if set to false won't draw lines, default true.<br>**close**: connect all points to close a polygon, default false.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void draw_pose(image::Image &img, std::vector<int> points, int radius = 4, image::Color color = image::COLOR_RED, const std::vector<image::Color> &colors = std::vector<image::Color>(), bool body = true, bool close = false)
> ```
#### draw\_seg\_mask {#draw\_seg\_mask-2}

```python
def draw_seg_mask(self, img: maix.image.Image, x: int, y: int, seg_mask: maix.image.Image, threshold: int = 127) -> None
```
Draw segmentation on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image object, maix.image.Image type.<br>**seg_mask**: segmentation mask image by detect method, a grayscale image<br>**threshold**: only mask's value > threshold will be draw on image, value from 0 to 255.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void draw_seg_mask(image::Image &img, int x, int y, image::Image &seg_mask, int threshold = 127)
> ```
#### labels {#labels-3}

Labels list

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<string> labels
> ```
#### label\_path {#label\_path-3}

Label file path

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string label_path
> ```
#### mean {#mean-7}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-7}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
### PP\_OCR {#PP\_OCR}

PP_OCR class


> C++ defination code:
> ```cpp
> class PP_OCR
> ```

#### \_\_init\_\_ {#\_\_init\_\_-21}

```python
def __init__(self, model: str = '') -> None
```
Constructor of PP_OCR class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> PP_OCR(const string &model = "")
> ```
#### load {#load-14}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### detect {#detect-5}

```python
def detect(self, img: maix.image.Image, thresh: float = 0.3, box_thresh: float = 0.6, fit: maix.image.Fit = ..., char_box: bool = False) -> OCR_Objects
```
Detect objects from image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Image want to detect, if image's size not match model input's, will auto resize with fit method.<br>**thresh**: Confidence threshold where pixels have charactor, default 0.3.<br>**box_thresh**: Box threshold, the box prob higher than this value will be valid, default 0.6.<br>**fit**: Resize method, default image.Fit.FIT_CONTAIN.<br>**char_box**: Calculate every charactor's box, default false, if true then you can get charactor's box by nn.OCR_Object's char_boxes attribute.<br>|
| **throw** | If image format not match model input format or no memory, will throw err::Exception. |
| **return** | nn.OCR_Objects type. In C++, you should delete it after use. |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::OCR_Objects *detect(image::Image &img, float thresh = 0.3, float box_thresh = 0.6, maix::image::Fit fit = maix::image::FIT_CONTAIN, bool char_box = false)
> ```
#### recognize {#recognize}

```python
def recognize(self, img: maix.image.Image, box_points: list[int] = []) -> OCR_Object
```
Only recognize, not detect

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image to recognize chractors, can be a stanrd cropped charactors image,<br>if crop image not standard, you can use box_points to assgin where the charactors' 4 corner is.<br>**box_points**: list type, length must be 8 or 0, default empty means not transfer image to standard image.<br>4 points postiion, format: [x1, y1, x2, y2, x3, y3, x4, y4], point 1 at the left-top, point 2 right-top...<br>**char_box**: Calculate every charactor's box, default false, if true then you can get charactor's box by nn.OCR_Object's char_boxes attribute.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> nn::OCR_Object *recognize(image::Image &img, const std::vector<int> &box_points = std::vector<int>())
> ```
#### draw\_seg\_mask {#draw\_seg\_mask-3}

```python
def draw_seg_mask(self, img: maix.image.Image, x: int, y: int, seg_mask: maix.image.Image, threshold: int = 127) -> None
```
Draw segmentation on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image object, maix.image.Image type.<br>**seg_mask**: segmentation mask image by detect method, a grayscale image<br>**threshold**: only mask's value > threshold will be draw on image, value from 0 to 255.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void draw_seg_mask(image::Image &img, int x, int y, image::Image &seg_mask, int threshold = 127)
> ```
#### input\_size {#input\_size-8}

```python
def input_size(self) -> maix.image.Size
```
Get model input size

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-9}

```python
def input_width(self) -> int
```
Get model input width

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-9}

```python
def input_height(self) -> int
```
Get model input height

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-9}

```python
def input_format(self) -> maix.image.Format
```
Get input image format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### mean {#mean-8}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-8}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
#### rec\_mean {#rec\_mean}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> rec_mean
> ```
#### rec\_scale {#rec\_scale}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> rec_scale
> ```
#### labels {#labels-4}

labels (charactors)

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<std::string> labels
> ```
#### det {#det}

model have detect model

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool det
> ```
#### rec {#rec}

model have recognize model

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool rec
> ```
### YOLOWorld {#YOLOWorld}

YOLOWorld class


> C++ defination code:
> ```cpp
> class YOLOWorld
> ```

#### \_\_init\_\_ {#\_\_init\_\_-22}

```python
def __init__(self, model: str = '', text_feature: str = '', labels: str = '', dual_buff: bool = True) -> None
```
Constructor of YOLOWorld class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>**text_feature**: class text feature path, more info refer to load method, default empty, you can load class text feature later by load function.<br>**labels**: Class labels or labels file path.<br>If string class labels: labels split by comma, e.g. "person, car, cat".<br>If file path: labels file path, each line is a label.<br>**dual_buff**: direction [in], prepare dual input output buffer to accelarate forward, that is, when NPU is forwarding we not wait and prepare the next input buff.<br>If you want to ensure every time forward output the input's result, set this arg to false please.<br>Default true to ensure speed.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> YOLOWorld(const string &model = "", const string &text_feature = "", const string &labels = "", bool dual_buff = true)
> ```
#### load {#load-15}

```python
def load(self, model: str, text_feature: str, labels: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>**text_feature**: Class text feature bin file path.<br>**labels**: Class labels or labels file path.<br>If string class labels: labels split by comma, e.g. "person, car, cat".<br>If file path: labels file path, each line is a label.<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model, const string &text_feature, const string &labels)
> ```
#### learn\_text\_feature {#learn\_text\_feature}

```python
def learn_text_feature(model: str, labels: list[str], feature_path: str, labels_path: str) -> maix.err.Err
```
Set detector class labels dynamically, will generate class text feature and save to text_feature path set in load method or constructor.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **labels**: class labels you want to recognize, list type. e.g. ["person", "car", "cat"]<br>|
| **return** | err::Err |
| **static** | True |

> C++ defination code:
> ```cpp
> static err::Err learn_text_feature(const std::string &model, std::vector<std::string> labels, const std::string &feature_path, const std::string &labels_path)
> ```
#### detect {#detect-6}

```python
def detect(self, img: maix.image.Image, conf_th: float = 0.5, iou_th: float = 0.45, fit: maix.image.Fit = ..., sort: int = 0) -> Objects
```
Detect objects from image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Image want to detect, if image's size not match model input's, will auto resize with fit method.<br>**conf_th**: Confidence threshold, default 0.5.<br>**iou_th**: IoU threshold, default 0.45.<br>**fit**: Resize method, default image.Fit.FIT_CONTAIN.<br>**sort**: sort result according to object size, default 0 means not sort, 1 means bigger in front, -1 means smaller in front.<br>|
| **throw** | If image format not match model input format, will throw err::Exception. |
| **return** | Object list. In C++, you should delete it after use. |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::Objects *detect(image::Image &img, float conf_th = 0.5, float iou_th = 0.45, maix::image::Fit fit = maix::image::FIT_CONTAIN, int sort = 0)
> ```
#### input\_size {#input\_size-9}

```python
def input_size(self) -> maix.image.Size
```
Get model input size

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-10}

```python
def input_width(self) -> int
```
Get model input width

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-10}

```python
def input_height(self) -> int
```
Get model input height

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-10}

```python
def input_format(self) -> maix.image.Format
```
Get input image format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### labels {#labels-5}

Labels list

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<string> labels
> ```
#### mean {#mean-9}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-9}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
### NanoTrack {#NanoTrack}

NanoTrack class


> C++ defination code:
> ```cpp
> class NanoTrack
> ```

#### \_\_init\_\_ {#\_\_init\_\_-23}

```python
def __init__(self, model: str = '') -> None
```
Constructor of NanoTrack class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> NanoTrack(const string &model = "")
> ```
#### load {#load-16}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### init {#init-2}

```python
def init(self, img: maix.image.Image, x: int, y: int, w: int, h: int) -> None
```
Init tracker, give tacker first target image and target position.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Image want to detect, target should be in this image.<br>**x**: the target position left top coordinate x.<br>**y**: the target position left top coordinate y.<br>**w**: the target width.<br>**h**: the target height.<br>|
| **throw** | If image format not match model input format, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> void init(image::Image &img, int x, int y, int w, int h)
> ```
#### track {#track-2}

```python
def track(self, img: maix.image.Image, threshold: float = 0.9) -> Object
```
Track object acoording to last object position and the init function learned target feature.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image to detect object and track, can be any resolution, before detect it will crop a area according to last time target's position.<br>**threshold**: If score < threshold, will see this new detection is invalid, but remain return this new detecion,  default 0.9.<br>|
| **return** | object, attribute [x, y, w, h] and score are the predict target position and score, points attribute provide more info:<br>0~3  [ search_x, search_y, search_w, search_h ]: search area for this time track, based on last correct start position.<br>4~5  [ predict_cx, predict_cy]: predict center according to this time input.<br>6    [ search_size ]: search_area size based on last correct start position, center is (search_x - search_w / 2, search_y - search_h / 2).<br>7    [ predict_template_size ]: template size based on predict target, center is (predict_cx, predict_cy).<br>8~11 [ correct_cx, correct_cy, correct_w, correct_h]: latest correct (score > threshold) target position. |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::Object track(image::Image &img, float threshold = 0.9)
> ```
#### input\_size {#input\_size-10}

```python
def input_size(self) -> maix.image.Size
```
Get model input size

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-11}

```python
def input_width(self) -> int
```
Get model input width

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-11}

```python
def input_height(self) -> int
```
Get model input height

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-11}

```python
def input_format(self) -> maix.image.Format
```
Get input image format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### mean {#mean-10}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-10}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
### FaceObject {#FaceObject}

Face object


> C++ defination code:
> ```cpp
> class FaceObject
> ```

#### \_\_init\_\_ {#\_\_init\_\_-24}

```python
def __init__(self, x: int = 0, y: int = 0, w: int = 0, h: int = 0, class_id: int = 0, score: float = 0, points: list[int] = [], feature: list[float] = [], face: maix.image.Image = ...) -> None
```
Constructor

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> FaceObject(int x = 0, int y = 0, int w = 0, int h = 0, int class_id = 0, float score = 0, std::vector<int> points = std::vector<int>(), std::vector<float> feature = std::vector<float>(), image::Image face = image::Image())
> ```
#### \_\_str\_\_ {#\_\_str\_\_-5}

```python
def __str__(self) -> str
```
FaceObject info to string

| item | description |
| --- | --- |
| **type** | func |
| **return** | FaceObject info string |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string to_str()
> ```
#### x {#x-3}

FaceObject left top coordinate x

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int x
> ```
#### y {#y-3}

FaceObject left top coordinate y

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int y
> ```
#### w {#w-3}

FaceObject width

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int w
> ```
#### h {#h-3}

FaceObject height

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int h
> ```
#### class\_id {#class\_id-3}

FaceObject class id

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int class_id
> ```
#### score {#score-4}

FaceObject score

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float score
> ```
#### points {#points-3}

keypoints

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<int> points
> ```
#### feature {#feature}

feature, float list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> feature
> ```
#### face {#face}

face image

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> image::Image face
> ```
### FaceObjects {#FaceObjects}

Objects Class for detect result


> C++ defination code:
> ```cpp
> class FaceObjects
> ```

#### \_\_init\_\_ {#\_\_init\_\_-25}

```python
def __init__(self) -> None
```
Constructor of FaceObjects class

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> FaceObjects()
> ```
#### add {#add-3}

```python
def add(self, x: int = 0, y: int = 0, w: int = 0, h: int = 0, class_id: int = 0, score: float = 0, points: list[int] = [], feature: list[float] = [], face: maix.image.Image = ...) -> FaceObject
```
Add object to FaceObjects

| item | description |
| --- | --- |
| **type** | func |
| **throw** | Throw exception if no memory |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::FaceObject &add(int x = 0, int y = 0, int w = 0, int h = 0, int class_id = 0, float score = 0, std::vector<int> points = std::vector<int>(), std::vector<float> feature = std::vector<float>(), image::Image face = image::Image())
> ```
#### remove {#remove-3}

```python
def remove(self, idx: int) -> maix.err.Err
```
Remove object form FaceObjects

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err remove(int idx)
> ```
#### at {#at-3}

```python
def at(self, idx: int) -> FaceObject
```
Get object item

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::FaceObject &at(int idx)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-3}

```python
def __getitem__(self, idx: int) -> FaceObject
```
Get object item

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::FaceObject &operator[](int idx)
> ```
#### \_\_len\_\_ {#\_\_len\_\_-3}

```python
def __len__(self) -> int
```
Get size

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> size_t size()
> ```
#### \_\_iter\_\_ {#\_\_iter\_\_-3}

```python
def __iter__(self) -> typing.Iterator
```
Begin

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<FaceObject*>::iterator begin()
> ```
### FaceRecognizer {#FaceRecognizer}

FaceRecognizer class


> C++ defination code:
> ```cpp
> class FaceRecognizer
> ```

#### \_\_init\_\_ {#\_\_init\_\_-26}

```python
def __init__(self, detect_model: str = '', feature_model: str = '', dual_buff: bool = True) -> None
```
Constructor of FaceRecognizer class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **detect_model**: face detect model path, default empty, you can load model later by load function.<br>**feature_model**: feature extract model<br>**dual_buff**: direction [in], prepare dual input output buffer to accelarate forward, that is, when NPU is forwarding we not wait and prepare the next input buff.<br>If you want to ensure every time forward output the input's result, set this arg to false please.<br>Default true to ensure speed.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> FaceRecognizer(const string &detect_model = "", const string &feature_model = "", bool dual_buff = true)
> ```
#### load {#load-17}

```python
def load(self, detect_model: str, feature_model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **detect_model**: face detect model path, default empty, you can load model later by load function.<br>**feature_model**: feature extract model<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &detect_model, const string &feature_model)
> ```
#### recognize {#recognize-2}

```python
def recognize(self, img: maix.image.Image, conf_th: float = 0.5, iou_th: float = 0.45, compare_th: float = 0.8, get_feature: bool = False, get_face: bool = False, fit: maix.image.Fit = ...) -> FaceObjects
```
Detect objects from image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Image want to detect, if image's size not match model input's, will auto resize with fit method.<br>**conf_th**: Detect confidence threshold, default 0.5.<br>**iou_th**: Detect IoU threshold, default 0.45.<br>**compare_th**: Compare two face score threshold, default 0.8, if two faces' score < this value, will see this face fas unknown.<br>**get_feature**: return feature or not, if true will copy features to result, if false will not copy feature to result to save time and memory.<br>**get_face**: return face image or not, if true result object's face attribute will valid, or face sttribute is empty. Get face image will alloc memory and copy image, so will lead to slower speed.<br>**fit**: Resize method, default image.Fit.FIT_CONTAIN.<br>|
| **throw** | If image format not match model input format, will throw err::Exception. |
| **return** | FaceObjects object. In C++, you should delete it after use. |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::FaceObjects *recognize(image::Image &img, float conf_th = 0.5, float iou_th = 0.45, float compare_th = 0.8, bool get_feature = false, bool get_face = false, maix::image::Fit fit = maix::image::FIT_CONTAIN)
> ```
#### add\_face {#add\_face}

```python
def add_face(self, face: FaceObject, label: str) -> maix.err.Err
```
Add face to lib

| item | description |
| --- | --- |
| **type** | func |
| **param** | **face**: face object, find by recognize<br>**label**: face label(name)<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err add_face(nn::FaceObject *face, const std::string &label)
> ```
#### remove\_face {#remove\_face}

```python
def remove_face(self, idx: int = -1, label: str = '') -> maix.err.Err
```
remove face from lib

| item | description |
| --- | --- |
| **type** | func |
| **param** | **idx**: index of face in lib, default -1 means use label, value [0,face_num), idx and label must have one, idx have high priotiry.<br>**label**: which face to remove, default to empty string mean use idx, idx and label must have one, idx have high priotiry.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err remove_face(int idx = -1, const std::string &label = "")
> ```
#### save\_faces {#save\_faces}

```python
def save_faces(self, path: str) -> maix.err.Err
```
Save faces info to a file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **path**: where to save, string type.<br>|
| **return** | err.Err type |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err save_faces(const std::string &path)
> ```
#### load\_faces {#load\_faces}

```python
def load_faces(self, path: str) -> maix.err.Err
```
Load faces info from a file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **path**: from where to load, string type.<br>|
| **return** | err::Err type |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load_faces(const std::string &path)
> ```
#### input\_size {#input\_size-11}

```python
def input_size(self) -> maix.image.Size
```
Get model input size

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-12}

```python
def input_width(self) -> int
```
Get model input width

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-12}

```python
def input_height(self) -> int
```
Get model input height

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-12}

```python
def input_format(self) -> maix.image.Format
```
Get input image format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### mean\_detector {#mean\_detector}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean_detector
> ```
#### scale\_detector {#scale\_detector}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale_detector
> ```
#### mean\_feature {#mean\_feature}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean_feature
> ```
#### scale\_feature {#scale\_feature}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale_feature
> ```
#### labels {#labels-6}

labels, list type, first is \"unknown\"

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<std::string> labels
> ```
#### features {#features}

features

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<std::vector<float>> features
> ```
### Classifier {#Classifier}

Classifier


> C++ defination code:
> ```cpp
> class Classifier
> ```

#### \_\_init\_\_ {#\_\_init\_\_-27}

```python
def __init__(self, model: str = '', dual_buff: bool = True) -> None
```
Construct a new Classifier object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: MUD model path, if empty, will not load model, you can call load() later.<br>if not empty, will load model and will raise err::Exception if load failed.<br>**dual_buff**: direction [in], prepare dual input output buffer to accelarate forward, that is, when NPU is forwarding we not wait and prepare the next input buff.<br>If you want to ensure every time forward output the input's result, set this arg to false please.<br>Default true to ensure speed.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Classifier(const string &model = "", bool dual_buff = true)
> ```
#### load {#load-18}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file, model format is .mud,\nMUD file should contain [extra] section, have key-values:\n- model_type: classifier\n- input_type: rgb or bgr\n- mean: 123.675, 116.28, 103.53\n- scale: 0.017124753831663668, 0.01750700280112045, 0.017429193899782137\n- labels: imagenet_classes.txt

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: MUD model path<br>|
| **return** | error code, if load failed, return error code |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### classify {#classify-2}

```python
def classify(self, img: maix.image.Image, softmax: bool = True, fit: maix.image.Fit = ...) -> list[tuple[int, float]]
```
Forward image to model, get result. Only for image input, use classify_raw for tensor input.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image, format should match model input_type， or will raise err.Exception<br>**softmax**: if true, will do softmax to result, or will return raw value<br>**fit**: image resize fit mode, default Fit.FIT_COVER, see image.Fit.<br>|
| **throw** | If error occurred, will raise err::Exception, you can find reason in log, mostly caused by args error or hardware error. |
| **return** | result, a list of (label, score). If in dual_buff mode, value can be one element list and score is zero when not ready. In C++, you need to delete it after use. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::pair<int, float>> *classify(image::Image &img, bool softmax = true, image::Fit fit = image::FIT_COVER)
> ```
#### classify\_raw {#classify\_raw}

```python
def classify_raw(self, data: maix.tensor.Tensor, softmax: bool = True) -> list[tuple[int, float]]
```
Forward tensor data to model, get result

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: tensor data, format should match model input_type， or will raise err.Excetion<br>**softmax**: if true, will do softmax to result, or will return raw value<br>|
| **throw** | If error occurred, will raise err::Exception, you can find reason in log, mostly caused by args error or hardware error. |
| **return** | result, a list of (label, score). In C++, you need to delete it after use. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::pair<int, float>> *classify_raw(tensor::Tensor &data, bool softmax = true)
> ```
#### input\_size {#input\_size-12}

```python
def input_size(self) -> maix.image.Size
```
Get model input size, only for image input

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-13}

```python
def input_width(self) -> int
```
Get model input width, only for image input

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-13}

```python
def input_height(self) -> int
```
Get model input height, only for image input

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-13}

```python
def input_format(self) -> maix.image.Format
```
Get input image format, only for image input

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### input\_shape {#input\_shape-3}

```python
def input_shape(self) -> list[int]
```
Get input shape, if have multiple input, only return first input shape

| item | description |
| --- | --- |
| **type** | func |
| **return** | input shape, list type |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> input_shape()
> ```
#### labels {#labels-7}

Labels list

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<string> labels
> ```
#### label\_path {#label\_path-4}

Label file path

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string label_path
> ```
#### mean {#mean-11}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-11}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
### FaceLandmarksObject {#FaceLandmarksObject}

FaceLandmarksObject class


> C++ defination code:
> ```cpp
> class FaceLandmarksObject
> ```

#### \_\_init\_\_ {#\_\_init\_\_-28}

```python
def __init__(self) -> None
```
Valid or not(score > conf_th when detect).

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> FaceLandmarksObject()
> ```
#### valid {#valid}

Valid or not(score > conf_th when detect).

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> bool valid
> ```
#### score {#score-5}

whether face in image score, value from 0 to 1.0.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float score
> ```
#### points {#points-4}

landmarks points, format: x0, y0, ..., xn-1, yn-1.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<int> points
> ```
#### points\_z {#points\_z}

landmarks points, format: z0, z1, ..., zn-1.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<int> points_z
> ```
### FaceLandmarks {#FaceLandmarks}

FaceLandmarks class


> C++ defination code:
> ```cpp
> class FaceLandmarks
> ```

#### \_\_init\_\_ {#\_\_init\_\_-29}

```python
def __init__(self, model: str = '') -> None
```
Constructor of FaceLandmarks class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> FaceLandmarks(const string &model = "")
> ```
#### load {#load-19}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### detect {#detect-7}

```python
def detect(self, img: maix.image.Image, conf_th: float = 0.5, landmarks_abs: bool = True, landmarks_rel: bool = False) -> FaceLandmarksObject
```
Detect objects from image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Image want to detect, if image's size not match model input's, will auto resize with fit method.<br>**conf_th**: Hand detect confidence threshold, default 0.7.<br>**landmarks_rel**: outputs the relative coordinates of 21 points with respect to the top-left vertex of the hand.<br>In obj.points, the last 21x2 values are arranged as x0y0x1y1...x20y20.<br>Value from 0 to obj.w.<br>|
| **throw** | If image format not match model input format, will throw err::Exception. |
| **return** | Object list. In C++, you should delete it after use.<br>Object's points value format: box_topleft_x, box_topleft_y, box_topright_x, box_topright_y, box_bottomright_x, box_bottomright_y， box_bottomleft_x, box_bottomleft_y,<br>x0, y0, z1, x1, y1, z2, ..., x20, y20, z20.<br>If landmarks_rel is True, will be box_topleft_x, box_topleft_y...,x20,y20,z20,x0_rel,y0_rel,...,x20_rel,y20_rel.<br>Z is depth, the larger the value, the farther away from the palm, and the positive value means closer to the camera. |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::FaceLandmarksObject *detect(image::Image &img, float conf_th = 0.5, bool landmarks_abs = true, bool landmarks_rel = false)
> ```
#### crop\_image {#crop\_image}

```python
def crop_image(self, img: maix.image.Image, x: int, y: int, w: int, h: int, points: list[int], new_width: int = -1, new_height: int = -1, scale: float = 1.2) -> maix.image.Image
```
Crop image from source image by 2 points(2 eyes)

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x,y,w,h**: face rectangle, x,y is left-top point.<br>**img**: source image<br>**points**: 2 points, eye_left_x, eye_left_y, eye_right_x, eye_right_y<br>**scale**: crop size scale relative to rectangle's max side length(w or h), final value is `scale *max(w, h)`,default 1.2.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> maix::image::Image *crop_image(maix::image::Image &img, int x, int y, int w, int h, std::vector<int> points, int new_width = -1, int new_height = -1, float scale = 1.2)
> ```
#### input\_size {#input\_size-13}

```python
def input_size(self, detect: bool = True) -> maix.image.Size
```
Get model input size

| item | description |
| --- | --- |
| **type** | func |
| **param** | **detect**: detect or landmarks model, default true.<br>|
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size(bool detect = true)
> ```
#### input\_width {#input\_width-14}

```python
def input_width(self, detect: bool = True) -> int
```
Get model input width

| item | description |
| --- | --- |
| **type** | func |
| **param** | **detect**: detect or landmarks model, default true.<br>|
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width(bool detect = true)
> ```
#### input\_height {#input\_height-14}

```python
def input_height(self, detect: bool = True) -> int
```
Get model input height

| item | description |
| --- | --- |
| **type** | func |
| **param** | **detect**: detect or landmarks model, default true.<br>|
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height(bool detect = true)
> ```
#### input\_format {#input\_format-14}

```python
def input_format(self) -> maix.image.Format
```
Get input image format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### draw\_face {#draw\_face}

```python
def draw_face(self, img: maix.image.Image, points: list[int], num: int, points_z: list[int] = [], r_min: int = 2, r_max: int = 4) -> None
```
Draw hand and landmarks on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image object, maix.image.Image type.<br>**leftright,**: 0 means left, 1 means right<br>**points**: points result from detect method: x0, y0, x1, y1, ..., xn-1, yn-1.<br>**points_z**: points result from detect method: z0, z1, ..., zn-1.<br>**r_min**: min radius of points.<br>**r_max**: min radius of points.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void draw_face(image::Image &img, const std::vector<int> &points, int num, const std::vector<int> &points_z=std::vector<int>(), int r_min = 2, int r_max = 4)
> ```
#### mean {#mean-12}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-12}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
#### landmarks\_num {#landmarks\_num}

landmarks number.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> int landmarks_num
> ```
### YOLOv5 {#YOLOv5}

YOLOv5 class


> C++ defination code:
> ```cpp
> class YOLOv5
> ```

#### \_\_init\_\_ {#\_\_init\_\_-30}

```python
def __init__(self, model: str = '', dual_buff: bool = True) -> None
```
Constructor of YOLOv5 class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>**dual_buff**: direction [in], prepare dual input output buffer to accelarate forward, that is, when NPU is forwarding we not wait and prepare the next input buff.<br>If you want to ensure every time forward output the input's result, set this arg to false please.<br>Default true to ensure speed.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> YOLOv5(const string &model = "", bool dual_buff = true)
> ```
#### load {#load-20}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### detect {#detect-8}

```python
def detect(self, img: maix.image.Image, conf_th: float = 0.5, iou_th: float = 0.45, fit: maix.image.Fit = ..., sort: int = 0) -> list[Object]
```
Detect objects from image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Image want to detect, if image's size not match model input's, will auto resize with fit method.<br>**conf_th**: Confidence threshold, default 0.5.<br>**iou_th**: IoU threshold, default 0.45.<br>**fit**: Resize method, default image.Fit.FIT_CONTAIN.<br>**sort**: sort result according to object size, default 0 means not sort, 1 means bigger in front, -1 means smaller in front.<br>|
| **throw** | If image format not match model input format, will throw err::Exception. |
| **return** | Object list. In C++, you should delete it after use. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<nn::Object> *detect(image::Image &img, float conf_th = 0.5, float iou_th = 0.45, maix::image::Fit fit = maix::image::FIT_CONTAIN, int sort = 0)
> ```
#### input\_size {#input\_size-14}

```python
def input_size(self) -> maix.image.Size
```
Get model input size

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size()
> ```
#### input\_width {#input\_width-15}

```python
def input_width(self) -> int
```
Get model input width

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width()
> ```
#### input\_height {#input\_height-15}

```python
def input_height(self) -> int
```
Get model input height

| item | description |
| --- | --- |
| **type** | func |
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height()
> ```
#### input\_format {#input\_format-15}

```python
def input_format(self) -> maix.image.Format
```
Get input image format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### labels {#labels-8}

Labels list

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<string> labels
> ```
#### label\_path {#label\_path-5}

Label file path

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string label_path
> ```
#### mean {#mean-13}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-13}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
#### anchors {#anchors}

Get anchors

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> anchors
> ```
### Speech {#Speech}

Speech


> C++ defination code:
> ```cpp
> class Speech
> ```

#### \_\_init\_\_ {#\_\_init\_\_-31}

```python
def __init__(self, model: str = '') -> None
```
Construct a new Speech object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> Speech(const string &model = "")
> ```
#### load {#load-21}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### init {#init-3}

```python
def init(self, dev_type: SpeechDevice, device_name: str = '') -> maix.err.Err
```
Init the ASR library and select the type and name of the audio device.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **dev_type**: device type want to detect, can choose between WAV, PCM, or MIC.<br>**device_name**: device name want to detect, can choose a WAV file, a PCM file, or a MIC device name.<br>|
| **throw** | **1**. If am model is not loaded, will throw err::ERR_NOT_IMPL.<br>**2**. If device is not supported, will throw err::ERR_NOT_IMPL.<br>|
| **return** | err::Err type, if init success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err init(nn::SpeechDevice dev_type, const string &device_name = "")
> ```
#### devive {#devive}

```python
def devive(self, dev_type: SpeechDevice, device_name: str) -> maix.err.Err
```
Reset the device, usually used for PCM/WAV recognition,\nsuch as identifying the next WAV file.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **dev_type**: device type want to detect, can choose between WAV, PCM, or MIC.<br>**device_name**: device name want to detect, can choose a WAV file, a PCM file, or a MIC device name.<br>|
| **throw** | If device is not supported, will throw err::ERR_NOT_IMPL. |
| **return** | err::Err type, if init success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err devive(nn::SpeechDevice dev_type, const string &device_name)
> ```
#### dec\_deinit {#dec\_deinit}

```python
def dec_deinit(self, decoder: SpeechDecoder) -> None
```
Deinit the decoder.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **decoder**: decoder type want to deinit<br>can choose between DECODER_RAW, DECODER_DIG, DECODER_LVCSR, DECODER_KWS or DECODER_ALL.<br>|
| **throw** | If device is not supported, will throw err::ERR_NOT_IMPL. |
| **static** | False |

> C++ defination code:
> ```cpp
> void dec_deinit(nn::SpeechDecoder decoder)
> ```
#### raw {#raw}

```python
def raw(self, callback: typing.Callable[[list[tuple[int, float]], int], None]) -> maix.err.Err
```
Init raw decoder, it will output the prediction results of the original AM.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **callback**: raw decoder user callback.<br>|
| **return** | err::Err type, if init success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err raw(std::function<void(std::vector<std::pair<int, float>>, int)> callback)
> ```
#### digit {#digit}

```python
def digit(self, blank: int, callback: typing.Callable[[str, int], None]) -> maix.err.Err
```
Init digit decoder, it will output the Chinese digit recognition results within the last 4 seconds.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **blank**: If it exceeds this value, insert a '_' in the output result to indicate idle mute.<br>**callback**: digit decoder user callback.<br>|
| **return** | err::Err type, if init success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err digit(int blank, std::function<void(char*, int)> callback)
> ```
#### kws {#kws}

```python
def kws(self, kw_tbl: list[str], kw_gate: list[float], callback: typing.Callable[[list[float], int], None], auto_similar: bool = True) -> maix.err.Err
```
Init kws decoder, it will output a probability list of all registered keywords in the latest frame,\nusers can set their own thresholds for wake-up.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **kw_tbl**: Keyword list, filled in with spaces separated by pinyin, for example: xiao3 ai4 tong2 xue2<br>**kw_gate**: kw_gate, keyword probability gate table, the number should be the same as kw_tbl<br>**auto_similar**: Whether to perform automatic homophone processing,<br>setting it to true will automatically calculate the probability by using pinyin with different tones as homophones<br>**callback**: digit decoder user callback.<br>|
| **return** | err::Err type, if init success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err kws(std::vector<string> kw_tbl, std::vector<float> kw_gate, std::function<void(std::vector<float>, int)> callback, bool auto_similar = true)
> ```
#### lvcsr {#lvcsr}

```python
def lvcsr(self, sfst_name: str, sym_name: str, phones_txt: str, words_txt: str, callback: typing.Callable[[tuple[str, str], int], None], beam: float = 8, bg_prob: float = 10, scale: float = 0.5, mmap: bool = False) -> maix.err.Err
```
Init lvcsr decoder, it will output continuous speech recognition results (less than 1024 Chinese characters).

| item | description |
| --- | --- |
| **type** | func |
| **param** | **sfst_name**: Sfst file path.<br>**sym_name**: Sym file path (output symbol table).<br>**phones_txt**: Path to phones.bin (pinyin table).<br>**words_txt**: Path to words.bin (dictionary table).<br>**callback**: lvcsr decoder user callback.<br>**beam**: The beam size for WFST search is set to 8 by default, and it is recommended to be between 3 and 9.<br>The larger the size, the larger the search space, and the more accurate but slower the search.<br>**bg_prob**: The absolute value of the natural logarithm of the default probability value for background pinyin<br>outside of BEAM-CNT is set to 10 by default.<br>**scale**: acoustics_cost = log(pny_prob)*scale.<br>**mmap**: use mmap to load the WFST decoding image,<br>If set to true, the beam should be less than 5.<br>|
| **return** | err::Err type, if init success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err lvcsr(const string &sfst_name, const string &sym_name,
>                        const string &phones_txt, const string &words_txt, 
>                        std::function<void(std::pair<char*, char*>, int)> callback,
>                        float beam = 8, float bg_prob = 10, float scale = 0.5, bool mmap = false)
> ```
#### run {#run}

```python
def run(self, frame: int) -> int
```
Run speech recognition, user can run 1 frame at a time and do other processing after running,\nor it can run continuously within a thread and be stopped by an external thread.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **frame**: The number of frames per run.<br>|
| **return** | int type, return actual number of frames in the run. |
| **static** | False |

> C++ defination code:
> ```cpp
> int run(int frame)
> ```
#### clear {#clear-2}

```python
def clear(self) -> None
```
Reset internal cache operation

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> void clear()
> ```
#### frame\_time {#frame\_time}

```python
def frame_time(self) -> int
```
Get the time of one frame.

| item | description |
| --- | --- |
| **type** | func |
| **return** | int type, return the time of one frame. |
| **static** | False |

> C++ defination code:
> ```cpp
> int frame_time()
> ```
#### similar {#similar}

```python
def similar(self, pny: str, similar_pnys: list[str]) -> maix.err.Err
```
Manually register mute words, and each pinyin can register up to 10 homophones,\nplease note that using this interface to register homophones will overwrite,\nthe homophone table automatically generated in the \"automatic homophone processing\" feature.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **dev_type**: device type want to detect, can choose between WAV, PCM, or MIC.<br>**device_name**: device name want to detect, can choose a WAV file, a PCM file, or a MIC device name.<br>|
| **return** | err::Err type, if init success, return err::ERR_NONE |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err similar(const string &pny, std::vector<std::string> similar_pnys)
> ```
#### skip\_frames {#skip\_frames}

```python
def skip_frames(self, num: int) -> None
```
Run some frames and drop, this can be used to avoid\nincorrect recognition results when switching decoders.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **num**: number of frames to run and drop<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void skip_frames(int num)
> ```
#### mean {#mean-14}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-14}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
#### dev\_type {#dev\_type}

```python
def dev_type(self) -> SpeechDevice
```
get device type

| item | description |
| --- | --- |
| **type** | func |
| **return** | nn::SpeechDevice type, see SpeechDevice of this module |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::SpeechDevice dev_type()
> ```
### HandLandmarks {#HandLandmarks}

HandLandmarks class


> C++ defination code:
> ```cpp
> class HandLandmarks
> ```

#### \_\_init\_\_ {#\_\_init\_\_-32}

```python
def __init__(self, model: str = '') -> None
```
Constructor of HandLandmarks class

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: model path, default empty, you can load model later by load function.<br>|
| **throw** | If model arg is not empty and load failed, will throw err::Exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> HandLandmarks(const string &model = "")
> ```
#### load {#load-22}

```python
def load(self, model: str) -> maix.err.Err
```
Load model from file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **model**: Model path want to load<br>|
| **return** | err::Err |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err load(const string &model)
> ```
#### detect {#detect-9}

```python
def detect(self, img: maix.image.Image, conf_th: float = 0.7, iou_th: float = 0.45, conf_th2: float = 0.8, landmarks_rel: bool = False) -> Objects
```
Detect objects from image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: Image want to detect, if image's size not match model input's, will auto resize with fit method.<br>**conf_th**: Hand detect confidence threshold, default 0.7.<br>**iou_th**: IoU threshold, default 0.45.<br>**conf_th2**: Hand detect confidence second time check threshold, default 0.8.<br>**landmarks_rel**: outputs the relative coordinates of 21 points with respect to the top-left vertex of the hand.<br>In obj.points, the last 21x2 values are arranged as x0y0x1y1...x20y20.<br>Value from 0 to obj.w.<br>|
| **throw** | If image format not match model input format, will throw err::Exception. |
| **return** | Object list. In C++, you should delete it after use.<br>Object's points value format: box_topleft_x, box_topleft_y, box_topright_x, box_topright_y, box_bottomright_x, box_bottomright_y， box_bottomleft_x, box_bottomleft_y,<br>x0, y0, z1, x1, y1, z2, ..., x20, y20, z20.<br>If landmarks_rel is True, will be box_topleft_x, box_topleft_y...,x20,y20,z20,x0_rel,y0_rel,...,x20_rel,y20_rel.<br>Z is depth, the larger the value, the farther away from the palm, and the positive value means closer to the camera. |
| **static** | False |

> C++ defination code:
> ```cpp
> nn::Objects *detect(image::Image &img, float conf_th = 0.7, float iou_th = 0.45, float conf_th2 = 0.8, bool landmarks_rel = false)
> ```
#### input\_size {#input\_size-15}

```python
def input_size(self, detect: bool = True) -> maix.image.Size
```
Get model input size

| item | description |
| --- | --- |
| **type** | func |
| **param** | **detect**: detect or landmarks model, default true.<br>|
| **return** | model input size |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size input_size(bool detect = true)
> ```
#### input\_width {#input\_width-16}

```python
def input_width(self, detect: bool = True) -> int
```
Get model input width

| item | description |
| --- | --- |
| **type** | func |
| **param** | **detect**: detect or landmarks model, default true.<br>|
| **return** | model input size of width |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_width(bool detect = true)
> ```
#### input\_height {#input\_height-16}

```python
def input_height(self, detect: bool = True) -> int
```
Get model input height

| item | description |
| --- | --- |
| **type** | func |
| **param** | **detect**: detect or landmarks model, default true.<br>|
| **return** | model input size of height |
| **static** | False |

> C++ defination code:
> ```cpp
> int input_height(bool detect = true)
> ```
#### input\_format {#input\_format-16}

```python
def input_format(self) -> maix.image.Format
```
Get input image format

| item | description |
| --- | --- |
| **type** | func |
| **return** | input image format, image::Format type. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format input_format()
> ```
#### draw\_hand {#draw\_hand}

```python
def draw_hand(self, img: maix.image.Image, leftright: int, points: list[int], r_min: int = 4, r_max: int = 10, box: bool = True, box_thickness: int = 1, box_color_l: maix.image.Color = ..., box_color_r: maix.image.Color = ...) -> None
```
Draw hand and landmarks on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: image object, maix.image.Image type.<br>**leftright,**: 0 means left, 1 means right<br>**points**: points result from detect method: box_topleft_x, box_topleft_y, box_topright_x, box_topright_y, box_bottomright_x, box_bottomright_y， box_bottomleft_x, box_bottomleft_y,<br>x0, y0, z1, x1, y1, z2, ..., x20, y20, z20<br>**r_min**: min radius of points.<br>**r_max**: min radius of points.<br>**box**: draw box or not, default true.<br>**box_color**: color of box.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void draw_hand(image::Image &img, int leftright, const std::vector<int> &points, int r_min = 4, int r_max = 10, bool box = true, int box_thickness = 1, image::Color box_color_l = image::COLOR_RED, image::Color box_color_r = image::COLOR_GREEN)
> ```
#### labels {#labels-9}

Labels list

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<string> labels
> ```
#### label\_path {#label\_path-6}

Label file path

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::string label_path
> ```
#### mean {#mean-15}

Get mean value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> mean
> ```
#### scale {#scale-15}

Get scale value, list type

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> std::vector<float> scale
> ```
