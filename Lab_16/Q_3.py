import pandas as pd

# Read file

df = pd.read_csv('attacks.csv', delimiter=',', encoding='ISO-8859-1')

wdf = df.iloc[:, 0:16]

# Question: Modify your code to print out the six countries that have experienced the highest number of fatal shark attacks.

data_with_fatal_res = wdf[wdf['Fatal'] == 'Y']

result = data_with_fatal_res['Country'].value_counts().head(6)

print(result)
