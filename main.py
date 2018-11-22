import csv
import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

olympic_data = pd.read_csv("athlete_events.csv")

# def overview(data):
#     print('columns')
#     print data.columns.values
#     print('_'*40)
#     print('column info')
#     print data.info()
#     print('_'*40)
#     print('numeric columns')
#     print data.describe()
#     print('_'*40)
#     print('non numeric columns')
#     print data.describe(include=[np.object])
#
# # #fill NaN values
# def trait_fill(col, sex):
#     val = olympic_data[olympic_data.Sex == sex][col].dropna().mean().round(0)
#
#     olympic_data[col] = olympic_data.apply(
#     lambda row: val if np.isnan(row[col]) and row['Sex'] is sex else row[col], axis=1
#     )
#
# def df_build(d1, d2, by):
#     df = pd.merge(d1, d2, how='outer')
#     df.sort_values(by=by, inplace=True)
#     df.fillna(method='ffill', inplace=True)
#     return df
#
# trait_fill('Height', 'M')
# trait_fill('Height', 'F')
# trait_fill('Weight', 'M')
# trait_fill('Weight', 'F')
# trait_fill('Age', 'M')
# trait_fill('Age', 'F')
#
# #change sex vals to 1 and 0
# for dataset in [olympic_data]:
#     dataset['Sex'] = dataset['Sex'].map({'F': 0, 'M': 1}).astype(int)
#
# #athlete count of summer and winter games---------------------------------------
# winter_athlete_count = olympic_data[olympic_data.Season == 'Winter']
# summer_athlete_count = olympic_data[olympic_data.Season == 'Summer']
# winter_athlete_count = winter_athlete_count[['Year', 'ID']].groupby(['Year'], as_index=False).count()
# summer_athlete_count = summer_athlete_count[['Year', 'ID']].groupby(['Year'], as_index=False).count()
# winter_athlete_count.rename(index=str, columns={'Year': 'Year', 'ID': 'winter_athlete_count'}, inplace=True)
# summer_athlete_count.rename(index=str, columns={'Year': 'Year', 'ID': 'summer_athlete_count'}, inplace=True)
#
# years = sorted(olympic_data['Year'].unique())
# games_counts = pd.DataFrame({})
# games_counts['Year'] = pd.Series(years)
# games_counts = df_build(winter_athlete_count, summer_athlete_count, 'Year')
#
# # games_counts.plot(x='Year', y=['winter_athlete_count', 'summer_athlete_count'])
#
# #get ratio of men to women at each game-----------------------------------------
# sex_ratio = olympic_data[['Games', 'Sex']].groupby(['Games'], as_index=False).count()
# p1 = olympic_data[['Games', 'Sex']].groupby(['Games'], as_index=False).sum()
# p1 = p1['Sex'].astype(int).tolist()
# p2 = sex_ratio['Sex'].astype(int).tolist()
#
# female_count = []
# for i in range(len(p1)):
#     female_count.append(p2[i] - p1[i])
# sex_ratio['F'] = pd.Series(female_count)
#
# for dataset in [sex_ratio]:
#     dataset['M/F'] = dataset['Sex'] / dataset['F']
#
# sex_ratio.rename(index=str, columns={'Sex': 'M', 'F':'F'}, inplace=True)
#
# # sex_ratio.plot(x='Games', y='M/F')
#
# #number of events each olympics-------------------------------------------------
# games = olympic_data[['Season', 'Year', 'Event']]
# winter = games[games.Season == 'Winter']
# winter_events_count = pd.DataFrame({'Year': winter.Year.unique(), 'winter_event_count':  winter.Year.unique()})
#
# for i, row in winter_events_count.iterrows():
#     count = len(winter[winter['Year'] == row['Year']]['Event'].unique().tolist())
#     row['winter_event_count'] = count
#
# summer = games[games.Season == 'Summer']
# summer_events_count = pd.DataFrame({'Year': summer.Year.unique(), 'summer_event_count':  summer.Year.unique()})
#
# for i, row in summer_events_count.iterrows():
#     count = len(summer[summer['Year'] == row['Year']]['Event'].unique().tolist())
#     row['summer_event_count'] = count
#
# games_events_count = pd.DataFrame({'Year': olympic_data['Year'].unique()})
# games_events_count = df_build(winter_events_count, summer_events_count, 'Year')
#
# # games_events_count.plot(x='Year', y=['winter_event_count', 'summer_event_count'])
#
# #male and female heights by season over time------------------------------------
# # plot = sns.FacetGrid(olympic_data, row='Season', col='Sex')
# # plot.map(sns.lineplot, 'Year', 'Height')
# # plot.add_legend()
#
# #best performing athletes-------------------------------------------------------
medal_winners = olympic_data[olympic_data.Medal.notna()]
unique_athletes = pd.Series(medal_winners['Name'].unique())
top_athletes = pd.DataFrame({"Athlete": unique_athletes, "Medal_Count": unique_athletes})
for i, row in top_athletes.iterrows():
    medals = len(medal_winners[medal_winners['Name'] == row['Athlete']])
    row['Medal_Count'] = medals

top_athletes.sort_values(by=['Medal_Count'], ascending=False, inplace=True)

print top_athletes
# plt.show()
