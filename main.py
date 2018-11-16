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

print olympic_data.Height
