#!/usr/bin/python
import requests
# RESTful API of Matrify.

#1 Kosova
password="13371337"

ct="Content-Type: application/json"
server="http://griever.pw:8182"
account="info@griever.pw"
db="He"
table="Kosova"

#
# Get an access_token that is used in following requests for authorization
#
url='{0}/account-api/{1}/account/auth'.format(server, account)
params = {'pw': password, 'staysignedin': 'false'}
r = requests.get(url, params=params)
print(r.url)
print(r.text)
print(r.status_code)
j=r.json()
access_token = j['access_token']
print("Access_token: " + access_token)

for i in range(100,210):
    i2 = i + 1
    i3 = str('%05d' % i2)
    url = '{0}/database-api/{1}/{2}/row/delete/{3}'.format(server, account, db, table)
    params = {'return_key': 'true', 'access_token': access_token}
    json = {'ids': [i3]}
    r = requests.post(url, params=params, json=json)
    print(r.text)

print("Sanitizing " +table+ " complete.")

# 2 Balkans
ct="Content-Type: application/json"
server="http://griever.pw:8182"
account="info@griever.pw"
db="He"
table="Balkans"

#
# Get an access_token that is used in following requests for authorization
#
url='{0}/account-api/{1}/account/auth'.format(server, account)
params = {'pw': password, 'staysignedin': 'false'}
r = requests.get(url, params=params)
print(r.url)
print(r.text)
print(r.status_code)
j=r.json()
access_token = j['access_token']
print("Access_token: " + access_token)

for i in range(100,210):
    i2 = i + 1
    i3 = str('%05d' % i2)
    url = '{0}/database-api/{1}/{2}/row/delete/{3}'.format(server, account, db, table)
    params = {'return_key': 'true', 'access_token': access_token}
    json = {'ids': [i3]}
    r = requests.post(url, params=params, json=json)
    print(r.text)

print("Sanitizing " +table+ " complete.")

# 3 Serbia

ct="Content-Type: application/json"
server="http://griever.pw:8182"
account="info@griever.pw"
db="He"
table="Serbia"

#
# Get an access_token that is used in following requests for authorization
#
url='{0}/account-api/{1}/account/auth'.format(server, account)
params = {'pw': password, 'staysignedin': 'false'}
r = requests.get(url, params=params)
print(r.url)
print(r.text)
print(r.status_code)
j=r.json()
access_token = j['access_token']
print("Access_token: " + access_token)

for i in range(100,210):
    i2 = i + 1
    i3 = str('%05d' % i2)
    url = '{0}/database-api/{1}/{2}/row/delete/{3}'.format(server, account, db, table)
    params = {'return_key': 'true', 'access_token': access_token}
    json = {'ids': [i3]}
    r = requests.post(url, params=params, json=json)
    print(r.text)

print("Sanitizing " +table+ " complete.")
