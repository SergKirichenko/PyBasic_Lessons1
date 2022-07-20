# модуль requests
import requests

url = "http://api.forismatic.com/api/1.0/"
params = {"method": "getQuote",
          "format": "json",
          "key": 1,
          "lang": "ru"}
response = requests.get(url, params=params)
print(response.status_code, response.json())
