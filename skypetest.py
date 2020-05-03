import json 
import csv
import pandas as pd 
import locale
import datetime as dt
import numpy as np
from pandas.io.json import json_normalize #package for flattening json in pandas df
#load json object
with open('sample_data/yes.json') as f: d = json.load(f)


#tells us parent node is 'programs'
d = json_normalize(d, 'messages', ['group' ])
#nycphil id	displayName	originalarrivaltime	messagetype	version	content	conversationid	from	properties	amsreferences	properties.emotions	properties.isserversidegenerated	properties.deletetime	properties.edittime	properties.urlpreviews	properties.forwardMetadata	properties.albumId	properties.poll	group

networkstring= 'ActiveNetwork'
softwarestring = 'SoftwareServices'

dataFNet = d[d['group'] == networkstring]
dataFSoft = d[d['group'] == softwarestring]
#dataFSoft['originalarrivaltime'] = dataFSoft['originalarrivaltime'].str[:10]
#dataFSoft.to_csv('software.csv')
dataFSoft['originalarrivaltime'] = pd.to_datetime(dataFSoft['originalarrivaltime'], errors='coerce')
#result = dataFSoft['originalarrivaltime'].dt.month_name(locale = 'French') 
#dataFSoft= dataFSoft[dataFSoft.originalarrivaltime.astype(str).str.contains('2020-04')]

#dataFSoft['originalarrivaltime']  = dataFSoft['originalarrivaltime'] .dt.tz_convert(None)
#pd.to_datetime(dataFSoft['originalarrivaltime'])
dataFSoft['year'] = pd.DatetimeIndex(dataFSoft['originalarrivaltime']).year
dataFSoft['month'] = pd.DatetimeIndex(dataFSoft['originalarrivaltime']).month

dataFSoft= dataFSoft[dataFSoft.month.astype(str).str.contains('4')] 
dataFSoft= dataFSoft[dataFSoft.year.astype(str).str.contains('2020')] 
#id	displayName	originalarrivaltime	messagetype	version	content	conversationid	from	properties	amsreferences	properties.emotions	properties.isserversidegenerated	properties.deletetime	properties.edittime	properties.urlpreviews	properties.forwardMetadata	properties.albumId	properties.poll	group	year	month
columns = ['id', 'messagetype', 'version','content', 'conversationid','from','properties','amsreferences', 'properties.emotions',  'properties.isserversidegenerated','properties.deletetime', 'properties.edittime', 'properties.urlpreviews', 'properties.forwardMetadata','properties.albumId','properties.poll','year', 'month'   ]
dataFSoft.drop(columns, inplace=True, axis=1)
dataFSoft['originalarrivaltime'] = dataFSoft['originalarrivaltime'].astype(str).str[:10]
print(pd.pivot_table(dataFSoft,values='originalarrivaltime', index='displayName', 
                    columns='originalarrivaltime',
             aggfunc={'originalarrivaltime': 'count'}
)
)

#final = dataFSoft['displayName'].value_counts()
#final.to_csv('final.csv')


