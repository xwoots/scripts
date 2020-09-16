#/usr/bin/pyton3

import shutil, os, re

pwd = os.getcwd()

list = os.listdir(pwd)

i = 0

for filename in list:
	if filename.endswith(".torrent"):
		shutil.move(filename, "/home/mateuw/torrents")
