import pandas as pd

# Read file

df = pd.read_csv('attacks.csv', delimiter=',', encoding='ISO-8859-1')

wdf = df.iloc[:, 0:16]

# Question: Based on the data in the Activity column are you more likely to be attacked by a shark if you are "Surfing" or "Scuba Diving".

data_if_surfing = wdf['Activity'] == 'Surfing'
data_if_diving = wdf['Activity'] == 'Scuba diving'

result = wdf['Activity'][(data_if_surfing) | (data_if_diving)].value_counts().tolist()
print(f'Number of attacks when Surfing {result[0]}')
print(f'Number of attacks when Scuba Diving {result[1]}')
