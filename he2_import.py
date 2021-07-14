#!/usr/bin/python

import requests
import csv

#
# This Python script is an example that demonstrates how to
# use the RESTful API of Matrify.
#
# It works with an table that has the columns Id, Name, Modified. Those columns
# exist per default, when a new empty table is created.
#

password="13371337"

ct="Content-Type: application/json"
server="http://griever.pw:8182"
account="admin@gmail.com"
db="Herald_DB"
table="Hurrrraldo"

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

#
# Add a complete row to a table. Every cell must be set. Cells that are
# set automatically (e.g. KEY, MODIFIED, CREATED columns) can be set to 'auto'.
#


#


f = open('timeSorted.csv', encoding="utf8")
csv_f = csv.reader(f)

for row in csv_f:
    time = row[0]
    title = row[1]
    aUrl = row[2]

    url = '{0}/database-api/{1}/{2}/row/add/{3}'.format(server, account, db, table)
    params = {'return_key': 'true', 'access_token': access_token}
    json = {'tableId': table, 'cells': ['auto', time, title, aUrl]}
    r = requests.post(url, params=params, json=json)
    print(r.text)
