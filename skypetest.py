import pandas as pd 
import json
import csv
from pandas.io.json import json_normalize #package for flattening json in pandas df
with open('yes.json') as f: d = json.load(f) #loads the JSON data to a dataframe

d = json_normalize(d, 'messages', ['group' ]) #normalize the complex JSON file to a readable dataframe
columns = ['id', 'messagetype', 'version','content', 'conversationid','from','properties','amsreferences', 'properties.emotions',  'properties.isserversidegenerated','properties.deletetime', 'properties.edittime', 'properties.urlpreviews', 'properties.forwardMetadata','properties.albumId','properties.poll' ]
d.drop(columns, inplace=True, axis=1) # Drops unusable column for better time complexity and reduce loading time
networkstring= 'ActiveNetwork' #names variables
softwarestring = 'SoftwareServices' 

dataFNet = d[d['group'] == networkstring]  #divide the dataframe based on column value
dataFSoft = d[d['group'] == softwarestring] #divide the dataframe based on column value

#For Software Division
dataFSoft['originalarrivaltime'] = pd.to_datetime(dataFSoft['originalarrivaltime'], errors='coerce') # formats the date time using panda library
dataFSoft['year'] = pd.DatetimeIndex(dataFSoft['originalarrivaltime']).year # adds new column for further checking of year for logical check
dataFSoft['month'] = pd.DatetimeIndex(dataFSoft['originalarrivaltime']).month # adds new month for further logical checking
dataFSoft= dataFSoft[dataFSoft.month.astype(str).str.contains('4')]  # checks if the rows matches specific month, months in number form, i.e. January-1, Feb-2
dataFSoft= dataFSoft[dataFSoft.year.astype(str).str.contains('2020')] #checks row against certain year
dataFSoft['originalarrivaltime'] = dataFSoft['originalarrivaltime'].astype(str).str[:10] # make a substring of entire time stamp to minimize loading time and keep only the date
dataFSoft.drop(columns=['group', 'year','month'], inplace=True, axis=1) #drops extra column for better time complexity
dataFSoft=pd.pivot_table(dataFSoft,values='originalarrivaltime', index='displayName', columns='originalarrivaltime',aggfunc={'originalarrivaltime': 'count'}) # uses pivot table for synchronization of the date column to header and match with displayName
dataFSoft.fillna(0,inplace=True) # fill all missing value with zero
dataFSoft.to_csv('software.csv') # import the result to a csv file

#For Network Division
dataFNet['originalarrivaltime'] = pd.to_datetime(dataFNet['originalarrivaltime'], errors='coerce') # formats the data time using panda library
dataFNet['year'] = pd.DatetimeIndex(dataFNet['originalarrivaltime']).year # adds new column for further checking of year for logical check
dataFNet['month'] = pd.DatetimeIndex(dataFNet['originalarrivaltime']).month # adds new month for further logical checking
dataFNet= dataFNet[dataFNet.month.astype(str).str.contains('4')]  # checks if the rows matches specific month, months in number form, i.e. January-1, Feb-2
dataFNet= dataFNet[dataFNet.year.astype(str).str.contains('2020')] #checks row against certain year
dataFNet['originalarrivaltime'] = dataFNet['originalarrivaltime'].astype(str).str[:10] # make a substring to reduce loading
dataFNet.drop(columns=['group', 'year','month'], inplace=True, axis=1) #drops extra column for better time complexity
dataFNet=pd.pivot_table(dataFNet,values='originalarrivaltime', index='displayName', columns='originalarrivaltime',aggfunc={'originalarrivaltime': 'count'}) # uses pivot table for synchronization of the date column to header and match with displayName
dataFNet.fillna(0,inplace=True) # fill all missing value with zero
dataFNet.to_csv('network.csv') # import the result to a csv file


