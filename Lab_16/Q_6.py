import pandas as pd

# Read file

df = pd.read_csv('attacks.csv', delimiter=',', encoding='ISO-8859-1')

wdf = df.iloc[:, 0:16]

# Question: For each individual country print out the percentage of fatal shark attacks.
country_list = wdf['Country'].value_counts().keys()

for country in country_list:
    fatal = wdf[(wdf['Country'] == country) & (wdf['Fatal'] == 'Y')]
    non_fatal = wdf[(wdf['Country'] == country) & (wdf['Fatal'] == 'N')]
    if len(fatal) > 0:
        result = len(fatal) * 100 / (len(fatal) + len(non_fatal))
        print(f'The percentage of fatal attacks: {country} {round(result, 2)}%')
    else:
        print(f'No fatal attacks in: {country}')
