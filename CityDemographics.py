from os import path
import pandas as pd
import numpy as np

BASE_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/DiversityData/csvfiles'

#Define file paths to all csv files:
#Demographic files:
ATL_DEMO = path.join(BASE_DIR, 'Demographics/AtlantaCityRaceSexAge.csv')
ATX_DEMO = path.join(BASE_DIR, 'Demographics/AustinCityRaceSexAge.csv')
BAL_DEMO = path.join(BASE_DIR, 'Demographics/BaltimoreCityRaceSexAge.csv')
BOS_DEMO = path.join(BASE_DIR, 'Demographics/BostonCityRaceSexAge.csv')
CHA_DEMO = path.join(BASE_DIR, 'Demographics/CharlotteCityRaceSexAge.csv')
DTX_DEMO = path.join(BASE_DIR, 'Demographics/DallasCityRaceSexAge.csv')
DC_DEMO = path.join(BASE_DIR, 'Demographics/DCCityRaceSexAge.csv')
GBR_DEMO = path.join(BASE_DIR, 'Demographics/GreensboroCityRaceSexAge.csv')
LA_DEMO = path.join(BASE_DIR, 'Demographics/LosAngelesCityRaceSexAge.csv')
NYC_DEMO = path.join(BASE_DIR, 'Demographics/NewYorkCityRaceSexAge.csv')
PIT_DEMO = path.join(BASE_DIR, 'Demographics/PittsburghCityRaceSexAge.csv')
RAL_DEMO = path.join(BASE_DIR, 'Demographics/RaleighCityRaceSexAge.csv')
SF_DEMO = path.join(BASE_DIR, 'Demographics/SanFranciscoCityRaceSexAge.csv')
SEA_DEMO = path.join(BASE_DIR, 'Demographics/SeattleCityRaceSexAge.csv')

#Income files:
ATL_INCOME = path.join(BASE_DIR, 'Income/AtlantaCityMeanIncome.csv')
ATX_INCOME = path.join(BASE_DIR, 'Income/AustinCityMeanIncome.csv')
BAL_INCOME = path.join(BASE_DIR, 'Income/BaltimoreCityMeanIncome.csv')
BOS_INCOME = path.join(BASE_DIR, 'Income/BostonCityMeanIncome.csv')
CHA_INCOME = path.join(BASE_DIR, 'Income/CharlotteCityMeanIncome.csv')
DTX_INCOME = path.join(BASE_DIR, 'Income/DallasCityMeanIncome.csv')
DC_INCOME = path.join(BASE_DIR, 'Income/DCMeanIncome.csv')
GBR_INCOME = path.join(BASE_DIR, 'Income/GreensboroCityMeanIncome.csv')
LA_INCOME = path.join(BASE_DIR, 'Income/LosAngelesCityMeanIncome.csv')
NY_INCOME = path.join(BASE_DIR, 'Income/NewYorkCityMeanIncome.csv')
PGH_INCOME = path.join(BASE_DIR, 'Income/PittsburghCityMeanIncome.csv')
RAL_INCOME = path.join(BASE_DIR, 'Income/RaleighCityMeanIncome.csv')
SF_INCOME = path.join(BASE_DIR, 'Income/SanFranciscoCityMeanIncome.csv')
SEA_INCOME = path.join(BASE_DIR, 'Income/SeattleCityMeanIncome.csv')

#Cost of living index:
COL_INDEX = path.join(BASE_DIR, 'Income/CostOfLivingIndex.csv')


#Define the DataFrame that we're writing our new data to
city_comparison_df = pd.DataFrame(columns=['TotalPop', 'White','Black', 'Asian', 'NativeAm', 'Other', 'TwoOrMoreRaces', 'BlackAndWhite'],
    index=['Atlanta', 'Austin', 'Baltimore', 'Boston', 'Charlotte', 'Dallas', 'District of Columbia', 'Greensboro', 'Los Angeles', 'New York', 'Pittsburgh', 'Raleigh', 'San Francisco', 'Seattle'])

#Define dicts with file path, city and state for each location so that we can pass them in to all of our necessary functions. 
#This formatting is required to read the census csv files:

ATL_dict = {'csv_file' : ATL_DEMO, 'city_name': 'Atlanta', 'state_name': 'Georgia'}
ATX_dict = {'csv_file' : ATX_DEMO, 'city_name': 'Austin', 'state_name': 'Texas'}
BAL_dict = {'csv_file' : BAL_DEMO, 'city_name': 'Baltimore', 'state_name': 'Maryland'}
BOS_dict = {'csv_file' : BOS_DEMO, 'city_name': 'Boston', 'state_name': 'Massachusetts'}
CHA_dict = {'csv_file' : CHA_DEMO, 'city_name': 'Charlotte', 'state_name': 'North Carolina'}
DTX_dict = {'csv_file' : DTX_DEMO, 'city_name': 'Dallas', 'state_name': 'Texas'}
DC_dict = {'csv_file' : DC_DEMO, 'city_name': 'District of Columbia', 'state_name': None}
GBR_dict= {'csv_file' : GBR_DEMO, 'city_name': 'Greensboro', 'state_name': 'North Carolina'}
LA_dict = {'csv_file' : LA_DEMO, 'city_name': 'Los Angeles', 'state_name': 'California'}
NYC_dict = {'csv_file' : NYC_DEMO, 'city_name': 'New York', 'state_name': 'New York'}
PIT_dict = {'csv_file' : PIT_DEMO, 'city_name': 'Pittsburgh', 'state_name': 'Pennsylvania'}
RAL_dict = {'csv_file' : RAL_DEMO, 'city_name': 'Raleigh', 'state_name': 'North Carolina'}
SF_dict = {'csv_file' : SF_DEMO, 'city_name': 'San Francisco', 'state_name': 'California'}
SEA_dict = {'csv_file' : SEA_DEMO, 'city_name': 'Seattle', 'state_name': 'Washington'}

dict_list = [ATL_dict, ATX_dict, BAL_dict, BOS_dict, CHA_dict, DTX_dict, DC_dict, GBR_dict, LA_dict, NYC_dict, PIT_dict, RAL_dict, SF_dict, SEA_dict]
nums_list = [34, 38, 39, 45, 40, 58, 59, 60]
cols_list = ['TotalPop', 'White','Black', 'Asian', 'NativeAm', 'Other', 'TwoOrMoreRaces', 'BlackAndWhite']

def get_demographic_data(dict_list, nums_list, cols_list):

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

get_demographic_data(dict_list, nums_list, cols_list)

print(city_comparison_df)
city_comparison_df.to_csv(path.join(BASE_DIR, 'Analysis/CityComparison.csv'))