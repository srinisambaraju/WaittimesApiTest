import requests
import urllib3
import json


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://wait-times.tech-brands.com/getStoreWaitTime?stores=[100]"
# url = "https://techbrands.my.workfront.com/projects"
payload = {'apiKey': 'J5oRWT8a13'}
get_version = requests.get(url, headers=payload)

# print(json.loads(get_version.text))

print(get_version.json())