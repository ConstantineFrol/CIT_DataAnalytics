import pandas as pd

# Read file

df = pd.read_csv('attacks.csv', delimiter=',', encoding='ISO-8859-1')

wdf = df.iloc[:, 0:16]

# Question: Determine from the dataset what percentage of all recorded shark attacks were fatal.

num_rows = len(wdf.index)
num_fatal = wdf['Fatal'].value_counts().tolist()[1]
result = num_fatal * 100 / num_rows
print(f'Percentage of attacks that are:\n{round(result, 2)}')
