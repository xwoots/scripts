#/usr/bin/pyton3

import shutil, os, re

pwd = os.getcwd()

list = os.listdir(pwd)

i = 0

for filename in list:
	if filename.endswith(".ext"): // Modify ext by the extension
		shutil.move(filename, "/path/to/move") // Replace by the path to move
