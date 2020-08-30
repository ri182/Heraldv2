import requests
import sys

url = "https://newscatcher.p.rapidapi.com/v1/search_free"

querystring = {"media":"False","lang":"en","q":"Balkans"}

headers = {
    'x-rapidapi-host': "newscatcher.p.rapidapi.com",
    'x-rapidapi-key': "239fc3a7c5msha26c49255fae67fp19f5a2jsn768f9b8a2233"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


original_stdout = sys.stdout 

with open('news_a_bl.json', 'w') as f:
    sys.stdout = f 
    print(response.text)
    sys.stdout = original_stdout