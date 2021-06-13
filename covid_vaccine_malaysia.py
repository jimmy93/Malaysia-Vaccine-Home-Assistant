import csv
import requests
import json
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Malaysia.csv'
resp = requests.get(url)
decoded_content = resp.content.decode('utf-8')
reader = csv.DictReader(decoded_content.splitlines(), delimiter = ',')
list_from_csv = []
for row in reader:
    list_from_csv.append(row)
print(json.dumps(list_from_csv[-1]))
