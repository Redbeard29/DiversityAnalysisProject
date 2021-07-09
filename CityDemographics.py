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
city_comparison_df = pd.DataFrame(columns=['TotalPop', 'White','Black','AAPI', 'NativeAmerican','Other', 'TwoOrMoreRaces', 'BlackAndWhite'],
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

dict_list = [ATL_dict, ATX_dict, BOS_dict, CHA_dict, DTX_dict, DC_dict, GBR_dict, PIT_dict, RAL_dict]

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

def percent_white(city_dict):
    """
    This function takes in the same dict, and uses
    that data to find the percentage of the city's white residents in the associated csv file. 
    """
    csv_file = pd.read_csv(city_dict['csv_file'])
    city_name = city_dict['city_name']
    state_name = city_dict['state_name']

    if(state_name == None):
        return csv_file[city_name + '!!2019 Estimate'][38]
    else:
        return csv_file[city_name +' city, ' + state_name + '!!2019 Estimate'][38]

ATL_pw = percent_white(ATL_dict)
ATX_pw = percent_white(ATX_dict)
BOS_pw = percent_white(BOS_dict)
CHA_pw = percent_white(CHA_dict)
DTX_pw = percent_white(DTX_dict)
DC_pw = percent_white(DC_dict)
GBR_pw = percent_white(GBR_dict)
PIT_pw = percent_white(PIT_dict)
RAL_pw = percent_white(RAL_dict)

city_comparison_df['White'] = [ATL_pw, ATX_pw, BOS_pw, CHA_pw, DTX_pw, DC_pw, GBR_pw, PIT_pw, RAL_pw]

def percent_black(city_dict):
    """
    This function finds the percentage of the city's black residents in the associated csv file. 
    """
    csv_file = pd.read_csv(city_dict['csv_file'])
    city_name = city_dict['city_name']
    state_name = city_dict['state_name']

    if(state_name == None):
        return csv_file[city_name + '!!2019 Estimate'][39]
    else:
        return csv_file[city_name +' city, ' + state_name + '!!2019 Estimate'][39]

ATL_pb = percent_black(ATL_dict)
ATX_pb = percent_black(ATX_dict)
BOS_pb = percent_black(BOS_dict)
CHA_pb = percent_black(CHA_dict)
DTX_pb = percent_black(DTX_dict)
DC_pb = percent_black(DC_dict)
GBR_pb = percent_black(GBR_dict)
PIT_pb = percent_black(PIT_dict)
RAL_pb = percent_black(RAL_dict)

city_comparison_df['Black'] = [ATL_pb, ATX_pb, BOS_pb, CHA_pb, DTX_pb, DC_pb, GBR_pb, PIT_pb, RAL_pb]

def percent_aapi(city_dict):
    """
    This function finds the percentage of the city's asian american and pacific islander residents in the associated csv file. 
    """
    csv_file = pd.read_csv(city_dict['csv_file'])
    city_name = city_dict['city_name']
    state_name = city_dict['state_name']

    if(state_name == None):
        asian_percentage = (csv_file[city_name + '!!2019 Estimate'][45])
        asian_float = float(asian_percentage.replace('%', ''))
        pi_percentage = (csv_file[city_name + '!!2019 Estimate'][53])
        pi_float = float(pi_percentage.replace('%', ''))
        aapi_total = asian_float + pi_float
        return str(round(aapi_total, 2)) + '%'
    else:
        asian_percentage = (csv_file[city_name +' city, ' + state_name + '!!2019 Estimate'][45])
        asian_float = float(asian_percentage.replace('%', ''))
        pi_percentage = (csv_file[city_name +' city, ' + state_name + '!!2019 Estimate'][53])
        pi_float = float(pi_percentage.replace('%', ''))
        aapi_total = asian_float + pi_float
        return str(round(aapi_total, 2))+ '%'

ATL_aapi = percent_aapi(ATL_dict)
ATX_aapi = percent_aapi(ATX_dict)
BOS_aapi = percent_aapi(BOS_dict)
CHA_aapi = percent_aapi(CHA_dict)
DTX_aapi = percent_aapi(DTX_dict)
DC_aapi = percent_aapi(DC_dict)
GBR_aapi = percent_aapi(GBR_dict)
PIT_aapi = percent_aapi(PIT_dict)
RAL_aapi = percent_aapi(RAL_dict)

city_comparison_df['AAPI'] = [ATL_aapi, ATX_aapi, BOS_aapi, CHA_aapi, DTX_aapi, DC_aapi, GBR_aapi, PIT_aapi, RAL_aapi]

def percent_natam(city_dict):
    """
    This function finds the percentage of the city's black residents in the associated csv file. 
    """
    csv_file = pd.read_csv(city_dict['csv_file'])
    city_name = city_dict['city_name']
    state_name = city_dict['state_name']

    if(state_name == None):
        return csv_file[city_name + '!!2019 Estimate'][40]
    else:
        return csv_file[city_name +' city, ' + state_name + '!!2019 Estimate'][40]

ATL_na = percent_natam(ATL_dict)
ATX_na = percent_natam(ATX_dict)
BOS_na = percent_natam(BOS_dict)
CHA_na = percent_natam(CHA_dict)
DTX_na = percent_natam(DTX_dict)
DC_na = percent_natam(DC_dict)
GBR_na = percent_natam(GBR_dict)
PIT_na = percent_natam(PIT_dict)
RAL_na = percent_natam(RAL_dict)

city_comparison_df['NativeAmerican'] = [ATL_na, ATX_na, BOS_na, CHA_na, DTX_na, DC_na, GBR_na, PIT_na, RAL_na]

def percent_other(city_dict):
    """
    This function finds the percentage of the city's black residents in the associated csv file. 
    """
    csv_file = pd.read_csv(city_dict['csv_file'])
    city_name = city_dict['city_name']
    state_name = city_dict['state_name']

    if(state_name == None):
        return csv_file[city_name + '!!2019 Estimate'][58]
    else:
        return csv_file[city_name +' city, ' + state_name + '!!2019 Estimate'][58]

ATL_ot = percent_other(ATL_dict)
ATX_ot = percent_other(ATX_dict)
BOS_ot = percent_other(BOS_dict)
CHA_ot = percent_other(CHA_dict)
DTX_ot = percent_other(DTX_dict)
DC_ot = percent_other(DC_dict)
GBR_ot = percent_other(GBR_dict)
PIT_ot = percent_other(PIT_dict)
RAL_ot = percent_other(RAL_dict)

city_comparison_df['Other'] = [ATL_ot, ATX_ot, BOS_ot, CHA_ot, DTX_ot, DC_ot, GBR_ot, PIT_ot, RAL_ot]

def two_or_more_races(city_dict):
    """
    This function finds the percentage of the city's black residents in the associated csv file. 
    """
    csv_file = pd.read_csv(city_dict['csv_file'])
    city_name = city_dict['city_name']
    state_name = city_dict['state_name']

    if(state_name == None):
        return csv_file[city_name + '!!2019 Estimate'][59]
    else:
        return csv_file[city_name +' city, ' + state_name + '!!2019 Estimate'][59]

ATL_two = two_or_more_races(ATL_dict)
ATX_two = two_or_more_races(ATX_dict)
BOS_two = two_or_more_races(BOS_dict)
CHA_two = two_or_more_races(CHA_dict)
DTX_two = two_or_more_races(DTX_dict)
DC_two = two_or_more_races(DC_dict)
GBR_two = two_or_more_races(GBR_dict)
PIT_two = two_or_more_races(PIT_dict)
RAL_two = two_or_more_races(RAL_dict)

city_comparison_df['TwoOrMoreRaces'] = [ATL_two, ATX_two, BOS_two, CHA_two, DTX_two, DC_two, GBR_two, PIT_two, RAL_two]

def black_and_white(city_dict):
    """
    This function finds the percentage of the city's black residents in the associated csv file. 
    """
    csv_file = pd.read_csv(city_dict['csv_file'])
    city_name = city_dict['city_name']
    state_name = city_dict['state_name']

    if(state_name == None):
        return csv_file[city_name + '!!2019 Estimate'][60]
    else:
        return csv_file[city_name +' city, ' + state_name + '!!2019 Estimate'][60]

ATL_baw = black_and_white(ATL_dict)
ATX_baw = black_and_white(ATX_dict)
BOS_baw = black_and_white(BOS_dict)
CHA_baw = black_and_white(CHA_dict)
DTX_baw = black_and_white(DTX_dict)
DC_baw = black_and_white(DC_dict)
GBR_baw = black_and_white(GBR_dict)
PIT_baw = black_and_white(PIT_dict)
RAL_baw = black_and_white(RAL_dict)

city_comparison_df['BlackAndWhite'] = [ATL_baw, ATX_baw, BOS_baw, CHA_baw, DTX_baw, DC_baw, GBR_baw, PIT_baw, RAL_baw]

print(city_comparison_df)