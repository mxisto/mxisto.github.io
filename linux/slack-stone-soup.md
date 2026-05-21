---
title: Compiling DCSS in Slackware/SalixOS
css: "../stylesheets/main.css"
output:
    html_document:
        mathjax: NULL
---
[\<\-\-\-\-- Back to Index](../index.html)

Building and compiling **Dungeon Crawl Stone Soup** with graphical tiles on Salix/Slackware.

Things to consider regarding Slackware:

1. the SlackBuild availiable is the one that uses the CLI for rendering the game (`nodeps` source package)
2. the **glibc** version availiable is too old to use the latest Appimage
3. the graphical tiles are too cool to not be an standard option in the SlackBuild

## Libraries Needed
* lua
* pngcrush
* python-pip
* python-PyYAML
* SDL2
* SDL2_image

Both were based on the minimal install base set of packages, some of them might already be installed if you decided to go for the "full" installation during setup.

In Slack, use [slackpkg](https://slackpkg.org/documentation.html):

::: codeblock
```bash
sudo slackpkg lua pngcrush python-pip python-PyYAML SDL2 SDL2_image
```
:::

In Salix, use:

::: codeblock
```bash
sudo slapt-get --install lua pngcrush python-pip python-PyYAML SDL2 SDL2_image

```
:::

In this case, we are only downloading the packages that don't get downloaded from the packaged dependencies from DCSS (see below):

## Git instructions
Excerpt from [DCSS's installation guide](https://github.com/crawl/crawl/blob/master/crawl-ref/INSTALL.md):

::: codeblock
```bash
# Clone the repository
git clone https://github.com/crawl/crawl.git
cd crawl

# se DCSS's packaged dependencies
git submodule update --init

# Build DCSS 
# (TILES=y builds the graphical version) 
# (-j* specifies the number of CPU cores to use in the make process)
cd crawl-ref/source
make -j4 TILES=y

# Play DCSS by running the compiled binary
./crawl
```
:::
***
