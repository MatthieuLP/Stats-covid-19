# Imports
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Alias
file_deads = 'time_series_covid19_deaths_global.csv'
file_cases = 'time_series_covid19_confirmed_global.csv'
pays = ['Italy', 'Spain', 'France', 'Hubei (China)', 'US', 'Netherlands', 'Jiangxi (China)', 'Singapore', 'Argentina']

## Pays à analyser : Italy (137), Spain (202), France (116), Hubei (China) (62), US (226), Netherlands (170), Jiangxi (China) (66), Singapore (197), Argentina (6)

################### Question A ###################
data_confirmed_cases = pd.read_csv(file_cases).loc[[137, 202, 116, 62, 226, 170, 66, 197, 6]]
data_confirmed_cases.drop(['Lat', 'Long', 'Province/State', 'Country/Region'], axis='columns', inplace=True)
data_death_cases = pd.read_csv(file_deads).loc[[137, 202, 116, 62, 226, 170, 66, 197, 6]]
data_death_cases.drop(['Lat', 'Long', 'Province/State', 'Country/Region'], axis='columns', inplace=True)
i=0
for idx, rows1 in data_death_cases.iterrows():
    fig, ax = plt.subplots(figsize=(17, 8))
    plt.plot(rows1, color="orange", label="morts")
    for idy, rows2 in data_confirmed_cases.iterrows():
        if(idx == idy):
            plt.plot(rows2, color="blue", label="contaminés")
    plt.xlabel("Dates")
    plt.ylabel("Nombre de gens")
    plt.title("Nombre journalier de cas et de morts: "+pays[i])
    plt.setp(ax.get_xticklabels(), rotation=88)
    plt.legend()
    i=i+1

plt.show()

################### Question B ###################
# data_confirmed_cases = pd.read_csv(file_cases).loc[[137, 202, 116, 62, 226, 170, 66, 197, 6]]
# data_confirmed_cases.drop(['Lat', 'Long', 'Province/State', 'Country/Region'], axis='columns', inplace=True)
# data_death_cases = pd.read_csv(file_deads).loc[[137, 202, 116, 62, 226, 170, 66, 197, 6]]
# data_death_cases.drop(['Lat', 'Long', 'Province/State', 'Country/Region'], axis='columns', inplace=True)
# i=0
# for idx, rows1 in data_death_cases.iterrows():
#     fig, ax = plt.subplots(figsize=(17, 8))
#     plt.plot(rows1, color="orange", label="total morts")
#     for idy, rows2 in data_confirmed_cases.iterrows():
#         if(idx == idy):
#             plt.plot(rows2, color="blue", label="total contaminés")
#     plt.xlabel("Dates")
#     plt.ylabel("Nombre de gens")
#     plt.title("Nombre total de cas et de morts: "+pays[i])
#     plt.setp(ax.get_xticklabels(), rotation=88)
#     plt.legend()
#     i=i+1
#
# plt.show()


###############Question C#################
# data_death_cases = pd.read_csv(file_cases).loc[[137, 202, 116, 62, 226, 170, 66, 197, 6]]
# data_death_cases.drop(['Lat', 'Long', 'Province/State', 'Country/Region'], axis='columns', inplace=True)
# print(data_death_cases)
#
# pays = ['Italy', 'Spain', 'France', 'Hubei (China)', 'US', 'Netherlands', 'Jiangxi (China)', 'Singapore', 'Argentina']
#
# fig, ax = plt.subplots(figsize=(17, 8))
# j=0
# for idx, rows in data_death_cases.iterrows():
#     plt.plot(rows, label=pays[j])
#     plt.setp(ax.get_xticklabels(), rotation=88)
#     j=j+1
#
#
#
# plt.xlabel("Dates")
# plt.ylabel("Nombre de cas confirmés")
# plt.legend()
# plt.show()

###############Question D#################
# data_death_cases = pd.read_csv(file_deads).loc[[137, 202, 116, 62, 226, 170, 66, 197, 6]]
# data_death_cases.drop(['Lat', 'Long', 'Province/State', 'Country/Region'], axis='columns', inplace=True)
# print(data_death_cases)
#
# pays = ['Italy', 'Spain', 'France', 'Hubei (China)', 'US', 'Netherlands', 'Jiangxi (China)', 'Singapore', 'Argentina']
#
# fig, ax = plt.subplots(figsize=(17, 8))
# j=0
# for idx, rows in data_death_cases.iterrows():
#     plt.plot(rows, label=pays[j])
#     plt.setp(ax.get_xticklabels(), rotation=88)
#     j=j+1
#
#
#
# plt.xlabel("Dates")
# plt.ylabel("Nombre de cas décès")
# plt.legend()
# plt.show()
