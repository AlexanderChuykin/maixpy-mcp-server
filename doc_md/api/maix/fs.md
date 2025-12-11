---
title: maix.fs
---

maix.fs module


> You can use `maix.fs` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### SEEK {#SEEK}

SEEK enums

| item | describe |
| --- | --- |
| **values** | **FS_SEEK_SET**: Seek from beginning of file.<br>**FS_SEEK_CUR**: Seek from current position.<br>**FS_SEEK_END**: Seek from end of file.<br>
> C++ defination code:
> ```cpp
> enum class SEEK
>     {
>         FS_SEEK_SET = 0,  // Seek from beginning of file.
>         FS_SEEK_CUR = 1,  // Seek from current position.
>         FS_SEEK_END = 2,  // Seek from end of file.
>     }
> ```


## Variable {#Variable}



## Function {#Function}

### isabs {#isabs}

```python
def isabs(path: str) -> bool
```
Check if the path is absolute path

| item | description |
| --- | --- |
| **param** | **path**: path to check<br>|
| **return** | true if path is absolute path |

> C++ defination code:
> ```cpp
> bool isabs(const std::string &path)
> ```
### isdir {#isdir}

```python
def isdir(path: str) -> bool
```
Check if the path is a directory, if not exist, throw exception

| item | description |
| --- | --- |
| **param** | **path**: path to check<br>|
| **return** | true if path is a directory |

> C++ defination code:
> ```cpp
> bool isdir(const std::string &path)
> ```
### isfile {#isfile}

```python
def isfile(path: str) -> bool
```
Check if the path is a file, if not exist, throw exception

| item | description |
| --- | --- |
| **param** | **path**: path to check<br>|
| **return** | true if path is a file |

> C++ defination code:
> ```cpp
> bool isfile(const std::string &path)
> ```
### islink {#islink}

```python
def islink(path: str) -> bool
```
Check if the path is a link, if not exist, throw exception

| item | description |
| --- | --- |
| **param** | **path**: path to check<br>|
| **return** | true if path is a link |

> C++ defination code:
> ```cpp
> bool islink(const std::string &path)
> ```
### symlink {#symlink}

```python
def symlink(src: str, link: str, force: bool = False) -> maix.err.Err
```
Create soft link

| item | description |
| --- | --- |
| **param** | **src**: real file path<br>**link**: link file path<br>**force**: force link, if already have link file, will delet it first then create.<br>|

> C++ defination code:
> ```cpp
> err::Err symlink(const std::string &src, const std::string &link, bool force = false)
> ```
### exists {#exists}

```python
def exists(path: str) -> bool
```
Check if the path exists

| item | description |
| --- | --- |
| **param** | **path**: path to check<br>|
| **return** | true if path exists |

> C++ defination code:
> ```cpp
> bool exists(const std::string &path)
> ```
### mkdir {#mkdir}

```python
def mkdir(path: str, exist_ok: bool = True, recursive: bool = True) -> maix.err.Err
```
Create a directory recursively

| item | description |
| --- | --- |
| **param** | **path**: path to create<br>**exist_ok**: if true, also return true if directory already exists<br>**recursive**: if true, create directory recursively, otherwise, only create one directory, default is true<br>|
| **return** | err::ERR_NONE(err.Err.ERR_NONE in MaixPy) if success, other error code if failed |

> C++ defination code:
> ```cpp
> err::Err mkdir(const std::string &path, bool exist_ok = true, bool recursive = true)
> ```
### rmdir {#rmdir}

```python
def rmdir(path: str, recursive: bool = False) -> maix.err.Err
```
Remove a directory

| item | description |
| --- | --- |
| **param** | **path**: path to remove<br>**recursive**: if true, remove directory recursively, otherwise, only remove empty directory, default is false<br>|
| **return** | err::ERR_NONE(err.Err.ERR_NONE in MaixPy) if success, other error code if failed |

> C++ defination code:
> ```cpp
> err::Err rmdir(const std::string &path, bool recursive = false)
> ```
### remove {#remove}

```python
def remove(path: str) -> maix.err.Err
```
Remove a file

| item | description |
| --- | --- |
| **param** | **path**: path to remove<br>|
| **return** | err::ERR_NONE(err.Err.ERR_NONE in MaixPy) if success, other error code if failed |

> C++ defination code:
> ```cpp
> err::Err remove(const std::string &path)
> ```
### rename {#rename}

```python
def rename(src: str, dst: str) -> maix.err.Err
```
Rename a file or directory

| item | description |
| --- | --- |
| **param** | **src**: source path<br>**dst**: destination path, if destination dirs not exist, will auto create<br>|
| **return** | err::ERR_NONE(err.Err.ERR_NONE in MaixPy) if success, other error code if failed |

> C++ defination code:
> ```cpp
> err::Err rename(const std::string &src, const std::string &dst)
> ```
### sync {#sync}

```python
def sync() -> None
```
Sync files, ensure they're wrriten to disk from RAM


> C++ defination code:
> ```cpp
> void sync()
> ```
### getsize {#getsize}

```python
def getsize(path: str) -> int
```
Get file size

| item | description |
| --- | --- |
| **param** | **path**: path to get size<br>|
| **return** | file size if success, -err::Err code if failed |

> C++ defination code:
> ```cpp
> int getsize(const std::string &path)
> ```
### dirname {#dirname}

```python
def dirname(path: str) -> str
```
Get directory name of path

| item | description |
| --- | --- |
| **param** | **path**: path to get dirname<br>|
| **return** | dirname if success, empty string if failed |

> C++ defination code:
> ```cpp
> std::string dirname(const std::string &path)
> ```
### basename {#basename}

```python
def basename(path: str) -> str
```
Get base name of path

| item | description |
| --- | --- |
| **param** | **path**: path to get basename<br>|
| **return** | basename if success, empty string if failed |

> C++ defination code:
> ```cpp
> std::string basename(const std::string &path)
> ```
### abspath {#abspath}

```python
def abspath(path: str) -> str
```
Get absolute path

| item | description |
| --- | --- |
| **param** | **path**: path to get absolute path<br>|
| **return** | absolute path if success, empty string if failed |

> C++ defination code:
> ```cpp
> std::string abspath(const std::string &path)
> ```
### getcwd {#getcwd}

```python
def getcwd() -> str
```
Get current working directory

| item | description |
| --- | --- |
| **return** | current working directory absolute path |

> C++ defination code:
> ```cpp
> std::string getcwd()
> ```
### realpath {#realpath}

```python
def realpath(path: str) -> str
```
Get realpath of path

| item | description |
| --- | --- |
| **param** | **path**: path to get realpath<br>|
| **return** | realpath if success, empty string if failed |

> C++ defination code:
> ```cpp
> std::string realpath(const std::string &path)
> ```
### splitext {#splitext}

```python
def splitext(path: str) -> list[str]
```
Get file extension

| item | description |
| --- | --- |
| **param** | **path**: path to get extension<br>|
| **return** | prefix_path and extension list if success, empty string if failed |

> C++ defination code:
> ```cpp
> std::vector<std::string> splitext(const std::string &path)
> ```
### listdir {#listdir}

```python
def listdir(path: str, recursive: bool = False, full_path: bool = False) -> list[str]
```
List files in directory

| item | description |
| --- | --- |
| **param** | **path**: path to list<br>**recursive**: if true, list recursively, otherwise, only list current directory, default is false<br>**full_path**: if true, return full path, otherwise, only return basename, default is false<br>|
| **return** | files list if success, nullptr if failed, you should manually delete it in C++. |

> C++ defination code:
> ```cpp
> std::vector<std::string> *listdir(const std::string &path, bool recursive = false, bool full_path = false)
> ```
### join {#join}

```python
def join(paths: list[str]) -> str
```
Join paths

| item | description |
| --- | --- |
| **param** | **paths**: paths to join<br>|
| **return** | joined path if success, empty string if failed |

> C++ defination code:
> ```cpp
> std::string join(const std::vector<std::string> &paths)
> ```
### open {#open}

```python
def open(path: str, mode: str) -> File
```
Open a file, and return a File object

| item | description |
| --- | --- |
| **param** | **path**: path to open<br>**mode**: open mode, support "r", "w", "a", "r+", "w+", "a+", "rb", "wb", "ab", "rb+", "wb+", "ab+"<br>|
| **return** | File object if success(need to delete object manually in C/C++), nullptr if failed |

> C++ defination code:
> ```cpp
> fs::File *open(const std::string &path, const std::string &mode)
> ```
### tempdir {#tempdir}

```python
def tempdir() -> str
```
Get temp files directory

| item | description |
| --- | --- |
| **return** | temp files directory |

> C++ defination code:
> ```cpp
> std::string tempdir()
> ```


## Class {#Class}

### File {#File}

File read write ops


> C++ defination code:
> ```cpp
> class File
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, path: str = '', mode: str = 'r') -> None
```
Construct File object

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> File(const std::string path = "", const std::string &mode = "r")
> ```
#### open {#open-2}

```python
def open(self, path: str, mode: str) -> maix.err.Err
```
Open a file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **path**: path to open<br>**mode**: open mode, support "r", "w", "a", "r+", "w+", "a+", "rb", "wb", "ab", "rb+", "wb+", "ab+"<br>|
| **return** | err::ERR_NONE(err.Err.ERR_NONE in MaixPy) if success, other error code if failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err open(const std::string &path, const std::string &mode)
> ```
#### close {#close}

```python
def close(self) -> None
```
Close a file.

| item | description |
| --- | --- |
| **type** | func |
| **attention** | not ensure data is written to disk, you can use sync() before close to ensure data is written to disk. |
| **static** | False |

> C++ defination code:
> ```cpp
> void close()
> ```
#### read {#read}

```python
def read(self, size: int) -> list[int]
```
Read data from file API2

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: max read size<br>|
| **return** | bytes data if success(need delete manually in C/C++), nullptr if failed |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint8_t> *read(int size)
> ```
#### readline {#readline}

```python
def readline(self) -> str
```
Read line from file

| item | description |
| --- | --- |
| **type** | func |
| **return** | line if success, None(nullptr in C++) if failed. You need to delete the returned object manually in C/C++. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string *readline()
> ```
#### eof {#eof}

```python
def eof(self) -> int
```
End of file or not

| item | description |
| --- | --- |
| **type** | func |
| **return** | 0 if not reach end of file, else eof. |
| **static** | False |

> C++ defination code:
> ```cpp
> int eof()
> ```
#### write {#write}

```python
def write(self, buf: list[int]) -> int
```
Write data to file API2

| item | description |
| --- | --- |
| **type** | func |
| **param** | **buf**: buffer to write<br>|
| **attention** | will not ensure data is flush to kernel or written to disk, you can use flush() to flush data to kernel,<br>and sync() to ensure data is written to disk. |
| **return** | write size if success, -err::Err code if failed |
| **static** | False |

> C++ defination code:
> ```cpp
> int write(const std::vector<uint8_t> &buf)
> ```
#### seek {#seek-2}

```python
def seek(self, offset: int, whence: int) -> int
```
Seek file position

| item | description |
| --- | --- |
| **type** | func |
| **param** | **offset**: offset to seek<br>**whence**: @see maix.fs.SEEK<br>|
| **return** | new position if success, -err::Err code if failed |
| **static** | False |

> C++ defination code:
> ```cpp
> int seek(int offset, int whence)
> ```
#### tell {#tell}

```python
def tell(self) -> int
```
Get file position

| item | description |
| --- | --- |
| **type** | func |
| **return** | file position if success, -err::Err code if failed |
| **static** | False |

> C++ defination code:
> ```cpp
> int tell()
> ```
#### size {#size}

```python
def size(self) -> int
```
Get file size

| item | description |
| --- | --- |
| **type** | func |
| **attention** | will change file seek position temporarily when get file size. |
| **return** | file size if success, -err::Err code if failed |
| **static** | False |

> C++ defination code:
> ```cpp
> int size()
> ```
#### flush {#flush}

```python
def flush(self) -> maix.err.Err
```
Flush file, ensure data is written to kernel buffer.

| item | description |
| --- | --- |
| **type** | func |
| **attention** | not ensure data is written to disk, use sync() to ensure data is written to disk. |
| **return** | err::ERR_NONE(err.Err.ERR_NONE in MaixPy) if success, other error code if failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err flush()
> ```
#### sync {#sync-2}

```python
def sync(self) -> maix.err.Err
```
Sync file, ensure data is written to disk.

| item | description |
| --- | --- |
| **type** | func |
| **return** | err::ERR_NONE(err.Err.ERR_NONE in MaixPy) if success, other error code if failed |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err sync()
> ```
