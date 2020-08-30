import requests
import sys

url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI"

querystring = {"autoCorrect":"false","pageNumber":"1","pageSize":"50","q":"Kosovo","safeSearch":"false"}

headers = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "239fc3a7c5msha26c49255fae67fp19f5a2jsn768f9b8a2233"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


original_stdout = sys.stdout 

with open('news_b_ks.json', 'w') as f:
    sys.stdout = f 
    print(response.text)
    sys.stdout = original_stdout