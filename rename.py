#!/usr/bin/env python3

import shutil, os, re

os.chdir ('/home/mateuw/rutorrent/downloads/completed/Animes/My Hero Academia S04')

list = os.listdir('/home/mateuw/rutorrent/downloads/completed/Animes/My Hero Academia S04')

for filename in list:
    dst = re.sub('S4 - ', 'S04E', filename)
    src = filename 
    os.rename(src, dst)

