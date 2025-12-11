---
title: maix.image
---

maix.image module, image related definition and functions


> You can use `maix.image` to access this module with MaixPy
> This module is generated from [MaixPy](https://github.com/sipeed/MaixPy) and [MaixCDK](https://github.com/sipeed/MaixCDK)

## Module {#Module}

No module


## Enum {#Enum}

### Format {#Format}

Image formats

| item | describe |
| --- | --- |
| **attention** | for MaixPy firmware developers, update this enum will also need to update the fmt_size and fmt_names too !!! |
| **values** | **FMT_RGB888**: RGBRGB...RGB, R at the lowest address<br>**FMT_BGR888**: BGRBGR...BGR, B at the lowest address<br>**FMT_RGBA8888**: RGBARGBA...RGBA, R at the lowest address<br>**FMT_BGRA8888**: BGRABGRA...BGRA, B at the lowest address<br>**FMT_RGB565**: <br>**FMT_BGR565**: <br>**FMT_YUV422SP**: YYY...UVUVUV...UVUV<br>**FMT_YUV422P**: YYY...UUU...VVV<br>**FMT_YVU420SP**: YYY...VUVUVU...VUVU, NV21<br>**FMT_YUV420SP**: YYY...UVUVUV...UVUV, NV12<br>**FMT_YVU420P**: YYY...VVV...UUU<br>**FMT_YUV420P**: YYY...UUU...VVV<br>**FMT_GRAYSCALE**: <br>**FMT_BGGR6**: 6-bit Bayer format with a BGGR pattern.<br>**FMT_GBRG6**: 6-bit Bayer format with a GBRG pattern.<br>**FMT_GRBG6**: 6-bit Bayer format with a GRBG pattern.<br>**FMT_RGGB6**: 6-bit Bayer format with a RGGB pattern.<br>**FMT_BGGR8**: 8-bit Bayer format with a BGGR pattern.<br>**FMT_GBRG8**: 8-bit Bayer format with a GBRG pattern.<br>**FMT_GRBG8**: 8-bit Bayer format with a GRBG pattern.<br>**FMT_RGGB8**: 8-bit Bayer format with a RGGB pattern.<br>**FMT_BGGR10**: 10-bit Bayer format with a BGGR pattern.<br>**FMT_GBRG10**: 10-bit Bayer format with a GBRG pattern.<br>**FMT_GRBG10**: 10-bit Bayer format with a GRBG pattern.<br>**FMT_RGGB10**: 10-bit Bayer format with a RGGB pattern.<br>**FMT_BGGR12**: 12-bit Bayer format with a BGGR pattern.<br>**FMT_GBRG12**: 12-bit Bayer format with a GBRG pattern.<br>**FMT_GRBG12**: 12-bit Bayer format with a GRBG pattern.<br>**FMT_RGGB12**: 12-bit Bayer format with a RGGB pattern.<br>**FMT_UNCOMPRESSED_MAX**: <br>**FMT_COMPRESSED_MIN**: <br>**FMT_JPEG**: <br>**FMT_PNG**: <br>**FMT_COMPRESSED_MAX**: <br>**FMT_INVALID**: format not valid<br>
> C++ defination code:
> ```cpp
> enum Format
>     {
>         FMT_RGB888 = 0, // RGBRGB...RGB, R at the lowest address
>         FMT_BGR888,     // BGRBGR...BGR, B at the lowest address
>         FMT_RGBA8888,   // RGBARGBA...RGBA, R at the lowest address
>         FMT_BGRA8888,   // BGRABGRA...BGRA, B at the lowest address
>         FMT_RGB565,
>         FMT_BGR565,
>         FMT_YUV422SP, // YYY...UVUVUV...UVUV
>         FMT_YUV422P,  // YYY...UUU...VVV
>         FMT_YVU420SP, // YYY...VUVUVU...VUVU, NV21
>         FMT_YUV420SP, // YYY...UVUVUV...UVUV, NV12
>         FMT_YVU420P,  // YYY...VVV...UUU
>         FMT_YUV420P,  // YYY...UUU...VVV
>         FMT_GRAYSCALE,
>         FMT_BGGR6,      // 6-bit Bayer format with a BGGR pattern.
>         FMT_GBRG6,      // 6-bit Bayer format with a GBRG pattern.
>         FMT_GRBG6,      // 6-bit Bayer format with a GRBG pattern.
>         FMT_RGGB6,      // 6-bit Bayer format with a RGGB pattern.
>         FMT_BGGR8,      // 8-bit Bayer format with a BGGR pattern.
>         FMT_GBRG8,      // 8-bit Bayer format with a GBRG pattern.
>         FMT_GRBG8,      // 8-bit Bayer format with a GRBG pattern.
>         FMT_RGGB8,      // 8-bit Bayer format with a RGGB pattern.
>         FMT_BGGR10,     // 10-bit Bayer format with a BGGR pattern.
>         FMT_GBRG10,     // 10-bit Bayer format with a GBRG pattern.
>         FMT_GRBG10,     // 10-bit Bayer format with a GRBG pattern.
>         FMT_RGGB10,     // 10-bit Bayer format with a RGGB pattern.
>         FMT_BGGR12,     // 12-bit Bayer format with a BGGR pattern.
>         FMT_GBRG12,     // 12-bit Bayer format with a GBRG pattern.
>         FMT_GRBG12,     // 12-bit Bayer format with a GRBG pattern.
>         FMT_RGGB12,     // 12-bit Bayer format with a RGGB pattern.
>         FMT_UNCOMPRESSED_MAX,
> 
>         // compressed format below, not compressed should define upper
>         FMT_COMPRESSED_MIN,
>         FMT_JPEG,
>         FMT_PNG,
>         FMT_COMPRESSED_MAX,
> 
>         FMT_INVALID = 0xFF  // format not valid
>     }
> ```
### Fit {#Fit}

Object fit method

| item | describe |
| --- | --- |
| **values** | **FIT_NONE**: no object fit, keep original<br>**FIT_FILL**: width to new width, height to new height, may be stretch<br>**FIT_CONTAIN**: keep aspect ratio, fill blank area with black color<br>**FIT_COVER**: keep aspect ratio, crop image to fit new size<br>**FIT_MAX**: <br>
> C++ defination code:
> ```cpp
> enum Fit
>     {
>         FIT_NONE = -1, // no object fit, keep original
>         FIT_FILL = 0,  // width to new width, height to new height, may be stretch
>         FIT_CONTAIN,   // keep aspect ratio, fill blank area with black color
>         FIT_COVER,     // keep aspect ratio, crop image to fit new size
>         FIT_MAX
>     }
> ```
### ResizeMethod {#ResizeMethod}

Resize method

| item | describe |
| --- | --- |
| **values** | **NEAREST**: <br>**BILINEAR**: <br>**BICUBIC**: <br>**AREA**: <br>**LANCZOS**: <br>**HAMMING**: <br>**RESIZE_METHOD_MAX**: <br>
> C++ defination code:
> ```cpp
> enum ResizeMethod
>     {
>         NEAREST = 0,
>         BILINEAR,
>         BICUBIC,
>         AREA,
>         LANCZOS,
>         HAMMING,
>         RESIZE_METHOD_MAX
>     }
> ```
### ApriltagFamilies {#ApriltagFamilies}

Family of apriltag

| item | describe |
| --- | --- |
| **values** | **TAG16H5**: <br>**TAG25H7**: <br>**TAG25H9**: <br>**TAG36H10**: <br>**TAG36H11**: <br>**ARTOOLKIT**: <br>
> C++ defination code:
> ```cpp
> enum ApriltagFamilies
>     {
>         TAG16H5   = 1,
>         TAG25H7   = 2,
>         TAG25H9   = 4,
>         TAG36H10  = 8,
>         TAG36H11  = 16,
>         ARTOOLKIT = 32
>     }
> ```
### TemplateMatch {#TemplateMatch}

Template match method

| item | describe |
| --- | --- |
| **values** | **SEARCH_EX**: Exhaustive search<br>**SEARCH_DS**: Diamond search<br>
> C++ defination code:
> ```cpp
> enum TemplateMatch
>     {
>         SEARCH_EX,  // Exhaustive search
>         SEARCH_DS,  // Diamond search
>     }
> ```
### CornerDetector {#CornerDetector}

CornerDetector class

| item | describe |
| --- | --- |
| **values** | **CORNER_FAST**: <br>**CORNER_AGAST**: <br>
> C++ defination code:
> ```cpp
> enum CornerDetector
>     {
>         CORNER_FAST,
>         CORNER_AGAST
>     }
> ```
### EdgeDetector {#EdgeDetector}

EdgeDetector class

| item | describe |
| --- | --- |
| **values** | **EDGE_CANNY**: <br>**EDGE_SIMPLE**: <br>
> C++ defination code:
> ```cpp
> enum EdgeDetector
>     {
>         EDGE_CANNY,
>         EDGE_SIMPLE,
>     }
> ```
### FlipDir {#FlipDir}

FlipDir

| item | describe |
| --- | --- |
| **values** | **X**: <br>**Y**: <br>**XY**: <br>
> C++ defination code:
> ```cpp
> enum class FlipDir
>     {
>         X,
>         Y,
>         XY
>     }
> ```
### QRCodeDecoderType {#QRCodeDecoderType}

QRCode decode type class

| item | describe |
| --- | --- |
| **values** | **QRCODE_DECODER_TYPE_ZBAR**: <br>**QRCODE_DECODER_TYPE_QUIRC**: <br>**QRCODE_DECODER_TYPE_ZXING**: <br>
> C++ defination code:
> ```cpp
> enum class QRCodeDecoderType {
>         QRCODE_DECODER_TYPE_ZBAR,
>         QRCODE_DECODER_TYPE_QUIRC,
>         QRCODE_DECODER_TYPE_ZXING
>     }
> ```
### LineType {#LineType}

Line type class

| item | describe |
| --- | --- |
| **values** | **LINE_NORMAL**: <br>**LINE_CROSS**: <br>**LINE_T**: <br>**LINE_L**: <br>
> C++ defination code:
> ```cpp
> enum class LineType {
>         LINE_NORMAL,
>         LINE_CROSS,
>         LINE_T,
>         LINE_L,
>     }
> ```
### CMap {#CMap}

Image formats

| item | describe |
| --- | --- |
| **attention** | for MaixPy firmware developers, update this enum will also need to update the fmt_size and fmt_names too !!! |
| **values** | **TURBO**: Google-designed smooth, bright colormap; good Jet replacement for heatmaps<br>**VIRIDIS**: Default perceptually uniform colormap; colorblind-friendly and widely recommended<br>**INFERNO**: High-contrast, perceptually uniform; ideal for dark backgrounds and scientific data<br>**PLASMA**: Bright and visually appealing; perceptually uniform and colorblind-friendly<br>**CIVIDIS**: Grayscale-compatible and colorblind-safe; designed for visual accessibility<br>**CUBEHELIX**: Perceptually uniform and printable in grayscale; spirals through color space<br>**MAGMA**: Dark background-optimized; smooth gradient with good visibility in low-light visuals<br>**TWILIGHT**: Cyclic gradient; useful for circular data such as angles or phase data<br>**TWILIGHT_SHIFTED**: Phase-shifted version of Twilight; same use case but shifted zero point<br>**GREYS**: Monotonic black-to-white gradient; useful for basic grayscale visualization<br>**JET**: Classic but non-uniform RGB colormap; visually vibrant but not perceptually linear<br>**COOLWARM**: Blue-white-red diverging map; ideal for visualizing deviation from a neutral center<br>**RDYBU**: Red-white-blue diverging map; suitable for highlighting opposing directions/values<br>**SET1**: High-contrast colors; up to 9 distinct categories, ideal for class segmentation<br>**TAB10**: Matplotlib default for 10-category labeling; visually distinct and colorblind-friendly<br>**TAB20**: Matplotlib default for 20-category labeling; visually distinct and colorblind-friendly<br>**THERMAL_WHITE_HOT**: Hotter whiter; used thermal imaging mode due to its natural contrast.<br>**THERMAL_BLACK_HOT**: Hotter darker; Often used in security and tactical applications for better object detection.<br>**THERMAL_RED_HOT**: Hotter red，cooler areas dark； Emphasizes hotspots, useful for quick temperature anomaly detection.<br>**THERMAL_WHITE_HOT_SD**: White Hot SD (Smooth Detail): Enhanced White Hot with improved local contrast and smoother tone transitions.<br>Helps distinguish fine temperature differences in subtle thermal scenes.<br>**THERMAL_BLACK_HOT_SD**: Black Hot SD (Smooth Detail): Enhanced Black Hot with detail-preserving smoothing and finer thermal gradients.<br>Improves readability of dark-hot scenes with less visual noise.<br>**THERMAL_RED_HOT_SD**: Red Hot SD (Smooth Detail): Enhanced Red Hot with more gradual color changes and smoother heat spot highlighting.<br>Offers better heat trace visualization with reduced abrupt transitions.<br>**THERMAL_IRONBOW**: Ironbow: A classic thermal colormap that uses a smooth gradient from dark to bright (black → red → yellow → white).<br>Commonly used in industrial and medical thermography for better visualization.<br>**THERMAL_NIGHT**: Night: A low-brightness thermal mode optimized for night operations or low-light display environments.<br>Typically enhances visibility in high-contrast night-time scenarios.<br>**GITHUB_GREEN**: GitHub-themed green-based palette; custom usage such as contribution graphs<br>**MAX**: Total count of valid colormaps (not a colormap itself)<br>
> C++ defination code:
> ```cpp
> enum class CMap
>     {
>         // Sequential (Perceptually uniform linear gradients)
>         TURBO = 0,           // Google-designed smooth, bright colormap; good Jet replacement for heatmaps
>         VIRIDIS,             // Default perceptually uniform colormap; colorblind-friendly and widely recommended
>         INFERNO,             // High-contrast, perceptually uniform; ideal for dark backgrounds and scientific data
>         PLASMA,              // Bright and visually appealing; perceptually uniform and colorblind-friendly
>         CIVIDIS,             // Grayscale-compatible and colorblind-safe; designed for visual accessibility
>         CUBEHELIX,           // Perceptually uniform and printable in grayscale; spirals through color space
>         MAGMA,               // Dark background-optimized; smooth gradient with good visibility in low-light visuals
>         TWILIGHT,            // Cyclic gradient; useful for circular data such as angles or phase data
>         TWILIGHT_SHIFTED,    // Phase-shifted version of Twilight; same use case but shifted zero point
>         GREYS,               // Monotonic black-to-white gradient; useful for basic grayscale visualization
> 
>         // Traditional (Legacy and visually distinct maps)
>         JET,                 // Classic but non-uniform RGB colormap; visually vibrant but not perceptually linear
> 
>         // Diverging (Center-out maps for relative differences)
>         COOLWARM,            // Blue-white-red diverging map; ideal for visualizing deviation from a neutral center
>         RDYBU,               // Red-white-blue diverging map; suitable for highlighting opposing directions/values
> 
>         // Qualitative (For categorical or class label data)
>         SET1,                // High-contrast colors; up to 9 distinct categories, ideal for class segmentation
>         TAB10,               // Matplotlib default for 10-category labeling; visually distinct and colorblind-friendly
>         TAB20,               // Matplotlib default for 20-category labeling; visually distinct and colorblind-friendly
> 
>         // thermal
>         THERMAL_WHITE_HOT,   // Hotter whiter; used thermal imaging mode due to its natural contrast.
>         THERMAL_BLACK_HOT,   // Hotter darker; Often used in security and tactical applications for better object detection.
>         THERMAL_RED_HOT,     // Hotter red，cooler areas dark； Emphasizes hotspots, useful for quick temperature anomaly detection.
>         THERMAL_WHITE_HOT_SD, /* White Hot SD (Smooth Detail): Enhanced White Hot with improved local contrast and smoother tone transitions.
>                                  Helps distinguish fine temperature differences in subtle thermal scenes.
>                               */
>         THERMAL_BLACK_HOT_SD, /* Black Hot SD (Smooth Detail): Enhanced Black Hot with detail-preserving smoothing and finer thermal gradients.
>                                  Improves readability of dark-hot scenes with less visual noise.
>                               */
>         THERMAL_RED_HOT_SD,   /* Red Hot SD (Smooth Detail): Enhanced Red Hot with more gradual color changes and smoother heat spot highlighting.
>                                  Offers better heat trace visualization with reduced abrupt transitions.
>                               */
>         THERMAL_IRONBOW,      /* Ironbow: A classic thermal colormap that uses a smooth gradient from dark to bright (black → red → yellow → white).
>                                  Commonly used in industrial and medical thermography for better visualization.
>                               */
>         THERMAL_NIGHT,      /* Night: A low-brightness thermal mode optimized for night operations or low-light display environments.
>                                  Typically enhances visibility in high-contrast night-time scenarios.
>                               */
> 
>         // Special / Custom
>         GITHUB_GREEN,        // GitHub-themed green-based palette; custom usage such as contribution graphs
> 
>         MAX                 // Total count of valid colormaps (not a colormap itself)
>     }
> ```


## Variable {#Variable}

### fmt\_size {#fmt\_size}

Image format size in bytes

| item | description |
| --- | --- |
| **attention** | It's a copy of this variable in MaixPy,<br>so change it in C++ (e.g. update var in hello function) will not take effect the var inMaixPy.<br>So we add const for this var to avoid this mistake. |
| **value** | **{<br>        3,<br>        3,<br>        4,<br>        4,<br>        2,<br>        2,<br>        2,<br>        2,<br>        1.5,<br>        1.5,<br>        1.5,<br>        1.5,<br>        1, // grayscale<br>        0.75,   // 6-bit Bayer format<br>        0.75,   // 6-bit Bayer format<br>        0.75,   // 6-bit Bayer format<br>        0.75,   // 6-bit Bayer format<br>        1,      // 8-bit Bayer format<br>        1,      // 8-bit Bayer format<br>        1,      // 8-bit Bayer format<br>        1,      // 8-bit Bayer format<br>        1.25,   // 10-bit Bayer format<br>        1.25,   // 10-bit Bayer format<br>        1.25,   // 10-bit Bayer format<br>        1.25,   // 10-bit Bayer format<br>        1.5,    // 12-bit Bayer format<br>        1.5,    // 12-bit Bayer format<br>        1.5,    // 12-bit Bayer format<br>        1.5,    // 12-bit Bayer format<br>        0, // uncompereed_max<br>        0, // compressed_min<br>        1, // jpeg<br>        1, // png<br>        0, // compressed_max<br>        0  // invalid<br>        }** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const std::vector<float> fmt_size = {
>         3,
>         3,
>         4,
>         4,
>         2,
>         2,
>         2,
>         2,
>         1.5,
>         1.5,
>         1.5,
>         1.5,
>         1, // grayscale
>         0.75,   // 6-bit Bayer format
>         0.75,   // 6-bit Bayer format
>         0.75,   // 6-bit Bayer format
>         0.75,   // 6-bit Bayer format
>         1,      // 8-bit Bayer format
>         1,      // 8-bit Bayer format
>         1,      // 8-bit Bayer format
>         1,      // 8-bit Bayer format
>         1.25,   // 10-bit Bayer format
>         1.25,   // 10-bit Bayer format
>         1.25,   // 10-bit Bayer format
>         1.25,   // 10-bit Bayer format
>         1.5,    // 12-bit Bayer format
>         1.5,    // 12-bit Bayer format
>         1.5,    // 12-bit Bayer format
>         1.5,    // 12-bit Bayer format
>         0, // uncompereed_max
>         0, // compressed_min
>         1, // jpeg
>         1, // png
>         0, // compressed_max
>         0  // invalid
>         }
> ```
### fmt\_names {#fmt\_names}

Image format string.\n!!Deprecated!! Please use format_name() function instead.\nThis attribute will be removed in future.

| item | description |
| --- | --- |
| **value** | **{<br>        "RGB888",<br>        "BGR888",<br>        "RGBA8888",<br>        "BGRA8888",<br>        "RGB565",<br>        "BGR565",<br>        "YUV422SP",<br>        "YUV422P",<br>        "YVU420SP",<br>        "YUV420SP",<br>        "YVU420P",<br>        "YUV420P",<br>        "GRAYSCALE",<br>        "BGGR6",<br>        "GBRG6",<br>        "GRBG6",<br>        "RG6B6",<br>        "BGGR8",<br>        "GBRG8",<br>        "GRBG8",<br>        "RG6B8",<br>        "BGGR10",<br>        "GBRG10",<br>        "GRBG10",<br>        "RG6B10",<br>        "BGGR12",<br>        "GBRG12",<br>        "GRBG12",<br>        "RG6B12",<br>        "UNCOMPRESSED_MAX",<br>        "COMPRESSED_MIN",<br>        "JPEG",<br>        "PNG",<br>        "COMPRESSED_MAX",<br>        "INVALID"<br>        }** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const std::vector<std::string> fmt_names = {
>         "RGB888",
>         "BGR888",
>         "RGBA8888",
>         "BGRA8888",
>         "RGB565",
>         "BGR565",
>         "YUV422SP",
>         "YUV422P",
>         "YVU420SP",
>         "YUV420SP",
>         "YVU420P",
>         "YUV420P",
>         "GRAYSCALE",
>         "BGGR6",
>         "GBRG6",
>         "GRBG6",
>         "RG6B6",
>         "BGGR8",
>         "GBRG8",
>         "GRBG8",
>         "RG6B8",
>         "BGGR10",
>         "GBRG10",
>         "GRBG10",
>         "RG6B10",
>         "BGGR12",
>         "GBRG12",
>         "GRBG12",
>         "RG6B12",
>         "UNCOMPRESSED_MAX",
>         "COMPRESSED_MIN",
>         "JPEG",
>         "PNG",
>         "COMPRESSED_MAX",
>         "INVALID"
>         }
> ```
### COLOR\_WHITE {#COLOR\_WHITE}

Predefined color white

| item | description |
| --- | --- |
| **value** | **image::Color::from_rgb(255, 255, 255)** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const image::Color COLOR_WHITE = image::Color::from_rgb(255, 255, 255)
> ```
### COLOR\_BLACK {#COLOR\_BLACK}

Predefined color black

| item | description |
| --- | --- |
| **value** | **image::Color::from_rgb(0, 0, 0)** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const image::Color COLOR_BLACK = image::Color::from_rgb(0, 0, 0)
> ```
### COLOR\_RED {#COLOR\_RED}

Predefined color red

| item | description |
| --- | --- |
| **value** | **image::Color::from_rgb(255, 0, 0)** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const image::Color COLOR_RED = image::Color::from_rgb(255, 0, 0)
> ```
### COLOR\_GREEN {#COLOR\_GREEN}

Predefined color green

| item | description |
| --- | --- |
| **value** | **image::Color::from_rgb(0, 255, 0)** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const image::Color COLOR_GREEN = image::Color::from_rgb(0, 255, 0)
> ```
### COLOR\_BLUE {#COLOR\_BLUE}

Predefined color blue

| item | description |
| --- | --- |
| **value** | **image::Color::from_rgb(0, 0, 255)** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const image::Color COLOR_BLUE = image::Color::from_rgb(0, 0, 255)
> ```
### COLOR\_YELLOW {#COLOR\_YELLOW}

Predefined color yellow

| item | description |
| --- | --- |
| **value** | **image::Color::from_rgb(255, 255, 0)** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const image::Color COLOR_YELLOW = image::Color::from_rgb(255, 255, 0)
> ```
### COLOR\_PURPLE {#COLOR\_PURPLE}

Predefined color purple

| item | description |
| --- | --- |
| **value** | **image::Color::from_rgb(143, 0, 255)** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const image::Color COLOR_PURPLE = image::Color::from_rgb(143, 0, 255)
> ```
### COLOR\_ORANGE {#COLOR\_ORANGE}

Predefined color orange

| item | description |
| --- | --- |
| **value** | **image::Color::from_rgb(255, 127, 0)** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const image::Color COLOR_ORANGE = image::Color::from_rgb(255, 127, 0)
> ```
### COLOR\_GRAY {#COLOR\_GRAY}

Predefined color gray

| item | description |
| --- | --- |
| **value** | **image::Color::from_rgb(127, 127, 127)** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const image::Color COLOR_GRAY = image::Color::from_rgb(127, 127, 127)
> ```
### COLOR\_INVALID {#COLOR\_INVALID}

Predefined color invalid, for special usage.

| item | description |
| --- | --- |
| **value** | **image::Color(0, 0, 0, 0, image::Format::FMT_INVALID)** |
| **readonly**| True |

> C++ defination code:
> ```cpp
> const image::Color COLOR_INVALID = image::Color(0, 0, 0, 0, image::Format::FMT_INVALID)
> ```


## Function {#Function}

### format\_name {#format\_name}

```python
def format_name(fmt: Format) -> str
```
Get format name by format.

| item | description |
| --- | --- |
| **return** | format name string |

> C++ defination code:
> ```cpp
> std::string format_name(maix::image::Format fmt)
> ```
### resize\_map\_pos {#resize\_map\_pos}

```python
def resize_map_pos(w_in: int, h_in: int, w_out: int, h_out: int, fit: Fit, x: int, y: int, w: int = -1, h: int = -1) -> list[int]
```
map point position or rectangle position from one image size to another image size(resize)

| item | description |
| --- | --- |
| **param** | **int**: h_out target image height<br>**fit**: resize method, see maix.image.Fit<br>**x**: original point x, or rectagle left-top point's x<br>**y**: original point y, or rectagle left-top point's y<br>**w**: original rectagle width, can be -1 if not use this arg, default -1.<br>**h**: original rectagle height, can be -1 if not use this arg, default -1.<br>|
| **return** | list type, [x, y] if map point, [x, y, w, h] if resize rectangle. |

> C++ defination code:
> ```cpp
> std::vector<int> resize_map_pos(int w_in, int h_in, int w_out, int h_out, image::Fit fit, int x, int y, int w = -1, int h = -1)
> ```
### resize\_map\_pos\_reverse {#resize\_map\_pos\_reverse}

```python
def resize_map_pos_reverse(w_in: int, h_in: int, w_out: int, h_out: int, fit: Fit, x: int, y: int, w: int = -1, h: int = -1) -> list[int]
```
reverse resize_map_pos method, when we call image.resize method resiz image 'a' to image 'b', we want to known the original position on 'a' whith a knew point on 'b'

| item | description |
| --- | --- |
| **param** | **int**: h_out image height after resized<br>**fit**: resize method, see maix.image.Fit<br>**x**: point on resized image x, or rectagle left-top point's x<br>**y**: original point y, or rectagle left-top point's y<br>**w**: original rectagle width, can be -1 if not use this arg, default -1.<br>**h**: original rectagle height, can be -1 if not use this arg, default -1.<br>|
| **return** | list type, [x, y] if map point, [x, y, w, h] if resize rectangle. |

> C++ defination code:
> ```cpp
> std::vector<int> resize_map_pos_reverse(int w_in, int h_in, int w_out, int h_out, image::Fit fit, int x, int y, int w = -1, int h = -1)
> ```
### load {#load}

```python
def load(path: str, format: Format = ...) -> Image
```
Load image from file, and convert to Image object

| item | description |
| --- | --- |
| **param** | **path**: image file path<br>**format**: read as this format, if not match, will convert to this format, by default is RGB888<br>|
| **return** | Image object, if load failed, will return None(nullptr in C++), so you should care about it. |

> C++ defination code:
> ```cpp
> image::Image *load(const std::string &path, image::Format format = image::Format::FMT_RGB888)
> ```
### from\_bytes {#from\_bytes}

```python
def from_bytes(width: int, height: int, format: Format, data: maix.Bytes(bytes), copy: bool = True) -> Image
```
Create image from bytes

| item | description |
| --- | --- |
| **param** | **width**: image width<br>**height**: image height<br>**format**: image format<br>**data**: image data, if data is None, will malloc memory for image data<br>If the image is in jpeg format, data must be filled in.<br>**copy**: if true and data is not None, will copy data to new buffer, else will use data directly. default is true to avoid memory leak.<br>Use it carefully!!!<br>|
| **return** | Image object |

> C++ defination code:
> ```cpp
> image::Image *from_bytes(int width, int height, image::Format format, Bytes *data, bool copy = true)
> ```
### load\_font {#load\_font}

```python
def load_font(name: str, path: str, size: int = 16) -> maix.err.Err
```
Load font from file

| item | description |
| --- | --- |
| **param** | **name**: font name, used to identify font<br>**path**: font file path, support ttf, ttc, otf<br>**size**: font size, font height, by default is 16<br>|
| **return** | error code, err::ERR_NONE is ok, other is error |

> C++ defination code:
> ```cpp
> err::Err load_font(const std::string &name, const char *path, int size = 16)
> ```
### set\_default\_font {#set\_default\_font}

Set default font, if not call this method, default is hershey_plain

| item | description |
| --- | --- |
| **param** | **name**: font name, supported names can be get by fonts()<br>|
| **return** | error code, err::ERR_NONE is ok, other is error |

> C++ defination code:
> ```cpp
> err::Err set_default_font(const std::string &name)
> ```
### fonts {#fonts}

```python
def fonts() -> list[str]
```
Get all loaded fonts

| item | description |
| --- | --- |
| **return** | all loaded fonts, string list type |

> C++ defination code:
> ```cpp
> std::vector<std::string> *fonts()
> ```
### string\_size {#string\_size}

```python
def string_size(string: str, scale: float = 1, thickness: int = 1, font: str = '') -> Size
```
Get text rendered width and height

| item | description |
| --- | --- |
| **param** | **string**: text content<br>**scale**: font scale, by default(value is 1)<br>**thickness**: text thickness(line width), by default(value is 1)<br>|
| **return** | text rendered width and height, [width, height] |

> C++ defination code:
> ```cpp
> image::Size string_size(std::string string, float scale = 1, int thickness = 1, const std::string &font = "")
> ```
### cmap\_to\_str {#cmap\_to\_str}

```python
def cmap_to_str(cmap: CMap) -> str
```
Get the string representation of a colormap enum value.

| item | description |
| --- | --- |
| **param** | **cmap**: Colormap enum value, @see image::CMap<br>|
| **return** | Corresponding colormap name as a string. |

> C++ defination code:
> ```cpp
> std::string cmap_to_str(image::CMap cmap)
> ```
### cmap\_from\_str {#cmap\_from\_str}

```python
def cmap_from_str(name: str) -> CMap
```
Get the colormap enum value from a string name.

| item | description |
| --- | --- |
| **param** | **name**: Name of the colormap (case-insensitive).<br>|
| **return** | Corresponding colormap enum value, or throws if name is invalid. |

> C++ defination code:
> ```cpp
> image::CMap cmap_from_str(const std::string& name)
> ```
### cmap\_strs {#cmap\_strs}

```python
def cmap_strs(classify: bool = False) -> list[str]
```
Get a list of all available colormap name strings.

| item | description |
| --- | --- |
| **param** | **claasify**: cmaps for classify, wihch cmap size not equal to 256.<br>|
| **return** | Vector of all supported colormap name strings. |

> C++ defination code:
> ```cpp
> std::vector<std::string> cmap_strs(bool classify = false)
> ```
### cmap\_color {#cmap\_color}

```python
def cmap_color(gray: int, cmap: CMap) -> Color
```
Get the mapped color of a grayscale value under a specific colormap.

| item | description |
| --- | --- |
| **param** | **gray**: Grayscale value in [0, 255].<br>**cmap**: Colormap enum value to map the grayscale to color.<br>|
| **return** | The mapped image::Color. |

> C++ defination code:
> ```cpp
> image::Color cmap_color(uint8_t gray, image::CMap cmap)
> ```
### cmap\_colors {#cmap\_colors}

```python
def cmap_colors(cmap: CMap) -> list[Color]
```
Get all 256 mapped colors of a colormap.

| item | description |
| --- | --- |
| **param** | **cmap**: Colormap enum value.<br>|
| **return** | Vector of 256 image::Color values corresponding to grayscale values [0, 255].<br>Return value will alloc data, you need to delete it after use in C++. |

> C++ defination code:
> ```cpp
> std::vector<image::Color> cmap_colors(image::CMap cmap)
> ```
### cmap\_colors\_rgb {#cmap\_colors\_rgb}

```python
def cmap_colors_rgb(cmap: CMap) -> list[typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]]
```
Get all 256 mapped RGB colors of a colormap.

| item | description |
| --- | --- |
| **param** | **cmap**: Colormap enum value.<br>|
| **return** | Vector of 256 RGB arrays (each array has 3 uint8_t: R, G, B).<br>Return value is a internal table refrence. |

> C++ defination code:
> ```cpp
> const std::vector<std::array<uint8_t, 3>> &cmap_colors_rgb(image::CMap cmap)
> ```
### cv2image {#cv2image}

```python
def cv2image(array: numpy.ndarray[numpy.uint8], bgr: bool = True, copy: bool = True) -> Image
```
OpenCV Mat(numpy array object) to Image object

| item | description |
| --- | --- |
| **param** | **array**: numpy array object, must be a 3-dim or 2-dim continuous array with shape hwc or hw<br>**bgr**: if set bgr, the return image will be marked as BGR888 or BGRA8888 format(only mark, not ensure return image is real BGR format), grayscale will ignore this arg.<br>**copy**: if true, will alloc new buffer and copy data, else will directly use array's data buffer, default true.<br>Use this arg carefully, when set to false, ther array MUST keep alive until we don't use the return img of this func, or will cause program crash.<br>|
| **return** | Image object |

> C++ defination code:
> ```cpp
> image::Image *cv2image(py::array_t<uint8_t, py::array::c_style> array, bool bgr = true, bool copy = true)
> ```
### image2cv {#image2cv}

```python
def image2cv(img: Image, ensure_bgr: bool = True, copy: bool = True) -> numpy.ndarray[numpy.uint8]
```
Image object to OpenCV Mat(numpy array object)

| item | description |
| --- | --- |
| **param** | **img**: Image object, maix.image.Image type.<br>**ensure_bgr**: auto convert to BGR888 or BGRA8888 if img format is not BGR or BGRA, if set to false, will not auto convert and directly use img's data, default true.<br>If copy is false, ensure_bgr always be false.<br>**copy**: Whether alloc new image and copy data or not, if ensure_bgr and img is not bgr or bgra format, always copy,<br>if not copy, array object will directly use img's data buffer, will faster but change array will affect img's data, default true.<br>|
| **attention** | take care of ensure_bgr and copy param. |
| **return** | numpy array object |

> C++ defination code:
> ```cpp
> py::array_t<uint8_t, py::array::c_style> image2cv(image::Image *img, bool ensure_bgr = true, bool copy = true)
> ```


## Class {#Class}

### Size {#Size}

Image size type


> C++ defination code:
> ```cpp
> class Size
> ```

#### \_\_init\_\_ {#\_\_init\_\_}

```python
def __init__(self, width: int = 0, height: int = 0) -> None
```
Construct a new Size object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **width**: image width<br>**height**: image height<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Size(int width = 0, int height = 0)
> ```
#### width {#width}

```python
def width(self, width: int = -1) -> int
```
width of size

| item | description |
| --- | --- |
| **type** | func |
| **param** | **width**: set new width, if not set, only return current width<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> int width(int width = -1)
> ```
#### height {#height}

```python
def height(self, height: int = -1) -> int
```
height of size

| item | description |
| --- | --- |
| **type** | func |
| **param** | **height**: set new height, if not set, only return current height<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> int height(int height = -1)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **param** | **index**: 0 for width, 1 for height<br>|
| **return** | int& width or height |
| **static** | False |

> C++ defination code:
> ```cpp
> int &operator[](int index)
> ```
#### \_\_str\_\_ {#\_\_str\_\_}

```python
def __str__(self) -> str
```
to string

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string __str__()
> ```
### Line {#Line}

Line class


> C++ defination code:
> ```cpp
> class Line
> ```

#### \_\_init\_\_ {#\_\_init\_\_-2}

```python
def __init__(self, x1: int, y1: int, x2: int, y2: int, magnitude: int = 0, theta: int = 0, rho: int = 0) -> None
```
Line constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x1**: coordinate x1 of the straight line<br>**y1**: coordinate y1 of the straight line<br>**x2**: coordinate x2 of the straight line<br>**y2**: coordinate y2 of the straight line<br>**magnitude**: magnitude of the straight line after Hough transformation<br>**theta**: angle of the straight line after Hough transformation<br>**rho**: p-value of the straight line after Hough transformation<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Line(int x1, int y1, int x2, int y2, int magnitude = 0, int theta = 0, int rho = 0)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-2}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **param** | **index**: [0] get x1 of line<br>[1] get y1 of line<br>[2] get x2 of line<br>[3] get y2 of line<br>[4] get length of line<br>[5] get magnitude of the straight line after Hough transformation<br>[6] get angle of the straight line after Hough transformation (0-179 degrees)<br>[7] get p-value of the straight line after Hough transformation<br>|
| **return** | int& |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### x1 {#x1}

```python
def x1(self) -> int
```
get x1 of line

| item | description |
| --- | --- |
| **type** | func |
| **return** | return x1 of the line, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int x1()
> ```
#### y1 {#y1}

```python
def y1(self) -> int
```
get y1 of line

| item | description |
| --- | --- |
| **type** | func |
| **return** | return y1 of the line, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int y1()
> ```
#### x2 {#x2}

```python
def x2(self) -> int
```
get x2 of line

| item | description |
| --- | --- |
| **type** | func |
| **return** | return x2 of the line, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int x2()
> ```
#### y2 {#y2}

```python
def y2(self) -> int
```
get y2 of line

| item | description |
| --- | --- |
| **type** | func |
| **return** | return y2 of the line, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int y2()
> ```
#### length {#length}

```python
def length(self) -> int
```
get length of line

| item | description |
| --- | --- |
| **type** | func |
| **return** | return length of the line, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int length()
> ```
#### magnitude {#magnitude}

```python
def magnitude(self) -> int
```
get magnitude of the straight line after Hough transformation

| item | description |
| --- | --- |
| **type** | func |
| **return** | return magnitude, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int magnitude()
> ```
#### theta {#theta}

```python
def theta(self) -> int
```
get angle of the straight line after Hough transformation (0-179 degrees)

| item | description |
| --- | --- |
| **type** | func |
| **return** | return angle, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int theta()
> ```
#### rho {#rho}

```python
def rho(self) -> int
```
get p-value of the straight line after Hough transformation

| item | description |
| --- | --- |
| **type** | func |
| **return** | return p-value, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int rho()
> ```
### Rect {#Rect}

Rect class


> C++ defination code:
> ```cpp
> class Rect
> ```

#### \_\_init\_\_ {#\_\_init\_\_-3}

```python
def __init__(self, corners: list[list[int]], x: int, y: int, w: int, h: int, magnitude: int = 0) -> None
```
Rect constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **corners**: corners of rect<br>**x**: coordinate x of the straight line<br>**y**: coordinate y of the straight line<br>**w**: coordinate w of the straight line<br>**h**: coordinate h of the straight line<br>**magnitude**: magnitude of the straight line after Hough transformation<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Rect(std::vector<std::vector<int>> &corners, int x, int y, int w, int h, int magnitude = 0)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-3}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **param** | **index**: [0] get x of rect<br>[1] get y of rect<br>[2] get w of rect<br>[3] get h of rect<br>[4] get magnitude of the straight line after Hough transformation<br>|
| **return** | int& |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### corners {#corners}

```python
def corners(self) -> list[list[int]]
```
get corners of rect

| item | description |
| --- | --- |
| **type** | func |
| **return** | return the coordinate of the rect. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::vector<int>> corners()
> ```
#### rect {#rect-2}

```python
def rect(self) -> list[int]
```
get rectangle of rect

| item | description |
| --- | --- |
| **type** | func |
| **return** | return the rectangle of the rect. format is {x, y, w, h}, type is std::vector<int> |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> rect()
> ```
#### x {#x}

```python
def x(self) -> int
```
get x of rect

| item | description |
| --- | --- |
| **type** | func |
| **return** | return x of the rect, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int x()
> ```
#### y {#y}

```python
def y(self) -> int
```
get y of rect

| item | description |
| --- | --- |
| **type** | func |
| **return** | return y of the rect, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int y()
> ```
#### w {#w}

```python
def w(self) -> int
```
get w of rect

| item | description |
| --- | --- |
| **type** | func |
| **return** | return w of the rect, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int w()
> ```
#### h {#h}

```python
def h(self) -> int
```
get h of rect

| item | description |
| --- | --- |
| **type** | func |
| **return** | return h of the rect, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int h()
> ```
#### magnitude {#magnitude-2}

```python
def magnitude(self) -> int
```
get the rectangle’s magnitude.

| item | description |
| --- | --- |
| **type** | func |
| **return** | return magnitude, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int magnitude()
> ```
### Circle {#Circle}

circle class


> C++ defination code:
> ```cpp
> class Circle
> ```

#### \_\_init\_\_ {#\_\_init\_\_-4}

```python
def __init__(self, x: int, y: int, r: int, magnitude: int) -> None
```
Circle constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: coordinate x of the circle<br>**y**: coordinate y of the circle<br>**r**: coordinate r of the circle<br>**magnitude**: coordinate y2 of the straight line<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Circle(int x, int y, int r, int magnitude)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-4}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **param** | **index**: [0] get x of circle<br>[1] get y of circle<br>[2] get r of circle<br>[3] get magnitude of the circle after Hough transformation<br>|
| **return** | int& |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### x {#x-2}

```python
def x(self) -> int
```
get x of circle

| item | description |
| --- | --- |
| **type** | func |
| **return** | return x of the circle, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int x()
> ```
#### y {#y-2}

```python
def y(self) -> int
```
get y of circle

| item | description |
| --- | --- |
| **type** | func |
| **return** | return y of the circle, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int y()
> ```
#### r {#r}

```python
def r(self) -> int
```
get r of circle

| item | description |
| --- | --- |
| **type** | func |
| **return** | return r of the circle, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int r()
> ```
#### magnitude {#magnitude-3}

```python
def magnitude(self) -> int
```
get magnitude of the circle after Hough transformation

| item | description |
| --- | --- |
| **type** | func |
| **return** | return magnitude, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int magnitude()
> ```
### Blob {#Blob}

Blob class


> C++ defination code:
> ```cpp
> class Blob
> ```

#### \_\_init\_\_ {#\_\_init\_\_-5}

```python
def __init__(self, rect: list[int], corners: list[list[int]], mini_corners: list[list[int]], cx: float, cy: float, pixels: int, rotation: float, code: int, count: int, perimeter: int, roundness: float, x_hist_bins: list[int], y_hist_bins: list[int]) -> None
```
Blob constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **rect**: blob rect, type is std::vector<int><br>**corners**: blob corners, type is std::vector<std::vector<int>><br>**mini_corners**: blob mini_corners, type is std::vector<std::vector<int>><br>**cx**: blob center x, type is float<br>**cy**: blob center y, type is float<br>**pixels**: blob pixels, type is int<br>**rotation**: blob rotation, type is float<br>**code**: blob code, type is int<br>**count**: blob count, type is int<br>**perimeter**: blob perimeter, type is int<br>**roundness**: blob roundness, type is float<br>**x_hist_bins**: blob x_hist_bins, type is std::vector<int><br>**y_hist_bins**: blob y_hist_bins, type is std::vector<int><br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Blob(std::vector<int> &rect, std::vector<std::vector<int>> &corners, std::vector<std::vector<int>> &mini_corners,float cx, float cy, int pixels, float rotation, int code, int count, int perimeter, float roundness, std::vector<int> &x_hist_bins, std::vector<int> &y_hist_bins)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-5}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **param** | **index**: [0] Returns the blob’s bounding box x coordinate<br>[1] Returns the blob’s bounding box y coordinate<br>[2] Returns the blob’s bounding box w coordinate<br>[3] Returns the blob’s bounding box h coordinate<br>[4] Returns the number of pixels that are part of this blob<br>[5] Returns the centroid x position of the blob<br>[6] Returns the centroid y position of the blob<br>|
| **return** | int& width or height |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### corners {#corners-2}

```python
def corners(self) -> list[list[int]]
```
get blob corners

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns a list of 4 (x,y) tuples of the 4 corners of the object.<br>(x0, y0)___________(x1, y1)<br>|           |<br>|           |<br>|           |<br>|___________|<br>(x3, y3)           (x2, y2)<br>note: the order of corners may change |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::vector<int>> corners()
> ```
#### mini\_corners {#mini\_corners}

```python
def mini_corners(self) -> list[list[int]]
```
get blob mini corners

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns a list of 4 (x,y) tuples of the 4 corners than bound the min area rectangle of the blob.<br>(x0, y0)___________(x1, y1)<br>|           |<br>|           |<br>|           |<br>|___________|<br>(x3, y3)           (x2, y2)<br>note: the order of corners may change |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::vector<int>> mini_corners()
> ```
#### rect {#rect-3}

```python
def rect(self) -> list[int]
```
get blob rect

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the center coordinates and width and height of the rectangle. format is (x, y, w, h)<br>w<br>(x, y) ___________<br>|           |<br>|           |  h<br>|           |<br>|___________| |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> rect()
> ```
#### x {#x-3}

```python
def x(self) -> int
```
get blob x of the upper left coordinate

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the x coordinate of the upper left corner of the rectangle. |
| **static** | False |

> C++ defination code:
> ```cpp
> int x()
> ```
#### y {#y-3}

```python
def y(self) -> int
```
get blob y of the upper left coordinate

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the y coordinate of the upper left corner of the rectangle. |
| **static** | False |

> C++ defination code:
> ```cpp
> int y()
> ```
#### w {#w-2}

```python
def w(self) -> int
```
get blob width

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the blob’s bounding box w coordinate |
| **static** | False |

> C++ defination code:
> ```cpp
> int w()
> ```
#### h {#h-2}

```python
def h(self) -> int
```
get blob height

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the blob’s bounding box h coordinate |
| **static** | False |

> C++ defination code:
> ```cpp
> int h()
> ```
#### pixels {#pixels}

```python
def pixels(self) -> int
```
get blob pixels

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the number of pixels that are part of this blob. |
| **static** | False |

> C++ defination code:
> ```cpp
> int pixels()
> ```
#### cx {#cx}

```python
def cx(self) -> int
```
get blob center x

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the centroid x position of the blob |
| **static** | False |

> C++ defination code:
> ```cpp
> int cx()
> ```
#### cy {#cy}

```python
def cy(self) -> int
```
get blob center y

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the centroid y position of the blob |
| **static** | False |

> C++ defination code:
> ```cpp
> int cy()
> ```
#### cxf {#cxf}

```python
def cxf(self) -> float
```
get blob center x

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the centroid x position of the blob |
| **static** | False |

> C++ defination code:
> ```cpp
> float cxf()
> ```
#### cyf {#cyf}

```python
def cyf(self) -> float
```
get blob center y

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the centroid y position of the blob |
| **static** | False |

> C++ defination code:
> ```cpp
> float cyf()
> ```
#### rotation {#rotation}

```python
def rotation(self) -> float
```
get blob rotation

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the rotation of the blob in radians (float). If the blob is like a pencil or pen this value will be unique for 0-180 degrees. |
| **static** | False |

> C++ defination code:
> ```cpp
> float rotation()
> ```
#### rotation\_rad {#rotation\_rad}

```python
def rotation_rad(self) -> float
```
get blob rotation_rad

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the rotation of the blob in radians |
| **static** | False |

> C++ defination code:
> ```cpp
> float rotation_rad()
> ```
#### rotation\_deg {#rotation\_deg}

```python
def rotation_deg(self) -> int
```
get blob rotation_deg

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the rotation of the blob in degrees. |
| **static** | False |

> C++ defination code:
> ```cpp
> int rotation_deg()
> ```
#### code {#code}

```python
def code(self) -> int
```
get blob code

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns a 32-bit binary number with a bit set in it for each color threshold that’s part of this blob |
| **static** | False |

> C++ defination code:
> ```cpp
> int code()
> ```
#### count {#count}

```python
def count(self) -> int
```
get blob count

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the number of blobs merged into this blob. |
| **static** | False |

> C++ defination code:
> ```cpp
> int count()
> ```
#### perimeter {#perimeter}

```python
def perimeter(self) -> int
```
get blob merge_cnt

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the number of pixels on this blob’s perimeter. |
| **static** | False |

> C++ defination code:
> ```cpp
> int perimeter()
> ```
#### roundness {#roundness}

```python
def roundness(self) -> float
```
get blob roundness

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns a value between 0 and 1 representing how round the object is |
| **static** | False |

> C++ defination code:
> ```cpp
> float roundness()
> ```
#### elongation {#elongation}

```python
def elongation(self) -> float
```
get blob elongation

| item | description |
| --- | --- |
| **type** | func |
| **returnReturns** | a value between 0 and 1 representing how long (not round) the object is |
| **static** | False |

> C++ defination code:
> ```cpp
> float elongation()
> ```
#### area {#area}

```python
def area(self) -> int
```
get blob area

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the area of the bounding box around the blob |
| **static** | False |

> C++ defination code:
> ```cpp
> int area()
> ```
#### density {#density}

```python
def density(self) -> float
```
get blob density

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the density ratio of the blob |
| **static** | False |

> C++ defination code:
> ```cpp
> float density()
> ```
#### extent {#extent}

```python
def extent(self) -> float
```
Alias for blob.density()

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the density ratio of the blob |
| **static** | False |

> C++ defination code:
> ```cpp
> float extent()
> ```
#### compactness {#compactness}

```python
def compactness(self) -> float
```
get blob compactness

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the compactness ratio of the blob |
| **static** | False |

> C++ defination code:
> ```cpp
> float compactness()
> ```
#### solidity {#solidity}

```python
def solidity(self) -> float
```
get blob solidity

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the solidity ratio of the blob |
| **static** | False |

> C++ defination code:
> ```cpp
> float solidity()
> ```
#### convexity {#convexity}

```python
def convexity(self) -> float
```
get blob convexity

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns a value between 0 and 1 representing how convex the object is |
| **static** | False |

> C++ defination code:
> ```cpp
> float convexity()
> ```
#### x\_hist\_bins {#x\_hist\_bins}

```python
def x_hist_bins(self) -> list[int]
```
get blob x_hist_bins

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the x_hist_bins of the blob |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> x_hist_bins()
> ```
#### y\_hist\_bins {#y\_hist\_bins}

```python
def y_hist_bins(self) -> list[int]
```
get blob y_hist_bins

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the y_hist_bins of the blob |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> y_hist_bins()
> ```
#### major\_axis\_line {#major\_axis\_line}

```python
def major_axis_line(self) -> list[int]
```
get blob major_axis_line

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns a line tuple (x1, y1, x2, y2) of the minor axis of the blob. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> major_axis_line()
> ```
#### minor\_axis\_line {#minor\_axis\_line}

```python
def minor_axis_line(self) -> list[int]
```
get blob minor_axis_line

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns a line tuple (x1, y1, x2, y2) of the minor axis of the blob. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> minor_axis_line()
> ```
#### enclosing\_circle {#enclosing\_circle}

```python
def enclosing_circle(self) -> list[int]
```
get blob enclosing_circle

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns a circle tuple (x, y, r) of the circle that encloses the min area rectangle of a blob. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> enclosing_circle()
> ```
#### enclosed\_ellipse {#enclosed\_ellipse}

```python
def enclosed_ellipse(self) -> list[int]
```
get blob enclosed_ellipse

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns an ellipse tuple (x, y, rx, ry, rotation) of the ellipse that fits inside of the min area rectangle of a blob. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> enclosed_ellipse()
> ```
### QRCode {#QRCode}

QRCode class


> C++ defination code:
> ```cpp
> class QRCode
> ```

#### \_\_init\_\_ {#\_\_init\_\_-6}

```python
def __init__(self, rect: list[int], corners: list[list[int]], payload: str, version: int, ecc_level: int, mask: int, data_type: int, eci: int) -> None
```
QRCode constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **rect**: rect of corners, type is std::vector<int><br>**corners**: corners of QRCode<br>**payload**: payload of the QRCode<br>**version**: version of the QRCode<br>**ecc_level**: ecc_level of the QRCode<br>**mask**: mask of the QRCode<br>**data_type**: data_type of the QRCode<br>**eci**: eci of the QRCode<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> QRCode(std::vector<int> &rect, std::vector<std::vector<int>> &corners, std::string &payload, int version, int ecc_level, int mask, int data_type, int eci)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-6}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **param** | **index**: [0] Returns the qrcode’s bounding box x coordinate<br>[1] Returns the qrcode’s bounding box y coordinate<br>[2] Returns the qrcode’s bounding box w coordinate<br>[3] Returns the qrcode’s bounding box h coordinate<br>[4] Not support this index, try to use payload() method<br>[5] Returns the version of qrcode<br>[6] Returns the error correction level of qrcode<br>[7] Returns the mask of qrcode<br>[8] Returns the datatype of qrcode<br>[9] Returns the eci of qrcode<br>|
| **return** | int& |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### corners {#corners-3}

```python
def corners(self) -> list[list[int]]
```
get coordinate of QRCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return the coordinate of the QRCode. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::vector<int>> corners()
> ```
#### rect {#rect-4}

```python
def rect(self) -> list[int]
```
get rectangle of QRCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return the rectangle of the QRCode. format is {x, y, w, h}, type is std::vector<int> |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> rect()
> ```
#### x {#x-4}

```python
def x(self) -> int
```
get x of QRCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return x of the QRCode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int x()
> ```
#### y {#y-4}

```python
def y(self) -> int
```
get y of QRCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return y of the QRCode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int y()
> ```
#### w {#w-3}

```python
def w(self) -> int
```
get w of QRCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return w of the QRCode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int w()
> ```
#### h {#h-3}

```python
def h(self) -> int
```
get h of QRCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return h of the QRCode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int h()
> ```
#### payload {#payload}

```python
def payload(self) -> str
```
get QRCode payload

| item | description |
| --- | --- |
| **type** | func |
| **return** | return area of the QRCode |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string payload()
> ```
#### version {#version}

```python
def version(self) -> int
```
get QRCode version

| item | description |
| --- | --- |
| **type** | func |
| **return** | return version of the QRCode |
| **static** | False |

> C++ defination code:
> ```cpp
> int version()
> ```
#### ecc\_level {#ecc\_level}

```python
def ecc_level(self) -> int
```
get QRCode error correction level

| item | description |
| --- | --- |
| **type** | func |
| **return** | return error correction level of the QRCode |
| **static** | False |

> C++ defination code:
> ```cpp
> int ecc_level()
> ```
#### mask {#mask}

```python
def mask(self) -> int
```
get QRCode mask

| item | description |
| --- | --- |
| **type** | func |
| **return** | return mask of the QRCode |
| **static** | False |

> C++ defination code:
> ```cpp
> int mask()
> ```
#### data\_type {#data\_type}

```python
def data_type(self) -> int
```
get QRCode dataType

| item | description |
| --- | --- |
| **type** | func |
| **return** | return mask of the QRCode |
| **static** | False |

> C++ defination code:
> ```cpp
> int data_type()
> ```
#### eci {#eci}

```python
def eci(self) -> int
```
get QRCode eci

| item | description |
| --- | --- |
| **type** | func |
| **return** | return data of the QRCode |
| **static** | False |

> C++ defination code:
> ```cpp
> int eci()
> ```
#### is\_numeric {#is\_numeric}

```python
def is_numeric(self) -> bool
```
check QRCode is numeric

| item | description |
| --- | --- |
| **type** | func |
| **return** | return true if the result type of the QRCode is numeric |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_numeric()
> ```
#### is\_alphanumeric {#is\_alphanumeric}

```python
def is_alphanumeric(self) -> bool
```
check QRCode is alphanumeric

| item | description |
| --- | --- |
| **type** | func |
| **return** | return true if the result type of the QRCode is alphanumeric |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_alphanumeric()
> ```
#### is\_binary {#is\_binary}

```python
def is_binary(self) -> bool
```
check QRCode is binary

| item | description |
| --- | --- |
| **type** | func |
| **return** | return true if the result type of the QRCode is binary |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_binary()
> ```
#### is\_kanji {#is\_kanji}

```python
def is_kanji(self) -> bool
```
check QRCode is kanji

| item | description |
| --- | --- |
| **type** | func |
| **return** | return true if the result type of the QRCode is kanji |
| **static** | False |

> C++ defination code:
> ```cpp
> bool is_kanji()
> ```
### AprilTag {#AprilTag}

AprilTag class


> C++ defination code:
> ```cpp
> class AprilTag
> ```

#### \_\_init\_\_ {#\_\_init\_\_-7}

```python
def __init__(self, rect: list[int], corners: list[list[int]], id: int, famliy: int, centroid_x: float, centroid_y: float, rotation: float, decision_margin: float, hamming: int, goodness: float, x_translation: float, y_translation: float, z_translation: float, x_rotation: float, y_rotation: float, z_rotation: float) -> None
```
AprilTag constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **rect**: Inlucdes the top-left corner and the width and height of the rectangle. format is {x, y, w, h}, type is std::vector<int><br>**corners**: Includes the four corners of the rectangle. format is {{x0, y0}, {x1, y1}, {x2, y2}, {x3, y3}}, type is std::vector<std::vector<int>><br>**id**: The id of the AprilTag<br>**famliy**: The family of the AprilTag<br>**centroid_x**: The x coordinate of the center of the AprilTag<br>**centroid_y**: The y coordinate of the center of the AprilTag<br>**rotation**: The rotation of the AprilTag<br>**decision_margin**: The decision_margin of the AprilTag<br>**hamming**: The hamming of the AprilTag<br>**goodness**: The goodness of the AprilTag<br>**x_translation**: The x_translation of the AprilTag<br>**y_translation**: The y_translation of the AprilTag<br>**z_translation**: The z_translation of the AprilTag<br>**x_rotation**: The x_rotation of the AprilTag<br>**y_rotation**: The y_rotation of the AprilTag<br>**z_rotation**: The z_rotation of the AprilTag<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> AprilTag(std::vector<int> &rect, std::vector<std::vector<int>> &corners, int id, int famliy, float centroid_x, float centroid_y, float rotation, float decision_margin, int hamming, float goodness, float x_translation, float y_translation, float z_translation, float x_rotation, float y_rotation, float z_rotation)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-7}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **param** | **index**: [0] Returns the apriltag’s bounding box x coordinate<br>[1] Returns the apriltag’s bounding box y coordinate<br>[2] Returns the apriltag’s bounding box w coordinate<br>[3] Returns the apriltag’s bounding box h coordinate<br>[4] Returns the apriltag’s id<br>[5] Returns the apriltag’s family<br>[6] Not support<br>[7] Not support<br>[8] Not support<br>[9] Not support<br>[10] Returns the apriltag’s hamming<br>[11] Not support<br>[12] Not support<br>[13] Not support<br>[14] Not support<br>[15] Not support<br>[16] Not support<br>[17] Not support<br>|
| **return** | int& |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### corners {#corners-4}

```python
def corners(self) -> list[list[int]]
```
get coordinate of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return the coordinate of the AprilTag. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::vector<int>> corners()
> ```
#### rect {#rect-5}

```python
def rect(self) -> list[int]
```
get rectangle of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return the rectangle of the AprilTag. format is {x, y, w, h}, type is std::vector<int> |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> rect()
> ```
#### x {#x-5}

```python
def x(self) -> int
```
get x of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return x of the AprilTag, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int x()
> ```
#### y {#y-5}

```python
def y(self) -> int
```
get y of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return y of the AprilTag, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int y()
> ```
#### w {#w-4}

```python
def w(self) -> int
```
get w of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return w of the AprilTag, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int w()
> ```
#### h {#h-4}

```python
def h(self) -> int
```
get h of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return h of the AprilTag, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int h()
> ```
#### id {#id}

```python
def id(self) -> int
```
get id of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return id of the AprilTag, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int id()
> ```
#### family {#family}

```python
def family(self) -> int
```
get family of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return family of the AprilTag, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int family()
> ```
#### cx {#cx-2}

```python
def cx(self) -> int
```
get cx of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return cx of the AprilTag, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int cx()
> ```
#### cxf {#cxf-2}

```python
def cxf(self) -> float
```
get cxf of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return cxf of the AprilTag, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float cxf()
> ```
#### cy {#cy-2}

```python
def cy(self) -> int
```
get cy of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return cy of the AprilTag, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int cy()
> ```
#### cyf {#cyf-2}

```python
def cyf(self) -> float
```
get cyf of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return cyf of the AprilTag, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float cyf()
> ```
#### rotation {#rotation-2}

```python
def rotation(self) -> float
```
get rotation of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return rotation of the AprilTag, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float rotation()
> ```
#### decision\_margin {#decision\_margin}

```python
def decision_margin(self) -> float
```
Get decision_margin of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the quality of the apriltag match (0.0 - 1.0) where 1.0 is the best. |
| **static** | False |

> C++ defination code:
> ```cpp
> float decision_margin()
> ```
#### hamming {#hamming}

```python
def hamming(self) -> int
```
get hamming of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the number of accepted bit errors for this tag.<br>return 0, means 0 bit errors will be accepted.<br>1 is TAG25H7, means up to 1 bit error may be accepted<br>2 is TAG25H9, means up to 3 bit errors may be accepted<br>3 is TAG36H10, means up to 3 bit errors may be accepted<br>4 is TAG36H11, means up to 4 bit errors may be accepted<br>5 is ARTOOLKIT, means 0 bit errors will be accepted |
| **static** | False |

> C++ defination code:
> ```cpp
> int hamming()
> ```
#### goodness {#goodness}

```python
def goodness(self) -> float
```
get goodness of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return goodness of the AprilTag, type is float<br>Note: This value is always 0.0 for now. |
| **static** | False |

> C++ defination code:
> ```cpp
> float goodness()
> ```
#### x\_translation {#x\_translation}

```python
def x_translation(self) -> float
```
get x_translation of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return x_translation of the AprilTag, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float x_translation()
> ```
#### y\_translation {#y\_translation}

```python
def y_translation(self) -> float
```
get y_translation of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return y_translation of the AprilTag, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float y_translation()
> ```
#### z\_translation {#z\_translation}

```python
def z_translation(self) -> float
```
get z_translation of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return z_translation of the AprilTag, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float z_translation()
> ```
#### x\_rotation {#x\_rotation}

```python
def x_rotation(self) -> float
```
get x_rotation of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return x_rotation of the AprilTag, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float x_rotation()
> ```
#### y\_rotation {#y\_rotation}

```python
def y_rotation(self) -> float
```
get y_rotation of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return y_rotation of the AprilTag, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float y_rotation()
> ```
#### z\_rotation {#z\_rotation}

```python
def z_rotation(self) -> float
```
get z_rotation of AprilTag

| item | description |
| --- | --- |
| **type** | func |
| **return** | return z_rotation of the AprilTag, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float z_rotation()
> ```
### DataMatrix {#DataMatrix}

DataMatrix class


> C++ defination code:
> ```cpp
> class DataMatrix
> ```

#### \_\_init\_\_ {#\_\_init\_\_-8}

```python
def __init__(self, rect: list[int], corners: list[list[int]], payload: str, rotation: float, rows: int, columns: int, capacity: int, padding: int) -> None
```
DataMatrix constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **rect**: Inlucdes the top-left corner and the width and height of the rectangle. format is {x, y, w, h}, type is std::vector<int><br>**corners**: Includes the four corners of the rectangle. format is {{x0, y0}, {x1, y1}, {x2, y2}, {x3, y3}}, type is std::vector<std::vector<int>><br>**payload**: The payload of the DataMatrix<br>**rotation**: The rotation of the DataMatrix<br>**rows**: The rows of the DataMatrix<br>**columns**: The columns of the DataMatrix<br>**capacity**: The capacity of the DataMatrix<br>**padding**: The padding of the DataMatrix<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> DataMatrix(std::vector<int> &rect, std::vector<std::vector<int>> &corners, std::string &payload, float rotation, int rows, int columns, int capacity, int padding)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-8}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **param** | **index**: [0] get x of DataMatrix<br>[1] get y of DataMatrix<br>[2] get w of DataMatrix<br>[3] get h of DataMatrix<br>[4] Not support this index, try to use payload() method<br>[5] Not support this index, try to use rotation() method<br>[6] get rows of DataMatrix<br>[7] get columns of DataMatrix<br>[8] get capacity of DataMatrix<br>[9] get padding of DataMatrix<br>|
| **return** | int& |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### corners {#corners-5}

```python
def corners(self) -> list[list[int]]
```
get coordinate of DataMatrix

| item | description |
| --- | --- |
| **type** | func |
| **return** | return the coordinate of the DataMatrix. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::vector<int>> corners()
> ```
#### rect {#rect-6}

```python
def rect(self) -> list[int]
```
get rectangle of DataMatrix

| item | description |
| --- | --- |
| **type** | func |
| **return** | return the rectangle of the DataMatrix. format is {x, y, w, h}, type is std::vector<int> |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> rect()
> ```
#### x {#x-6}

```python
def x(self) -> int
```
get x of DataMatrix

| item | description |
| --- | --- |
| **type** | func |
| **return** | return x of the DataMatrix, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int x()
> ```
#### y {#y-6}

```python
def y(self) -> int
```
get y of DataMatrix

| item | description |
| --- | --- |
| **type** | func |
| **return** | return y of the DataMatrix, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int y()
> ```
#### w {#w-5}

```python
def w(self) -> int
```
get w of DataMatrix

| item | description |
| --- | --- |
| **type** | func |
| **return** | return w of the DataMatrix, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int w()
> ```
#### h {#h-5}

```python
def h(self) -> int
```
get h of DataMatrix

| item | description |
| --- | --- |
| **type** | func |
| **return** | return h of the DataMatrix, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int h()
> ```
#### payload {#payload-2}

```python
def payload(self) -> str
```
get payload of DataMatrix

| item | description |
| --- | --- |
| **type** | func |
| **return** | return payload of the DataMatrix, type is std::string |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string payload()
> ```
#### rotation {#rotation-3}

```python
def rotation(self) -> float
```
get rotation of DataMatrix

| item | description |
| --- | --- |
| **type** | func |
| **return** | return rotation of the DataMatrix, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float rotation()
> ```
#### rows {#rows}

```python
def rows(self) -> int
```
get rows of DataMatrix

| item | description |
| --- | --- |
| **type** | func |
| **return** | return rows of the DataMatrix, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int rows()
> ```
#### columns {#columns}

```python
def columns(self) -> int
```
get columns of DataMatrix

| item | description |
| --- | --- |
| **type** | func |
| **return** | return columns of the DataMatrix, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int columns()
> ```
#### capacity {#capacity}

```python
def capacity(self) -> int
```
get capacity of DataMatrix

| item | description |
| --- | --- |
| **type** | func |
| **return** | returns how many characters could fit in this data matrix, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int capacity()
> ```
#### padding {#padding}

```python
def padding(self) -> int
```
get padding of DataMatrix

| item | description |
| --- | --- |
| **type** | func |
| **return** | returns how many unused characters are in this data matrix, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int padding()
> ```
### BarCode {#BarCode}

BarCode class


> C++ defination code:
> ```cpp
> class BarCode
> ```

#### \_\_init\_\_ {#\_\_init\_\_-9}

```python
def __init__(self, rect: list[int], corners: list[list[int]], payload: str, type: int, rotation: float, quality: int) -> None
```
BarCode constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **rect**: Inlucdes the top-left corner and the width and height of the rectangle. format is {x, y, w, h}, type is std::vector<int><br>**corners**: Includes the four corners of the rectangle. format is {{x0, y0}, {x1, y1}, {x2, y2}, {x3, y3}}, type is std::vector<std::vector<int>><br>**payload**: The payload of the BarCode<br>**type**: The type of the BarCode<br>**rotation**: The rotation of the BarCode<br>**quality**: The quality of the BarCode<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> BarCode(std::vector<int> &rect, std::vector<std::vector<int>> &corners, std::string &payload, int type, float rotation, int quality)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-9}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **param** | **index**: [0] get x of BarCode<br>[1] get y of BarCode<br>[2] get w of BarCode<br>[3] get h of BarCode<br>[4] Not support this index, try to use payload() method<br>[5] get type of BarCode<br>[6] Not support this index, try to use rotation() method<br>[7] get quality of BarCode<br>|
| **return** | int& |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### corners {#corners-6}

```python
def corners(self) -> list[list[int]]
```
get coordinate of BarCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return the coordinate of the BarCode. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<std::vector<int>> corners()
> ```
#### rect {#rect-7}

```python
def rect(self) -> list[int]
```
get rectangle of BarCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return the rectangle of the BarCode. format is {x, y, w, h}, type is std::vector<int> |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> rect()
> ```
#### x {#x-7}

```python
def x(self) -> int
```
get x of BarCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return x of the BarCode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int x()
> ```
#### y {#y-7}

```python
def y(self) -> int
```
get y of BarCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return y of the BarCode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int y()
> ```
#### w {#w-6}

```python
def w(self) -> int
```
get w of BarCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return w of the BarCode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int w()
> ```
#### h {#h-6}

```python
def h(self) -> int
```
get h of BarCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return h of the BarCode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int h()
> ```
#### payload {#payload-3}

```python
def payload(self) -> str
```
get payload of BarCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return payload of the BarCode, type is std::string |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string payload()
> ```
#### type {#type}

```python
def type(self) -> int
```
get type of BarCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return type of the BarCode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int type()
> ```
#### rotation {#rotation-4}

```python
def rotation(self) -> float
```
get rotation of BarCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return rotation of the BarCode, type is float. FIXME: always return 0.0 |
| **static** | False |

> C++ defination code:
> ```cpp
> float rotation()
> ```
#### quality {#quality}

```python
def quality(self) -> int
```
get quality of BarCode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return quality of the BarCode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int quality()
> ```
### Statistics {#Statistics}

Statistics class


> C++ defination code:
> ```cpp
> class Statistics
> ```

#### \_\_init\_\_ {#\_\_init\_\_-10}

```python
def __init__(self, format: Format, l_statistics: list[int], a_statistics: list[int], b_statistics: list[int]) -> None
```
Statistics constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **format**: The statistics source image format<br>**l_statistics**: The statistics of the L channel. format is {mean, median, mode, std_dev, min, max, lq, uq}, type is std::vector<int><br>**a_statistics**: The statistics of the A channel. format is {mean, median, mode, std_dev, min, max, lq, uq}, type is std::vector<int><br>**b_statistics**: The statistics of the B channel. format is {mean, median, mode, std_dev, min, max, lq, uq}, type is std::vector<int><br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Statistics(image::Format format, std::vector<int> &l_statistics, std::vector<int> &a_statistics, std::vector<int> &b_statistics)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-10}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **param** | **index**: array index<br>|
| **return** | int& |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### format {#format-2}

```python
def format(self) -> Format
```
get format of Statistics source image

| item | description |
| --- | --- |
| **type** | func |
| **return** | return format of the Statistics source image, type is image::Format |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format format()
> ```
#### l\_mean {#l\_mean}

```python
def l_mean(self) -> int
```
get L channel mean

| item | description |
| --- | --- |
| **type** | func |
| **return** | return L channel mean, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int l_mean()
> ```
#### l\_median {#l\_median}

```python
def l_median(self) -> int
```
get L channel median

| item | description |
| --- | --- |
| **type** | func |
| **return** | return L channel median, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int l_median()
> ```
#### l\_mode {#l\_mode}

```python
def l_mode(self) -> int
```
get L channel mode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return L channel mode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int l_mode()
> ```
#### l\_std\_dev {#l\_std\_dev}

```python
def l_std_dev(self) -> int
```
get L channel std_dev

| item | description |
| --- | --- |
| **type** | func |
| **return** | return L channel std_dev, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int l_std_dev()
> ```
#### l\_min {#l\_min}

```python
def l_min(self) -> int
```
get L channel min

| item | description |
| --- | --- |
| **type** | func |
| **return** | return L channel min, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int l_min()
> ```
#### l\_max {#l\_max}

```python
def l_max(self) -> int
```
get L channel max

| item | description |
| --- | --- |
| **type** | func |
| **return** | return L channel max, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int l_max()
> ```
#### l\_lq {#l\_lq}

```python
def l_lq(self) -> int
```
get L channel lq

| item | description |
| --- | --- |
| **type** | func |
| **return** | return L channel lq, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int l_lq()
> ```
#### l\_uq {#l\_uq}

```python
def l_uq(self) -> int
```
get L channel uq

| item | description |
| --- | --- |
| **type** | func |
| **return** | return L channel uq, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int l_uq()
> ```
#### a\_mean {#a\_mean}

```python
def a_mean(self) -> int
```
get A channel mean

| item | description |
| --- | --- |
| **type** | func |
| **return** | return A channel mean, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int a_mean()
> ```
#### a\_median {#a\_median}

```python
def a_median(self) -> int
```
get A channea median

| item | description |
| --- | --- |
| **type** | func |
| **return** | return A channel median, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int a_median()
> ```
#### a\_mode {#a\_mode}

```python
def a_mode(self) -> int
```
get A channel mode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return A channel mode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int a_mode()
> ```
#### a\_std\_dev {#a\_std\_dev}

```python
def a_std_dev(self) -> int
```
get A channel std_dev

| item | description |
| --- | --- |
| **type** | func |
| **return** | return A channel std_dev, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int a_std_dev()
> ```
#### a\_min {#a\_min}

```python
def a_min(self) -> int
```
get A channel min

| item | description |
| --- | --- |
| **type** | func |
| **return** | return A channel min, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int a_min()
> ```
#### a\_max {#a\_max}

```python
def a_max(self) -> int
```
get A channel max

| item | description |
| --- | --- |
| **type** | func |
| **return** | return A channel max, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int a_max()
> ```
#### a\_lq {#a\_lq}

```python
def a_lq(self) -> int
```
get A channel lq

| item | description |
| --- | --- |
| **type** | func |
| **return** | return A channel lq, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int a_lq()
> ```
#### a\_uq {#a\_uq}

```python
def a_uq(self) -> int
```
get A channel uq

| item | description |
| --- | --- |
| **type** | func |
| **return** | return A channel uq, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int a_uq()
> ```
#### b\_mean {#b\_mean}

```python
def b_mean(self) -> int
```
get B channel mean

| item | description |
| --- | --- |
| **type** | func |
| **return** | return B channel mean, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int b_mean()
> ```
#### b\_median {#b\_median}

```python
def b_median(self) -> int
```
get B channea median

| item | description |
| --- | --- |
| **type** | func |
| **return** | return B channel median, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int b_median()
> ```
#### b\_mode {#b\_mode}

```python
def b_mode(self) -> int
```
get B channel mode

| item | description |
| --- | --- |
| **type** | func |
| **return** | return B channel mode, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int b_mode()
> ```
#### b\_std\_dev {#b\_std\_dev}

```python
def b_std_dev(self) -> int
```
get B channel std_dev

| item | description |
| --- | --- |
| **type** | func |
| **return** | return B channel std_dev, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int b_std_dev()
> ```
#### b\_min {#b\_min}

```python
def b_min(self) -> int
```
get B channel min

| item | description |
| --- | --- |
| **type** | func |
| **return** | return B channel min, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int b_min()
> ```
#### b\_max {#b\_max}

```python
def b_max(self) -> int
```
get B channel max

| item | description |
| --- | --- |
| **type** | func |
| **return** | return B channel max, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int b_max()
> ```
#### b\_lq {#b\_lq}

```python
def b_lq(self) -> int
```
get B channel lq

| item | description |
| --- | --- |
| **type** | func |
| **return** | return B channel lq, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int b_lq()
> ```
#### b\_uq {#b\_uq}

```python
def b_uq(self) -> int
```
get B channel uq

| item | description |
| --- | --- |
| **type** | func |
| **return** | return B channel uq, type is int |
| **static** | False |

> C++ defination code:
> ```cpp
> int b_uq()
> ```
### Displacement {#Displacement}

Displacement class


> C++ defination code:
> ```cpp
> class Displacement
> ```

#### \_\_init\_\_ {#\_\_init\_\_-11}

```python
def __init__(self, x_translation: float, y_translation: float, rotation: float, scale: float, response: float) -> None
```
Displacement constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x_translation**: The x_translation of the Displacement<br>**y_translation**: The y_translation of the Displacement<br>**rotation**: The rotation of the Displacement<br>**scale**: The scale of the Displacement<br>**response**: The response of the Displacement<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Displacement(float x_translation, float y_translation, float rotation, float scale, float response)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-11}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **param** | **index**: array index<br>|
| **return** | int& |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### x\_translation {#x\_translation-2}

```python
def x_translation(self) -> float
```
get x_translation of Displacement

| item | description |
| --- | --- |
| **type** | func |
| **return** | return x_translation of the Displacement, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float x_translation()
> ```
#### y\_translation {#y\_translation-2}

```python
def y_translation(self) -> float
```
get y_translation of Displacement

| item | description |
| --- | --- |
| **type** | func |
| **return** | return y_translation of the Displacement, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float y_translation()
> ```
#### rotation {#rotation-5}

```python
def rotation(self) -> float
```
get rotation of Displacement

| item | description |
| --- | --- |
| **type** | func |
| **return** | return rotation of the Displacement, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float rotation()
> ```
#### scale {#scale}

```python
def scale(self) -> float
```
get scale of Displacement

| item | description |
| --- | --- |
| **type** | func |
| **return** | return scale of the Displacement, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float scale()
> ```
#### response {#response}

```python
def response(self) -> float
```
get response of Displacement

| item | description |
| --- | --- |
| **type** | func |
| **return** | return response of the Displacement, type is float |
| **static** | False |

> C++ defination code:
> ```cpp
> float response()
> ```
### Percentile {#Percentile}

Percentile class


> C++ defination code:
> ```cpp
> class Percentile
> ```

#### \_\_init\_\_ {#\_\_init\_\_-12}

```python
def __init__(self, l_value: int, a_value: int = 0, b_value: int = 0) -> None
```
Percentile constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **l_value**: for grayscale image, it is grayscale percentile value (between 0 and 255).<br>for rgb888 image, it is l channel percentile value of lab (between 0 and 100).<br>**a_value**: for rgb888 image, it is a channel percentile value of lab format(between -128 and 127).<br>**b_value**: for rgb888 image, it is b channel percentile value of lab format(between -128 and 127).<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Percentile(int l_value, int a_value = 0, int b_value = 0)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-12}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### value {#value}

```python
def value(self) -> int
```
Return the grayscale percentile value (between 0 and 255).

| item | description |
| --- | --- |
| **type** | func |
| **return** | returns grayscale percentile value |
| **static** | False |

> C++ defination code:
> ```cpp
> int value()
> ```
#### l\_value {#l\_value}

```python
def l_value(self) -> int
```
Return the l channel percentile value of lab format (between 0 and 100).

| item | description |
| --- | --- |
| **type** | func |
| **return** | returns l channel percentile value |
| **static** | False |

> C++ defination code:
> ```cpp
> int l_value()
> ```
#### a\_value {#a\_value}

```python
def a_value(self) -> int
```
Return the a channel percentile value of lab format (between -128 and 127).

| item | description |
| --- | --- |
| **type** | func |
| **return** | returns a channel percentile value |
| **static** | False |

> C++ defination code:
> ```cpp
> int a_value()
> ```
#### b\_value {#b\_value}

```python
def b_value(self) -> int
```
Return the b channel percentile value of lab format (between -128 and 127).

| item | description |
| --- | --- |
| **type** | func |
| **return** | returns b channel percentile value |
| **static** | False |

> C++ defination code:
> ```cpp
> int b_value()
> ```
### Threshold {#Threshold}

Threshold class


> C++ defination code:
> ```cpp
> class Threshold
> ```

#### \_\_init\_\_ {#\_\_init\_\_-13}

```python
def __init__(self, l_value: int, a_value: int = 0, b_value: int = 0) -> None
```
Threshold constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **l_value**: for grayscale image, it is grayscale threshold value (between 0 and 255).<br>for rgb888 image, it is l channel threshold value of lab (between 0 and 100).<br>**a_value**: for rgb888 image, it is a channel threshold value of lab format(between -128 and 127).<br>**b_value**: for rgb888 image, it is b channel threshold value of lab format(between -128 and 127).<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Threshold(int l_value, int a_value = 0, int b_value = 0)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-13}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### value {#value-2}

```python
def value(self) -> int
```
Return the grayscale threshold value (between 0 and 255).

| item | description |
| --- | --- |
| **type** | func |
| **return** | returns grayscale threshold value |
| **static** | False |

> C++ defination code:
> ```cpp
> int value()
> ```
#### l\_value {#l\_value-2}

```python
def l_value(self) -> int
```
Return the l channel threshold value of lab format (between 0 and 100).

| item | description |
| --- | --- |
| **type** | func |
| **return** | returns l channel percentile value |
| **static** | False |

> C++ defination code:
> ```cpp
> int l_value()
> ```
#### a\_value {#a\_value-2}

```python
def a_value(self) -> int
```
Return the a channel threshold value of lab format (between -128 and 127).

| item | description |
| --- | --- |
| **type** | func |
| **return** | returns a channel percentile value |
| **static** | False |

> C++ defination code:
> ```cpp
> int a_value()
> ```
#### b\_value {#b\_value-2}

```python
def b_value(self) -> int
```
Return the b channel threshold value of lab format (between -128 and 127).

| item | description |
| --- | --- |
| **type** | func |
| **return** | returns b channel percentile value |
| **static** | False |

> C++ defination code:
> ```cpp
> int b_value()
> ```
### Histogram {#Histogram}

Histogram class


> C++ defination code:
> ```cpp
> class Histogram
> ```

#### \_\_init\_\_ {#\_\_init\_\_-14}

```python
def __init__(self, l_bin: list[float], a_bin: list[float], b_bin: list[float], format: Format = ...) -> None
```
Histogram constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **l_value**: for grayscale image, it is grayscale threshold value list (the range of element values in the list is 0 and 255).<br>for rgb888 image, it is l channel threshold value list of lab (the range of element values in the list is 0 and 100).<br>**a_value**: for rgb888 image, it is a channel threshold value list of lab format(the range of element values in the list is -128 and 127).<br>**b_value**: for rgb888 image, it is b channel threshold value list of lab format(the range of element values in the list is -128 and 127).<br>**format**: format of the source image<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Histogram(std::vector<float> l_bin, std::vector<float> a_bin, std::vector<float> b_bin, image::Format format = image::Format::FMT_RGB888)
> ```
#### \_\_getitem\_\_ {#\_\_getitem\_\_-14}

```python
def __getitem__(self, index: int) -> int
```
Subscript operator

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int &__getitem__(int index)
> ```
#### bins {#bins}

```python
def bins(self) -> list[float]
```
Returns a list of floats for the grayscale histogram.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<float> bins()
> ```
#### l\_bins {#l\_bins}

```python
def l_bins(self) -> list[float]
```
Returns a list of floats for the RGB565 histogram LAB L channel.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<float> l_bins()
> ```
#### a\_bins {#a\_bins}

```python
def a_bins(self) -> list[float]
```
Returns a list of floats for the RGB565 histogram LAB A channel.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<float> a_bins()
> ```
#### b\_bins {#b\_bins}

```python
def b_bins(self) -> list[float]
```
Returns a list of floats for the RGB565 histogram LAB B channel.

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<float> b_bins()
> ```
#### get\_percentile {#get\_percentile}

```python
def get_percentile(self, percentile: float) -> Percentile
```
Computes the CDF of the histogram channels and returns a image::Percentile object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **percentile**: the values of the histogram at the passed in percentile (0.0 - 1.0) (float).<br>So, if you pass in 0.1 this method will tell you (going from left-to-right in the histogram)<br>what bin when summed into an accumulator caused the accumulator to cross 0.1. This is useful<br>to determine min (with 0.1) and max (with 0.9) of a color distribution without outlier effects<br>ruining your results for adaptive color tracking.<br>|
| **return** | image::Percentile object |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Percentile get_percentile(float percentile)
> ```
#### get\_threshold {#get\_threshold}

```python
def get_threshold(self) -> Threshold
```
Uses Otsu’s Method to compute the optimal threshold values that split the histogram into two halves for each channel of the histogram and returns a image::Threshold object.

| item | description |
| --- | --- |
| **type** | func |
| **return** | image::Threshold object |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Threshold get_threshold()
> ```
#### get\_statistics {#get\_statistics}

```python
def get_statistics(self) -> Statistics
```
Computes the mean, median, mode, standard deviation, min, max, lower quartile, and upper quartile of each color channel in the histogram and returns a image::Statistics object.

| item | description |
| --- | --- |
| **type** | func |
| **return** | image::Statistics object |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Statistics get_statistics()
> ```
### LBPKeyPoint {#LBPKeyPoint}

LBPKeyPoint class


> C++ defination code:
> ```cpp
> class LBPKeyPoint
> ```

#### \_\_init\_\_ {#\_\_init\_\_-15}

```python
def __init__(self, data: list[int]) -> None
```
LBPKeyPoint constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: The data of the LBPKeyPoint<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> LBPKeyPoint(std::valarray<uint8_t> &data)
> ```
### KeyPoint {#KeyPoint}

KeyPoint class


> C++ defination code:
> ```cpp
> class KeyPoint
> ```

#### \_\_init\_\_ {#\_\_init\_\_-16}

```python
def __init__(self, x: int, y: int, score: int, octave: int, angle: int, matched: int, desc: list[int]) -> None
```
KeyPoint constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: The x of the KeyPoint<br>**y**: The y of the KeyPoint<br>**score**: The score of the KeyPoint<br>**octave**: The octave of the KeyPoint<br>**angle**: The angle of the KeyPoint<br>**matched**: The matched of the KeyPoint<br>**desc**: The desc of the KeyPoint<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> KeyPoint(uint16_t x, uint16_t y, uint16_t score, uint16_t octave, uint16_t angle, uint16_t matched, std::vector<uint8_t> &desc)
> ```
### KPTMatch {#KPTMatch}

KPTMatch class


> C++ defination code:
> ```cpp
> class KPTMatch
> ```

#### \_\_init\_\_ {#\_\_init\_\_-17}

```python
def __init__(self, cx: int, cy: int, x: int, y: int, w: int, h: int, score: int, theta: int, match: int) -> None
```
KPTMatch constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **cx**: The cx of the KPTMatch<br>**cy**: The cy of the KPTMatch<br>**x**: The x of the KPTMatch<br>**y**: The y of the KPTMatch<br>**w**: The w of the KPTMatch<br>**h**: The h of the KPTMatch<br>**score**: The score of the KPTMatch<br>**theta**: The theta of the KPTMatch<br>**match**: The match of the KPTMatch<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> KPTMatch(int cx, int cy, int x, int y, int w, int h, int score, int theta, int match)
> ```
### ORBKeyPoint {#ORBKeyPoint}

ORBKeyPoint class


> C++ defination code:
> ```cpp
> class ORBKeyPoint
> ```

#### \_\_init\_\_ {#\_\_init\_\_-18}

```python
def __init__(self, data: list[KeyPoint], threshold: int, normalized: bool) -> None
```
ORBKeyPoint constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: The data of the ORBKeyPoint<br>**threshold**: The threshold of the ORBKeyPoint<br>**normalized**: The normalized of the ORBKeyPoint<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> ORBKeyPoint(std::vector<image::KeyPoint> &data, int threshold, bool normalized)
> ```
#### get\_data {#get\_data}

```python
def get_data(self) -> list[KeyPoint]
```
get data of ORBKeyPoint

| item | description |
| --- | --- |
| **type** | func |
| **return** | return data of the ORBKeyPoint, type is std::vector<KeyPoint> |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::KeyPoint> get_data()
> ```
### HaarCascade {#HaarCascade}

HaarCascade class


> C++ defination code:
> ```cpp
> class HaarCascade
> ```

#### \_\_init\_\_ {#\_\_init\_\_-19}

```python
def __init__(self) -> None
```
HaarCascade constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **data**: The data of the HaarCascade<br>**threshold**: The threshold of the HaarCascade<br>**normalized**: The normalized of the HaarCascade<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> HaarCascade()
> ```
### LineGroup {#LineGroup}

LineGroup class


> C++ defination code:
> ```cpp
> class LineGroup
> ```

#### \_\_init\_\_ {#\_\_init\_\_-20}

```python
def __init__(self, id: int, type: LineType, lines: list[Line]) -> None
```
LineGroup constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **id**: The id of line<br>**type**: The line list type, @see image::LineType<br>**lines**: The line list<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> LineGroup(int id, image::LineType type, std::vector<image::Line> lines)
> ```
#### id {#id-2}

```python
def id(self) -> int
```
Get the line id of group, first id is 0.

| item | description |
| --- | --- |
| **type** | func |
| **return** | return id |
| **static** | False |

> C++ defination code:
> ```cpp
> int id()
> ```
#### type {#type-2}

```python
def type(self) -> LineType
```
Get the line type of group

| item | description |
| --- | --- |
| **type** | func |
| **return** | returns line type. @see LineType |
| **static** | False |

> C++ defination code:
> ```cpp
> image::LineType type()
> ```
#### lines {#lines}

```python
def lines(self) -> list[Line]
```
Get a list of line

| item | description |
| --- | --- |
| **type** | func |
| **return** | returns a list composed of Line objects |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::Line> lines()
> ```
### Color {#Color}

Color class


> C++ defination code:
> ```cpp
> class Color
> ```

#### \_\_init\_\_ {#\_\_init\_\_-21}

```python
def __init__(self, ch1: int, ch2: int = 0, ch3: int = 0, alpha: float = 0, format: Format = ...) -> None
```
Color constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **alpha**: alpha channel, value range: 0 ~ 1, 0 means transparent.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Color(uint8_t ch1, uint8_t ch2 = 0, uint8_t ch3 = 0, float alpha = 0, image::Format format = image::FMT_GRAYSCALE)
> ```
#### r {#r-2}

Color red channel

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint8_t r
> ```
#### g {#g}

Color green channel

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint8_t g
> ```
#### b {#b}

Color blue channel

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint8_t b
> ```
#### alpha {#alpha}

Color alpha channel, value from 0.0 to 1.0, float value, 0 means transparent.

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> float alpha
> ```
#### gray {#gray}

Color gray channel

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> uint8_t gray
> ```
#### format {#format-3}

Color format

| item | description |
| --- | --- |
| **type** | var |
| **static** | False |
| **readonly** | False |

> C++ defination code:
> ```cpp
> image::Format format
> ```
#### hex {#hex}

```python
def hex(self) -> int
```
Get color's hex value

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> uint32_t hex()
> ```
#### from\_rgb {#from\_rgb}

```python
def from_rgb(r: int, g: int, b: int) -> Color
```
Create Color object from RGB channels

| item | description |
| --- | --- |
| **type** | func |
| **static** | True |

> C++ defination code:
> ```cpp
> static image::Color from_rgb(uint8_t r, uint8_t g, uint8_t b)
> ```
#### from\_bgr {#from\_bgr}

```python
def from_bgr(b: int, g: int, r: int) -> Color
```
Create Color object from BGR channels

| item | description |
| --- | --- |
| **type** | func |
| **static** | True |

> C++ defination code:
> ```cpp
> static image::Color from_bgr(uint8_t b, uint8_t g, uint8_t r)
> ```
#### from\_gray {#from\_gray}

```python
def from_gray(gray: int) -> Color
```
Create Color object from gray channel

| item | description |
| --- | --- |
| **type** | func |
| **static** | True |

> C++ defination code:
> ```cpp
> static image::Color from_gray(uint8_t gray)
> ```
#### from\_rgba {#from\_rgba}

```python
def from_rgba(r: int, g: int, b: int, alpha: float) -> Color
```
Create Color object from RGBA channels

| item | description |
| --- | --- |
| **type** | func |
| **param** | **alpha**: alpha channel, float value, value range: 0 ~ 1<br>|
| **static** | True |

> C++ defination code:
> ```cpp
> static image::Color from_rgba(uint8_t r, uint8_t g, uint8_t b, float alpha)
> ```
#### from\_bgra {#from\_bgra}

```python
def from_bgra(b: int, g: int, r: int, alpha: float) -> Color
```
Create Color object from BGRA channels

| item | description |
| --- | --- |
| **type** | func |
| **param** | **alpha**: alpha channel, float value, value range: 0 ~ 1<br>|
| **static** | True |

> C++ defination code:
> ```cpp
> static image::Color from_bgra(uint8_t b, uint8_t g, uint8_t r, float alpha)
> ```
#### from\_hex {#from\_hex}

```python
def from_hex(hex: int, format: Format) -> Color
```
Create Color object from hex value

| item | description |
| --- | --- |
| **type** | func |
| **param** | **hex**: hex value, e.g. 0x0000FF00, lower address if first channel<br>**format**: color format, @see image::Format<br>|
| **static** | True |

> C++ defination code:
> ```cpp
> static image::Color from_hex(uint32_t hex, image::Format &format)
> ```
#### to\_format {#to\_format}

```python
def to_format(self, format: Format) -> None
```
Convert Color format

| item | description |
| --- | --- |
| **type** | func |
| **param** | **format**: format want to convert to, @see image::Format, only support RGB888, BGR888, RGBA8888, BGRA8888, GRAYSCALE.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> void to_format(const image::Format &format)
> ```
#### to\_format2 {#to\_format2}

```python
def to_format2(self, format: Format) -> Color
```
Convert color format and return a new Color object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **format**: format want to convert to, @see image::Format, only support RGB888, BGR888, RGBA8888, BGRA8888, GRAYSCALE.<br>|
| **return** | new Color object, you need to delete it manually in C++. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Color *to_format2(const image::Format &format)
> ```
### Image {#Image}

Image class


> C++ defination code:
> ```cpp
> class Image
> ```

#### \_\_init\_\_ {#\_\_init\_\_-22}

```python
def __init__(self, width: int, height: int, format: Format = ..., bg: Color = ...) -> None
```
Image constructor

| item | description |
| --- | --- |
| **type** | func |
| **param** | **width**: image width, should > 0<br>**height**: image height, should > 0<br>**format**: image format @see image::Format<br>**bg**: background color, default is black, grayscale color will be faster,<br>if bg is image.COLOR_INVALID, will not fill background color, so background may be garbage(random content).<br>So you can set to image.COLOR_INVALID to save time in some case.<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> Image(int width, int height, image::Format format = image::Format::FMT_RGB888, const image::Color &bg = image::COLOR_INVALID)
> ```
#### format {#format-4}

```python
def format(self) -> Format
```
Get image's format

| item | description |
| --- | --- |
| **type** | func |
| **see** | image.Format |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Format format()
> ```
#### size {#size-2}

```python
def size(self) -> Size
```
Get image's size, [width, height]

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Size size()
> ```
#### data\_size {#data\_size}

```python
def data_size(self) -> int
```
Get image's data size

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int data_size()
> ```
#### width {#width-2}

```python
def width(self) -> int
```
Get image's width

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int width()
> ```
#### height {#height-2}

```python
def height(self) -> int
```
Get image's height

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> int height()
> ```
#### \_\_str\_\_ {#\_\_str\_\_-2}

```python
def __str__(self) -> str
```
To string method

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string __str__()
> ```
#### to\_str {#to\_str}

```python
def to_str(self) -> str
```
To string method

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> std::string to_str()
> ```
#### get\_pixel {#get\_pixel}

```python
def get_pixel(self, x: int, y: int, rgbtuple: bool = False) -> list[int]
```
Get pixel of image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: pixel's coordinate x. x must less than image's width<br>**y**: pixel's coordinate y. y must less than image's height<br>**rgbtuple**: switch return value method. rgbtuple decides whether to split the return or not. default is false.<br>|
| **return** | pixel value,<br>According to image format and rgbtuple, return different value:<br>format is FMT_RGB888, rgbtuple is true, return [R, G, B]; rgbtuple is false, return [RGB]<br>foramt is FMT_BGR888, rgbtuple is true, return [B, G, R]; rgbtuple is false, return [BGR]<br>format is FMT_GRAYSCALE, return [GRAY]; |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<uint32_t> get_pixel(int x, int y, bool rgbtuple = false)
> ```
#### set\_pixel {#set\_pixel}

```python
def set_pixel(self, x: int, y: int, pixel: list[int]) -> maix.err.Err
```
Set pixel of image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: pixel's coordinate x. x must less than image's width<br>**y**: pixel's coordinate y. y must less than image's height<br>**pixel**: pixel value, according to image format and size of pixel, has different operation:<br>format is FMT_RGB888, pixel size must be 1 or 3, if size is 1, will split pixel[0] to [R, G, B]; if size is 3, will use pixel directly<br>format is FMT_BGR888, pixel size must be 1 or 3, if size is 1, will split pixel[0] to [B, G, R]; if size is 3, will use pixel directly<br>format is FMT_GRAYSCALE, pixel size must be 1, will use pixel directly<br>|
| **return** | error code, Err::ERR_NONE is ok, other is error |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err set_pixel(int x, int y, std::vector<uint32_t> pixel)
> ```
#### to\_tensor {#to\_tensor}

```python
def to_tensor(self, chw: bool = False, copy: bool = True) -> maix.tensor.Tensor
```
Convert Image object to tensor::Tensor object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **chw**: convert to tensor with CHW or HWC layout result, image is HWC,<br>so default chw is false, if set true, will convert to CHW layout.<br>Attention, if set chw to true, copy must be true, or will raise err.Exception.<br>**copy**: if true, will alloc memory for tensor data, else will use the memory of Image object.<br>Attention, if set chw to true, copy must be true, or will raise err.Exception.<br>|
| **return** | tensor::Tensor object pointer, an allocated tensor object |
| **static** | False |

> C++ defination code:
> ```cpp
> tensor::Tensor *to_tensor(bool chw = false, bool copy = true)
> ```
#### to\_tensor\_float32 {#to\_tensor\_float32}

```python
def to_tensor_float32(self, chw: bool = False, mean: list[float] = [], scale: list[float] = []) -> maix.tensor.Tensor
```
Convert image to float32 tensor, and support normlize with mean and scale(1/std).\nIf mean and scale not empty, Will execute (data - mean) * scale, and return float32 tensor.Tensor.

| item | description |
| --- | --- |
| **type** | func |
| **attention** | only support grayscale, RGB, BGR, RGBA, BGRA image. |
| **param** | **chw**: convert to chw layout or not, default false.<br>**mean**: mean value, list type, can be on or three elements according to image's format. Default empty means not normalize.<br>**scale**: scale value, list type, can be on or three elements according to image's format.  Default empty means not normalize.<br>|
| **return** | float32 tensor.Tensor object with new alloc memory, so you need to delete it manually in C++. |
| **static** | False |

> C++ defination code:
> ```cpp
> tensor::Tensor * to_tensor_float32(bool chw = false, std::vector<float> mean = std::vector<float>(), std::vector<float> scale = std::vector<float>())
> ```
#### to\_bytes {#to\_bytes}

```python
def to_bytes(*args, **kwargs)
```
Get image's data and convert to array bytes

| item | description |
| --- | --- |
| **type** | func |
| **param** | **copy**: if true, will alloc memory and copy data to new buffer,<br>else will use the memory of Image object, delete bytes object will not affect Image object，<br>but delete Image object will make bytes object invalid, it may cause program crash !!!!<br>So use this param carefully.<br>|
| **return** | image's data bytes, need be delete by caller in C++. |
| **static** | False |

> C++ defination code:
> ```cpp
> Bytes *to_bytes(bool copy = true)
> ```
#### to\_format {#to\_format-2}

```python
def to_format(self, format: Format) -> Image
```
Convert image to specific format

| item | description |
| --- | --- |
| **type** | func |
| **param** | **format**: format want to convert to, @see image::Format, only support RGB888, BGR888, RGBA8888, BGRA8888, GRAYSCALE, JPEG.<br>|
| **return** | new image object. Need be delete by caller in C++. |
| **throw** | err.Exception, if two images' format not support, **or already the format**, will raise exception |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *to_format(const image::Format &format)
> ```
#### to\_jpeg {#to\_jpeg}

```python
def to_jpeg(self, quality: int = 95, buff: capsule = None, buff_size: int = 0) -> Image
```
Convert image to jpeg

| item | description |
| --- | --- |
| **type** | func |
| **param** | **quality**: the quality of jpg, default is 95. For MaixCAM supported range is (50, 100], if <= 50 will be fixed to 51.<br>**buff**: user's buffer, if buff is nullptr, will malloc memory for new image data, else will use buff directly<br>**buff_size**: the size of buff, if buff is nullptr, buff_size is ignored.<br>|
| **return** | new image object. Need be delete by caller in C++. |
| **throw** | err.Exception, if two images' format not support, **or already the format**, will raise exception |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *to_jpeg(int quality = 95, void *buff = nullptr, size_t buff_size = 0)
> ```
#### draw\_image {#draw\_image}

```python
def draw_image(self, x: int, y: int, img: Image) -> Image
```
Draw image on this image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: left top corner of image point's coordinate x<br>**y**: left top corner of image point's coordinate y<br>**img**: image object to draw, the caller's channel must <= the args' channel,<br>e.g. caller is RGB888, args is RGBA8888, will throw exception, but caller is RGBA8888, args is RGB888 or RGBA8888 is ok<br>|
| **return** | this image object self |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *draw_image(int x, int y, image::Image &img)
> ```
#### draw\_rect {#draw\_rect}

```python
def draw_rect(self, x: int, y: int, w: int, h: int, color: Color, thickness: int = 1) -> Image
```
Fill rectangle color to image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: left top corner of rectangle point's coordinate x<br>**y**: left top corner of rectangle point's coordinate y<br>**w**: rectangle width<br>**h**: rectangle height<br>**color**: rectangle color<br>**thickness**: rectangle thickness(line width), by default(value is 1), -1 means fill rectangle<br>|
| **return** | this image object self |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *draw_rect(int x, int y, int w, int h, const image::Color &color, int thickness = 1)
> ```
#### draw\_line {#draw\_line}

```python
def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: Color, thickness: int = 1) -> Image
```
Draw line on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x1**: start point's coordinate x<br>**y1**: start point's coordinate y<br>**x2**: end point's coordinate x<br>**y2**: end point's coordinate y<br>**color**: line color @see image::Color<br>**thickness**: line thickness(line width), by default(value is 1)<br>|
| **return** | this image object self |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *draw_line(int x1, int y1, int x2, int y2, const image::Color &color, int thickness = 1)
> ```
#### draw\_circle {#draw\_circle}

```python
def draw_circle(self, x: int, y: int, radius: int, color: Color, thickness: int = 1) -> Image
```
Draw circle on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: circle center point's coordinate x<br>**y**: circle center point's coordinate y<br>**radius**: circle radius<br>**color**: circle color @see image::Color<br>**thickness**: circle thickness(line width), default -1 means fill circle<br>|
| **return** | this image object self |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *draw_circle(int x, int y, int radius, const image::Color &color, int thickness = 1)
> ```
#### draw\_ellipse {#draw\_ellipse}

```python
def draw_ellipse(self, x: int, y: int, a: int, b: int, angle: float, start_angle: float, end_angle: float, color: Color, thickness: int = 1) -> Image
```
Draw ellipse on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: ellipse center point's coordinate x<br>**y**: ellipse center point's coordinate y<br>**a**: ellipse major axis length<br>**b**: ellipse minor axis length<br>**angle**: ellipse rotation angle<br>**start_angle**: ellipse start angle<br>**end_angle**: ellipse end angle<br>**color**: ellipse color @see image::Color<br>**thickness**: ellipse thickness(line width), by default(value is 1), -1 means fill ellipse<br>|
| **return** | this image object self |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *draw_ellipse(int x, int y, int a, int b, float angle, float start_angle, float end_angle, const image::Color &color, int thickness = 1)
> ```
#### draw\_string {#draw\_string}

```python
def draw_string(self, x: int, y: int, textstring: str, color: Color = ..., scale: float = 1, thickness: int = -1, wrap: bool = True, wrap_space: int = 4, font: str = '') -> Image
```
Draw text on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: text left top point's coordinate x<br>**y**: text left top point's coordinate y<br>**string**: text content<br>**color**: text color @see image::Color, default is white<br>**scale**: font scale, by default(value is 1)<br>**thickness**: text thickness(line width), if negative, the glyph is filled, by default(value is -1)<br>**wrap**: if true, will auto wrap text to next line if text width > image width, by default(value is true)<br>|
| **return** | this image object self |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *draw_string(int x, int y, const std::string &textstring, const image::Color &color = image::COLOR_WHITE, float scale = 1, int thickness = -1,
>                                 bool wrap = true, int wrap_space = 4, const std::string &font = "")
> ```
#### draw\_cross {#draw\_cross}

```python
def draw_cross(self, x: int, y: int, color: Color, size: int = 5, thickness: int = 1) -> Image
```
Draw cross on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: cross center point's coordinate x<br>**y**: cross center point's coordinate y<br>**color**: cross color @see image::Color<br>**size**: how long the lines of the cross extend, by default(value is 5). So the line length is `2 * size + thickness`<br>**thickness**: cross thickness(line width), by default(value is 1)<br>|
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *draw_cross(int x, int y, const image::Color &color, int size = 5, int thickness = 1)
> ```
#### draw\_arrow {#draw\_arrow}

```python
def draw_arrow(self, x0: int, y0: int, x1: int, y1: int, color: Color, thickness: int = 1) -> Image
```
Draw arrow on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x0**: start coordinate of the arrow x0<br>**y0**: start coordinate of the arrow y0<br>**x1**: end coordinate of the arrow x1<br>**y1**: end coordinate of the arrow y1<br>**color**: cross color @see image::Color<br>**thickness**: cross thickness(line width), by default(value is 1)<br>|
| **return** | this image object self |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *draw_arrow(int x0, int y0, int x1, int y1, const image::Color &color, int thickness = 1)
> ```
#### draw\_edges {#draw\_edges}

```python
def draw_edges(self, corners: list[list[int]], color: Color, size: int = 0, thickness: int = 1, fill: bool = False) -> Image
```
Draw edges on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **corners**: edges, [[x0, y0], [x1, y1], [x2, y2], [x3, y3]]<br>**color**: edges color @see image::Color<br>**size**: the circle of radius size. TODO: support in the future<br>**thickness**: edges thickness(line width), by default(value is 1)<br>**fill**: if true, will fill edges, by default(value is false)<br>|
| **return** | this image object self |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *draw_edges(std::vector<std::vector<int>> corners, const image::Color &color, int size = 0, int thickness = 1, bool fill = false)
> ```
#### draw\_keypoints {#draw\_keypoints}

```python
def draw_keypoints(self, keypoints: list[int], color: Color, size: int = 4, thickness: int = -1, line_thickness: int = 0) -> Image
```
Draw keypoints on image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **keypoints**: keypoints, [x1, y1, x2, y2...] or [x, y, rotation_andle_in_degrees, x2, y2, rotation_andle_in_degrees2](TODO: rotation_andle_in_degrees support in the future)<br>**color**: keypoints color @see image::Color<br>**size**: size of keypoints(radius)<br>**thickness**: keypoints thickness(line width), by default(value is -1 means fill circle)<br>**line_thickness**: line thickness, default 0 means not draw lines, > 0 will draw lines connect points.<br>|
| **return** | this image object self |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *draw_keypoints(const std::vector<int> &keypoints, const image::Color &color, int size = 4, int thickness = -1, int line_thickness = 0)
> ```
#### resize {#resize}

```python
def resize(self, width: int, height: int, fit: Fit = ..., method: ResizeMethod = ...) -> Image
```
Resize image, will create a new resized image object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **width**: new width, if value is -1, will use height to calculate aspect ratio<br>**height**: new height, if value is -1, will use width to calculate aspect ratio<br>**fit**: fill, contain, cover, by default is fill<br>**method**: resize method, by default is NEAREST<br>|
| **return** | Always return a new resized image object even size not change, So in C++ you should take care of the return value to avoid memory leak.<br>And it's better to judge whether the size has changed before calling this function to make the program more efficient.<br>e.g.<br>if img->width() != width || img->height() != height:<br>img = img->resize(width, height); |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *resize(int width, int height, image::Fit fit = image::Fit::FIT_FILL, image::ResizeMethod method = image::ResizeMethod::NEAREST)
> ```
#### affine {#affine}

```python
def affine(self, src_points: list[int], dst_points: list[int], width: int = -1, height: int = -1, method: ResizeMethod = ...) -> Image
```
Affine transform image, will create a new transformed image object, need 3 points.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **src_points**: three source points, [x1, y1, x2, y2, x3, y3]<br>**dst_points**: three destination points, [x1, y1, x2, y2, x3, y3]<br>**width**: new width, if value is -1, will use height to calculate aspect ratio<br>**height**: new height, if value is -1, will use width to calculate aspect ratio<br>**method**: resize method, by default is bilinear<br>|
| **return** | new transformed image object |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *affine(std::vector<int> src_points, std::vector<int> dst_points, int width = -1, int height = -1, image::ResizeMethod method = image::ResizeMethod::BILINEAR)
> ```
#### perspective {#perspective}

```python
def perspective(self, src_points: list[int], dst_points: list[int], width: int = -1, height: int = -1, method: ResizeMethod = ...) -> Image
```
Perspective transform image, will create a new transformed image object, need 4 points.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **src_points**: three source points, [x1, y1, x2, y2, x3, y3, x4, y4]<br>**dst_points**: three destination points, [x1, y1, x2, y2, x3, y3, x4, y4]<br>**width**: new width, if value is -1, will use height to calculate aspect ratio<br>**height**: new height, if value is -1, will use width to calculate aspect ratio<br>**method**: resize method, by default is bilinear<br>|
| **return** | new transformed image object |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image* perspective(std::vector<int> src_points, std::vector<int> dst_points, int width = -1, int height = -1, image::ResizeMethod method = image::ResizeMethod::BILINEAR)
> ```
#### copy {#copy}

```python
def copy(self) -> Image
```
Copy image, will create a new copied image object

| item | description |
| --- | --- |
| **type** | func |
| **return** | new copied image object |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *copy()
> ```
#### crop {#crop}

```python
def crop(self, x: int, y: int, w: int, h: int) -> Image
```
Crop image, will create a new cropped image object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: left top corner of crop rectangle point's coordinate x<br>**y**: left top corner of crop rectangle point's coordinate y<br>**w**: crop rectangle width<br>**h**: crop rectangle height<br>|
| **return** | new cropped image object |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *crop(int x, int y, int w, int h)
> ```
#### rotate {#rotate}

```python
def rotate(self, angle: float, width: int = -1, height: int = -1, method: ResizeMethod = ...) -> Image
```
Rotate image, will create a new rotated image object

| item | description |
| --- | --- |
| **type** | func |
| **param** | **angle**: anti-clock wise rotate angle, if angle is 90 or 270, and width or height is -1, will swap width and height, or will throw exception<br>**width**: new width, if value is -1, will use height to calculate aspect ratio<br>**height**: new height, if value is -1, will use width to calculate aspect ratio<br>**method**: resize method, by default is bilinear<br>|
| **return** | new rotated image object |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *rotate(float angle, int width = -1, int height = -1, image::ResizeMethod method = image::ResizeMethod::BILINEAR)
> ```
#### flip {#flip}

```python
def flip(self, dir: FlipDir) -> Image
```
Vertical flip image, and return a new image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **dir**: flip dir, see image.FlipDir, e.g. image.FlipDir.X is vertical flip.<br>|
| **return** | new flipped image. |
| **throw** | When arg error, will throw out err.Err exception. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *flip(const image::FlipDir dir)
> ```
#### mean\_pool {#mean\_pool}

```python
def mean_pool(self, x_div: int, y_div: int, copy: bool = False) -> Image
```
Finds the mean of x_div * y_div squares in the image and returns the modified image composed of the mean of each square.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x_div**: The width of the squares.<br>**y_div**: The height of the squares.<br>**copy**: Select whether to return a new image or modify the original image. default is false.<br>If true, returns a new image composed of the mean of each square; If false, returns the modified image composed of the mean of each square.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *mean_pool(int x_div, int y_div, bool copy = false)
> ```
#### midpoint\_pool {#midpoint\_pool}

```python
def midpoint_pool(self, x_div: int, y_div: int, bias: float = 0.5, copy: bool = False) -> Image
```
Finds the midpoint of x_div * y_div squares in the image and returns the modified image composed of the mean of each square.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x_div**: The width of the squares.<br>**y_div**: The height of the squares.<br>**bias**: The bias of the midpoint. default is 0.5.<br>midpoint value is equal to (max * bias + min * (1 - bias))<br>**copy**: Select whether to return a new image or modify the original image. default is false.<br>If true, returns a new image composed of the midpoint of each square; If false, returns the modified image composed of the midpoint of each square.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *midpoint_pool(int x_div, int y_div, double bias = 0.5, bool copy = false)
> ```
#### compress {#compress}

```python
def compress(self, quality: int = 95) -> Image
```
JPEG compresses the image in place, the same as to_jpeg functioin, it's recommend to use to_jpeg instead.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **quality**: The quality of the compressed image. default is 95.<br>|
| **return** | Returns the compressed JPEG image |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *compress(int quality = 95)
> ```
#### clear {#clear}

```python
def clear(self, mask: Image = None) -> Image
```
Sets all pixels in the image to zero

| item | description |
| --- | --- |
| **type** | func |
| **param** | **mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *clear(image::Image *mask = nullptr)
> ```
#### mask\_rectange {#mask\_rectange}

```python
def mask_rectange(self, x: int = -1, y: int = -1, w: int = -1, h: int = -1) -> Image
```
Zeros a rectangular part of the image. If no arguments are supplied this method zeros the center of the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: The x coordinate of the top left corner of the rectangle.<br>**y**: The y coordinate of the top left corner of the rectangle.<br>**w**: The width of the rectangle.<br>**h**: The height of the rectangle.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *mask_rectange(int x = -1, int y = -1, int w = -1, int h = -1)
> ```
#### mask\_circle {#mask\_circle}

```python
def mask_circle(self, x: int = -1, y: int = -1, radius: int = -1) -> Image
```
Zeros a circular part of the image. If no arguments are supplied this method zeros the center of the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: The x coordinate of the center of the circle.<br>**y**: The y coordinate of the center of the circle.<br>**radius**: The radius of the circle.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *mask_circle(int x = -1, int y = -1, int radius = -1)
> ```
#### mask\_ellipse {#mask\_ellipse}

```python
def mask_ellipse(self, x: int = -1, y: int = -1, radius_x: int = -1, radius_y: int = -1, rotation_angle_in_degrees: float = 0) -> Image
```
Zeros a ellipse part of the image. If no arguments are supplied this method zeros the center of the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: The x coordinate of the center of the ellipse.<br>**y**: The y coordinate of the center of the ellipse.<br>**radius_x**: The radius of the ellipse in the x direction.<br>**radius_y**: The radius of the ellipse in the y direction.<br>**rotation_angle_in_degrees**: The rotation angle of the ellipse in degrees.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *mask_ellipse(int x = -1, int y = -1, int radius_x = -1, int radius_y = -1, float rotation_angle_in_degrees = 0)
> ```
#### binary {#binary}

```python
def binary(self, thresholds: list[list[int]] = [], invert: bool = False, zero: bool = False, mask: Image = None, to_bitmap: bool = False, copy: bool = False) -> Image
```
Sets all pixels in the image to black or white depending on if the pixel is inside of a threshold in the threshold list thresholds or not.

| item | description |
| --- | --- |
| **type** | func |
| **note** | For GRAYSCALE format, Lmin and Lmax range is [0, 255]. For RGB888 format, Lmin and Lmax range is [0, 100]. |
| **param** | **thresholds**: You can define multiple thresholds.<br>For GRAYSCALE format, you can use {{Lmin, Lmax}, ...} to define one or more thresholds.<br>For RGB888 format, you can use {{Lmin, Lmax, Amin, Amax, Bmin, Bmax}, ...} to define one or more thresholds.<br>Where the upper case L,A,B represent the L,A,B channels of the LAB image format, and min, max represent the minimum and maximum values of the corresponding channels.<br>**invert**: If true, the thresholds will be inverted before the operation. default is false.<br>**zero**: If zero is true, the image will be set the pixels within the threshold to 0, other pixels remain unchanged. If zero is false, the image will be set to black or white. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>**to_bitmap**: If true, the image will be converted to a bitmap image before thresholding. default is false. TODO: support in the future<br>**copy**: Select whether to return a new image or modify the original image. default is false.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *binary(std::vector<std::vector<int>> thresholds = std::vector<std::vector<int>>(), bool invert = false, bool zero = false, image::Image *mask = nullptr, bool to_bitmap = false, bool copy = false)
> ```
#### invert {#invert}

```python
def invert(self) -> Image
```
Inverts the image in place.

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the image after the operation is completed |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *invert()
> ```
#### b\_and {#b\_and}

```python
def b_and(self, other: Image, mask: Image = None) -> Image
```
Performs a bitwise and operation between the image and the other image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.        TODO: support path?<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *b_and(image::Image *other, image::Image *mask = nullptr)
> ```
#### b\_nand {#b\_nand}

```python
def b_nand(self, other: Image, mask: Image = None) -> Image
```
Performs a bitwise nand operation between the image and the other image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.        TODO: support path?<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *b_nand(image::Image *other, image::Image *mask = nullptr)
> ```
#### b\_or {#b\_or}

```python
def b_or(self, other: Image, mask: Image = None) -> Image
```
Performs a bitwise or operation between the image and the other image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.        TODO: support path?<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *b_or(image::Image *other, image::Image *mask = nullptr)
> ```
#### b\_nor {#b\_nor}

```python
def b_nor(self, other: Image, mask: Image = None) -> Image
```
Performs a bitwise nor operation between the image and the other image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.        TODO: support path?<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *b_nor(image::Image *other, image::Image *mask = nullptr)
> ```
#### b\_xor {#b\_xor}

```python
def b_xor(self, other: Image, mask: Image = None) -> Image
```
Performs a bitwise xor operation between the image and the other image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.        TODO: support path?<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *b_xor(image::Image *other, image::Image *mask = nullptr)
> ```
#### b\_xnor {#b\_xnor}

```python
def b_xnor(self, other: Image, mask: Image = None) -> Image
```
Performs a bitwise xnor operation between the image and the other image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.        TODO: support path?<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *b_xnor(image::Image *other, image::Image *mask = nullptr)
> ```
#### awb {#awb}

```python
def awb(self, max: bool = False) -> Image
```
Performs an auto white balance operation on the image. TODO: support in the future

| item | description |
| --- | --- |
| **type** | func |
| **param** | **max**: if True uses the white-patch algorithm instead. default is false.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *awb(bool max = false)
> ```
#### ccm {#ccm}

```python
def ccm(self, matrix: list[float]) -> Image
```
Multiples the passed (3x3) or (4x3) floating-point color-correction-matrix with the image.\nnote: Grayscale format is not support.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **matrix**: The color correction matrix to use. 3x3 or 4x3 matrix.<br>Weights may either be positive or negative, and the sum of each column in the 3x3 matrix should generally be 1.<br>example:<br>{<br>1, 0, 0,<br>0, 1, 0,<br>0, 0, 1,<br>}<br>Where the last row of the 4x3 matrix is an offset per color channel. If you add an offset you may wish to make the<br>weights sum to less than 1 to account for the offset.<br>example:<br>{<br>1, 0, 0,<br>0, 1, 0,<br>0, 0, 1,<br>0, 0, 0,<br>}<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *ccm(std::vector<float> &matrix)
> ```
#### gamma {#gamma}

```python
def gamma(self, gamma: float = 1.0, contrast: float = 1.0, brightness: float = 0.0) -> Image
```
Quickly changes the image gamma, contrast, and brightness. Create a array whose size is usually 255,\nand use the parameters gamma, contrast, and brightness to calculate the value of the array, and then map the\nimage pixel value through the value of the array.\nThe calculation method for array is: array[array_idx] = (powf((array_idx / 255.0), (1 / gamma)) * contrast + brightness) * scale,\n`powf` is a function used to calculate floating point power.\n`array` is the array used for mapping.\n`array_idx` is the index of the array, the maximum value is determined according to the image format, usually 255.\n`scale` is a constant, the value is determined by the image format, usually 255.\nMapping method:\nAssume that a pixel value in the image is 128, then map the pixel value to the value of array[128]\nUsers can adjust the value of the array through the gamma, contrast, and brightness parameters.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **gamma**: The contrast gamma greater than 1.0 makes the image darker in a non-linear manner while less than 1.0 makes the image brighter. default is 1.0.<br>**contrast**: The contrast value greater than 1.0 makes the image brighter in a linear manner while less than 1.0 makes the image darker. default is 1.0.<br>**brightness**: The brightness value greater than 0.0 makes the image brighter in a constant manner while less than 0.0 makes the image darker. default is 0.0.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *gamma(double gamma = 1.0, double contrast = 1.0, double brightness = 0.0)
> ```
#### gamma\_corr {#gamma\_corr}

```python
def gamma_corr(self, gamma: float, contrast: float = 1.0, brightness: float = 0.0) -> Image
```
Alias for Image.gamma.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **gamma**: The contrast gamma greater than 1.0 makes the image darker in a non-linear manner while less than 1.0 makes the image brighter. default is 1.0.<br>**contrast**: The contrast value greater than 1.0 makes the image brighter in a linear manner while less than 1.0 makes the image darker. default is 1.0.<br>**brightness**: The brightness value greater than 0.0 makes the image brighter in a constant manner while less than 0.0 makes the image darker. default is 0.0.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *gamma_corr(double gamma, double contrast = 1.0, double brightness = 0.0)
> ```
#### negate {#negate}

```python
def negate(self) -> Image
```
Flips (numerically inverts) all pixels values in an image

| item | description |
| --- | --- |
| **type** | func |
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *negate()
> ```
#### replace {#replace}

```python
def replace(self, other: Image = None, hmirror: bool = False, vflip: bool = False, transpose: bool = False, mask: Image = None) -> Image
```
Replaces all pixels in the image with the corresponding pixels in the other image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.<br>**hmirror**: If true, the image will be horizontally mirrored before the operation. default is false.<br>**vflip**: If true, the image will be vertically flipped before the operation. default is false.<br>**transpose**: If true, the image can be used to rotate 90 degrees or 270 degrees.<br>hmirror = false, vflip = false, transpose = false, the image will not be rotated.<br>hmirror = false, vflip = true, transpose = true, the image will be rotated 90 degrees.<br>hmirror = true, vflip = true, transpose = false, the image will be rotated 180 degrees.<br>hmirror = true, vflip = false, transpose = true, the image will be rotated 270 degrees.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *replace(image::Image *other = nullptr, bool hmirror = false, bool vflip = false, bool transpose = false, image::Image *mask = nullptr)
> ```
#### set {#set}

```python
def set(self, other: Image, hmirror: bool = False, vflip: bool = False, transpose: bool = False, mask: Image = None) -> Image
```
Alias for Image::replace.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.<br>**hmirror**: If true, the image will be horizontally mirrored before the operation. default is false.<br>**vflip**: If true, the image will be vertically flipped before the operation. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *set(image::Image *other, bool hmirror = false, bool vflip = false, bool transpose = false, image::Image *mask = nullptr)
> ```
#### add {#add}

```python
def add(self, other: Image, mask: Image = None) -> Image
```
Adds the other image to the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.    TODO: support path?<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *add(image::Image *other, image::Image *mask = nullptr)
> ```
#### sub {#sub}

```python
def sub(self, other: Image, reverse: bool = False, mask: Image = None) -> Image
```
Subtracts the other image from the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.    TODO: support path?<br>**reverse**: If true, the image will be reversed before the operation. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *sub(image::Image *other, bool reverse = false, image::Image *mask = nullptr)
> ```
#### mul {#mul}

```python
def mul(self, other: Image, invert: bool = False, mask: Image = None) -> Image
```
Multiplies the image by the other image.\nNote: This method is meant for image blending and cannot multiply the pixels in the image by a scalar like 2.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.    TODO: support path?<br>**invert**: If true, the image will be change the multiplication operation from a*b to 1/((1/a)*(1/b)).<br>In particular, this lightens the image instead of darkening it (e.g. multiply versus burn operations). default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *mul(image::Image *other, bool invert = false, image::Image *mask = nullptr)
> ```
#### div {#div}

```python
def div(self, other: Image, invert: bool = False, mod: bool = False, mask: Image = None) -> Image
```
Divides the image by the other image.\nThis method is meant for image blending and cannot divide the pixels in the image by a scalar like 2.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.    TODO: support path?<br>**invert**: If true, the image will be change the division direction from a/b to b/a. default is false.<br>**mod**: If true, the image will be change the division operation to the modulus operation. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *div(image::Image *other, bool invert = false, bool mod = false, image::Image *mask = nullptr)
> ```
#### min {#min}

```python
def min(self, other: Image, mask: Image = None) -> Image
```
Caculate the minimum of each pixel in the image and the other image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *min(image::Image *other, image::Image *mask = nullptr)
> ```
#### max {#max}

```python
def max(self, other: Image, mask: Image = None) -> Image
```
Caculate the maximum of each pixel in the image and the other image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *max(image::Image *other, image::Image *mask = nullptr)
> ```
#### difference {#difference}

```python
def difference(self, other: Image, mask: Image = None) -> Image
```
Caculate the absolute value of the difference between each pixel in the image and the other image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *difference(image::Image *other, image::Image *mask = nullptr)
> ```
#### blend {#blend}

```python
def blend(self, other: Image, alpha: int = 128, mask: Image = None) -> Image
```
Blends the image with the other image.\nres = alpha * this_img / 256 + (256 - alpha) * other_img / 256

| item | description |
| --- | --- |
| **type** | func |
| **param** | **other**: The other image should be an image and should be the same size as the image being operated on.<br>**alpha**: The alpha value of the blend, the value range is [0, 256],default is 128.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *blend(image::Image *other, int alpha = 128, image::Image *mask = nullptr)
> ```
#### histeq {#histeq}

```python
def histeq(self, adaptive: bool = False, clip_limit: int = -1, mask: Image = None) -> Image
```
Runs the histogram equalization algorithm on the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **adaptive**: If true, an adaptive histogram equalization method will be run on the image instead which as generally better results than non-adaptive histogram qualization but a longer run time. default is false.<br>**clip_limit**: Provides a way to limit the contrast of the adaptive histogram qualization. Use a small value for this, like 10, to produce good histogram equalized contrast limited images. default is -1.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *histeq(bool adaptive = false, int clip_limit = -1, image::Image *mask = nullptr)
> ```
#### mean {#mean}

```python
def mean(self, size: int, threshold: bool = False, offset: int = 0, invert: bool = False, mask: Image = None) -> Image
```
Standard mean blurring filter using a box filter.\nThe parameters offset and invert are valid when threshold is True.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**threshold**: If true, which will enable adaptive thresholding of the image which sets pixels to white or black based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them.<br>default is false.<br>**offset**: The larger the offset value, the lower brightness pixels on the original image will be set to white. default is 0.<br>**invert**: If true, the image will be inverted before the operation. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *mean(int size, bool threshold = false, int offset = 0, bool invert = false, image::Image *mask = nullptr)
> ```
#### median {#median}

```python
def median(self, size: int, percentile: float = 0.5, threshold: bool = False, offset: int = 0, invert: bool = False, mask: Image = None) -> Image
```
Runs the median filter on the image. The median filter is the best filter for smoothing surfaces while preserving edges but it is very slow.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**percentile**: This parameter controls the percentile of the value used in the kernel. You can set this to 0 for a min filter, 0.25 for a lower quartile filter, 0.75 for an upper quartile filter, and 1.0 for a max filter. default is 0.5.<br>**threshold**: If true, which will enable adaptive thresholding of the image which sets pixels to white or black based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them.<br>default is false.<br>**offset**: The larger the offset value, the lower brightness pixels on the original image will be set to white. default is 0.<br>**invert**: If true, the image will be inverted before the operation. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *median(int size, double percentile = 0.5, bool threshold = false, int offset = 0, bool invert = false, image::Image *mask = nullptr)
> ```
#### mode {#mode}

```python
def mode(self, size: int, threshold: bool = False, offset: int = 0, invert: bool = False, mask: Image = None) -> Image
```
Runs the mode filter on the image by replacing each pixel with the mode of their neighbors.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**threshold**: If true, which will enable adaptive thresholding of the image which sets pixels to white or black based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them.<br>default is false.<br>**offset**: The larger the offset value, the lower brightness pixels on the original image will be set to white. default is 0.<br>**invert**: If true, the image will be inverted before the operation. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *mode(int size, bool threshold = false, int offset = 0, bool invert = false, image::Image *mask = nullptr)
> ```
#### midpoint {#midpoint}

```python
def midpoint(self, size: int, bias: float = 0.5, threshold: bool = False, offset: int = 0, invert: bool = False, mask: Image = None) -> Image
```
Runs the midpoint filter on the image.This filter finds the midpoint (max * bias + min * (1 - bias)) of each pixel neighborhood in the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**bias**: The bias of the midpoint. default is 0.5.<br>**threshold**: If true, which will enable adaptive thresholding of the image which sets pixels to white or black based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them.<br>default is false.<br>**offset**: The larger the offset value, the lower brightness pixels on the original image will be set to white. default is 0.<br>**invert**: If true, the image will be inverted before the operation. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *midpoint(int size, double bias = 0.5, bool threshold = false, int offset = 0, bool invert = false, image::Image *mask = nullptr)
> ```
#### morph {#morph}

```python
def morph(self, size: int, kernel: list[int], mul: float = -1, add: float = 0.0, threshold: bool = False, offset: int = 0, invert: bool = False, mask: Image = None) -> Image
```
Convolves the image by a filter kernel. This allows you to do general purpose convolutions on an image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**kernel**: The kernel used for convolution. The kernel should be a list of lists of numbers. The kernel should be the same size as the actual kernel size.<br>**mul**: This parameter is used to multiply the convolved pixel results. default is auto.<br>**add**: This parameter is the value to be added to each convolution pixel result. default is 0.0.<br>**threshold**: If true, which will enable adaptive thresholding of the image which sets pixels to white or black based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them.<br>default is false.<br>**offset**: The larger the offset value, the lower brightness pixels on the original image will be set to white. default is 0.<br>**invert**: If true, the image will be inverted before the operation. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *morph(int size, std::vector<int> kernel, float mul = -1, float add = 0.0, bool threshold = false, int offset = 0, bool invert = false, image::Image *mask = nullptr)
> ```
#### gaussian {#gaussian}

```python
def gaussian(self, size: int, unsharp: bool = False, mul: float = -1, add: float = 0.0, threshold: bool = False, offset: int = 0, invert: bool = False, mask: Image = None) -> Image
```
Convolves the image by a smoothing guassian kernel.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**unsharp**: If true, this method will perform an unsharp mask operation instead of gaussian filtering operation, this improves the clarity of image edges. default is false.<br>**mul**: This parameter is used to multiply the convolved pixel results. default is auto.<br>**add**: This parameter is the value to be added to each convolution pixel result. default is 0.0.<br>**threshold**: If true, which will enable adaptive thresholding of the image which sets pixels to white or black based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them.<br>default is false.<br>**offset**: The larger the offset value, the lower brightness pixels on the original image will be set to white. default is 0.<br>**invert**: If true, the image will be inverted before the operation. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *gaussian(int size, bool unsharp = false, float mul = -1, float add = 0.0, bool threshold = false, int offset = 0, bool invert = false, image::Image *mask = nullptr)
> ```
#### laplacian {#laplacian}

```python
def laplacian(self, size: int, sharpen: bool = False, mul: float = -1, add: float = 0.0, threshold: bool = False, offset: int = 0, invert: bool = False, mask: Image = None) -> Image
```
Convolves the image by a edge detecting laplacian kernel.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**sharpen**: If True, this method will sharpen the image instead of an unthresholded edge detection image. Then increase the kernel size to improve image clarity. default is false.<br>**mul**: This parameter is used to multiply the convolved pixel results. default is auto.<br>**add**: This parameter is the value to be added to each convolution pixel result. default is 0.0.<br>**threshold**: If true, which will enable adaptive thresholding of the image which sets pixels to white or black based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them.<br>default is false.<br>**offset**: The larger the offset value, the lower brightness pixels on the original image will be set to white. default is 0.<br>**invert**: If true, the image will be inverted before the operation. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *laplacian(int size, bool sharpen = false, float mul = -1, float add = 0.0, bool threshold = false, int offset = 0, bool invert = false, image::Image *mask = nullptr)
> ```
#### bilateral {#bilateral}

```python
def bilateral(self, size: int, color_sigma: float = 0.1, space_sigma: float = 1, threshold: bool = False, offset: int = 0, invert: bool = False, mask: Image = None) -> Image
```
Convolves the image by a bilateral filter.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**color_sigma**: Controls how closely colors are matched using the bilateral filter. default is 0.1.<br>**space_sigma**: Controls how closely pixels space-wise are blurred with each other. default is 1.<br>**threshold**: If true, which will enable adaptive thresholding of the image which sets pixels to white or black based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them.<br>default is false.<br>**offset**: The larger the offset value, the lower brightness pixels on the original image will be set to white. default is 0.<br>**invert**: If true, the image will be inverted before the operation. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *bilateral(int size, double color_sigma = 0.1, double space_sigma = 1, bool threshold = false, int offset = 0, bool invert = false, image::Image *mask = nullptr)
> ```
#### linpolar {#linpolar}

```python
def linpolar(self, reverse: bool = False) -> Image
```
Re-project’s and image from cartessian coordinates to linear polar coordinates.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **reverse**: If true, the image will be reverse polar transformed. default is false.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *linpolar(bool reverse = false)
> ```
#### logpolar {#logpolar}

```python
def logpolar(self, reverse: bool = False) -> Image
```
Re-project’s and image from cartessian coordinates to log polar coordinates.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **reverse**: If true, the image will be reverse polar transformed. default is false.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *logpolar(bool reverse = false)
> ```
#### lens\_corr {#lens\_corr}

```python
def lens_corr(self, strength: float = 1.8, zoom: float = 1.0, x_corr: float = 0.0, y_corr: float = 0.0) -> Image
```
Performs a lens correction operation on the image. TODO: support in the future

| item | description |
| --- | --- |
| **type** | func |
| **param** | **strength**: The strength of the lens correction. default is 1.8.<br>**zoom**: The zoom of the lens correction. default is 1.0.<br>**x_corr**: The x correction of the lens correction. default is 0.0.<br>**y_corr**: The y correction of the lens correction. default is 0.0.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *lens_corr(double strength = 1.8, double zoom = 1.0, double x_corr = 0.0, double y_corr = 0.0)
> ```
#### rotation\_corr {#rotation\_corr}

```python
def rotation_corr(self, x_rotation: float = 0.0, y_rotation: float = 0.0, z_rotation: float = 0.0, x_translation: float = 0.0, y_translation: float = 0.0, zoom: float = 1.0, fov: float = 60.0, corners: list[float] = []) -> Image
```
Performs a rotation correction operation on the image. TODO: support in the future

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x_rotation**: The x rotation of the rotation correction. default is 0.0.<br>**y_rotation**: The y rotation of the rotation correction. default is 0.0.<br>**z_rotation**: The z rotation of the rotation correction. default is 0.0.<br>**x_translation**: The x translation of the rotation correction. default is 0.0.<br>**y_translation**: The y translation of the rotation correction. default is 0.0.<br>**zoom**: The zoom of the rotation correction. default is 1.0.<br>**fov**: The fov of the rotation correction. default is 60.0.<br>**corners**: The corners of the rotation correction. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *rotation_corr(double x_rotation = 0.0, double y_rotation = 0.0, double z_rotation = 0.0, double x_translation = 0.0, double y_translation = 0.0, double zoom = 1.0, double fov = 60.0, std::vector<float> corners = std::vector<float>())
> ```
#### get\_histogram {#get\_histogram}

```python
def get_histogram(self, thresholds: list[list[int]] = [], invert: bool = False, roi: list[int] = [], bins: int = -1, l_bins: int = 100, a_bins: int = 256, b_bins: int = 256, difference: Image = None) -> Histogram
```
Computes the normalized histogram on all color channels and returns a image::Histogram object.

| item | description |
| --- | --- |
| **type** | func |
| **note** | For GRAYSCALE format, Lmin and Lmax range is [0, 255]. For RGB888 format, Lmin and Lmax range is [0, 100]. |
| **param** | **thresholds**: You can define multiple thresholds.<br>For GRAYSCALE format, you can use {{Lmin, Lmax}, ...} to define one or more thresholds.<br>For RGB888 format, you can use {{Lmin, Lmax, Amin, Amax, Bmin, Bmax}, ...} to define one or more thresholds.<br>Where the upper case L,A,B represent the L,A,B channels of the LAB image format, and min, max represent the minimum and maximum values of the corresponding channels.<br>**invert**: If true, the thresholds will be inverted before the operation. default is false.<br>**roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**bins**: The number of bins to use for the histogram.<br>In GRAYSCALE format, setting range is [2, 256], default is 100.<br>In RGB888 format, setting range is [2, 100], default is 100.<br>**l_bins**: The number of bins to use for the l channel of the histogram. Only valid in RGB888 format.<br>If an invalid value is set, bins will be used instead. The setting range is [2, 100], default is 100.<br>**a_bins**: The number of bins to use for the a channel of the histogram.<br>Only valid in RGB888 format.The setting range is [2, 256],  default is 256.<br>**b_bins**: The number of bins to use for the b channel of the histogram.<br>Only valid in RGB888 format. The setting range is [2, 256], default is 256.<br>**difference**: difference may be set to an image object to cause this method to operate on the difference image between the current image and the difference image object.<br>default is None.<br>|
| **return** | Returns image::Histogram object |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Histogram get_histogram(std::vector<std::vector<int>> thresholds = std::vector<std::vector<int>>(), bool invert = false, std::vector<int> roi = std::vector<int>(), int bins = -1, int l_bins = 100, int a_bins = 256, int b_bins = 256, image::Image *difference = nullptr)
> ```
#### get\_statistics {#get\_statistics-2}

```python
def get_statistics(self, thresholds: list[list[int]] = [], invert: bool = False, roi: list[int] = [], bins: int = -1, l_bins: int = -1, a_bins: int = -1, b_bins: int = -1, difference: Image = None) -> Statistics
```
Gets the statistics of the image. TODO: support in the future

| item | description |
| --- | --- |
| **type** | func |
| **note** | For GRAYSCALE format, Lmin and Lmax range is [0, 255]. For RGB888 format, Lmin and Lmax range is [0, 100]. |
| **param** | **thresholds**: You can define multiple thresholds.<br>For GRAYSCALE format, you can use {{Lmin, Lmax}, ...} to define one or more thresholds.<br>For RGB888 format, you can use {{Lmin, Lmax, Amin, Amax, Bmin, Bmax}, ...} to define one or more thresholds.<br>Where the upper case L,A,B represent the L,A,B channels of the LAB image format, and min, max represent the minimum and maximum values of the corresponding channels.<br>**invert**: If true, the image will be inverted before the operation. default is false.<br>**roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**bins**: The number of bins to use for the statistics. default is -1.<br>**l_bins**: The number of bins to use for the l channel of the statistics. default is -1.<br>**a_bins**: The number of bins to use for the a channel of the statistics. default is -1.<br>**b_bins**: The number of bins to use for the b channel of the statistics. default is -1.<br>**difference**: The difference image to use for the statistics. default is None.<br>|
| **return** | Returns the statistics of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Statistics get_statistics(std::vector<std::vector<int>> thresholds = std::vector<std::vector<int>>(), bool invert = false, std::vector<int> roi = std::vector<int>(), int bins = -1, int l_bins = -1, int a_bins = -1, int b_bins = -1, image::Image *difference = nullptr)
> ```
#### get\_regression {#get\_regression}

```python
def get_regression(self, thresholds: list[list[int]] = [], invert: bool = False, roi: list[int] = [], x_stride: int = 2, y_stride: int = 1, area_threshold: int = 10, pixels_threshold: int = 10, robust: bool = False) -> list[Line]
```
Gets the regression of the image.

| item | description |
| --- | --- |
| **type** | func |
| **note** | For GRAYSCALE format, Lmin and Lmax range is [0, 255]. For RGB888 format, Lmin and Lmax range is [0, 100]. |
| **param** | **thresholds**: You can define multiple thresholds.<br>For GRAYSCALE format, you can use {{Lmin, Lmax}, ...} to define one or more thresholds.<br>For RGB888 format, you can use {{Lmin, Lmax, Amin, Amax, Bmin, Bmax}, ...} to define one or more thresholds.<br>Where the upper case L,A,B represent the L,A,B channels of the LAB image format, and min, max represent the minimum and maximum values of the corresponding channels.<br>**invert**: If true, the image will be inverted before the operation. default is false.<br>**roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**x_stride**: The x stride to use for the regression. default is 2.<br>**y_stride**: The y stride to use for the regression. default is 1.<br>**area_threshold**: The area threshold to use for the regression. default is 10.<br>**pixels_threshold**: The pixels threshold to use for the regression. default is 10.<br>**robust**: If true, the regression will be robust. default is false.<br>|
| **return** | Returns the regression of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::Line> get_regression(std::vector<std::vector<int>> thresholds = std::vector<std::vector<int>>(), bool invert = false, std::vector<int> roi = std::vector<int>(), int x_stride = 2, int y_stride = 1, int area_threshold = 10, int pixels_threshold = 10, bool robust = false)
> ```
#### save {#save}

```python
def save(self, path: str, quality: int = 95) -> maix.err.Err
```
Save image to file

| item | description |
| --- | --- |
| **type** | func |
| **param** | **path**: file path<br>**quality**: image quality, by default(value is 95), support jpeg and png format<br>|
| **return** | error code, err::ERR_NONE is ok, other is error |
| **static** | False |

> C++ defination code:
> ```cpp
> err::Err save(const char *path, int quality = 95)
> ```
#### flood\_fill {#flood\_fill}

```python
def flood_fill(self, x: int, y: int, seed_threshold: float = 0.05, floating_threshold: float = 0.05, color: Color = ..., invert: bool = False, clear_background: bool = False, mask: Image = None) -> Image
```
Flood fills a region of the image starting from location x, y.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **x**: The x coordinate of the seed point.<br>**y**: The y coordinate of the seed point.<br>**seed_threshold**: The seed_threshold value controls how different any pixel in the fill area may be from the original starting pixel. default is 0.05.<br>**floating_threshold**: The floating_threshold value controls how different any pixel in the fill area may be from any neighbor pixels. default is 0.05.<br>**color**: The color to fill the region with. default is white.<br>**invert**: If true, the image will be inverted before the operation. default is false.<br>**clear_background**: If true, the background will be cleared before the operation. default is false.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None. FIXME: the mask image works abnormally<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *flood_fill(int x, int y, float seed_threshold = 0.05, float floating_threshold = 0.05, image::Color color = image::COLOR_WHITE, bool invert = false, bool clear_background = false, image::Image *mask = nullptr)
> ```
#### erode {#erode}

```python
def erode(self, size: int, threshold: int = -1, mask: Image = None) -> Image
```
Erodes the image in place.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**threshold**: The number of pixels in the kernel that are not 0. If it is less than or equal to the threshold, set the center pixel to black. default is (kernel_size - 1).<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *erode(int size, int threshold = -1, image::Image *mask = nullptr)
> ```
#### dilate {#dilate}

```python
def dilate(self, size: int, threshold: int = 0, mask: Image = None) -> Image
```
Dilates the image in place.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**threshold**: The number of pixels in the kernel that are not 0. If it is greater than or equal to the threshold, set the center pixel to white. default is 0.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *dilate(int size, int threshold = 0, image::Image *mask = nullptr)
> ```
#### open {#open}

```python
def open(self, size: int, threshold: int = 0, mask: Image = None) -> Image
```
Performs erosion and dilation on an image in order.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**threshold**: As the threshold for erosion and dilation, the actual threshold for erosion is (kernel_size - 1 - threshold), the actual threshold for dialation is threshold. default is 0.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *open(int size, int threshold = 0, image::Image *mask = nullptr)
> ```
#### close {#close}

```python
def close(self, size: int, threshold: int = 0, mask: Image = None) -> Image
```
Performs dilation and erosion on an image in order.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**threshold**: As the threshold for erosion and dilation, the actual threshold for erosion is (kernel_size - 1 - threshold), the actual threshold for dialation is threshold. default is 0.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *close(int size, int threshold = 0, image::Image *mask = nullptr)
> ```
#### top\_hat {#top\_hat}

```python
def top_hat(self, size: int, threshold: int = 0, mask: Image = None) -> Image
```
Returns the image difference of the image and Image.open()’ed image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**threshold**: As the threshold for open method. default is 0.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *top_hat(int size, int threshold = 0, image::Image *mask = nullptr)
> ```
#### black\_hat {#black\_hat}

```python
def black_hat(self, size: int, threshold: int = 0, mask: Image = None) -> Image
```
Returns the image difference of the image and Image.close()’ed image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **size**: Kernel size. The actual kernel size is ((size * 2) + 1) * ((size * 2) + 1). Use 1(3x3 kernel), 2(5x5 kernel).<br>**threshold**: As the threshold for close method. default is 0.<br>**mask**: Mask is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on.<br>Only pixels set in the mask are modified. default is None.<br>|
| **return** | Returns the image after the operation is completed. |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image *black_hat(int size, int threshold = 0, image::Image *mask = nullptr)
> ```
#### find\_blobs {#find\_blobs}

```python
def find_blobs(self, thresholds: list[list[int]] = [], invert: bool = False, roi: list[int] = [], x_stride: int = 2, y_stride: int = 1, area_threshold: int = 10, pixels_threshold: int = 10, merge: bool = False, margin: int = 0, x_hist_bins_max: int = 0, y_hist_bins_max: int = 0) -> list[Blob]
```
Finds all blobs in the image and returns a list of image.Blob class which describe each Blob.\nPlease see the image.Blob object more more information.

| item | description |
| --- | --- |
| **type** | func |
| **note** | For GRAYSCALE format, Lmin and Lmax range is [0, 255]. For RGB888 format, Lmin and Lmax range is [0, 100]. |
| **param** | **thresholds**: You can define multiple thresholds.<br>For GRAYSCALE format, you can use {{Lmin, Lmax}, ...} to define one or more thresholds.<br>For RGB888 format, you can use {{Lmin, Lmax, Amin, Amax, Bmin, Bmax}, ...} to define one or more thresholds.<br>Where the upper case L,A,B represent the L,A,B channels of the LAB image format, and min, max represent the minimum and maximum values of the corresponding channels.<br>**invert**: if true, will invert thresholds before find blobs, default is false<br>**roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**x_stride**: x stride is the number of x pixels to skip when doing the hough transform. default is 2<br>**y_stride**: y_stride is the number of y pixels to skip when doing the hough transform. default is 1<br>**area_threshold**: area threshold, if the blob area is smaller than area_threshold, the blob is not returned, default is 10<br>**pixels_threshold**: pixels threshold, if the blob pixels is smaller than area_threshold, the blob is not returned,, default is 10.<br>when x_stride and y_stride is equal to 1, pixels_threshold is equivalent to area_threshold<br>**merge**: if True merges all not filtered out blobs whos bounding rectangles intersect each other. default is false<br>**margin**: margin can be used to increase or decrease the size of the bounding rectangles for blobs during the intersection test.<br>For example, with a margin of 1 blobs whos bounding rectangles are 1 pixel away from each other will be merged. default is 0<br>**x_hist_bins_max**: if set to non-zero populates a histogram buffer in each blob object with an x_histogram projection of all columns in the object. This value then sets the number of bins for that projection.<br>**y_hist_bins_max**: if set to non-zero populates a histogram buffer in each blob object with an y_histogram projection of all rows in the object. This value then sets the number of bins for that projection.<br>|
| **return** | Return the blob when found blobs, format is (blob1, blob2, ...), you can use blob class methods to do more operations. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::Blob> find_blobs(std::vector<std::vector<int>> thresholds = std::vector<std::vector<int>>(), bool invert = false, std::vector<int> roi = std::vector<int>(), int x_stride = 2, int y_stride = 1, int area_threshold = 10, int pixels_threshold = 10, bool merge = false, int margin = 0, int x_hist_bins_max = 0, int y_hist_bins_max = 0)
> ```
#### find\_lines {#find\_lines}

```python
def find_lines(self, roi: list[int] = [], x_stride: int = 2, y_stride: int = 1, threshold: float = 1000, theta_margin: float = 25, rho_margin: float = 25) -> list[Line]
```
Find lines in image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**x_stride**: x stride is the number of x pixels to skip when doing the hough transform. default is 2<br>**y_stride**: y_stride is the number of y pixels to skip when doing the hough transform. default is 1<br>**threshold**: threshold threshold controls what lines are detected from the hough transform. Only lines with a magnitude greater than or equal to threshold are returned.<br>The right value of threshold for your application is image dependent. default is 1000.<br>**theta_margin**: theta_margin controls the merging of detected lines. default is 25.<br>**rho_margin**: rho_margin controls the merging of detected lines. default is 25.<br>|
| **return** | Return the line when found lines, format is (line1, line2, ...), you can use line class methods to do more operations |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::Line> find_lines(std::vector<int> roi = std::vector<int>(), int x_stride = 2, int y_stride = 1, double threshold = 1000, double theta_margin = 25, double rho_margin = 25)
> ```
#### find\_line\_segments {#find\_line\_segments}

```python
def find_line_segments(self, roi: list[int] = [], merge_distance: int = 0, max_theta_difference: int = 15) -> list[Line]
```
Finds all line segments in the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**merge_distance**: The maximum distance between two lines to merge them. default is 0.<br>**max_theta_difference**: The maximum difference between two lines to merge them. default is 15.<br>|
| **return** | Return the line when found lines, format is (line1, line2, ...), you can use line class methods to do more operations |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::Line> find_line_segments(std::vector<int> roi = std::vector<int>(), int merge_distance = 0, int max_theta_difference = 15)
> ```
#### search\_line\_path {#search\_line\_path}

```python
def search_line_path(self, threshold: int = 30, merge_degree: int = 10, min_len_of_new_path: int = 10) -> list[LineGroup]
```
Search the path of line

| item | description |
| --- | --- |
| **type** | func |
| **param** | **threshold**: Threshold for finding a line, the larger the value the more accurate the line is found<br>**merge_degree**: Minimum angle difference required when merging multiple lines<br>**min_len_of_new_path**: The minimum length of a new path, if the crossing length exceeds this value, it is considered a new path.<br>|
| **return** | Return the line when found lines, format is (groupline1, groupline2, ...), you can use LineGroup class methods to do more operations |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::LineGroup> search_line_path(int threshold = 30, int merge_degree = 10, int min_len_of_new_path = 10)
> ```
#### find\_circles {#find\_circles}

```python
def find_circles(self, roi: list[int] = [], x_stride: int = 2, y_stride: int = 1, threshold: int = 2000, x_margin: int = 10, y_margin: int = 10, r_margin: int = 10, r_min: int = 2, r_max: int = -1, r_step: int = 2) -> list[Circle]
```
Find circles in image

| item | description |
| --- | --- |
| **type** | func |
| **param** | **roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**x_stride**: x stride is the number of x pixels to skip when doing the hough transform. default is 2<br>**y_stride**: y_stride is the number of y pixels to skip when doing the hough transform. default is 1<br>**threshold**: threshold controls what circles are detected from the hough transform. Only circles with a magnitude greater than or equal to threshold are returned.<br>The right value of threshold for your application is image dependent.<br>**x_margin**: x_margin controls the merging of detected circles. Circles which are x_margin, y_margin, and r_margin pixels apart are merged. default is 10<br>**y_margin**: y_margin controls the merging of detected circles. Circles which are x_margin, y_margin, and r_margin pixels apart are merged. default is 10<br>**r_margin**: r_margin controls the merging of detected circles. Circles which are x_margin, y_margin, and r_margin pixels apart are merged. default is 10<br>**r_min**: r_min controls the minimum circle radius detected. Increase this to speed up the algorithm. default is 2<br>**r_max**: r_max controls the maximum circle radius detected. Decrease this to speed up the algorithm. default is min(roi.w / 2, roi.h / 2)<br>**r_step**: r_step controls how to step the radius detection by. default is 2.<br>|
| **return** | Return the circle when found circles, format is (circle1, circle2, ...), you can use circle class methods to do more operations |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::Circle> find_circles(std::vector<int> roi = std::vector<int>(), int x_stride = 2, int y_stride = 1, int threshold = 2000, int x_margin = 10, int y_margin = 10, int r_margin = 10, int r_min = 2, int r_max = -1, int r_step = 2)
> ```
#### find\_rects {#find\_rects}

```python
def find_rects(self, roi: list[int] = [], threshold: int = 10000) -> list[Rect]
```
Finds all rects in the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**threshold**: The threshold to use for the rects. default is 10000.<br>|
| **return** | Returns the rects of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::Rect> find_rects(std::vector<int> roi = std::vector<int>(), int threshold = 10000)
> ```
#### find\_qrcodes {#find\_qrcodes}

```python
def find_qrcodes(self, roi: list[int] = [], decoder_type: QRCodeDecoderType = ...) -> list[QRCode]
```
Finds all qrcodes in the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**decoder_type**: Select the QR code decoding method. Choosing QRCODE_DECODER_TYPE_QUIRC allows for retrieving QR code version, ECC level, mask, data type, and other details,<br>though it may decode slower at lower resolutions. Opting for QRCODE_DECODER_TYPE_ZBAR enables faster decoding at lower resolutions but may slow down at higher resolutions,<br>providing only the QR code content and position information. default is QRCODE_DECODER_TYPE_ZBAR.<br>Choosing the QRCODE_DECODER_TYPE_ZXING option will use the ZXing library for decoding. Supports both QRCode and Datamatrix.<br>Can be used as an alternative to function find_datamatrices to decode Datamatrix codes.<br>If you find that find_datamatrices is not working well for your Datamatrix codes, you can try using this option instead.<br>Provides only the QR code/ datamatrix content and position information. default is QRCODE_DECODER_TYPE_ZXING.<br>|
| **return** | Returns the qrcodes / (and/or datamatrix for option ZXing) of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::QRCode> find_qrcodes(std::vector<int> roi = std::vector<int>(), image::QRCodeDecoderType decoder_type = image::QRCodeDecoderType::QRCODE_DECODER_TYPE_ZBAR)
> ```
#### find\_apriltags {#find\_apriltags}

```python
def find_apriltags(self, roi: list[int] = [], families: ApriltagFamilies = ..., fx: float = -1, fy: float = -1, cx: int = -1, cy: int = -1) -> list[AprilTag]
```
Finds all apriltags in the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**families**: The families to use for the apriltags. default is TAG36H11.<br>**fx**: The camera X focal length in pixels, default is -1.<br>**fy**: The camera Y focal length in pixels, default is -1.<br>**cx**: The camera X center in pixels, default is image.width / 2.<br>**cy**: The camera Y center in pixels, default is image.height / 2.<br>|
| **return** | Returns the apriltags of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::AprilTag> find_apriltags(std::vector<int> roi = std::vector<int>(), image::ApriltagFamilies families = image::ApriltagFamilies::TAG36H11, float fx = -1, float fy = -1, int cx = -1, int cy = -1)
> ```
#### find\_datamatrices {#find\_datamatrices}

```python
def find_datamatrices(self, roi: list[int] = [], effort: int = 200) -> list[DataMatrix]
```
Finds all datamatrices in the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**effort**: Controls how much time to spend trying to find data matrix matches. default is 200.<br>|
| **return** | Returns the datamatrices of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::DataMatrix> find_datamatrices(std::vector<int> roi = std::vector<int>(), int effort = 200)
> ```
#### find\_barcodes {#find\_barcodes}

```python
def find_barcodes(self, roi: list[int] = []) -> list[BarCode]
```
Finds all barcodes in the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>|
| **return** | Returns the barcodes of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::BarCode> find_barcodes(std::vector<int> roi = std::vector<int>())
> ```
#### find\_displacement {#find\_displacement}

```python
def find_displacement(self, template_image: Image, roi: list[int] = [], template_roi: list[int] = [], logpolar: bool = False) -> Displacement
```
Finds the displacement between the image and the template.    TODO: support in the future\nnote: this method must be used on power-of-2 image sizes

| item | description |
| --- | --- |
| **type** | func |
| **param** | **template_image**: The template image.<br>**roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**template_roi**: The region-of-interest rectangle (x, y, w, h) to work in. If not specified, it is equal to the image rectangle.<br>**logpolar**: If true, it will instead find rotation and scale changes between the two images. default is false.<br>|
| **return** | Returns the displacement of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Displacement find_displacement(image::Image &template_image, std::vector<int> roi = std::vector<int>(), std::vector<int> template_roi = std::vector<int>(), bool logpolar = false)
> ```
#### find\_template {#find\_template}

```python
def find_template(self, template_image: Image, threshold: float, roi: list[int] = [], step: int = 2, search: TemplateMatch = ...) -> list[int]
```
Finds the template in the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **template_image**: The template image.<br>**threshold**: Threshold is floating point number (0.0-1.0) where a higher threshold prevents false positives while lowering the detection rate while a lower threshold does the opposite.<br>**roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image. Only valid in SEARCH_EX mode.<br>**step**: The step size to use for the template. default is 2. Only valid in SEARCH_EX mode<br>**search**: The search method to use for the template. default is SEARCH_EX.<br>|
| **return** | Returns a bounding box tuple (x, y, w, h) for the matching location otherwise None. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> find_template(image::Image &template_image, float threshold, std::vector<int> roi = std::vector<int>(), int step = 2, image::TemplateMatch search = image::TemplateMatch::SEARCH_EX)
> ```
#### find\_features {#find\_features}

```python
def find_features(self, cascade: int, threshold: float = 0.5, scale: float = 1.5, roi: list[int] = []) -> list[int]
```
Finds the features in the image.  TODO: support in the future

| item | description |
| --- | --- |
| **type** | func |
| **param** | **cascade**: The cascade to use for the features. default is CASCADE_FRONTALFACE_ALT.<br>**threshold**: The threshold to use for the features. default is 0.5.<br>**scale**: The scale to use for the features. default is 1.5.<br>**roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>|
| **return** | Returns the features of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> find_features(int cascade, float threshold = 0.5, float scale = 1.5, std::vector<int> roi = std::vector<int>())
> ```
#### find\_lbp {#find\_lbp}

```python
def find_lbp(self, roi: list[int] = []) -> LBPKeyPoint
```
Finds the lbp in the image. TODO: support in the future.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>|
| **return** | Returns the lbp of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> image::LBPKeyPoint find_lbp(std::vector<int> roi = std::vector<int>())
> ```
#### find\_keypoints {#find\_keypoints}

```python
def find_keypoints(self, roi: list[int] = [], threshold: int = 20, normalized: bool = False, scale_factor: float = 1.5, max_keypoints: int = 100, corner_detector: CornerDetector = ...) -> ORBKeyPoint
```
Finds the keypoints in the image. TODO: support in the future.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**threshold**: The threshold to use for the keypoints. default is 20.<br>**normalized**: If true, the image will be normalized before the operation. default is false.<br>**scale_factor**: The scale factor to use for the keypoints. default is 1.5.<br>**max_keypoints**: The maximum number of keypoints to use for the keypoints. default is 100.<br>**corner_detector**: The corner detector to use for the keypoints. default is CORNER_AGAST.<br>|
| **return** | Returns the keypoints of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> image::ORBKeyPoint find_keypoints(std::vector<int> roi = std::vector<int>(), int threshold = 20, bool normalized = false, float scale_factor = 1.5, int max_keypoints = 100, image::CornerDetector corner_detector = image::CornerDetector::CORNER_AGAST)
> ```
#### find\_edges {#find\_edges}

```python
def find_edges(self, edge_type: EdgeDetector, roi: list[int] = [], threshold: list[int] = [100, 200]) -> Image
```
Finds the edges in the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **edge_type**: The edge type to use for the edges. default is EDGE_CANNY.<br>**roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**threshold**: The threshold to use for the edges. default is 20.<br>|
| **return** | Returns the edges of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image* find_edges(image::EdgeDetector edge_type, std::vector<int> roi = std::vector<int>(), std::vector<int> threshold = std::vector<int>({100, 200}))
> ```
#### find\_hog {#find\_hog}

```python
def find_hog(self, roi: list[int] = [], size: int = 8) -> Image
```
Finds the hog in the image.   TODO: support in the future

| item | description |
| --- | --- |
| **type** | func |
| **param** | **roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**size**: The size to use for the hog. default is 8.<br>|
| **return** | Returns the hog of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> image::Image* find_hog(std::vector<int> roi = std::vector<int>(), int size = 8)
> ```
#### match\_lbp\_descriptor {#match\_lbp\_descriptor}

```python
def match_lbp_descriptor(self, desc1: LBPKeyPoint, desc2: LBPKeyPoint) -> int
```
Matches the lbp descriptor of the image.  TODO: support in the future

| item | description |
| --- | --- |
| **type** | func |
| **param** | **desc1**: The descriptor to use for the match.<br>**desc2**: The descriptor to use for the match.<br>|
| **return** | Returns the match of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> int match_lbp_descriptor(image::LBPKeyPoint &desc1, image::LBPKeyPoint &desc2)
> ```
#### match\_orb\_descriptor {#match\_orb\_descriptor}

```python
def match_orb_descriptor(self, desc1: ORBKeyPoint, desc2: ORBKeyPoint, threshold: int = 95, filter_outliers: bool = False) -> KPTMatch
```
Matches the orb descriptor of the image. TODO: support in the future

| item | description |
| --- | --- |
| **type** | func |
| **param** | **desc1**: The descriptor to use for the match.<br>**desc2**: The descriptor to use for the match.<br>**threshold**: The threshold to use for the match. default is 95.<br>**filter_outliers**: If true, the image will be filter_outliers before the operation. default is false.<br>|
| **return** | Returns the match of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> image::KPTMatch match_orb_descriptor(image::ORBKeyPoint &desc1, image::ORBKeyPoint &desc2, int threshold = 95, bool filter_outliers = false)
> ```
#### resize\_map\_pos {#resize\_map\_pos-2}

```python
def resize_map_pos(self, w_out: int, h_out: int, fit: Fit, x: int, y: int, w: int = -1, h: int = -1) -> list[int]
```
map point position or rectangle position from this image size to another image size(resize)

| item | description |
| --- | --- |
| **type** | func |
| **param** | **int**: h_out target image height<br>**fit**: resize method, see maix.image.Fit<br>**x**: original point x, or rectagle left-top point's x<br>**y**: original point y, or rectagle left-top point's y<br>**w**: original rectagle width, can be -1 if not use this arg, default -1.<br>**h**: original rectagle height, can be -1 if not use this arg, default -1.<br>|
| **return** | list type, [x, y] if map point, [x, y, w, h] if resize rectangle. |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<int> resize_map_pos(int w_out, int h_out, image::Fit fit, int x, int y, int w = -1, int h = -1)
> ```
### QRCodeDetector {#QRCodeDetector}

QRCodeDetector class


> C++ defination code:
> ```cpp
> class QRCodeDetector
> ```

#### \_\_init\_\_ {#\_\_init\_\_-23}

```python
def __init__(self) -> None
```
QRCodeDetector constructor.\nUse npu to accelerate the speed of QR code scanning, note that this object will occupy npu resources

| item | description |
| --- | --- |
| **type** | func |
| **static** | False |

> C++ defination code:
> ```cpp
> QRCodeDetector()
> ```
#### detect {#detect}

```python
def detect(self, img: Image, roi: list[int] = [], decoder_type: QRCodeDecoderType = ...) -> list[QRCode]
```
Finds all qrcodes in the image.

| item | description |
| --- | --- |
| **type** | func |
| **param** | **img**: The image to find qrcodes.<br>**roi**: The region of interest, input in the format of (x, y, w, h), x and y are the coordinates of the upper left corner, w and h are the width and height of roi.<br>default is None, means whole image.<br>**decoder_type**: Select the QR code decoding method. Choosing QRCODE_DECODER_TYPE_QUIRC allows for retrieving QR code version, ECC level, mask, data type, and other details,<br>though it may decode slower at lower resolutions. Opting for QRCODE_DECODER_TYPE_ZBAR enables faster decoding at lower resolutions but may slow down at higher resolutions,<br>providing only the QR code content and position information. default is QRCODE_DECODER_TYPE_ZBAR.<br>|
| **return** | Returns the qrcodes of the image |
| **static** | False |

> C++ defination code:
> ```cpp
> std::vector<image::QRCode> detect(image::Image *img, std::vector<int> roi = std::vector<int>(), image::QRCodeDecoderType decoder_type = image::QRCodeDecoderType::QRCODE_DECODER_TYPE_ZBAR)
> ```
