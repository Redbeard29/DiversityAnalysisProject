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
ATL_MEAN_INCOME = path.join(BASE_DIR, 'Income/AtlantaCityMeanIncome.csv')
ATL_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/AtlantaCityMedianIncome.csv')
ATX_MEAN_INCOME = path.join(BASE_DIR, 'Income/AustinCityMeanIncome.csv')
ATX_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/AustinCityMedianIncome.csv')
BAL_MEAN_INCOME = path.join(BASE_DIR, 'Income/BaltimoreCityMeanIncome.csv')
BAL_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/BaltimoreCityMedianIncome.csv')
BOS_MEAN_INCOME = path.join(BASE_DIR, 'Income/BostonCityMeanIncome.csv')
BOS_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/BostonCityMedianIncome.csv')
CHA_MEAN_INCOME = path.join(BASE_DIR, 'Income/CharlotteCityMeanIncome.csv')
CHA_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/CharlotteCityMedianIncome.csv')
DTX_MEAN_INCOME = path.join(BASE_DIR, 'Income/DallasCityMeanIncome.csv')
DTX_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/DallasCityMedianIncome.csv')
DC_MEAN_INCOME = path.join(BASE_DIR, 'Income/DCMeanIncome.csv')
DC_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/DCMedianIncome.csv')
GBR_MEAN_INCOME = path.join(BASE_DIR, 'Income/GreensboroCityMeanIncome.csv')
GBR_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/GreensboroCityMedianIncome.csv')
LA_MEAN_INCOME = path.join(BASE_DIR, 'Income/LosAngelesCityMeanIncome.csv')
LA_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/LosAngelesCityMedianIncome.csv')
NY_MEAN_INCOME = path.join(BASE_DIR, 'Income/NewYorkCityMeanIncome.csv')
NY_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/NewYorkCityMedianIncome.csv')
PIT_MEAN_INCOME = path.join(BASE_DIR, 'Income/PittsburghCityMeanIncome.csv')
PIT_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/PittsburghCityMedianIncome.csv')
RAL_MEAN_INCOME = path.join(BASE_DIR, 'Income/RaleighCityMeanIncome.csv')
RAL_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/RaleighCityMedianIncome.csv')
SF_MEAN_INCOME = path.join(BASE_DIR, 'Income/SanFranciscoCityMeanIncome.csv')
SF_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/SanFranciscoCityMedianIncome.csv')
SEA_MEAN_INCOME = path.join(BASE_DIR, 'Income/SeattleCityMeanIncome.csv')
SEA_MEDIAN_INCOME = path.join(BASE_DIR, 'Income/SeattleCityMedianIncome.csv')

#Cost of living index:
# COL_INDEX = path.join(BASE_DIR, 'Income/CostOfLivingIndex.csv')


#Define the DataFrame that we're writing our new data to
city_comparison_df = pd.DataFrame(columns=['TotalPop', 'White','Black', 'Asian', 'NativeAm', 'Other', 'TwoOrMoreRaces', 'BlackAndWhite', 'MeanIncomeHousehold', 'MeanIncomePerCap', 'MIPCWhite', 'MIPCBlack', 'MIPCWhitePercOfTot', 'MIPCBlackPercOfTot', 'MedianIncomeHousehold', 'MedHoWhite', 'MedHoBlack', 'MedHoWhitePercOfTot', 'MedHoBlackPercOfTot'],
    index=['Atlanta', 'Austin', 'Baltimore', 'Boston', 'Charlotte', 'Dallas', 'District of Columbia', 'Greensboro', 'Los Angeles', 'New York', 'Pittsburgh', 'Raleigh', 'San Francisco', 'Seattle'])

#Define dicts with file paths for each csv, city and state for each location so that we can pass them in to all of our necessary functions. 
#This formatting is required to read the census csv files:

ATL_dict = {'demo_csv' : ATL_DEMO, 'mean_csv' : ATL_MEAN_INCOME, 'median_csv' : ATL_MEDIAN_INCOME, 'city_name': 'Atlanta', 'state_name': 'Georgia'}
ATX_dict = {'demo_csv' : ATX_DEMO, 'mean_csv' : ATX_MEAN_INCOME, 'median_csv' : ATX_MEDIAN_INCOME, 'city_name': 'Austin', 'state_name': 'Texas'}
BAL_dict = {'demo_csv' : BAL_DEMO, 'mean_csv' : BAL_MEAN_INCOME, 'median_csv' : BAL_MEDIAN_INCOME, 'city_name': 'Baltimore', 'state_name': 'Maryland'}
BOS_dict = {'demo_csv' : BOS_DEMO, 'mean_csv' : BOS_MEAN_INCOME, 'median_csv' : BOS_MEDIAN_INCOME, 'city_name': 'Boston', 'state_name': 'Massachusetts'}
CHA_dict = {'demo_csv' : CHA_DEMO, 'mean_csv' : CHA_MEAN_INCOME, 'median_csv' : CHA_MEDIAN_INCOME, 'city_name': 'Charlotte', 'state_name': 'North Carolina'}
DTX_dict = {'demo_csv' : DTX_DEMO, 'mean_csv' : DTX_MEAN_INCOME, 'median_csv' : DTX_MEDIAN_INCOME, 'city_name': 'Dallas', 'state_name': 'Texas'}
DC_dict = {'demo_csv' : DC_DEMO, 'mean_csv' : DC_MEAN_INCOME, 'median_csv' : DC_MEDIAN_INCOME, 'city_name': 'District of Columbia', 'state_name': None}
GBR_dict= {'demo_csv' : GBR_DEMO, 'mean_csv' : GBR_MEAN_INCOME, 'median_csv' : GBR_MEDIAN_INCOME, 'city_name': 'Greensboro', 'state_name': 'North Carolina'}
LA_dict = {'demo_csv' : LA_DEMO, 'mean_csv' : LA_MEAN_INCOME, 'median_csv' : LA_MEDIAN_INCOME, 'city_name': 'Los Angeles', 'state_name': 'California'}
NYC_dict = {'demo_csv' : NYC_DEMO, 'mean_csv' : NY_MEAN_INCOME, 'median_csv' : NY_MEDIAN_INCOME, 'city_name': 'New York', 'state_name': 'New York'}
PIT_dict = {'demo_csv' : PIT_DEMO, 'mean_csv' : PIT_MEAN_INCOME, 'median_csv' : PIT_MEDIAN_INCOME, 'city_name': 'Pittsburgh', 'state_name': 'Pennsylvania'}
RAL_dict = {'demo_csv' : RAL_DEMO, 'mean_csv' : RAL_MEAN_INCOME, 'median_csv' : RAL_MEDIAN_INCOME, 'city_name': 'Raleigh', 'state_name': 'North Carolina'}
SF_dict = {'demo_csv' : SF_DEMO, 'mean_csv' : SF_MEAN_INCOME, 'median_csv' : SF_MEDIAN_INCOME, 'city_name': 'San Francisco', 'state_name': 'California'}
SEA_dict = {'demo_csv' : SEA_DEMO, 'mean_csv' : SEA_MEAN_INCOME, 'median_csv' : SEA_MEDIAN_INCOME, 'city_name': 'Seattle', 'state_name': 'Washington'}

dict_list = [ATL_dict, ATX_dict, BAL_dict, BOS_dict, CHA_dict, DTX_dict, DC_dict, GBR_dict, LA_dict, NYC_dict, PIT_dict, RAL_dict, SF_dict, SEA_dict]


#Add demographic data to csv:

def get_demographic_data(dict_list):

    nums_list = [34, 38, 39, 45, 40, 58, 59, 60]
    cols_list = ['TotalPop', 'White','Black', 'Asian', 'NativeAm', 'Other', 'TwoOrMoreRaces', 'BlackAndWhite']

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
            else:
                city_comparison_df[cols_list[col_IDX]][city_name] = csv_file[city_name +' city, ' + state_name + '!!2019 Estimate'][nums_list[num_IDX]]
           
            col_IDX += 1
            num_IDX += 1
    
        get_mean_economic_data(city_dict)
        get_median_economic_data(city_dict)


def get_mean_economic_data(city_dict):

    nums_list = [1, 21, 23, 24, [23, 21], [24,21]]
    cols_list = ['MeanIncomeHousehold', 'MeanIncomePerCap', 'MIPCWhite', 'MIPCBlack', 'MIPCWhitePercOfTot', 'MIPCBlackPercOfTot']

    for x in range(len(city_dict)):
        csv_file = pd.read_csv(city_dict['mean_csv'])
        city_name = city_dict['city_name']
        state_name = city_dict['state_name']

        num_IDX = 0
        col_IDX = 0


        while(num_IDX < len(nums_list) and col_IDX < len(cols_list)):

            if [cols_list[col_IDX]] == ['MIPCWhitePercOfTot']:
                percentage_nums_list = nums_list[num_IDX]
                calculate_percentage(city_dict, percentage_nums_list, 'MIPCWhitePercOfTot', 'mean')
            
            elif [cols_list[col_IDX]] == ['MIPCBlackPercOfTot']:
                percentage_nums_list = nums_list[num_IDX]
                calculate_percentage(city_dict, percentage_nums_list, 'MIPCBlackPercOfTot', 'mean')

            elif(state_name == None):
                city_comparison_df[cols_list[col_IDX]][city_name] = '$' + (csv_file[city_name + '!!Mean income (dollars)!!Estimate'][nums_list[num_IDX]])

            else:
                city_comparison_df[cols_list[col_IDX]][city_name] = '$' + (csv_file[city_name +' city, ' + state_name + '!!Mean income (dollars)!!Estimate'][nums_list[num_IDX]])

            col_IDX += 1
            num_IDX += 1

def get_median_economic_data(city_dict):

    nums_list = [1, 3, 4, [3, 1], [4, 1]]
    cols_list = ['MedianIncomeHousehold', 'MedHoWhite', 'MedHoBlack', 'MedHoWhitePercOfTot', 'MedHoBlackPercOfTot']

    for x in range(len(city_dict)):
        csv_file = pd.read_csv(city_dict['median_csv'])
        city_name = city_dict['city_name']
        state_name = city_dict['state_name']

        num_IDX = 0
        col_IDX = 0

        while(num_IDX < len(nums_list) and col_IDX < len(cols_list)):

            if [cols_list[col_IDX]] == ['MedHoWhitePercOfTot']:
                percentage_nums_list = nums_list[num_IDX]
                calculate_percentage(city_dict, percentage_nums_list, 'MedHoWhitePercOfTot', 'median')
            
            elif [cols_list[col_IDX]] == ['MedHoBlackPercOfTot']:
                percentage_nums_list = nums_list[num_IDX]
                calculate_percentage(city_dict, percentage_nums_list, 'MedHoBlackPercOfTot', 'median')

            elif(state_name == None):
                city_comparison_df[cols_list[col_IDX]][city_name] = '$' + (csv_file[city_name + '!!Median income (dollars)!!Estimate'][nums_list[num_IDX]])

            else:
                city_comparison_df[cols_list[col_IDX]][city_name] = '$' + (csv_file[city_name +' city, ' + state_name + '!!Median income (dollars)!!Estimate'][nums_list[num_IDX]])

            col_IDX += 1
            num_IDX += 1


def calculate_percentage(city_dict, percentage_nums_list, column_name, csv_type):
    
    for x in range(len(city_dict)):
        csv_file = pd.read_csv(city_dict[csv_type + '_csv'])
        city_name = city_dict['city_name']
        state_name = city_dict['state_name']

        if(csv_type == 'mean'):
            if(state_name == None):
                first_mipc = csv_file[city_name + '!!Mean income (dollars)!!Estimate'][percentage_nums_list[0]]
                first_mipc = first_mipc.replace(',', '')
                total_mipc = csv_file[city_name + '!!Mean income (dollars)!!Estimate'][percentage_nums_list[1]]
                total_mipc = total_mipc.replace(',', '')
            else:
                first_mipc = csv_file[city_name +' city, ' + state_name + '!!Mean income (dollars)!!Estimate'][percentage_nums_list[0]]
                first_mipc = first_mipc.replace(',', '')
                total_mipc = csv_file[city_name +' city, ' + state_name + '!!Mean income (dollars)!!Estimate'][percentage_nums_list[1]]
                total_mipc = total_mipc.replace(',', '')

            city_comparison_df[column_name][city_name] = str(round((int(first_mipc) / int(total_mipc) * 100), 2)) + '%'


        else:
            if(state_name == None):
                first_mipc = csv_file[city_name + '!!Median income (dollars)!!Estimate'][percentage_nums_list[0]]
                first_mipc = first_mipc.replace(',', '')
                total_mipc = csv_file[city_name + '!!Median income (dollars)!!Estimate'][percentage_nums_list[1]]
                total_mipc = total_mipc.replace(',', '')
            else:
                first_mipc = csv_file[city_name +' city, ' + state_name + '!!Median income (dollars)!!Estimate'][percentage_nums_list[0]]
                first_mipc = first_mipc.replace(',', '')
                total_mipc = csv_file[city_name +' city, ' + state_name + '!!Median income (dollars)!!Estimate'][percentage_nums_list[1]]
                total_mipc = total_mipc.replace(',', '')

            city_comparison_df[column_name][city_name] = str(round((int(first_mipc) / int(total_mipc) * 100), 2)) + '%'


get_demographic_data(dict_list)


#def col_calculator(col_dict):
    #total_col = col_dict['Total']

#Define cost of living dictionaries to pass to col_calculator function:
# ATL_COL = {'Total' : 76.76, 'Rent' : 50.85, 'COLI Plus Rent' : 64.77, 'Groceries' : 78.2, 'Restaurant Price' : 68.66}
# ATX_COL = {'Total' : 63.84, 'Rent' : 54.47, 'COLI Plus Rent' : 59.51, 'Groceries' : 63.59, 'Restaurant Price' : 68.06}
# BAL_COL = {'Total' : 72.47, 'Rent' : 44.69, 'COLI Plus Rent' : 59.62, 'Groceries' : 70.62, 'Restaurant Price' : 73.92}
# BOS_COL = {'Total' : 88.67, 'Rent' : 77.37, 'COLI Plus Rent' : 83.44, 'Groceries' : 88.36, 'Restaurant Price' : 94.53}
# CHA_COL = {'Total' : 69.62, 'Rent' : 48.86, 'COLI Plus Rent' : 60.03, 'Groceries' : 66.76, 'Restaurant Price' : 68.8}
# DTX_COL = {'Total' : 67.68, 'Rent' : 50.13, 'COLI Plus Rent' : 59.57, 'Groceries' : 62.25, 'Restaurant Price' : 72.52}
# DC_COL = {'Total' : 83.91, 'Rent' : 78.24, 'COLI Plus Rent' : 81.29, 'Groceries' : 83.89, 'Restaurant Price' : 79.4}
# GBR_COL = {'Total' : None, 'Rent' : None, 'COLI Plus Rent' : None, 'Groceries' : None, 'Restaurant Price' : None}
# LA_COL = {'Total' : 79.6, 'Rent' : 74.08, 'COLI Plus Rent' : 77.05, 'Groceries' : 75.95, 'Restaurant Price' : 91.55}
# NYC_COL = {'Total' : 100, 'Rent' : 100, 'COLI Plus Rent' : 100, 'Groceries' : 100, 'Restaurant Price' : 100}
# PIT_COL = {'Total' : 78.46, 'Rent' : 39.82, 'COLI Plus Rent' : 60.6, 'Groceries' : 84.4, 'Restaurant Price' : 61.6}
# RAL_COL = {'Total' : 68.76, 'Rent' : 39.22, 'COLI Plus Rent' : 55.1, 'Groceries' : 70.8, 'Restaurant Price' : 70.47}
# SF_COL = {'Total' : 93.89, 'Rent' : 118.15, 'COLI Plus Rent' : 105.1, 'Groceries' : 96.89, 'Restaurant Price' : 94.37}
# SEA_COL = {'Total' : 86.38, 'Rent' : 71.02, 'COLI Plus Rent' : 79.28, 'Groceries' : 84.54, 'Restaurant Price' : 86.21}

# one_percent_rent = 42.189854344550476

# DC_rent = round(one_percent_rent * 78.24, 2)
# DTX_rent = round(one_percent_rent * 50.13, 2)
# RAL_rent = round(one_percent_rent * 39.22, 2)

city_comparison_df.to_csv(path.join(BASE_DIR, 'Analysis/CityComparison.csv'))

print(city_comparison_df)

# print(90005/54414)