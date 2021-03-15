#/usr/bin/pyton3

import shutil, os, re

path = input("Enter the path where the script will run : ")

print("""
Choose the file type to move :

  - Type (1) for images
  - Type (2) for videos
  - Type (3) for text documents
  - Type (4) for music
  - Type (5) for torrent files
  - Type (6) for ISOs
  - Type (7) for scripts
  - Type (8) for all the above

""")

file_type = input("Enter a number : ")

pictures_ext = ("png", "jpg", "jpeg", "gif", "webp")

videos_ext = ("mp4", "mkv", "webm")

texts_ext = (".pdf", ".odt", ".doc", ".docx")

musics_ext = ("mp3", "flac", ".wav")

torrents_ext = "torrent"

ISOs_ext = ".iso"

scripts_ext = (".sh", ".py")

# all_ext = pictures_ext + videos_ext + texts_ext + musics_ext + torrents_ext + ISOs_ext + scripts_ext

list = os.listdir(path)

username = os.getenv('USER')



if file_type == "1":
    for filename in list:
        if filename.endswith(pictures_ext):
            shutil.move(filename, f'/home/{username}/Pictures')
if file_type == "2":
    for filename in list:
        if filename.endswith(videos_ext):
            shutil.move(filename, f'/home/{username}/Videos')
if file_type == "3":
    for filename in list:
        if filename.endswith(texts_ext):
            shutil.move(filename, f'/home/{username}/Documents')
if file_type == "4":
    for filename in list:
        if filename.endswith(musics_ext):
            shutil.move(filename, f'/home/{username}/Music')
if file_type == "5":
    for filename in list:
        if filename.endswith(torrents_ext):
            shutil.move(filename, f'/home/{username}/Torrents')
if file_type == "6":
    for filename in list:
        if filename.endswith(ISOs_ext):
            shutil.move(filename, f'/home/{username}/ISOs')
if file_type == "7":
    for filename in list:
        if filename.endswith(scripts_ext):
            shutil.move(filename, f'/home/{username}/Scripts')
if file_type == "8":
    for filename in list:
        if filename.endswith(pictures_ext):
            shutil.move(filename, f'/home/{username}/Pictures')
    for filename in list:
        if filename.endswith(videos_ext):
            shutil.move(filename, f'/home/{username}/Videos')
    for filename in list:
        if filename.endswith(texts_ext):
            shutil.move(filename, f'/home/{username}/Documents')
    for filename in list:
        if filename.endswith(musics_ext):
            shutil.move(filename, f'/home/{username}/Music')
    for filename in list:
        if filename.endswith(torrents_ext):
            shutil.move(filename, f'/home/{username}/Torrents')
    for filename in list:
        if filename.endswith(ISOs_ext):
            shutil.move(filename, f'/home/{username}/ISOs')
    for filename in list:
        if filename.endswith(scripts_ext):
            shutil.move(filename, f'/home/{username}/Scripts')

