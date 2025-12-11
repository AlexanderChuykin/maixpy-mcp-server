---
title: maix.app
---

maix.app module


> You can use `maix.app` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}



## Variable {#Variable}



## Function {#Function}

### app\_id {#app\_id}

```python
def app_id() -> str
```
Get current APP ID.

| item | description |
| --- | --- |
| **return** | APP ID. |

> C++ defination code:
> ```cpp
> string app_id()
> ```
### set\_app\_id {#set\_app\_id}

```python
def set_app_id(app_id: str) -> str
```
Set current APP ID.

| item | description |
| --- | --- |
| **param** | **app_id**: APP ID.<br>|

> C++ defination code:
> ```cpp
> string set_app_id(const string &app_id)
> ```
### get\_apps\_info\_path {#get\_apps\_info\_path}

```python
def get_apps_info_path() -> str
```
Get APP info file path.


> C++ defination code:
> ```cpp
> string get_apps_info_path()
> ```
### get\_apps\_info {#get\_apps\_info}

```python
def get_apps_info(ignore_launcher: bool = False, ignore_app_store: bool = False) -> list[APP_Info]
```
Get APP info list.

| item | description |
| --- | --- |
| **param** | **ignore_launcher**: if true, ignore launcher APP. default false.<br>**ignore_app_store**: if true, ignore app store APP. default false.<br>|
| **return** | APP info list. APP_Info object list. |

> C++ defination code:
> ```cpp
> vector<app::APP_Info> &get_apps_info(bool ignore_launcher = false, bool ignore_app_store = false)
> ```
### get\_app\_info {#get\_app\_info}

```python
def get_app_info(app_id: str) -> APP_Info
```
Get app info by app id.

| item | description |
| --- | --- |
| **return** | app.APP_Info type. |

> C++ defination code:
> ```cpp
> app::APP_Info get_app_info(const std::string &app_id)
> ```
### get\_app\_data\_path {#get\_app\_data\_path}

```python
def get_app_data_path() -> str
```
Get APP info, APP can store private data in this directory.

| item | description |
| --- | --- |
| **return** | APP data path "./data", just return the data folder in current path because APP executed in app install path or project path.<br>So, you must execute your program in you project path to use the project/data folder when you debug your APP. |

> C++ defination code:
> ```cpp
> string get_app_data_path()
> ```
### get\_app\_path {#get\_app\_path}

```python
def get_app_path(app_id: str = '') -> str
```
Get APP path.

| item | description |
| --- | --- |
| **param** | **app_id**: APP ID, if empty, return current APP path, else return the APP path by app_id.<br>|
| **return** | APP path, just return the current path because APP executed in app install path or project path.<br>So, you must execute your program in you project path to use the project/data folder when you debug your APP. |

> C++ defination code:
> ```cpp
> string get_app_path(const string &app_id = "")
> ```
### get\_tmp\_path {#get\_tmp\_path}

```python
def get_tmp_path() -> str
```
Get global temporary data path, APPs can use this path as temporary data directory.

| item | description |
| --- | --- |
| **return** | temporary data path. |

> C++ defination code:
> ```cpp
> string get_tmp_path()
> ```
### get\_share\_path {#get\_share\_path}

```python
def get_share_path() -> str
```
Get data path of share, shared data like picture and video will put in this directory

| item | description |
| --- | --- |
| **return** | share data path. |

> C++ defination code:
> ```cpp
> string get_share_path()
> ```
### get\_picture\_path {#get\_picture\_path}

```python
def get_picture_path() -> str
```
Get picture path of share, shared picture will put in this directory

| item | description |
| --- | --- |
| **return** | share picture path. |

> C++ defination code:
> ```cpp
> string get_picture_path()
> ```
### get\_video\_path {#get\_video\_path}

```python
def get_video_path() -> str
```
Get video path of share, shared video will put in this directory

| item | description |
| --- | --- |
| **return** | share video path. |

> C++ defination code:
> ```cpp
> string get_video_path()
> ```
### get\_font\_path {#get\_font\_path}

```python
def get_font_path() -> str
```
Get font path of share, shared font will put in this directory

| item | description |
| --- | --- |
| **return** | share font path. |

> C++ defination code:
> ```cpp
> string get_font_path()
> ```
### get\_icon\_path {#get\_icon\_path}

```python
def get_icon_path() -> str
```
Get icon path of share, shared icon will put in this directory

| item | description |
| --- | --- |
| **return** | share icon path. |

> C++ defination code:
> ```cpp
> string get_icon_path()
> ```
### get\_sys\_config\_kv {#get\_sys\_config\_kv}

```python
def get_sys_config_kv(item: str, key: str, value: str = '', from_cache: bool = True) -> str
```
Get system config item value.\nYou can find all supported config items in https://wiki.sipeed.com/maixpy/doc/zh/basic/app.html .

| item | description |
| --- | --- |
| **param** | **item**: name of setting item, e.g. wifi, language. more see settings APP.<br>**key**: config key, e.g. for wifi, key can be ssid, for language, key can be locale.<br>**value**: default value, if not found, return this value.<br>**from_cache**: if true, read from cache, if false, read from file.<br>|
| **return** | config value, always string type, if not found, return empty string. |

> C++ defination code:
> ```cpp
> string get_sys_config_kv(const string &item, const string &key, const string &value = "", bool from_cache = true)
> ```
### set\_sys\_config\_kv {#set\_sys\_config\_kv}

```python
def set_sys_config_kv(item: str, key: str, value: str, write_file: bool = True) -> maix.err.Err
```
Set system config item value.

| item | description |
| --- | --- |
| **attention** | It's not recommend to use this method in your APP, this method should only called by settings APP.<br>If you have to do set config in your APP, some settings will not take effect until restart APP or reboot.<br>For example, if you change wifi ssid here, wifi will not take effect until reboot, it is recommend to call wifi API to connect. |

> C++ defination code:
> ```cpp
> err::Err set_sys_config_kv(const string &item, const string &key, const string &value, bool write_file = true)
> ```
### get\_app\_config\_kv {#get\_app\_config\_kv}

```python
def get_app_config_kv(item: str, key: str, value: str = '', from_cache: bool = True) -> str
```
Get APP config item value.

| item | description |
| --- | --- |
| **param** | **item**: name of setting item, e.g. user_info<br>**key**: config key, e.g. for user_info, key can be name, age etc.<br>**value**: default value, if not found, return this value.<br>**from_cache**: if true, read from cache, if false, read from file.<br>|
| **return** | config value, always string type, if not found, return empty string. |

> C++ defination code:
> ```cpp
> string get_app_config_kv(const string &item, const string &key, const string &value = "", bool from_cache = true)
> ```
### set\_app\_config\_kv {#set\_app\_config\_kv}

```python
def set_app_config_kv(item: str, key: str, value: str, write_file: bool = True) -> maix.err.Err
```
Set APP config item value.

| item | description |
| --- | --- |
| **param** | **item**: name of setting item, e.g. user_info<br>**key**: config key, e.g. for user_info, key can be name, age etc.<br>**value**: config value, always string type.<br>**write_file**: if true, write to file, if false, just write to cache.<br>|
| **return** | err::Err |

> C++ defination code:
> ```cpp
> err::Err set_app_config_kv(const string &item, const string &key, const string &value, bool write_file = true)
> ```
### get\_app\_config\_path {#get\_app\_config\_path}

```python
def get_app_config_path() -> str
```
Get APP config path, ini format, so you can use your own ini parser to parse it like `configparser` in Python.\nAll APP config info is recommended to store in this file.

| item | description |
| --- | --- |
| **return** | APP config path(ini format). |

> C++ defination code:
> ```cpp
> string get_app_config_path()
> ```
### set\_exit\_msg {#set\_exit\_msg}

```python
def set_exit_msg(code: maix.err.Err, msg: str) -> maix.err.Err
```
Set APP exit code and exit message.\nIf code != 0, the launcher will show a dialog to user, and display the msg.

| item | description |
| --- | --- |
| **param** | **code**: exit code, 0 means success, other means error, if code is 0, do nothing.<br>**msg**: exit message, if code is 0, msg is not used.<br>|
| **return** | exit code, the same as arg @code. |

> C++ defination code:
> ```cpp
> err::Err set_exit_msg(err::Err code, const string &msg)
> ```
### get\_exit\_msg {#get\_exit\_msg}

```python
def get_exit_msg(cache: bool = False) -> tuple[str, maix.err.Err, str]
```
Get APP exit code and exit message.

| item | description |
| --- | --- |
| **param** | **cache**: if true, read from cache, if false, read from file. default false.<br>|
| **return** | exit return app_id, exit code and exit message. |

> C++ defination code:
> ```cpp
> tuple<string, err::Err, string> get_exit_msg(bool cache = false)
> ```
### have\_exit\_msg {#have\_exit\_msg}

```python
def have_exit_msg(cache: bool = False) -> bool
```
Check if have exit msg

| item | description |
| --- | --- |
| **param** | **cache**: if true, just check from cache, if false, check from file. default false.<br>|
| **return** | true if have exit msg, false if not. |

> C++ defination code:
> ```cpp
> bool have_exit_msg(bool cache = false)
> ```
### switch\_app {#switch\_app}

```python
def switch_app(app_id: str, idx: int = -1, start_param: str = '') -> None
```
Exit this APP and start another APP(by launcher).\nCall this API will call set_exit_flag(true), you should check app::need_exit() in your code.\nAnd exit this APP if app::need_exit() return true.

| item | description |
| --- | --- |
| **param** | **app_id**: APP ID which will be started. app_id and idx must have one is valid.<br>**idx**: APP index. app_id and idx must have one is valid.<br>**start_param**: string type, will send to app, app can get this param by `app.get_start_param()`<br>|
| **attention** | If app id or idx the same as current app, do nothing. |

> C++ defination code:
> ```cpp
> void switch_app(const string &app_id, int idx = -1, const std::string &start_param = "")
> ```
### get\_start\_param {#get\_start\_param}

```python
def get_start_param() -> str
```
Get start param set by caller

| item | description |
| --- | --- |
| **return** | param, string type |

> C++ defination code:
> ```cpp
> const std::string get_start_param()
> ```
### need\_exit {#need\_exit}

```python
def need_exit() -> bool
```
Shoule this APP exit?

| item | description |
| --- | --- |
| **return** | true if this APP should exit, false if not. |
| **attention** | This API is a function, not a variable. |

> C++ defination code:
> ```cpp
> bool need_exit()
> ```
### running {#running}

```python
def running() -> bool
```
App should running? The same as !app::need_exit() (not app::need_exit() in MaixPy).

| item | description |
| --- | --- |
| **return** | true if this APP should running, false if not. |
| **attention** | This API is a function, not a variable. |

> C++ defination code:
> ```cpp
> bool running()
> ```
### set\_exit\_flag {#set\_exit\_flag}

```python
def set_exit_flag(exit: bool) -> None
```
Set exit flag. You can get exit flag by app.need_exit().

| item | description |
| --- | --- |
| **param** | **exit**: true if this APP should exit, false if not.<br>|

> C++ defination code:
> ```cpp
> void set_exit_flag(bool exit)
> ```


## Class {#Class}

### Version {#Version}

APP version


> C++ defination code:
> ```cpp
> class Version
> ```

#### \_\_str\_\_ {#\_\_str\_\_}

```python
def __str__(self) -> str
```
Convert to string, e.g. 1.0.0

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string __str__()
> ```
#### from\_str {#from\_str}

```python
def from_str(version_str: str) -> Version
```
Convert from string, e.g. \"1.0.0\"

| item | description |
| --- | --- |
| **type** | func |
| **static** | True |

> C++ defination code:
> ```cpp
> static app::Version from_str(const string &version_str)
> ```
### APP\_Info {#APP\_Info}

APP info


> C++ defination code:
> ```cpp
> class APP_Info
> ```

#### id {#id}

APP id

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> string id
> ```
#### name {#name}

APP name

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> string name
> ```
#### icon {#icon}

APP icon

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> string icon
> ```
#### version {#version-2}

APP version

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> Version version
> ```
#### exec {#exec}

APP exec

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> string exec
> ```
#### author {#author}

APP author

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> string author
> ```
#### desc {#desc}

APP desc

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> string desc
> ```
#### names {#names}

APP names

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> map<string, string> names
> ```
#### descs {#descs}

APP descs

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> map<string, string> descs
> ```
