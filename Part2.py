# Imports
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Ouvrir les fichiers csv

## Pays à analyser : Italy (137), Spain (202), France (116), Hubei (China) (62), US (226), Netherlands (170), Jiangxi (China) (66), Singapore (197), Argentina (6)

################### CAS ###################
file_cases = 'time_series_covid19_confirmed_global.csv'


##### Question b) #####
# data_confirmed_cases = pd.read_csv(file_cases).loc[[137, 202, 116, 62, 226, 170, 66, 197, 6]]
# data_confirmed_cases.drop(['Lat', 'Long', 'Province/State', 'Country/Region'], axis='columns', inplace=True)
# print(data_confirmed_cases)
#
#
# i=0
# pays = ['Italy', 'Spain', 'France', 'Hubei (China)', 'US', 'Netherlands', 'Jiangxi (China)', 'Singapore', 'Argentina']
# for idx, rows in data_confirmed_cases.iterrows():
#     fig, ax = plt.subplots(figsize=(17, 8))
#     plt.plot(rows)
#     plt.xlabel("Dates")
#     plt.ylabel("Nombre de cas confirmé")
#     plt.title(pays[i])
#     plt.setp(ax.get_xticklabels(), rotation=88)
#     i=i+1
#
# plt.show()


##### Question c) #####
# data_confirmed_cases = pd.read_csv(file_cases).loc[[137, 202, 116, 62, 226, 170, 66, 197, 6]]
# data_confirmed_cases.drop(['Lat', 'Long', 'Province/State', 'Country/Region'], axis='columns', inplace=True)
# print(data_confirmed_cases)
#
# pays = ['Italy', 'Spain', 'France', 'Hubei (China)', 'US', 'Netherlands', 'Jiangxi (China)', 'Singapore', 'Argentina']
#
# fig, ax = plt.subplots(figsize=(17, 8))
# i=0
# for idx, rows in data_confirmed_cases.iterrows():
#     plt.plot(rows, label=pays[i])
#     plt.setp(ax.get_xticklabels(), rotation=88)
#     i=i+1
#
#
#
# plt.xlabel("Dates")
# plt.ylabel("Nombre de cas confirmé")
# plt.legend()
# plt.show()

print("\n")
################### MORTS ###################
file_deads = 'time_series_covid19_deaths_global.csv'


##### Question b) #####
# data_death_cases = pd.read_csv(file_deads).loc[[137, 202, 116, 62, 226, 170, 66, 197, 6]]
# data_death_cases.drop(['Lat', 'Long', 'Province/State', 'Country/Region'], axis='columns', inplace=True)
# print(data_death_cases)
#
# j=0
# for idx, rows in data_death_cases.iterrows():
#     fig, ax = plt.subplots(figsize=(17, 8))
#     plt.plot(rows)
#     plt.xlabel("Dates")
#     plt.ylabel("Nombre de morts")
#     plt.title(pays[j])
#     plt.setp(ax.get_xticklabels(), rotation=88)
#     j=j+1
#
# plt.show()


##### Question d) #####
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
# plt.ylabel("Nombre de cas confirmé")
# plt.legend()
# plt.show()