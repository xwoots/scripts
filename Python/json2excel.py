import pandas as pd 
import json

json_file = input("Enter the path of the json file : ")
keys = input("Enter the keys to select separated by spaces : ").split()
output_xlsx = input("Enter a name for the output file : ")
specific_key = input("Is there a specific key to work on (y/n) : ")

with open(json_file, 'r') as f:
    data = json.load(f)

if specific_key == y:
    main_key = input("Enter the main key to work on : ")
    certs = data[mainkey]
else:
    certs = data

certs_df = pd.DataFrame(certs)
certs_parsed = certs_df[keys]
certs_parsed.to_excel(output_xlsx)
