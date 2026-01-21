'''
This script takes every .md file in every recursive directory and
generates a html page using pandoc.

At this time being it only works on POSIX systems since it is what I use to write the site

pandoc -s -o [file].html [file].md --css=[stylesheet].css --metadata title="[name] --mathml"

mathml is used instead of mathjax
'''

import os
import shlex

myfiles = []
mydir = []
dir_level = 0
dir_str = str('')

def show_dir():
    '''list .md files in current directory'''
    global myfiles, mydir
    os.system('clear')
    x = 0
    y = 0
    print("In directory: %s \n" % os.getcwd())
    for i in os.listdir():
        if "." not in i:
            mydir.append(i)
            print(f"{y}- {i}")
            y+=1
    
    print("\nCurrent page files here:\n")
    for i in os.listdir():
        if i.endswith('.md'):
            myfiles.append(i)
            print(f"{x}- {i}")
            x+=1
        elif i.endswith('.html'):
            print(f"   {i}")
    print("\n")

def change_dir(directory):
    '''changes the working directory, ".." goes one directory up like in "cd .."'''
    global myfiles, mydir
    if directory == "":
        print(None)
    else:
        myfiles.clear()
        mydir.clear()
        os.chdir(directory)
    os.system('clear')
    
def goback():
    '''goes back to last directory, separated funcion to avoid messing with the other one'''
    os.chdir("..")
    show_dir()
    myfiles.clear()
    mydir.clear()
    show_dir()

def pandoc(file):
    # styleshhet is hardcoded as main.css for now until I start to work with more style files
    global dir_level, dir_str
    if dir_level == 0:
        dir_str = str('.')
    
    style_path = str(dir_str+"stylesheets/main.css")
    name = str(input("Title for the page\n>> "))
    combo = str(f'pandoc -s -o {file}.html {file}.md --css=\\"{style_path}\\" --metadata title=\\"{name}\\" --mathml')
    try:
        args = shlex.split(combo, posix=True)
        a=' '.join(args)
        print(f"Running as: {a} \n")
        os.system(a)
        print("Done.\n")
        while True:
            repeat = input("Repeat process? (Y)es or (N)o?\n>> ").lower()
            if repeat == "y":
                os.system(a)
            else:
                os.system('clear')
                break
    except:
        print ("A error ocurred in the shlex process\n%s" % a)

def set_dir_level(response):
    '''adjusts the directory level in order to corretly point to the main.css file in ./stylesheets/'''
    global dir_level, dir_str
    if response == 1:
        dir_level+=1
        dir_str+=("../")
    else:
        dir_level-=1
        dir_str=dir_str[0:-3]

while True:    
    print("g) goto | h) goback | p) pandoc | q)quit\n")
    show_dir()
    option = str(input("Select a option\n>> ")).lower()
    if option == "g":
        select = int(input("Select directory by number\n>> "))
        directory = str(mydir[select])
        change_dir(directory)
        set_dir_level(1)
    elif option == "h":
        goback()
        set_dir_level(0)
    elif option == "p":
        select = int(input("Select name by number\n>> "))
        file = str(myfiles[select])
        file=file.strip('.md')
        print(file)
        pandoc(file)
    elif option == "q":
        break
    else:
        print("Not an option...")
