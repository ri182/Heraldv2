# importing the necessary packages 
import time
import sys
import os
import requests
import csv
import pandas as pd
from multiprocessing import Pool
import subprocess

def execfile(filepath):
    import os
    global_namespace = {
        "__file__": filepath,
        "__name__": "__main__",
    }
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), global_namespace)

if __name__ == '__main__':
    # Your desired code continues from here  
    # s = input("Enter your name: ")   
    wbalk = "Balkans"
    wkoso = "Kosova"
    wrsrb = "Serbia"

    ##Run API functions and conversions

    print('\nStarting Herald2')
    sys.stdout.write("Getting " + str(wbalk) + "...\n")
    execfile("./BK/news_a.py")
    execfile("./BK/news_b.py")
    time.sleep(0.2)
    sys.stdout.write("Getting " + str(wkoso) + "...\n")
    execfile("./KS/news_a.py")
    execfile("./KS/news_b.py")
    time.sleep(0.2)
    sys.stdout.write("Getting " + str(wrsrb) + "...\n")
    execfile("./RS/news_a.py")
    execfile("./RS/news_b.py")
    time.sleep(0.2)
    time.sleep(1)
    sys.stdout.write("Converting...\n")
    execfile("./BK/csv_convert_a.py")
    execfile("./BK/csv_convert_b.py")
    time.sleep(1)
    execfile("./KS/csv_convert_a.py")
    execfile("./KS/csv_convert_b.py")
    time.sleep(1)
    execfile("./RS/csv_convert_a.py")
    execfile("./RS/csv_convert_b.py")
    time.sleep(1)
    os.remove("news_a_bl.json")
    os.remove("news_b_bl.json")
    os.remove("news_a_rs.json")
    os.remove("news_b_rs.json")
    os.remove("news_a_ks.json")
    os.remove("news_b_ks.json")

    ##Crunch CSVs

    sys.stdout.write("Crunching CSV...\n")

    df = pd.read_csv('output_bk.csv', encoding='unicode_escape')
    df.to_csv('r_output_bk.csv', index=False)

    df = pd.read_csv('output_ks.csv', encoding='unicode_escape')
    df.to_csv('r_output_ks.csv', index=False)

    df = pd.read_csv('output_sr.csv', encoding='unicode_escape')
    df.to_csv('r_output_sr.csv', index=False)

# Timesort descending
file_rs = 'r_output_sr.csv'
df = pd.read_csv(file_rs, header=[0], parse_dates=[0])
df = df.sort_values('Time', ascending=False)

df.to_csv(r'timeSorted_rs.csv', index=False)
print("Finished datesort " + file_rs + "")

file_bk = 'r_output_bk.csv'
df = pd.read_csv(file_bk, header=[0], parse_dates=[0])
df = df.sort_values('Time', ascending=False)

df.to_csv(r'timeSorted_bk.csv', index=False)
print("Finished datesort " + file_bk + "")

file_ks = 'r_output_ks.csv'
df = pd.read_csv(file_ks, header=[0], parse_dates=[0])
df = df.sort_values('Time', ascending=False)

df.to_csv(r'timeSorted_ks.csv', index=False)
print("Finished datesort " + file_ks + "")

# Upload 1/3
# This Python script is an example that demonstrates how to
# use the RESTful API of Matrify.
#
# It works with an table that has the columns Id, Name, Modified. Those columns
# exist per default, when a new empty table is created.
#

password = "13371337"

ct = "Content-Type: application/json"
server = "http://griever.pw:8182"
account = "info@griever.pw"
db = "He"
table = "Balkans"

#
# Get an access_token that is used in following requests for authorization
#
url = '{0}/account-api/{1}/account/auth'.format(server, account)
params = {'pw': password, 'staysignedin': 'false'}
r = requests.get(url, params=params)
print(r.url)
print(r.text)
print(r.status_code)
j = r.json()
access_token = j['access_token']
print("Access_token: " + access_token)

#
# Add a complete row to a table. Every cell must be set. Cells that are
# set automatically (e.g. KEY, MODIFIED, CREATED columns) can be set to 'auto'.
#

f = open('timeSorted_bk.csv', encoding="utf8")
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

# Upload 2/3
# This Python script is an example that demonstrates how to
# use the RESTful API of Matrify.
#
# It works with an table that has the columns Id, Name, Modified. Those columns
# exist per default, when a new empty table is created.
#

password = "Radolfzell2600"

ct = "Content-Type: application/json"
server = "http://griever.pw:8182"
account = "info@griever.pw"
db = "He"
table = "Kosova"

#
# Get an access_token that is used in following requests for authorization
#
url = '{0}/account-api/{1}/account/auth'.format(server, account)
params = {'pw': password, 'staysignedin': 'false'}
r = requests.get(url, params=params)
print(r.url)
print(r.text)
print(r.status_code)
j = r.json()
access_token = j['access_token']
print("Access_token: " + access_token)

#
# Add a complete row to a table. Every cell must be set. Cells that are
# set automatically (e.g. KEY, MODIFIED, CREATED columns) can be set to 'auto'.
#

f = open('timeSorted_ks.csv', encoding="utf8")
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

# Upload 3/3
# This Python script is an example that demonstrates how to
# use the RESTful API of Matrify.
#
# It works with an table that has the columns Id, Name, Modified. Those columns
# exist per default, when a new empty table is created.
#

password = "Radolfzell2600"

ct = "Content-Type: application/json"
server = "http://griever.pw:8182"
account = "info@griever.pw"
db = "He"
table = "Serbia"

#
# Get an access_token that is used in following requests for authorization
#
url = '{0}/account-api/{1}/account/auth'.format(server, account)
params = {'pw': password, 'staysignedin': 'false'}
r = requests.get(url, params=params)
print(r.url)
print(r.text)
print(r.status_code)
j = r.json()
access_token = j['access_token']
print("Access_token: " + access_token)

#
# Add a complete row to a table. Every cell must be set. Cells that are
# set automatically (e.g. KEY, MODIFIED, CREATED columns) can be set to 'auto'.
#

f = open('timeSorted_rs.csv', encoding="utf8")
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

dir_name = "./"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".json"):
        os.remove(os.path.join(dir_name, item))
for item in test:
    if item.endswith(".csv"):
        os.remove(os.path.join(dir_name, item))
os.remove("timeSorted_rs.csv")
sys.stdout.write("Function complete.\n")
