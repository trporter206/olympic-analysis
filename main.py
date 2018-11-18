import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

olympic_data = pd.read_csv("athlete_events.csv")

def overview(data):
    print('columns')
    print data.columns.values
    print('_'*40)
    print('column info')
    print data.info()
    print('_'*40)
    print('numeric columns')
    print data.describe()
    print('_'*40)
    print('non numeric columns')
    print data.describe(include=[np.object])

# #fill NaN values
def trait_fill(col, sex):
    val = olympic_data[olympic_data.Sex == sex][col].dropna().mean().round(0)

    olympic_data[col] = olympic_data.apply(
    lambda row: val if np.isnan(row[col]) and row['Sex'] is sex else row[col], axis=1
    )

trait_fill('Height', 'M')
trait_fill('Height', 'F')
trait_fill('Weight', 'M')
trait_fill('Weight', 'F')
trait_fill('Age', 'M')
trait_fill('Age', 'F')

#change sex vals to 1 and 0
for dataset in [olympic_data]:
    dataset['Sex'] = dataset['Sex'].map({'F': 0, 'M': 1}).astype(int)

p = olympic_data[['Games', 'Sex']].groupby(['Games'], as_index=False).count()
p1 = olympic_data[['Games', 'Sex']].groupby(['Games'], as_index=False).sum()
p1 = p1['Sex'].astype(int).tolist()
p2 = p['Sex'].astype(int).tolist()

female_count = []
for i in range(len(p1)):
    female_count.append(p2[i] - p1[i])
p['F'] = pd.Series(female_count)

for dataset in [p]:
    dataset['M/F'] = dataset['Sex'] / dataset['F']

# p.plot(x='Games', y=['Sex', 'F'])
p.plot(x='Games', y='M/F')

plt.show()
