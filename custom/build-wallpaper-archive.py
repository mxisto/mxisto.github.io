'''
This script takes every image on ./files/wallpapers, 
make a thumbnail to it using imagemagik and makes a page
with links for the original images.

this is hardcoded but it only makes sense for making 
a script like this in some specific pages anyway

https://usage.imagemagick.org/thumbnails/

magick mogrify -format gif -path thumbs -thumbnail 100x100 *.{jpg,png}
'''

import os
import shlex

html = (os.getcwd()+'/wallpaper-archive.html')
print(html)

def magick(folder):
    os.chdir('..')
    print("Converting images to thumbnails...")
    os.chdir(folder)
    combo = str("magick mogrify -format gif -path thumbs -thumbnail 200x200 *.{jpg,png,jpeg}")
    try:
        args = shlex.split(combo, posix=True)
        a=' '.join(args)
        print(f"Running as: {a} \n")
        os.system(a)
        print("magick done.\n")
    except:
        print ("A error ocurred in the shlex process\n%s" % a)

def make_links(images):
    for i in os.listdir(images):
        if ('.') in i:
            temp = i.split('.')
            tmb = temp[0]
            page.write(f'<a href="../files/wallpapers/{i}"><img src="../files/wallpapers/thumbs/{tmb}.gif"></a> ')
    print("\nPage created.\n")

with open(html,"w",encoding="UTF-8") as page:
    page.write("""
    <!DOCTYPE html>
    <html>
    <html lang="">
    <head>
        <meta charset="utf-8">
        <title>Wallpaper Archive</title>
        <link rel="stylesheet" type="text/css" href="../stylesheets/main.css">
        <meta name="viewport" content=
        "width=device-width, initial-scale=1.0">
    <body>

    <p><a href="../index.html"> <----- Back to Index</a></p>

    <div style="text-align: center; align-content: center;">

    <div><h1>Wallpaper Archive</h1>
    <p>Some wallpapers that I've found online or made myself.</p>
    <i>(Click to see the full images)</i></div>
    <br>
    <hr size="5" width="50%">
    <br>
    """)
    
    os.chdir('..')

    images_folder = (os.getcwd()+'/files/wallpapers/')
    thumbs_folder = (os.getcwd()+'/files/wallpapers/thumbs')

    make_links(images_folder)
    magick(images_folder)

    page.write("""
    </body>
    </html>
    """)