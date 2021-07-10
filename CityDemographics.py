from os import path
import pandas as pd
import numpy as np

BASE_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/DiversityData/csvfiles'

#Define file paths to all csv files
ATL_DATA = path.join(BASE_DIR, 'AtlantaCityRaceSexAge.csv')
ATX_DATA = path.join(BASE_DIR, 'AustinCityRaceSexAge.csv')
BAL_DATA = path.join(BASE_DIR, 'BaltimoreCityRaceSexAge.csv')
BOS_DATA = path.join(BASE_DIR, 'BostonCityRaceSexAge.csv')
CHA_DATA = path.join(BASE_DIR, 'CharlotteCityRaceSexAge.csv')
DTX_DATA = path.join(BASE_DIR, 'DallasCityRaceSexAge.csv')
DC_DATA = path.join(BASE_DIR, 'DCCityRaceSexAge.csv')
GBR_DATA = path.join(BASE_DIR, 'GreensboroCityRaceSexAge.csv')
LA_DATA = path.join(BASE_DIR, 'LosAngelesCityRaceSexAge.csv')
NYC_DATA = path.join(BASE_DIR, 'NewYorkCityRaceSexAge.csv')
PIT_DATA = path.join(BASE_DIR, 'PittsburghCityRaceSexAge.csv')
RAL_DATA = path.join(BASE_DIR, 'RaleighCityRaceSexAge.csv')
SF_DATA = path.join(BASE_DIR, 'SanFranciscoCityRaceSexAge.csv')
SEA_DATA = path.join(BASE_DIR, 'SeattleCityRaceSexAge.csv')

#Define the DataFrame that we're writing our new data to
city_comparison_df = pd.DataFrame(columns=['TotalPop', 'White','Black', 'Asian', 'NativeAm', 'Other', 'TwoOrMoreRaces', 'BlackAndWhite'],
    index=['Atlanta', 'Austin', 'Baltimore', 'Boston', 'Charlotte', 'Dallas', 'District of Columbia', 'Greensboro', 'Los Angeles', 'New York', 'Pittsburgh', 'Raleigh', 'San Francisco', 'Seattle'])

#Define dicts with file path, city and state for each location so that we can pass them in to all of our necessary functions. 
#This formatting is required to read the census csv files:

ATL_dict = {'csv_file' : ATL_DATA, 'city_name': 'Atlanta', 'state_name': 'Georgia'}
ATX_dict = {'csv_file' : ATX_DATA, 'city_name': 'Austin', 'state_name': 'Texas'}
BAL_dict = {'csv_file' : BAL_DATA, 'city_name': 'Baltimore', 'state_name': 'Maryland'}
BOS_dict = {'csv_file' : BOS_DATA, 'city_name': 'Boston', 'state_name': 'Massachusetts'}
CHA_dict = {'csv_file' : CHA_DATA, 'city_name': 'Charlotte', 'state_name': 'North Carolina'}
DTX_dict = {'csv_file' : DTX_DATA, 'city_name': 'Dallas', 'state_name': 'Texas'}
DC_dict = {'csv_file' : DC_DATA, 'city_name': 'District of Columbia', 'state_name': None}
GBR_dict= {'csv_file' : GBR_DATA, 'city_name': 'Greensboro', 'state_name': 'North Carolina'}
LA_dict = {'csv_file' : LA_DATA, 'city_name': 'Los Angeles', 'state_name': 'California'}
NYC_dict = {'csv_file' : NYC_DATA, 'city_name': 'New York', 'state_name': 'New York'}
PIT_dict = {'csv_file' : PIT_DATA, 'city_name': 'Pittsburgh', 'state_name': 'Pennsylvania'}
RAL_dict = {'csv_file' : RAL_DATA, 'city_name': 'Raleigh', 'state_name': 'North Carolina'}
SF_dict = {'csv_file' : SF_DATA, 'city_name': 'San Francisco', 'state_name': 'California'}
SEA_dict = {'csv_file' : SEA_DATA, 'city_name': 'Seattle', 'state_name': 'Washington'}

dict_list = [ATL_dict, ATX_dict, BAL_dict, BOS_dict, CHA_dict, DTX_dict, DC_dict, GBR_dict, LA_dict, NYC_dict, PIT_dict, RAL_dict, SF_dict, SEA_dict]
nums_list = [34, 38, 39, 45, 40, 58, 59, 60]
cols_list = ['TotalPop', 'White','Black', 'Asian', 'NativeAm', 'Other', 'TwoOrMoreRaces', 'BlackAndWhite']

def get_data(dict_list, nums_list, cols_list):

    for x in range(len(dict_list)):
        city_dict = dict_list.pop()
        csv_file = pd.read_csv(city_dict['csv_file'])
        city_name = city_dict['city_name']
        state_name = city_dict['state_name']
        
        num_IDX = 0
        col_IDX = 0

        while(num_IDX < len(nums_list) and col_IDX < len(cols_list)):
            if(state_name == None):
                city_comparison_df[cols_list[col_IDX]][city_name] = csv_file[city_name + '!!2019 Estimate'][nums_list[num_IDX]]
                col_IDX += 1
                num_IDX += 1
            else:
                city_comparison_df[cols_list[col_IDX]][city_name] = csv_file[city_name +' city, ' + state_name + '!!2019 Estimate'][nums_list[num_IDX]]
                col_IDX += 1
                num_IDX += 1

get_data(dict_list, nums_list, cols_list)

print(city_comparison_df)
#city_comparison_df.to_csv(path.join(BASE_DIR, 'CityComparison.csv'))