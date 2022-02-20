#Creating a personalized CSV file from demographic data to explore areas of interest

from os import path
import pandas as pd
import numpy as np
BASE_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/DiversityData/csvfiles'

#Only County in DC is 'District of Columbia'
DC_data = pd.read_csv(path.join(BASE_DIR, 'DemoDataDC.csv'))

#Atlanta is mostly located in 'Fulton County'
GA_data = pd.read_csv(path.join(BASE_DIR, 'DemoDataGA.csv'))

#Austin is mostly located in 'Travis County', and Dallas is mostly located in 'Dallas County'
TX_data = pd.read_csv(path.join(BASE_DIR, 'DemoDataTX.csv'))

#Boston is located in 'Suffolk County'
MA_data = pd.read_csv(path.join(BASE_DIR, 'DemoDataMA.csv'))

#Raleigh is located in 'Wake County', Greensboro is located in 'Guilford County', and 
#Charlotte is located in 'Mecklenburg County'
NC_data = pd.read_csv(path.join(BASE_DIR, 'DemoDataNC.csv'))


def current_pop_all_ages(file_path, county_name):
    is_2019 = file_path['YEAR'] == 12
    all_ages = file_path['AGEGRP'] == 0
    cty_name = file_path['CTYNAME'] == county_name
    total_pop_2019 = file_path.loc[
        is_2019 & all_ages & cty_name,
        ['TOT_POP']
    ]
    return total_pop_2019

print(current_pop_all_ages(DC_data, 'District of Columbia'))
print(current_pop_all_ages(GA_data, 'Fulton County'))
print(current_pop_all_ages(TX_data, 'Travis County'))
print(current_pop_all_ages(TX_data, 'Dallas County'))
print(current_pop_all_ages(MA_data, 'Suffolk County'))
print(current_pop_all_ages(NC_data, 'Wake County'))
print(current_pop_all_ages(NC_data, 'Guilford County'))
print(current_pop_all_ages(NC_data, 'Mecklenburg County'))