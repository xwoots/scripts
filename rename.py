#!/usr/bin/env python3

import shutil, os, re

os.chdir ('/path/to/directory')

list = os.listdir('/path/to/directory/')

for filename in list:
    dst = re.sub('pattern_to_replace', 'replacement_pattern', filename)
    src = filename 
    os.rename(src, dst)

