#!/usr/bin/env python3

import shutil, os, re

os.chdir ('/path/to/directory')

list = os.listdir('/path/to/directory/')

for filename in list:
    dst = re.sub('to_replace', 'replacement', filename)
    src = filename 
    os.rename(src, dst)

