#!/usr/bin/env python3

import shutil, os, re

path = input("Enter the path where the script will run : ")

toreplace = input("Enter the pattern to replace : ")

replacement = input("Enter the replacement pattern : ")

os.chdir (path)

list = os.listdir(path)

for filename in list:
    dst = re.sub(toreplace, replacement, filename)
    src = filename 
    os.rename(src, dst)

