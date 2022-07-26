# THIS SCRIPT WILL AUTOMATICALY MOVE FILES FROM DOWNLOADS FOLDER TO SPECIFIC FOLDERS

# -------------------------------------------------------------------------------------------------------------------

import sys, os, logging, shutil, time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

# -------------------------------------------------------------------------------------------------------------------

# Variables for extensions

images_ext = (".png", ".jpg", ".jpeg", ".gif", ".webp")
videos_ext = (".mp4", ".mkv", ".webm")
docs_ext = (".pdf", ".odt", ".doc", ".docx", ".txt", ".ppsx")
musics_ext = (".mp3", ".flac", ".wav")
torrents_ext = ".torrent"
ISOs_ext = ".iso"
scripts_ext = (".sh", ".py", ".ps1")
data_ext = (".csv", ".json", ".xml", ".xlsx", ".xls", ".ods")
archives_ext = (".7z", ".gz", ".tar", ".zip")
programs_ext = (".exe", ".msi")
keys_ext = (".pem", ".pfx")

# Variable for directory to watch and current user name

watched_dir = "C:\\Users\\Mateuw\\Downloads"
username = os.getlogin()

# -------------------------------------------------------------------------------------------------------------------

# Function for moving file

def move_file(source_file, dest_dir):
    try:
        shutil.move(source_file.path, fr'C:\Users\{username}\Documents\{dest_dir}')
    except shutil.Error:
        print(fr'Le fichier existe déjà : C:\Users\{username}\Documents\{dest_dir}\{source_file.name}')

# -------------------------------------------------------------------------------------------------------------------

# Handler class

class Handler(FileSystemEventHandler):
    def on_created(self,event):
        time.sleep(10)
        for result in os.scandir(watched_dir):
            if result.name.endswith(images_ext):
                move_file(result, "Downloads_Images")
            elif result.name.endswith(videos_ext):
                move_file(result, "Downloads_Videos")
            elif result.name.endswith(docs_ext):
                move_file(result, "Downloads_Documents")
            elif result.name.endswith(musics_ext):
                move_file(result, "Downloads_Musics")
            elif result.name.endswith(torrents_ext):
                move_file(result, "Downloads_Torrents")
            elif result.name.endswith(ISOs_ext):
                move_file(result, "Downloads_ISOs")
            elif result.name.endswith(scripts_ext):
                move_file(result, "Downloads_Scripts")
            elif result.name.endswith(data_ext):
                move_file(result, "Downloads_Datas")
            elif result.name.endswith(archives_ext):
                move_file(result, "Downloads_Archives")
            elif result.name.endswith(programs_ext):
                move_file(result, "Downloads_Programs")
            elif result.name.endswith(keys_ext):
                move_file(result, "Downloads_Keys")

# -------------------------------------------------------------------------------------------------------------------

# Initialize the Observer and Event Handler

if __name__ == "__main__":
    logging.basicConfig(filename="mover.log", level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    path = 'C:\\Users\\Mateuw\\Downloads'
    event_handler_logs = LoggingEventHandler()                      
    event_handler = Handler()                                      
    observer = Observer()                                           
    observer.schedule(event_handler, path, recursive=False)         
    observer.schedule(event_handler_logs, path, recursive=True)     

    observer.start()                                               
    try:
        while observer.is_alive():                                
            observer.join(1)                                            
    finally:
        observer.stop()
        observer.join()