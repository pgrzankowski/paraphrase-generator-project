import requests
import json
response = requests.get('https://api.datamuse.com/words?ml=ringing+in+the+ears')
data = response.text
parse = json.loads(data)
for item in parse:
    print(item)