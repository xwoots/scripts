import shutil, os, subprocess
import googletrans
import requests
from requests.auth import HTTPBasicAuth

url = "http://192.168.20.17:1952/api/v1/series?size=1000"

r = requests.get(url, auth=HTTPBasicAuth("api@znetwork.local", "P@ssword"))

print(r)

series = r.json()
series_list = series['content']
#

for i in series_list:
	manga = i['metadata']['title']
	response = requests.get(f'http://kitsu.io/api/edge/manga?filter[text]={manga}')
	manga_results = response.json()
	
	print("")
	
	translator = googletrans.Translator()
	translation = translator.translate(manga_results["data"][0]["attributes"]["synopsis"], dest='fr')
	summary_trans = translation.text
	
	print("")
	
	serie_id = i['id']
	serie_url = f'http://192.168.20.17:1952/api/v1/series/{serie_id}/metadata'

	payload = {'summary' : summary_trans}

	serie_r = requests.patch(serie_url, auth=HTTPBasicAuth("api@znetwork.local", "P@ssword"), json=payload)

	print(serie_r)

