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
PIT_INCOME = path.join(BASE_DIR, 'Income/PittsburghCityMeanIncome.csv')
RAL_INCOME = path.join(BASE_DIR, 'Income/RaleighCityMeanIncome.csv')
SF_INCOME = path.join(BASE_DIR, 'Income/SanFranciscoCityMeanIncome.csv')
SEA_INCOME = path.join(BASE_DIR, 'Income/SeattleCityMeanIncome.csv')

#Cost of living index:
COL_INDEX = path.join(BASE_DIR, 'Income/CostOfLivingIndex.csv')


#Define the DataFrame that we're writing our new data to
city_comparison_df = pd.DataFrame(columns=['TotalPop', 'White','Black', 'Asian', 'NativeAm', 'Other', 'TwoOrMoreRaces', 'BlackAndWhite', 'AvgPerCapIncome'],
    index=['Atlanta', 'Austin', 'Baltimore', 'Boston', 'Charlotte', 'Dallas', 'District of Columbia', 'Greensboro', 'Los Angeles', 'New York', 'Pittsburgh', 'Raleigh', 'San Francisco', 'Seattle'])

#Define dicts with file path, city and state for each location so that we can pass them in to all of our necessary functions. 
#This formatting is required to read the census csv files:

ATL_dict = {'demo_csv' : ATL_DEMO, 'income_csv' : ATL_INCOME, 'city_name': 'Atlanta', 'state_name': 'Georgia'}
ATX_dict = {'demo_csv' : ATX_DEMO, 'income_csv' : ATX_INCOME, 'city_name': 'Austin', 'state_name': 'Texas'}
BAL_dict = {'demo_csv' : BAL_DEMO, 'income_csv' : BAL_INCOME, 'city_name': 'Baltimore', 'state_name': 'Maryland'}
BOS_dict = {'demo_csv' : BOS_DEMO, 'income_csv' : BOS_INCOME, 'city_name': 'Boston', 'state_name': 'Massachusetts'}
CHA_dict = {'demo_csv' : CHA_DEMO, 'income_csv' : CHA_INCOME, 'city_name': 'Charlotte', 'state_name': 'North Carolina'}
DTX_dict = {'demo_csv' : DTX_DEMO, 'income_csv' : DTX_INCOME, 'city_name': 'Dallas', 'state_name': 'Texas'}
DC_dict = {'demo_csv' : DC_DEMO, 'income_csv' : DC_INCOME, 'city_name': 'District of Columbia', 'state_name': None}
GBR_dict= {'demo_csv' : GBR_DEMO, 'income_csv' : GBR_INCOME, 'city_name': 'Greensboro', 'state_name': 'North Carolina'}
LA_dict = {'demo_csv' : LA_DEMO, 'income_csv' : LA_INCOME, 'city_name': 'Los Angeles', 'state_name': 'California'}
NYC_dict = {'demo_csv' : NYC_DEMO, 'income_csv' : NY_INCOME, 'city_name': 'New York', 'state_name': 'New York'}
PIT_dict = {'demo_csv' : PIT_DEMO, 'income_csv' : PIT_INCOME, 'city_name': 'Pittsburgh', 'state_name': 'Pennsylvania'}
RAL_dict = {'demo_csv' : RAL_DEMO, 'income_csv' : RAL_INCOME, 'city_name': 'Raleigh', 'state_name': 'North Carolina'}
SF_dict = {'demo_csv' : SF_DEMO, 'income_csv' : SF_INCOME, 'city_name': 'San Francisco', 'state_name': 'California'}
SEA_dict = {'demo_csv' : SEA_DEMO, 'income_csv' : SEA_INCOME, 'city_name': 'Seattle', 'state_name': 'Washington'}

dict_list = [ATL_dict, ATX_dict, BAL_dict, BOS_dict, CHA_dict, DTX_dict, DC_dict, GBR_dict, LA_dict, NYC_dict, PIT_dict, RAL_dict, SF_dict, SEA_dict]
nums_list = [34, 38, 39, 45, 40, 58, 59, 60, 22]
cols_list = ['TotalPop', 'White','Black', 'Asian', 'NativeAm', 'Other', 'TwoOrMoreRaces', 'BlackAndWhite', 'AvgPerCapIncome']

def get_demographic_data(dict_list, nums_list, cols_list):

    for x in range(len(dict_list)):
        city_dict = dict_list.pop()
        csv_file = pd.read_csv(city_dict['demo_csv'])
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

read_atl_income = pd.read_csv(ATL_INCOME)

print(read_atl_income['Atlanta city, Georgia!!Mean income (dollars)!!Estimate'][21])