import pandas as pd

# Read file

df = pd.read_csv('attacks.csv', delimiter=',', encoding='ISO-8859-1')

wdf = df.iloc[:, 0:16]

# Question: Read the shark attack into a Pandas DataFrame.
# Determ the six countries that have experienced the highest number of shark attacks.

most_country_att = wdf['Country'].value_counts().head(6)

# Show columns
print(type(most_country_att))
print(most_country_att)
