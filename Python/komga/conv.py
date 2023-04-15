#!\usr\bin\python3

import shutil, os, re, zipfile, subprocess


def to_cbz():
	input_path = input("Enter the path where the manga to convert is store : ")
	
	print("")
	
	manga_list = os.listdir(input_path)
	
	for ind, manga in enumerate(manga_list):
		print(f'{ind} - {manga}')
	
	print("")
	
	manga_pick = int(input("Select the manga to convert [0-9+] : "))
	
	full_path = f'{input_path}/{manga_list[manga_pick]}'
	
	print("")
	
	os.chdir(full_path)
	list = os.listdir(os.getcwd())
	
	for filename in list:
		if filename.endswith("cbz"):
			print(f'CBZ file exist : {filename}')
		else: 
			subprocess.run([f'zip -r \"{filename}.cbz\" \"{filename}\"'], shell=True)
			shutil.rmtree(filename)
			print(f'{filename} has been removed')

def to_jpg():
	input_path = input("Enter the path where the manga to convert is store : ")
	
	print("")
	
	manga_list = os.listdir(input_path)
	
	for ind, manga in enumerate(manga_list):
		print(f'{ind} - {manga}')
	
	print("")
	
	manga_pick = int(input("Select the manga to convert [0-9+] : "))
	
	full_path = f'{input_path}/{manga_list[manga_pick]}'
	
	print("")
	
	os.chdir(full_path)
	list = os.listdir(os.getcwd())
	
	for filename in list:
		if not filename.endswith("cbz"):
			print(f'CBZ file exist : {filename}')
		else: 
			subprocess.run([f'unzip \"{filename}\"'], shell=True)
			os.remove(filename)
			print(f'{filename} has been removed')

choice = input("Choisissez l'action à exécuter :\n\n 1. Créer une archive .cbz à partir d'un dossier\n 2. Extraire le contenu d'une archive .cbz\n\nVeuillez entrer votre choix [1-2] : ")

if choice == "1":
	to_cbz()
elif choice == "2":
	to_jpg()
else:
	print("\nChoix invalide !")
