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

#fill NA heights
female_data = olympic_data[olympic_data.Sex == "F"]
female_height = female_data.Height.dropna().mean().round(0)
male_data = olympic_data[olympic_data.Sex == "M"]
male_height = male_data.Height.dropna().mean().round(0)

olympic_data['Height'] = olympic_data.apply(
lambda row: female_height if np.isnan(row['Height']) and row['Sex'] is 'F' else row['Height'], axis=1
)
olympic_data['Height'] = olympic_data.apply(
lambda row: male_height if np.isnan(row['Height']) and row['Sex'] is 'M' else row['Height'], axis=1
)
