from os import path
import pandas as pd
import numpy as np

BASE_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/DiversityData/csvfiles'

ATL_DATA = pd.read_csv(path.join(BASE_DIR, 'AtlantaCityRaceSexAge.csv'))
ATX_DATA = pd.read_csv(path.join(BASE_DIR, 'AustinCityRaceSexAge.csv'))
BOS_DATA = pd.read_csv(path.join(BASE_DIR, 'BostonCityRaceSexAge.csv'))
CHA_DATA = pd.read_csv(path.join(BASE_DIR, 'CharlotteCityRaceSexAge.csv'))
DTX_DATA = pd.read_csv(path.join(BASE_DIR, 'DallasCityRaceSexAge.csv'))
DC_DATA = pd.read_csv(path.join(BASE_DIR, 'DCCityRaceSexAge.csv'))
GBR_DATA = pd.read_csv(path.join(BASE_DIR, 'GreensboroCityRaceSexAge.csv'))
PIT_DATA = pd.read_csv(path.join(BASE_DIR, 'PittsburghCityRaceSexAge.csv'))
RAL_DATA = pd.read_csv(path.join(BASE_DIR, 'RaleighCityRaceSexAge.csv'))

city_comparison_df = pd.DataFrame(columns=['TotalPop'], 
    index=['Atlanta', 'Austin', 'Boston', 'Charlotte', 'Dallas', 'D.C.', 'Greensboro', 'Pittsburgh', 'Raleigh'])

def get_total_pop(csv_file, city_name, state_name=None):
    if(state_name == None):
        return csv_file[city_name + '!!2019 Estimate'][34]
    else:
        return csv_file[city_name +' city, ' + state_name + '!!2019 Estimate'][34]

#define tuples to save rewriting code?:

ATL_population = get_total_pop(ATL_DATA, 'Atlanta', 'Georgia')
ATX_population = get_total_pop(ATX_DATA, 'Austin', 'Texas')
BOS_population = get_total_pop(BOS_DATA, 'Boston', 'Massachusetts')
CHA_population = get_total_pop(CHA_DATA, 'Charlotte', 'North Carolina')
DTX_population = get_total_pop(DTX_DATA, 'Dallas', 'Texas')
DC_population = get_total_pop(DC_DATA, 'District of Columbia')
GBR_population = get_total_pop(GBR_DATA, 'Greensboro', 'North Carolina')
PIT_population = get_total_pop(PIT_DATA, 'Pittsburgh', 'Pennsylvania')
RAL_population = get_total_pop(RAL_DATA, 'Raleigh', 'North Carolina')

city_comparison_df['TotalPop'] = [ATL_population, ATX_population, BOS_population, CHA_population, DTX_population, DC_population, GBR_population, PIT_population, RAL_population]

print(city_comparison_df)