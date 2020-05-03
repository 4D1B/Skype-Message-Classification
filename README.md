# Skype-Message-Classification


This program subtly focuses on data classification based on a raw JSON file.

## Getting Started

Let's see how we can get going to successfully run this program on local system.

### Prerequisites

Python has to be installed to run this program. Any latest version should be fine. Py 3.6.4 has been used to build and test this program.

```
python
```
Running this command on command prompt should be giving the python version of the system. If the system doesn't have python installed, it can be done via browser using google collab. 

```
https://colab.research.google.com/notebooks/intro.ipynb --for new Colab
https://colab.research.google.com/drive/1WCP5ZEtRJL0QvT59ectoyv_3Uylkw5RJ?usp=sharing -- To access this program which is written in google colab
```

yes.json which is the raw JSON file has to be uploaded in the folder section of the google colab if it is not already there.

### Installing

Python can be installed from this given site.

```
https://www.python.org/downloads/
```



## Running the tests

To run this test, the following command in command prompt has to be written

```
python skypetest.py 
```

Here, skypetest.py is the name of the file and python command is used to redirect to execute any specific python file.
To be Noted down that, in this program , source data file is used as 'yes.json'. It can be modified as per the location of the user's data source file. For example, 
If the user stores the JSON file in home/4d1b/ folder, the entire location has to be set as such so that the program can find the JSON file. 
It is recommended to set the working directory to this Git cloned folder so that, nothing extra has to be done.

### Break down into end to end tests

This skypetest.py gives output on all the existing users of the skype chat groups. Also, it shows the amount of time any specific users wrote in that very group. The output result is showed distinguishing the dates so that, it can be seen on each day how many messages have been written by any specific skype user.

```

```

### Program coding part

The following briefly explains the program


```
with open('yes.json') as f: d = json.load(f)
```
This command loads the json file into a dataframe where yes.json is the source data file in JSON format. For instance, d is a random name given.

```
d = json_normalize(d, 'messages', ['group' ])
```
This command normalizes the complex JSON raw file where the variables were kept nested. To make it easier and more comprehend, normalization is done.

```
networkstring= 'ActiveNetwork'
softwarestring = 'SoftwareServices'

dataFNet = d[d['group'] == networkstring]
dataFSoft = d[d['group'] == softwarestring]
```
Two variables are taken which splits the dataframe in two parts based on a specific column(group) value. 


```
dataFSoft['originalarrivaltime'] = pd.to_datetime(dataFSoft['originalarrivaltime'], errors='coerce')
```
Pandas library is used to format the date time.

```
dataFSoft['year'] = pd.DatetimeIndex(dataFSoft['originalarrivaltime']).year
dataFSoft['month'] = pd.DatetimeIndex(dataFSoft['originalarrivaltime']).month
```
Two extra columns are added for extracting the precise month and year value from any given row.

```
dataFSoft= dataFSoft[dataFSoft.month.astype(str).str.contains('4')] 
dataFSoft= dataFSoft[dataFSoft.year.astype(str).str.contains('2020')] 
```
Dataframe goes through logical check where only the rows of any specific months and year is kept where checking is done against the newly added columns previously.

```
columns = ['id', 'messagetype', 'version','content', 'conversationid','from','properties','amsreferences', 'properties.emotions',  'properties.isserversidegenerated','properties.deletetime', 'properties.edittime', 'properties.urlpreviews', 'properties.forwardMetadata','properties.albumId','properties.poll','year', 'month'   ]
dataFSoft.drop(columns, inplace=True, axis=1)
```
Only two relevant columns are kept, rest are dropped for making the complexity easier

```
dataFSoft['originalarrivaltime'] = dataFSoft['originalarrivaltime'].astype(str).str[:10]
```
Time stamp is cut to a substring and only the date value is kept for better visualization.

```
final=pd.pivot_table(dataFSoft,values='originalarrivaltime', index='displayName', 
                    columns='originalarrivaltime',
             aggfunc={'originalarrivaltime': 'count'}
)
```
Pivot table to move a specific columns values as header which counts the the number of rows based on the value of the specific column value. For instances, here originalarrivaltime is moved towards header so that it can be counted how many displayName occurences took place on each originalarrivaltime value.



## Deployment

```
final.to_csv('software.csv')
```
Finally, the output is converted to a csv formatted file. It is to be noted that, this CSV file will be created to the present working directory of the execution command.


## Built With

* [python](https://docs.python.org/3/) - Python has been used
* [pandas](https://pandas.pydata.org/docs/) - data structures and data analysis tools 
* [Numpy](https://numpy.org/) - Computation



 

## Authors

* **4d1b** - *Initial work* - [ADG](https://github.com/4d1b)




## Acknowledgments

* stackoverflow.com
* kaggle.com


