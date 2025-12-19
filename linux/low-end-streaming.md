[\<\-\-\-\-- Back to Index](../index.html)

***

Quick example on how to use low end hardware more efficiently for modern tasks.

## Configuration used in this example:
Laptop: Samsung RV411

- Processor: Intel Pentium P6100 (Dual core, 2,00GHz)
- RAM: 4GB DDR3
- Storage: 320GB HDD
- System: Fedora Linux 42 XFCE

## Use MPV for everything
mpv can be used in conjunction with yt-dlp to stream media from online sources (Youtube, Odysee, Peertube, and from direct media sources such as webm)

By default yt-dlp always gets the best quality format avaliable, but with a Pentium we are limited to 720p and below.

For this, you can add this line to your mpv configuration file:

***
```
# place this in .config/mpv/mpv.conf !
yt-dl-format=bestvideo[height<=?1080]+bestaudio/best
```
***

This does not affect the playback of local files, only online media since it depends on yt-dlp in order to use it.

## For local streaming
Pretty straightforward, prefer the following formats and codecs for your media:

720p or below
x264 | MPEG-4 AVC

***
