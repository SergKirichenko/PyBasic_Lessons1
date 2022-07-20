import requests
from requests_oauthlib import OAuth1
import os
from dotenv import load_dotenv
from urllib.parse import urlparse



load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
auth = OAuth1(API_KEY, API_SECRET)

id = 12
endpoint = f"http://api.thenounproject.com/icon/{id}"

response = requests.get(endpoint, auth=auth)
result = response.json()
icon_url = result["icon"]["icon_url"]

pars = urlparse(icon_url)
filename = pars.path.split("/")[-1]

icon_response = requests.get(icon_url)
with open(filename, 'wb') as file:
    file.write(icon_response.content)
