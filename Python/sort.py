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

def move_file(dir):
	global username
	global path
	try:
		shutil.move(filename, f'/home/{username}/{dir}')
	except shutil.Error:
		print(f'Le fichier existe déjà : /home/mateuw/{dir}/{filename}')
		rem_file = input("Supprimer le fichier ? [y/N] ")
		if rem_file == "y":
			os.remove(f'{path}/{filename}')

for filename in list:
	if filename.endswith(pictures_ext):
		move_file("Images")	
	elif filename.endswith(videos_ext):
		move_file("Vidéos")	
	elif filename.endswith(texts_ext):
		move_file("Documents")		
	elif filename.endswith(musics_ext):
		move_file("Musique")
	elif filename.endswith(torrents_ext):
		move_file("Torrents")
	elif filename.endswith(ISOs_ext):
		move_file("ISOs")
	elif filename.endswith(scripts_ext):
		move_file("Scripts")


	
