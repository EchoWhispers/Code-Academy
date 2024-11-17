import requests
import json


result = requests.get("https://api.thecatapi.com/v1/images/search")

aa = json.loads(result.text)
print(aa[0]["url"])