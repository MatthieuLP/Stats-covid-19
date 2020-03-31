# Imports
import pandas as pd
import numpy as np

# Ouvrir les fichiers csv

## Pays à analyser : Italy (137), Spain (202), France (116), Hubei (China) (62), US (226), Netherlands (170), Jiangxi (China) (66), Singapore (197), Argentina (6)


################### CAS ###################
file_cases = 'time_series_covid19_confirmed_global.csv'

data_confirmed_cases = pd.read_csv(file_cases).loc[[137, 202, 116, 62, 226, 170, 66, 197, 6]]
# print("Nombre de cas confirmé par pays :", data_confirmed_cases)

# On veut récupérer la dernière colonne de chaques lignes pour avoir le nombre de cas confirmé
print("Nombre de cas confirmé par pays : \n",data_confirmed_cases.loc[:,['Country/Region','3/22/20']])

print("\n")
################### MORTS ###################
file_deads = 'time_series_covid19_deaths_global.csv'

data_death_cases = pd.read_csv(file_deads).loc[[137, 202, 116, 62, 226, 170, 66, 197, 6]]
# print("Nombre de morts par pays :", data_death_cases)

# On veut récupérer la dernière colonne de chaques lignes pour avoir le nombre de cas confirmé
print("Nombre de morts par pays : \n", data_death_cases.loc[:,['Country/Region','3/22/20']])




