import pandas as pd

# Read file

df = pd.read_csv('attacks.csv', delimiter=',', encoding='ISO-8859-1')

wdf = df.iloc[:, 0:16]

# Question: In this question we are interested in looking at the number of recorded shark attacks over time for a specific country.

"""Write a function called 'calculateYearlyAttacks' that will take in a valid country name as a patameter and the attack dataframe.
It should print out the number of recorded shark attacks for the country for every year from 1925 to 2015"""


def calculate_yearly_attacks(country, wdf):
    years_list = pd.unique(wdf['Year'][(wdf['Year'] >= 1925) & (wdf['Year'] <= 2015)].to_list())

    for year in years_list:
        result = len(wdf[(wdf['Country'] == country) & (wdf['Year'] == year)])
        print(f'Number of attacks in {country} during {int(year)} is {result}\n------')


calculate_yearly_attacks('AUSTRALIA', wdf)
