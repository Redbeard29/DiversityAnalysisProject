from os import path
import pandas as pd
import numpy as np

BASE_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/DiversityData/csvfiles'

#Define file paths to all csv files
ATL_DATA = path.join(BASE_DIR, 'AtlantaCityRaceSexAge.csv')
ATX_DATA = path.join(BASE_DIR, 'AustinCityRaceSexAge.csv')
BOS_DATA = path.join(BASE_DIR, 'BostonCityRaceSexAge.csv')
CHA_DATA = path.join(BASE_DIR, 'CharlotteCityRaceSexAge.csv')
DTX_DATA = path.join(BASE_DIR, 'DallasCityRaceSexAge.csv')
DC_DATA = path.join(BASE_DIR, 'DCCityRaceSexAge.csv')
GBR_DATA = path.join(BASE_DIR, 'GreensboroCityRaceSexAge.csv')
PIT_DATA = path.join(BASE_DIR, 'PittsburghCityRaceSexAge.csv')
RAL_DATA = path.join(BASE_DIR, 'RaleighCityRaceSexAge.csv')

#Define the DataFrame that we're writing our new data to, including columns and indices
city_comparison_df = pd.DataFrame(columns=['TotalPop', 'White','Black','Asian', 'NativeAmerican','Other'], 
    index=['Atlanta', 'Austin', 'Boston', 'Charlotte', 'Dallas', 'D.C.', 'Greensboro', 'Pittsburgh', 'Raleigh'])

formatting_dict = {'csv_file' : None, 'city_name': None, 'state_name': None}

#Define dicts with file path, city and state for each location so that we can pass them in to all of our necessary functions. 
#This formatting is required to read the census csv files:

ATL_dict = {'csv_file' : ATL_DATA, 'city_name': 'Atlanta', 'state_name': 'Georgia'}
ATX_dict = {'csv_file' : ATX_DATA, 'city_name': 'Austin', 'state_name': 'Texas'}
BOS_dict = {'csv_file' : BOS_DATA, 'city_name': 'Boston', 'state_name': 'Massachusetts'}
CHA_dict = {'csv_file' : CHA_DATA, 'city_name': 'Charlotte', 'state_name': 'North Carolina'}
DTX_dict = {'csv_file' : DTX_DATA, 'city_name': 'Dallas', 'state_name': 'Texas'}
DC_dict = {'csv_file' : DC_DATA, 'city_name': 'District of Columbia', 'state_name': None}
GBR_dict= {'csv_file' : GBR_DATA, 'city_name': 'Greensboro', 'state_name': 'North Carolina'}
PIT_dict = {'csv_file' : PIT_DATA, 'city_name': 'Pittsburgh', 'state_name': 'Pennsylvania'}
RAL_dict = {'csv_file' : RAL_DATA, 'city_name': 'Raleigh', 'state_name': 'North Carolina'}

def get_total_pop(city_dict):
    """
    This function takes in a dictionary that holds the path to each csv file, each city's name, and each city's state name. It then uses
    that data to find the total population of the city in the associated csv file. 
    """
    csv_file = pd.read_csv(city_dict['csv_file'])
    city_name = city_dict['city_name']
    state_name = city_dict['state_name']

    if(state_name == None):
        return csv_file[city_name + '!!2019 Estimate'][34]
    else:
        return csv_file[city_name +' city, ' + state_name + '!!2019 Estimate'][34]

dict_list = [ATL_dict, ATX_dict, BOS_dict, CHA_dict, DTX_dict, DC_dict, GBR_dict, PIT_dict, RAL_dict]


ATL_pop = get_total_pop(ATL_dict)
ATX_pop = get_total_pop(ATX_dict)
BOS_pop = get_total_pop(BOS_dict)
CHA_pop = get_total_pop(CHA_dict)
DTX_pop = get_total_pop(DTX_dict)
DC_pop = get_total_pop(DC_dict)
GBR_pop = get_total_pop(GBR_dict)
PIT_pop = get_total_pop(PIT_dict)
RAL_pop = get_total_pop(RAL_dict)

city_comparison_df['TotalPop'] = [ATL_pop, ATX_pop, BOS_pop, CHA_pop, DTX_pop, DC_pop, GBR_pop, PIT_pop, RAL_pop]


print(city_comparison_df)