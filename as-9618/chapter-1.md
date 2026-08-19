# AS 9618 Chapter 1: Information Representation

<div class="chapter-meta"><strong>AS 9618 · Paper 1</strong><span>9618 · 2027–2029 · Version 2</span></div>

## Official Syllabus Checklist

Revise: number systems and codes; bitmap and vector graphics; sound representation and compression.

> The checklist paraphrases the syllabus for revision. Use the official syllabus as the final authority.

## Core Knowledge

Use the topic sections below to connect definitions, processes, comparisons and calculations.


<span id="_3-one-page-mind-map" class="legacy-anchor" aria-hidden="true"></span>

## Chapter at a Glance

Use this overview to convert, calculate, compare and justify information representation.

### Convert and encode

<span lang="zh-CN">先确认单位、数制和符号表示方法，再开始转换。</span>

- Convert between binary, denary, hexadecimal and binary-coded decimal.
- Distinguish decimal prefixes based on 1000 from binary prefixes based on 1024.
- Represent negative integers using the specified complement method and bit width.

**Exam cue:** Keep the required number of bits and identify overflow when the result is out of range.

### Calculate multimedia size

<span lang="zh-CN">列出所有影响文件大小的量，并统一单位。</span>

- Calculate bitmap size from dimensions and colour depth, including header data when specified.
- Calculate sound size from sampling rate, sampling resolution, channels and duration.
- Relate higher resolution or sampling values to both quality and storage size.

**Exam cue:** Write the complete formula and give the final answer in the requested unit.

### Compare representations

<span lang="zh-CN">比较时要说明存储方式、缩放效果和适用场景。</span>

- A bitmap stores pixels, while a vector graphic stores objects and their properties.
- Vector graphics scale without pixelation, while bitmap detail depends on resolution.
- ASCII, extended ASCII and Unicode provide different character ranges and storage requirements.

**Exam cue:** Give one linked difference rather than two separate descriptions.

### Choose compression

<span lang="zh-CN">根据是否允许永久丢失数据来选择压缩方法。</span>

- Lossless compression reconstructs the original data exactly.
- Lossy compression removes data permanently to achieve a smaller file.
- Buffering stores incoming stream data temporarily when delivery and playback rates differ.

**Exam cue:** Justify the compression or streaming choice using quality, bandwidth and user needs.

---

## 1.1 Data Representation

### Binary prefixes vs decimal prefixes

#### Core idea

<span lang="zh-CN">计算机中有两套常见单位</span>：

| Type | Example | Meaning | Used for |
| --- | --- | ---: | --- |
| Decimal prefix | KB, MB, GB, TB | powers of 1000 | storage devices, file size in many exam calculations |
| Binary prefix | KiB, MiB, GiB, TiB | powers of 1024 | memory / RAM / exact binary measurement |

#### Must-know table

| Unit | Value |
| --- | ---: |
| 1 kilobyte / KB | 1000 bytes |
| 1 kibibyte / KiB | 1024 bytes |
| 1 megabyte / MB | 1000 KB = 1 000 000 bytes |
| 1 mebibyte / MiB | 1024 KiB = 1 048 576 bytes |
| 1 gigabyte / GB | 1000 MB |
| 1 gibibyte / GiB | 1024 MiB |
| 1 terabyte / TB | 1000 GB |
| 1 tebibyte / TiB | 1024 GiB |
| 1 petabyte / PB | 1000 TB |
| 1 pebibyte / PiB | 1024 TiB |
| 1 exabyte / EB | 1000 PB |
| 1 exbibyte / EiB | 1024 PiB |

#### Mark scheme style phrase

> A binary prefix uses powers of 2 / 1024, while a decimal prefix uses powers of 10 / 1000.

#### Common mistake

| Mistake | Correction |
| --- | --- |
| saying 1 KB = 1024 bytes | In Cambridge wording, **KiB = 1024**, **KB = 1000** |
| mixing MB and MiB in calculation | Use the unit given in the question |
| writing “bigger” without numbers | Say 1024 vs 1000 |

---

### Number systems

| Number system | Base | Digits used | Key exam point |
| --- | ---: | --- | --- |
| Binary | 2 | 0, 1 | used by computer systems |
| Denary / decimal | 10 | 0–9 | normal human number system |
| Hexadecimal | 16 | 0–9, A–F | compact representation of binary |
| BCD | digit-based | 4 bits per denary digit | useful for exact decimal digits |

#### Hex table

| Denary | Binary | Hex | Denary | Binary | Hex |
| ---: | --- | --- | ---: | --- | --- |
| 0 | 0000 | 0 | 8 | 1000 | 8 |
| 1 | 0001 | 1 | 9 | 1001 | 9 |
| 2 | 0010 | 2 | 10 | 1010 | A |
| 3 | 0011 | 3 | 11 | 1011 | B |
| 4 | 0100 | 4 | 12 | 1100 | C |
| 5 | 0101 | 5 | 13 | 1101 | D |
| 6 | 0110 | 6 | 14 | 1110 | E |
| 7 | 0111 | 7 | 15 | 1111 | F |

---

### Binary ↔ denary

#### Binary to denary example

Convert `10010110` to denary.

```text
128 64 32 16 8 4 2 1
 1   0  0  1 0 1 1 0

= 128 + 16 + 4 + 2
= 150
```

#### Denary to binary example

Convert 558 to 12-bit binary.

```text
558 = 512 + 32 + 8 + 4 + 2

2048 1024 512 256 128 64 32 16 8 4 2 1
  0    0   1   0   0  0  1  0 1 1 1 0

Answer = 0010 0010 1110
```

#### Exam-style note

AS Paper 1 may ask for **12-bit binary**, not only 8-bit. Always count the required number of bits.

---

### Binary ↔ hexadecimal

#### Binary to hexadecimal

Convert `110001100111` to hexadecimal.

```text
Split into nibbles:
1100 0110 0111

1100 = C
0110 = 6
0111 = 7

Answer = C67
```

#### Hexadecimal to binary

Convert `22E` to binary.

```text
2 = 0010
2 = 0010
E = 1110

Answer = 0010 0010 1110
```

#### Hexadecimal to denary

Convert `2140` to denary.

```text
2 × 16^3 + 1 × 16^2 + 4 × 16^1 + 0
= 8192 + 256 + 64
= 8512
```

#### Common mistake

| Mistake | Correction |
| --- | --- |
| not grouping binary into 4-bit nibbles | Hex conversion must use groups of 4 bits |
| forgetting leading zeros | One hex digit = exactly 4 bits |
| treating A–F as letters only | A=10, B=11, C=12, D=13, E=14, F=15 |

---

### One's complement and two's complement

#### One's complement

One's complement reverses every bit.

```text
01011010
becomes
10100101
```

For AS 9618, understand it, but **two's complement is more exam-heavy**.

---

### Two's complement

#### 8-bit range

| Representation | Range |
| --- | --- |
| 8-bit unsigned | 0 to 255 |
| 8-bit two's complement | -128 to +127 |

#### Two's complement column values

```text
-128 64 32 16 8 4 2 1
```

#### Binary to denary example

Convert `11100010` to denary.

```text
-128 64 32 16 8 4 2 1
  1   1  1  0 0 0 1 0

= -128 + 64 + 32 + 2
= -30
```

#### Smallest and largest 8-bit two's complement

```text
Smallest = 1000 0000 = -128
Largest  = 0111 1111 = +127
```

#### Denary negative to two's complement

Convert -23 to 8-bit two's complement.

Step 1: write +23.

```text
00010111
```

Step 2: invert bits.

```text
11101000
```

Step 3: add 1.

```text
11101001
```

So:

```text
-23 = 11101001
```

---

### Binary subtraction using two's complement

Example: subtract denary 23 from `01001010`.

`01001010` = 74.

Need:

```text
74 - 23
```

Write -23 in two's complement:

```text
+23 = 00010111
invert = 11101000
add 1 = 11101001
```

Add:

```text
  01001010
+ 11101001
=1 00110011
```

Ignore the 9th carry bit:

```text
00110011 = 51
```

#### Mark scheme style phrase

> Convert the number being subtracted into its two's complement, then add it to the first binary number. Ignore any carry beyond the fixed number of bits if the result is within range.

---

### Overflow

#### Definition

> Overflow occurs when the result of a calculation is too large or too small to be represented using the available number of bits.

#### Important distinction

| Weak answer | Better answer |
| --- | --- |
| overflow happens because there is a carry | overflow happens because the result is outside the representable range |
| answer is too big | answer is too long to be represented in the same number of bits |
| 8-bit result has a 9th bit | good for unsigned, but also mention available bits / range |

#### For two's complement

Overflow can occur when:

+ adding two positive numbers gives a negative result
+ adding two negative numbers gives a positive result
+ result is outside -128 to +127 for 8-bit two's complement

---

### Binary Coded Decimal (BCD)

#### What BCD does

BCD stores each denary digit separately using 4 bits.

Example:

```text
573

5 = 0101
7 = 0111
3 = 0011

BCD = 0101 0111 0011
```

#### BCD to denary example

```text
0101 0111 0011
= 5 7 3
= 573
```

#### BCD is not normal binary

| Representation | Meaning |
| --- | --- |
| `0101 0111 0011` as BCD | 573 |
| `010101110011` as binary | 1395 |

#### BCD applications

| Application | Why BCD is suitable |
| --- | --- |
| financial / banking calculations | exact decimal values, avoids accumulating rounding errors |
| electronic display | each denary digit can be displayed separately |
| date/time in BIOS | straightforward conversion to displayed decimal digits |
| barcode systems | decimal digits can be represented accurately |

#### Mark scheme style phrase

> BCD is used where exact decimal digits are needed, because normal binary may not represent decimal fractions exactly and this could cause rounding errors.

---

### Character sets

#### Character set definition

> A character set is a set/list of characters and the binary codes used to represent them.

#### How text is stored

> Each character has a unique binary code, and the codes are stored in sequence.

---

### ASCII, extended ASCII and Unicode

| Character set | Typical bits | Key point |
| --- | ---: | --- |
| ASCII | 7 bits | 128 characters |
| Extended ASCII | 8 bits | 256 characters |
| Unicode | often 16 or 32 bits in syllabus examples | much wider range of languages and symbols |

#### Unicode advantages over ASCII

+ wider range of characters
+ more languages can be represented
+ symbols / emojis can be represented
+ suitable for global systems

#### Mark scheme style phrase

> Unicode can represent a wider range of characters, including more languages and symbols such as emojis.

#### Unicode drawback

+ may use more bits per character
+ file size may be larger

---

### Character code conversion

#### Binary Unicode to denary

Convert:

```text
0010 0111 0110 1110
```

```text
= 8192 + 1024 + 512 + 256 + 64 + 32 + 8 + 4 + 2
= 10094
```

#### Extended ASCII conversion example

| Character | Denary | 8-bit Binary | Hex |
| --- | ---: | --- | --- |
| ! | 33 | 0010 0001 | 21 |
| L | 76 | 0100 1100 | 4C |
| ü | 252 | 1111 1100 | FC |

---

## 1.2 Multimedia — Bitmap Images

### Bitmap image keywords

| Term | Meaning |
| --- | --- |
| Bitmap image | image made from pixels |
| Pixel | smallest element / dot / square of an image |
| Image resolution | number of pixels in the image |
| Screen resolution | number of pixels displayed on a screen / dots per inch in display context |
| Colour depth / bit depth | number of bits used to store the colour of one pixel |
| File header | metadata about the image file |
| Pixel density | number of pixels per unit area, such as ppi or dpi |

---

### Bit depth / colour depth

#### Formula

```text
Number of colours = 2 ^ bit depth
```

Examples:

| Bit depth | Number of colours |
| ---: | ---: |
| 1 bit | 2 |
| 4 bits | 16 |
| 8 bits | 256 |
| 16 bits | 65 536 |
| 24 bits | 16 777 216 |

#### Exam-style answer: effect of decreasing bit depth

| Effect on image | Effect on file |
| --- | --- |
| fewer colours / shades available | fewer bits used to store each pixel |
| image may not match original as well | less data stored |
| detail may be lost | file size is reduced |

#### Mark scheme style phrase

> Decreasing bit depth means fewer bits are used to store each pixel, so fewer colours or shades can be represented and the file size is reduced.

---

### Image file size calculation

#### Formula

```text
Image file size in bits = number of pixels × bit depth
```

or

```text
Image file size in bits = width × height × bit depth
```

Convert:

```text
bytes = bits / 8
KB or MB = divide by 1000
KiB or MiB = divide by 1024
```

#### Exam-style example

A camera creates an image with **2 million pixels** and **16-bit depth**. Calculate the file size in MB.

```text
2 000 000 × 16 = 32 000 000 bits
32 000 000 / 8 = 4 000 000 bytes
4 000 000 / 1 000 000 = 4 MB
```

#### 2024-style example

An image has 4000 × 3000 pixels and 4 bits per pixel.

```text
4000 × 3000 × 4 = 48 000 000 bits
48 000 000 / 8 = 6 000 000 bytes
= 6 MB
```

> <span lang="zh-CN">注意</span>：<span lang="zh-CN">如果题目或</span> mark scheme <span lang="zh-CN">用</span> MB，<span lang="zh-CN">通常按</span> decimal 1 MB = 1 000 000 bytes。<span lang="zh-CN">题目写</span> MiB <span lang="zh-CN">才用</span> 1024。

---

### File header

A bitmap file header may store:

+ file type
+ file size
+ image dimensions / resolution
+ bit depth / colour depth
+ compression type
+ location / offset of image data

#### Mark scheme phrase

> The file header stores metadata about the image, such as file type, file size, resolution, bit depth and compression method.

---

## Vector Graphics

### Vector graphic idea

Vector graphics do not store every pixel. They store objects / shapes mathematically.

Examples of objects:

+ line
+ rectangle
+ circle
+ ellipse
+ polygon
+ text object

### Property

> A property is an attribute of a vector object, such as position, line colour, fill colour, line thickness, radius or coordinates.

### Drawing list

> A drawing list stores the objects / commands needed to draw the image and the properties of each object.

#### Example drawing list

```text
CIRCLE centre(50,50), radius 20, fill red
LINE from(10,10) to(90,10), thickness 2
RECTANGLE top-left(20,20), width 40, height 30
```

### Vector vs bitmap

| Feature | Bitmap | Vector |
| --- | --- | --- |
| Made from | pixels | objects / shapes |
| File stores | colour of each pixel | drawing list + properties |
| Best for | photographs | logos, diagrams, maps |
| Scaling | may become pixelated | can scale without loss of quality |
| Editing | edit pixels | edit objects/properties |
| File size | can be large for high resolution | often smaller for simple diagrams |

#### Scenario answer

> A vector graphic is suitable for a logo because it can be resized without loss of quality, and the image is stored as objects with properties rather than as individual pixels.

---

## Sound Representation

### Analogue sound

Sound is naturally analogue. This means it changes continuously.

A computer must convert it into digital data by sampling.

### Sampling

#### Mark scheme style answer

> The amplitude of the sound wave is measured at regular time intervals. Each sample is converted into a binary value.

### Key terms

| Term | Meaning |
| --- | --- |
| Sampling rate | number of times the amplitude is measured per time interval / per second |
| Sampling resolution / bit depth | number of bits used to store each amplitude measurement |
| Analogue | continuously changing sound wave before being recorded by a computer |

### Effect of increasing sample rate / resolution

| Increase in... | Effect on sound | Effect on file |
| --- | --- | --- |
| sampling rate | more measurements per second, more accurate digital copy | larger file size |
| sampling resolution | amplitude stored with more precision | larger file size |

#### Sound file size formula

```text
Sound file size in bits =
sample rate × sampling resolution × duration × number of channels
```

#### Example

A 30-second stereo sound has sample rate 44 100 Hz and sampling resolution 16 bits.

```text
44 100 × 16 × 30 × 2 = 42 336 000 bits
42 336 000 / 8 = 5 292 000 bytes
```

---

## 1.3 Compression

### Why compression is needed

Compression reduces file size.

Benefits:

+ less storage space needed
+ less bandwidth needed
+ faster upload / download / transmission
+ less buffering in streaming
+ lower data allowance used

#### Mark scheme style phrase

> Compression reduces the file size so less bandwidth is needed and the file can be transmitted faster.

---

### Lossy compression

#### Definition

> Lossy compression reduces file size by permanently removing some data, so the original file cannot be fully reconstructed.

#### Suitable for

+ video streaming
+ music streaming
+ web photos
+ situations where small loss of quality is acceptable

#### 2025 real-time streaming justification

For real-time video conferences, lossy compression is usually more appropriate because:

+ it reduces file size more than lossless
+ less bandwidth / data is needed
+ buffering is reduced
+ the video can stay closer to real time
+ some removed data may not be noticed by the user
+ resolution / audio sample rate can be reduced without destroying the communication

---

### Lossless compression

#### Definition

> Lossless compression reduces file size without permanently removing data, so the original file can be restored exactly.

#### Suitable for

+ text files
+ program code
+ spreadsheets
+ legal / medical / scientific data
+ images where exact detail must not be lost

#### Mark scheme phrase

> The original file can be reconstructed exactly.

---

### Run-length encoding (RLE)

#### What RLE does

> RLE stores a run of repeated adjacent data as the value and the number of times it occurs.

Example:

```text
Original:
AAAAA BBB CC

RLE:
5A 3B 2C
```

For bitmap images:

```text
red red red red blue blue
becomes
4 red, 2 blue
```

#### When RLE works well

+ long runs of repeated values
+ simple graphics
+ flat-colour bitmap images

#### When RLE works badly

+ photographs
+ noisy images
+ text with few repeated characters
+ alternating patterns like `ABABABAB`

#### Common exam warning

> RLE can increase file size if there are few repeated adjacent values, because count information also has to be stored.

---

## Mark Scheme Keywords

### Data representation

+ **binary prefix**
+ **decimal prefix**
+ **powers of 2 / powers of 10**
+ **1024 / 1000**
+ **base 2 / base 10 / base 16**
+ **nibble**
+ **4 bits**
+ **two's complement**
+ **representable range**
+ **overflow**
+ **BCD**
+ **exact decimal digits**
+ **rounding errors**

### Character sets

+ **character set**
+ **unique binary code**
+ **stored in sequence**
+ **ASCII**
+ **extended ASCII**
+ **Unicode**
+ **wider range of characters**
+ **more languages**
+ **symbols / emojis**
+ **more bits per character**

### Bitmap / vector / sound

+ **pixel**
+ **bit depth**
+ **colour depth**
+ **resolution**
+ **screen resolution**
+ **file header**
+ **metadata**
+ **drawing list**
+ **property**
+ **object**
+ **sampling rate**
+ **sampling resolution**
+ **analogue**
+ **amplitude**

### Compression

+ **reduces file size**
+ **less storage**
+ **less bandwidth**
+ **faster transmission**
+ **less buffering**
+ **lossy**
+ **permanently removing data**
+ **lossless**
+ **original restored exactly**
+ **run-length encoding**
+ **repeated adjacent data**
+ **value and count**

---

## Topic-Specific Common Confusions

| Mistake | Why it loses marks | Correct version |
| --- | --- | --- |
| using 1024 for MB when question says MB | MB is decimal unless question says MiB | MB = 1 000 000 bytes |
| writing `110101` when 8-bit asked | not enough bits | write `00110101` |
| treating two's complement as unsigned | negative values wrong | use `-128 64 32 16 8 4 2 1` |
| saying overflow is “a carry” only | too vague | result cannot be represented in available bits |
| confusing BCD with binary | BCD stores each digit separately | split into 4-bit groups |
| saying Unicode only has “more letters” | too narrow | more characters, languages, symbols/emojis |
| saying higher bit depth means higher resolution | different terms | bit depth = bits per pixel; resolution = number of pixels |
| forgetting to divide bits by 8 | answer too large | bytes = bits / 8 |
| saying compression makes streaming “better” | vague | less bandwidth and less buffering |
| saying lossless is best for video call | not usually scenario-appropriate | lossy is often better for real-time streaming |
| saying RLE always compresses | false | only effective with repeated adjacent data |
| confusing sampling rate and sampling resolution | common sound mistake | rate = samples per second; resolution = bits per sample |

---

## Scenario Answer Bank

### Explain why Unicode is used for a global app

> Unicode is suitable because it can represent a wider range of characters than ASCII. This includes characters from more languages and symbols such as emojis, so users from different countries can use the app.

### Explain why decreasing bit depth reduces image file size

> Decreasing bit depth means fewer bits are used to store each pixel. This reduces the amount of data stored, so the file size becomes smaller. However, fewer colours or shades can be represented, so image detail may be lost.

### Explain why a bitmap image becomes pixelated when enlarged

> A bitmap image is made from a fixed number of pixels. When the image is enlarged, the same pixels cover a larger area, so individual pixels become more visible and the image appears less sharp.

### Explain why vector graphics are suitable for logos

> Vector graphics store objects and their properties rather than individual pixels. This means the image can be resized without losing quality, which is useful for a logo that may be used at different sizes.

### Explain how sound is sampled

> The amplitude of the analogue sound wave is measured at regular time intervals. Each measurement is converted into a binary value. A higher sampling rate or sampling resolution gives a more accurate digital representation but increases file size.

### Justify lossy compression for a video conference

> Lossy compression is suitable because a video is data-intensive and must be transmitted in real time. Lossy compression reduces the file size more than lossless compression, so less bandwidth is needed and buffering is reduced. Some loss of quality is acceptable because users can still understand the video and audio.

### Justify lossless compression for program code

> Lossless compression is suitable because the original file can be restored exactly. Program code must not lose any characters or instructions, otherwise the program may not run correctly.

### Explain BCD use in financial systems

> BCD is suitable because each decimal digit is stored separately. This helps represent decimal values accurately and avoids accumulating rounding errors that may occur when decimal fractions are stored in normal binary.

### Explain RLE using an image

> RLE identifies adjacent pixels with the same colour. It stores the colour and the number of times it is repeated. This reduces file size when the image contains long runs of the same colour.

---

## Process Diagrams

### Choosing a compression method

```mermaid
flowchart TD
A[Need to compress a file] --> B{Must the original be restored exactly?}
B -->|Yes| C[Use lossless compression]
B -->|No| D{Is real-time transmission or small file size more important?}
D -->|Yes| E[Use lossy compression]
D -->|No| F{Is small quality loss acceptable?}
F -->|Yes| E
F -->|No| C
C --> G[Examples: text, program code, medical image]
E --> H[Examples: video call, streaming audio, web photo]
```

### Bitmap file size calculation

```mermaid
flowchart LR
A[Number of pixels<br/>or width × height] --> B[Multiply by bit depth]
B --> C[File size in bits]
C --> D[Divide by 8]
D --> E[Bytes]
E --> F[Divide by 1000 or 1024<br/>depending on unit]
```

### Sound sampling process

```mermaid
flowchart LR
A[Analogue sound wave] --> B[Measure amplitude at regular intervals]
B --> C[Convert each sample to binary]
C --> D[Store sequence of binary values]
D --> E[Digital sound file]
```

---

## Required Ideas and Exam Language

Use technical terms as part of a complete statement: identify the component or method, state what it does, then link its effect to the question context. A keyword without a correct relationship is not a complete marking point.

## Common Confusions

- Do not substitute a related term for the process named in the question.
- Do not list advantages or definitions without linking them to the stated context.

## Worked Examples

The worked calculations, process templates and scenario answers above model the chain of reasoning expected in examination responses. Rework each example before reading its answer.

## 10-Mark Quick Check

**Total: 10 marks**

### Questions

1. State the difference between a kilobyte and a kibibyte. [1]  
2. Convert `110001100111` to hexadecimal. [1]  
3. Convert `11100010` from 8-bit two's complement to denary. [1]  
4. Write the smallest 8-bit two's complement binary value. [1]  
5. Convert BCD `0101 0111 0011` to denary. [1]  
6. State one advantage of Unicode over ASCII. [1]  
7. State the formula for bitmap file size in bits. [1]  
8. Give the term for the number of bits used to store each sound amplitude measurement. [1]  
9. Name one lossless compression method. [1]  
10. State why lossy compression may be suitable for real-time video streaming. [1]

## Quick Check Answers

1. KB = 1000 bytes; KiB = 1024 bytes.  
2. `C67`  
3. `-30`  
4. `10000000`  
5. `573`  
6. Unicode represents more characters/languages/symbols/emojis.  
7. `number of pixels × bit depth` or `width × height × bit depth`  
8. Sampling resolution / bit depth.  
9. Run-length encoding / RLE.  
10. It reduces file size more, so less bandwidth is needed and buffering is reduced.

---

## 20-Mark Exam Practice

**Total: 20 marks**

### Question 1: Number systems and character sets [8]

(a) State one difference between a tebibyte and a terabyte. [1]  
(b) Convert the denary integer 558 into 12-bit binary. [1]  
(c) Convert your answer in part (b) into hexadecimal. [1]  
(d) Convert the 8-bit two's complement binary integer `11100010` into denary. [1]  
(e) Write the smallest and largest 8-bit two's complement binary integers. [2]  
(f) Give one advantage of Unicode over ASCII. [1]  
(g) Explain one reason why BCD is used in financial calculations. [1]

#### Mark scheme

(a) Tebibyte uses binary prefix / powers of 2 / 1024, terabyte uses decimal prefix / powers of 10 / 1000. [1]  
(b) `0010 0010 1110` [1]  
(c) `22E` [1]  
(d) `-30` [1]  
(e) Smallest `10000000` [1], largest `01111111` [1]  
(f) Unicode can represent more characters / more languages / symbols / emojis. [1]  
(g) Decimal values must be accurate / avoids rounding errors / stores each denary digit separately. [1]

---

### Question 2: Bitmap image and sound [7]

A digital camera creates an image with 2 000 000 pixels and a bit depth of 16 bits.

(a) Calculate the file size in MB. Show working. [2]  
(b) Explain the effect of decreasing the bit depth on the image and on the image file. [4]  
(c) Give the term for the number of times the amplitude of a sound wave is measured per second. [1]

#### Mark scheme

(a)

```text
2 000 000 × 16 = 32 000 000 bits
32 000 000 / 8 = 4 000 000 bytes
4 000 000 / 1 000 000 = 4 MB
```

Award [1] for correct working, [1] for `4 MB`.

(b)

+ fewer colours / shades available [1]
+ image may not match original / detail is lost [1]
+ fewer bits used to store each pixel [1]
+ less data stored / file size reduced [1]

(c) Sampling rate. [1]

---

### Question 3: Compression scenario [5]

A school uses live video conferencing. The video is compressed before being transmitted using real-time bit streaming.

(a) Explain why the video is compressed before transmission. [2]  
(b) Identify whether lossy or lossless compression is more appropriate. Justify your answer. [3]

#### Mark scheme

(a)

+ video is data-intensive / large file size [1]
+ reducing file size reduces bandwidth / reduces buffering / allows faster transmission [1]

(b)

+ lossy compression is more appropriate [choice itself may not be awarded separately, but answer must be consistent]
+ reduces file size more than lossless [1]
+ less bandwidth / data is needed, so buffering is reduced [1]
+ some data can be removed without noticeably affecting user experience / resolution or audio sample rate can be reduced [1]

---

## Final Revision Checklist

- [ ] I can calculate with binary, hexadecimal, BCD and two's complement.
- [ ] I can calculate bitmap/vector and sampled-sound storage.
- [ ] I can compare character encodings and multimedia representations.
- [ ] I can justify lossy, lossless and RLE compression choices.
- [ ] I can complete and self-mark both chapter practices.
