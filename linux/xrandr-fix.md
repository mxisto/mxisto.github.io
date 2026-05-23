---
title: Fixing missing screen resolutions using xrandr
css: "stylesheets/main.css"
output:
    html_document:
        mathjax: NULL
        pandoc_args: ["--mathml"]
        self_contained: false
---

[\<\-\-\-\-- Back to Index](../index.html)

Sometimes issues on the video driver might hide more resolution options that both your monitor display and graphics processor are capable of, however it's easy to force an specific resolution via `xrandr` (of course, supposing that you're using **X11**)

## 1 - Using `cvt` to create a new resolution

Use the `cvt` command:

::: codeblock

```bash
	cvt [vertical] [horizontal] [hrtz]
```
:::

Let's use as an example a resolution of 1280x1024, 60 Hrtz. That will be --> `cvt 1280 1024 60`.

The command will output an result, copy the output text from the terminal, we will need it in the next step.

## 2 - Add the new resolution to `xrandr`

Here you can go and paste the result from `cvt` on the command `xrandr --newmode` in order to create a new resolution mode:

::: codeblock

```bash
xrandr --newmode "1280x1024_60.00"  109.00  1280 1360 1496 1712  1024 1027 1034 1063 -hsync +vsync
```
:::

## 3 - Seeing the available displays with `xrandr`
In a single display setup is likely that the display name will be something like `HDMI-0`, `VGA-0`, `DVI-0` and so on, the `xrandr` command will show you a summary of available displays but you can also use:

::: codeblock

```bash
xrandr --listmonitors
```
:::
...for a more concise output.

## 4 - Associating the new resolution with the display

Now we will add the new set resolution to the resolution list associated to the selected display:

::: codeblock

```bash
xrandr --addmode [DISPLAY NAME] 1280x1024_60.00
```
:::

Check if the resolution is now available using `xrandr`, you should see a new resolution option.

## 5 - Changing to the new resolution

You can do this using...

- arandr (in a Window Manager)
- the default "Display" options menu from your Desktop Enviroment (XFCE, KDE, etc.)
- the `xrandr` command

For the last option, use:

::: codeblock

```bash
xrandr --output [DISPLAY] --mode [VERTICAL]x[HORIZONTAL]
```
:::

...with the newly set resolution.

## 6 - Making it permanent

If you were to reboot or exit the session now you would lose all the changes made above. 

Create a file in the home directory named `.xprofile` and write in it what we saw in step **2** and **4**. In the example of a 1280x1024, 60Hrtz screen:

::: codeblock

```bash
#!/bin/sh
xrandr --newmode "1280x1024_60.00"  109.00  1280 1360 1496 1712  1024 1027 1034 1063 -hsync +vsync
xrandr --addmode DisplayPort-0 1280x1024_60.00
```
:::

---

