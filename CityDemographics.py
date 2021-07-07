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

ATL_population = ATL_DATA['Atlanta city, Georgia!!2019 Estimate'][1]
ATX_population = ATX_DATA['Austin city, Texas!!2019 Estimate'][1]
BOS_population = BOS_DATA['Boston city, Massachusetts!!2019 Estimate'][1]
CHA_population = CHA_DATA['Charlotte city, North Carolina!!2019 Estimate'][1]
DTX_population = DTX_DATA['Dallas city, Texas!!2019 Estimate'][1]
DC_population = DC_DATA['District of Columbia!!2019 Estimate'][1]
GBR_population = GBR_DATA['Greensboro city, North Carolina!!2019 Estimate'][1]
PIT_population = PIT_DATA['Pittsburgh city, Pennsylvania!!2019 Estimate'][1]
RAL_population = RAL_DATA['Raleigh city, North Carolina!!2019 Estimate'][1]

print(ATL_population)
print(ATX_population)
print(BOS_population)
print(CHA_population)
print(DTX_population)
print(DC_population)
print(GBR_population)
print(PIT_population)
print(RAL_population)