import requests
import json
from credentials import api_key, token

url = "https://api.trello.com/1/cards"

headers = {
  "Accept": "application/json"
}

query = {
  'idList': '5abbe4b7ddc1b351ef961414',
  'key': api_key,
  'token': token
}

response = requests.request(
   "POST",
   url,
   headers=headers,
   params=query
)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))