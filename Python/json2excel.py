import pandas as pd 
import json

# User inputs ; .split() is used for creating a array from user input
json_file = input("Enter the path of the json file : ")
keys = input("Enter the keys to select separated by spaces : ").split()
output_xlsx = input("Enter a name for the output file : ")
specific_key = input("Is there a specific key to work on (y/n) : ")

# Open and load the json document
with open(json_file, 'r') as f:
    data = json.load(f)

# Modify the data if we want to work with a specific key
if specific_key == y:
    mainkey = input("Enter the main key to work on : ")
    certs = data[mainkey]
else:
    certs = data

# Load data into DataFrame (rows/col table) / create new variable with only the keys we want / export to .xlsx
certs_df = pd.DataFrame(certs)
certs_parsed = certs_df[keys]
certs_parsed.to_excel(output_xlsx)
