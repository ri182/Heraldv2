import pandas as pd

file = 'output_sr.csv'
df = pd.read_csv(file, header=[0], parse_dates=[0])
df = df.sort_values('Time', ascending = False)

df.to_csv(r'timeSorted.csv', index = False)
print ("Finished datesort " +file+ "")