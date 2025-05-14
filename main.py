import pandas as pd

# Part_1
df = pd.read_csv('Lung_Cancer_Trends_Realistic.csv')

sep = '\n' + '_' * 100 + '\n'

print(df.head(), end=sep)

df.info()

print(sep, df.describe(), end=sep)

# Part_2
df = pd.read_csv('dz.csv')

df.dropna(inplace=True)

group = df.groupby('City')['Salary'].mean()

print(f'Средняя зарплата по городу:\n {group}')
