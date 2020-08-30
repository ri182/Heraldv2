import json
import csv
with open("./news_a_bl.json", encoding='utf-8') as file:
    data = json.load(file)

fname = "output_bk.csv"

with open(fname, "w", encoding='utf-8') as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["Time","Title","URL"])
    for item in data["articles"]:
        csv_file.writerow([item['published_date'],item['title'],item['link']])