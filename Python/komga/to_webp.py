from PIL import Image
import os, shutil, subprocess

path = input("Entre le chemin où le script s'écutera : ")

print("")

manga_list = os.listdir(path)

for ind, manga in enumerate(manga_list):
	print(f'{ind} - {manga}')

manga_pick = int(input("\nSélectionnez le manga à convertir [0-9+] : "))

full_path = f'{path}/{manga_list[manga_pick]}'

os.chdir(full_path)

mangas = os.listdir(full_path)

print("")

for dirname in mangas:
	chapters_list = os.listdir(dirname)
	if dirname.endwith(".cbz") or dirname.endwith(".cbr")
		subprocess.run([f'unzip \"{dirname}\"'], shell=True)
		shutil.rmtree(dirname)
		print(f'{filename} has been removed')
		dirname = os.path.splitext(dirname)[0]

	os.chdir(f'{os.getcwd()}/{dirname}')
	for filename in chapters_list:
		new_name = os.path.splitext(filename)[0] + '.webp'
		subprocess.call(f'cwebp -quiet -q 80 -z 6 {filename} -o {new_name}', shell=True)
		print(new_name)
		os.remove(filename)
	os.chdir(full_path)
	
	subprocess.run([f'zip -r \"{dirname}.cbz\" \"{dirname}\"'], shell=True)
                        shutil.rmtree(dirname)
                        print(f'{filename} has been removed'


