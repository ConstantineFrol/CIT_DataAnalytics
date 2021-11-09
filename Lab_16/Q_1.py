import pandas as pd

# Read file

df = pd.read_csv('attacks.csv', delimiter=',', encoding='ISO-8859-1')

# Question: What location globally has the highest number of shark attacks.

# Show columns
# print(df.columns)

# Create working DataFrame
wdf = df.iloc[:, 0:16]

atack_location = wdf['Location'].value_counts().to_frame().head(1)
print(atack_location)
