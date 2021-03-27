#/usr/bin/pyton3

import shutil, os, re

pictures_ext = ("png", "jpg", "jpeg", "gif", "webp")
videos_ext = ("mp4", "mkv", "webm")
texts_ext = (".pdf", ".odt", ".doc", ".docx")
musics_ext = ("mp3", "flac", ".wav")
torrents_ext = "torrent"
ISOs_ext = ".iso"
scripts_ext = (".sh", ".py")

path = input("Enter the path where the script will run : ")
os.chdir(path)
list = os.listdir(os.getcwd())
username = os.getenv('USER')

for filename in list:
	if filename.endswith(pictures_ext):
		shutil.move(filename, f'/home/{username}/Images')
	
	elif filename.endswith(videos_ext):
		shutil.move(filename, f'/home/{username}/Vidéos')
	
	elif filename.endswith(texts_ext):
		shutil.move(filename, f'/home/{username}/Documents')
	
	elif filename.endswith(musics_ext):
		shutil.move(filename, f'/home/{username}/Musique')
	
	elif filename.endswith(torrents_ext):
		shutil.move(filename, f'/home/{username}/Torrents')
	
	elif filename.endswith(ISOs_ext):
		shutil.move(filename, f'/home/{username}/ISOs')
	
	elif filename.endswith(scripts_ext):
		shutil.move(filename, f'/home/{username}/Scripts')

