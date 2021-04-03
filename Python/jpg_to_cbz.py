#!\usr\bin\python3

import shutil, os, re, zipfile, subprocess

manga = input("Enter the path where the script will run : ")
path = "/home/mateuw/data_share/downloads/completed/Mangas/" + manga
os.chdir(path)
list = os.listdir(os.getcwd())

for filename in list:
	if filename.endswith("cbz"):
		print(f'CBZ file exist : {filename}')
	else: 
		subprocess.run([f'zip -r \"{filename}.cbz\" \"{filename}\"'], shell=True)
		shutil.rmtree(filename)
		print(f'{filename} has been removed')
