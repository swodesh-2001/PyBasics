# Pandas Practice
 
## Table of Contents
1. [Dataframes](#dataframes)
2. [Obtaining Basic Information About DataFrame](#obtaining-basic-information-about-dataframe)
3. [Selection and Indexing](#selection-and-indexing)
4. [Index Basics](#index-basics)
5. [Filtering](#filtering)
6. [Useful Methods](#useful-methods)
7. [Handling Missing Data](#handling-missing-data)

## Dataframes
 Pandas DataFrame is a 2-dimensional labeled data structure with ability to contain columns of different types. We can make pandas dataframe through different methods:

### 1. From a Dictionary

```python
import pandas as pd

data = {'Name': ['Ram', 'Shyam', 'Sita', 'Geeta'],
        'Age': [28, 35, 42, 29],
        'City': ['New York', 'Paris', 'London', 'Sydney']}

df = pd.DataFrame(data)
print(df)
```



 ### 2. From a List of Lists

```python
data = [['Ram', 28, 'New York'],
        ['Shyam', 35, 'Paris'],
        ['Sita', 42, 'London'],
        ['Geeta', 29, 'Sydney']]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)
```


 ### 3. From a List of Dictionaries

```python
data = [{'Name': 'Ram', 'Age': 28, 'City': 'New York'},
        {'Name': 'Shyam', 'Age': 35, 'City': 'Paris'},
        {'Name': 'Sita', 'Age': 42, 'City': 'London'},
        {'Name': 'Geeta', 'Age': 29, 'City': 'Sydney'}]

df = pd.DataFrame(data)
print(df)
```

 ### 4. From a NumPy Array

```python
import numpy as np

data = np.array([['Ram', 28, 'New York'],
                 ['Shyam', 35, 'Paris'],
                 ['Sita', 42, 'London'],
                 ['Geeta', 29, 'Sydney']])

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)
```

Output in All above cases
```
    Name  Age      City
0    Ram   28  New York
1  Shyam   35     Paris
2   Sita   42    London
3  Geeta   29    Sydney
```



 ### 5. From a CSV File

```python
# Assuming 'data.csv' contains the data
df = pd.read_csv('weather.csv')
df.head()
```
Output 
```
Data.Precipitation	Date.Full	Date.Month	Date.Week of	Date.Year	Station.City	Station.Code	Station.Location	Station.State	Data.Temperature.Avg Temp	Data.Temperature.Max Temp	Data.Temperature.Min Temp	Data.Wind.Direction	Data.Wind.Speed
0	0.00	2016-01-03	1	3	2016	Birmingham	BHM	Birmingham, AL	Alabama	39	46	32	33	4.33
1	0.00	2016-01-03	1	3	2016	Huntsville	HSV	Huntsville, AL	Alabama	39	47	31	32	3.86
2	0.16	2016-01-03	1	3	2016	Mobile	MOB	Mobile, AL	Alabama	46	51	41	35	9.73
3	0.00	2016-01-03	1	3	2016	Montgomery	MGM	Montgomery, AL	Alabama	45	52	38	32	6.86
4	0.01	2016-01-03	1	3	2016	Anchorage	ANC	Anchorage, AK	Alaska	34	38	29	19	7.80
```


## Creating Pandas Series

Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). There are several ways to create a Series in Pandas:

 ### 1. From a List

```python
import pandas as pd

# Creating a Pandas Series from a list
a = [1, 2, 3, 4, 5]
var = pd.Series(a, index=['a', 'b', 'c', 'd', 'e'])
print(var)
print(var['e'])
```
`print(var['e'])`: Accesses the value associated with the index label 'e' in the series.

Output:
```
a    1
b    2
c    3
d    4
e    5
dtype: int64
5
```

###  2. From a NumPy Array

```python
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])
series = pd.Series(data)
print(series)
```
output
```
0    a
1    b
2    c
3    d
dtype: object
```

### 3. From a Dictionary

```python
# Creating a simple Pandas Series from a dictionary
food_calorie = {
    'apple': 420,
    'banana': 300,
    'egg': 50
}
my_series = pd.Series(food_calorie)
print(my_series)
```

Output:
```
apple     420
banana    300
egg        50
dtype: int64
```
**Creating series from only certain keys**

```python
another_var = pd.Series(food_calorie, index=['apple', 'egg'])
print(another_var)
```

Output:
```
apple    420
egg       50
dtype: int64
```


### 4. From a Scalar Value

```python
scalar_value = 5
series = pd.Series(scalar_value, index=['a', 'b', 'c', 'd'])
print(series)
```
Output:
```
a    5
b    5
c    5
d    5
dtype: int64
```
 5. Using `pd.date_range()` for Date Indices

```python
dates = pd.date_range('20240101', periods=4)
series = pd.Series([1, 2, 3, 4], index=dates)
print(series)
```
Output:
```
scalar_value = 5
series = pd.Series(scalar_value, index=['a', 'b', 'c', 'd'])
print(series)
```

## DATAFRAME CREATION

```python 
food_data = {
    "name": ['egg', 'chowmein', 'momo', 'achar', 'tarkari'],
    "calorie": [500, 600, 300, 40, 500]
}

food_var = pd.DataFrame(food_data)
food_var
```
Output:
```
	name	calorie
0	egg	500
1	chowmein	600
2	momo	300
3	achar	40
4	tarkari	500
```
**Locating the row**

```python
food_var.loc[2]
```
Output
```
name       momo
calorie     300
Name: 2, dtype: object
```
**Locating a list of rows**

```python
food_var.loc[0:3].head()
food_var.loc[[1, 3]].head()
```
Output
```
name	calorie
1	chowmein	600
3	achar	40
```

**Creating own index**

```python
indexed_food = pd.DataFrame(food_data, index=['first', 'second', 'third', 'fourth', 'fifth'])
indexed_food.head()
```
Output
```
name	calorie
first	egg	500
second	chowmein	600
third	momo	300
fourth	achar	40
fifth	tarkari	500

```

**Accessing named indexes**

```python
print(indexed_food.loc["first"])
```
Output
```
name       egg
calorie    500
Name: first, dtype: object
```
- `loc`: Accesses a group of rows by index label and returns a series for the specified row.

## Obtaining Basic Information About DataFrame

### Displaying basic information about DataFrame

```python
import pandas as pd
df = pd.read_csv("weather.csv")
df.info()
```
Output
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 16743 entries, 0 to 16742
Data columns (total 14 columns):
 #   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   Data.Precipitation         16743 non-null  float64
 1   Date.Full                  16743 non-null  object 
 2   Date.Month                 16743 non-null  int64  
 3   Date.Week of               16743 non-null  int64  
 4   Date.Year                  16743 non-null  int64  
 5   Station.City               16743 non-null  object 
 6   Station.Code               16743 non-null  object 
 7   Station.Location           16743 non-null  object 
 8   Station.State              16743 non-null  object 
 9   Data.Temperature.Avg Temp  16743 non-null  int64  
 10  Data.Temperature.Max Temp  16743 non-null  int64  
 11  Data.Temperature.Min Temp  16743 non-null  int64  
 12  Data.Wind.Direction        16743 non-null  int64  
 13  Data.Wind.Speed            16743 non-null  float64
dtypes: float64(2), int64(7), object(5)
memory usage: 1.8+ MB
```
###  Displaying columns
 ```python
df.columns
 ```
Output
```
Index(['Data.Precipitation', 'Date.Full', 'Date.Month', 'Date.Week of',
       'Date.Year', 'Station.City', 'Station.Code', 'Station.Location',
       'Station.State', 'Data.Temperature.Avg Temp',
       'Data.Temperature.Max Temp', 'Data.Temperature.Min Temp',
       'Data.Wind.Direction', 'Data.Wind.Speed'],
      dtype='object')
```
### Seeing first few rows
```python
df.head()
```

### Seeing last few rows
```python
df.tail()
```

### Accessing Certain Columns
```python
df['Data.Precipitation'].head()
```
Output
```
0    0.00
1    0.00
2    0.16
3    0.00
4    0.01
Name: Data.Precipitation, dtype: float64
```
### Renaming the columns
```python 
df.rename(columns= {'Data.Precipitation' : 'Data.Precipitate'})
```


## Selection and Indexing

### Selecting a single column
```python

data = [['Ram', 28, 'New York'],
        ['Shyam', 35, 'Paris'],
        ['Sita', 42, 'London'],
        ['Geeta', 29, 'Sydney']]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df['Name'])
```
Output
```
0      Ram
1    Shyam
2     Sita
3    Geeta
Name: Name, dtype: object
```
### Selecting multiple columns
```python
print(df[['Name', 'Age']])
```
Output
```
    Name  Age
0    Ram   28
1  Shyam   35
2   Sita   42
3  Geeta   29
```


### Selecting rows by index
```python
print(df.iloc[0])
```
Output
```
Name         Ram
Age           28
City    New York
Name: 0, dtype: object
```
### Selecting rows and columns by index
```python
print(df.iloc[0, 1])
```
Output
```
2016-01-03
```

### Extracting columns that meet certain conditions
```python
import pandas as pd
df = pd.read_csv("weather.csv")
print(df[['Date.Month', 'Station.Code']][df['Data.Wind.Speed'] == 2])
```
Output
```
      Date.Month Station.Code
3394            3          IPT
3406            3          TRI
4121            4          ORT
5362            5          BHM
5412            5          FAT
5535            5          HVR
5598            5          RDM
8513            7          CRW
10504           8          AGS
11624           9          CSV
12152           9          GPT
12488          10          HLN
12621          10          HTS
12936          10          CRW
13037          10          AGS
13583          10          HSV
14238          11          MCG
14563          11          TAL
14898          11          SAC
15053          11          RDU
16624           1          ROW
```

### Grouping (Lets Get only the sunday data)
```python
sunday_data = df.groupby('Date.Full')
sunday_data.head()
```
Output
```

Data.Precipitation	Date.Full	Date.Month	Date.Week of	Date.Year	Station.City	Station.Code	Station.Location	Station.State	Data.Temperature.Avg Temp	Data.Temperature.Max Temp	Data.Temperature.Min Temp	Data.Wind.Direction	Data.Wind.Speed
0	0.00	2016-01-03	1	3	2016	Birmingham	BHM	Birmingham, AL	Alabama	39	46	32	33	4.33
1	0.00	2016-01-03	1	3	2016	Huntsville	HSV	Huntsville, AL	Alabama	39	47	31	32	3.86
2	0.16	2016-01-03	1	3	2016	Mobile	MOB	Mobile, AL	Alabama	46	51	41	35	9.73
3	0.00	2016-01-03	1	3	2016	Montgomery	MGM	Montgomery, AL	Alabama	45	52	38	32	6.86
4	0.01	2016-01-03	1	3	2016	Anchorage	ANC	Anchorage, AK	Alaska	34	38	29	19	7.80
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
16426	0.51	2017-01-01	1	1	2017	Birmingham	BHM	Birmingham, AL	Alabama	54	64	45	22	6.28
16427	1.57	2017-01-01	1	1	2017	Huntsville	HSV	Huntsville, AL	Alabama	52	62	41	23	7.10
16428	1.72	2017-01-01	1	1	2017	Mobile	MOB	Mobile, AL	Alabama	62	71	53	22	6.33
16429	0.62	2017-01-01	1	1	2017	Montgomery	MGM	Montgomery, AL	Alabama	58	69	47	21	4.66
16430	0.52	2017-01-01	1	1	2017	Anchorage	ANC	Anchorage, AK	Alaska	20	27	12	7	2.45
265 rows × 14 columns
```

### Getting data of certain data from the group
```python
date_data.get_group('2016-01-03')
```
Output
```

Data.Precipitation	Date.Full	Date.Month	Date.Week of	Date.Year	Station.City	Station.Code	Station.Location	Station.State	Data.Temperature.Avg Temp	Data.Temperature.Max Temp	Data.Temperature.Min Temp	Data.Wind.Direction	Data.Wind.Speed
0	0.00	2016-01-03	1	3	2016	Birmingham	BHM	Birmingham, AL	Alabama	39	46	32	33	4.33
1	0.00	2016-01-03	1	3	2016	Huntsville	HSV	Huntsville, AL	Alabama	39	47	31	32	3.86
2	0.16	2016-01-03	1	3	2016	Mobile	MOB	Mobile, AL	Alabama	46	51	41	35	9.73
3	0.00	2016-01-03	1	3	2016	Montgomery	MGM	Montgomery, AL	Alabama	45	52	38	32	6.86
4	0.01	2016-01-03	1	3	2016	Anchorage	ANC	Anchorage, AK	Alaska	34	38	29	19	7.80
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
310	0.00	2016-01-03	1	3	2016	Casper	CPR	Casper, WY	Wyoming	21	28	13	22	16.13
311	0.00	2016-01-03	1	3	2016	Cheyenne	CYS	Cheyenne, WY	Wyoming	23	38	7	27	8.33
312	0.00	2016-01-03	1	3	2016	Lander	LND	Lander, WY	Wyoming	11	21	0	27	0.43
313	0.00	2016-01-03	1	3	2016	Rawlins	RWL	Rawlins, WY	Wyoming	3	19	-13	16	1.90
314	0.00	2016-01-03	1	3	2016	Sheridan	SHR	Sheridan, WY	Wyoming	22	36	7	21	0.80
315 rows × 14 columns
```

### Aggregations  
Lets see the average precipitation in each state
```python
df.groupby('Station.Code').agg({'Data.Precipitation':'mean' })
```
Output
```

ABE	0.551509
ABI	0.664340
ABQ	0.122264
ABR	0.340943
ACT	0.682075
...	...
WMC	0.160943
WRG	0.000000
YAK	2.073585
YKM	0.187925
YNG	0.727925
318 rows × 1 columns
```

### Merging Dataframes
```python
df1 = pd.DataFrame({"Station.Code" : ['ABE','ABI','ABQ'] })
df2 = pd.DataFrame({"Station.Code" : ['ABI','ABQ'] })
pd.merge(df1,df2,on='Station.Code')
# This returns the matching rows in both data frames
```
Output
```

Station.Code
0	ABI
1	ABQ
```

## Index Basics

```python

data = [['Ram', 28, 'New York'],
        ['Shyam', 35, 'Paris'],
        ['Sita', 42, 'London'],
        ['Geeta', 29, 'Sydney']]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

# Setting a new index
df.set_index('Name', inplace=True)
print(df)

# Resetting index
df.reset_index(inplace=True)
print(df)
```

Output:
```
       Age      City
Name                
Ram     28  New York
Shyam   35     Paris
Sita    42    London
Geeta   29    Sydney
    Name  Age      City
0    Ram   28  New York
1  Shyam   35     Paris
2   Sita   42    London
3  Geeta   29    Sydney
```

## Filtering
### Filtering with selection brackets
```python
print(df[df['Age'] > 25])

```
Output
```
    Name  Age      City
0    Ram   28  New York
1  Shyam   35     Paris
2   Sita   42    London
3  Geeta   29    Sydney
```

### Using isin() for filtering
```python
print(df[df['City'].isin(['New York', 'Paris'])])
```
Output
```
    Name  Age      City
0    Ram   28  New York
1  Shyam   35     Paris
```
### Using between() for filtering
```python
print(df[df['Age'].between(25, 30)])
```
Output
```
  Name  Age      City
0    Ram   28  New York
3  Geeta   29    Sydney
```

### Using contains() for filtering
```python 
print(df[df['Name'].str.contains('G')])
```
Output
```
     Name  Age    City
3  Geeta   29  Sydney
```
### Using query() for filtering
```python
print(df.query('Age < 30'))
```
Output
```
    Name  Age      City
0    Ram   28  New York
3  Geeta   29    Sydney
```

### Using loc[] for filtering
```python
print(df.loc[df['Age'] > 25])
```
Output
```
    Name  Age      City
0    Ram   28  New York
1  Shyam   35     Paris
2   Sita   42    London
3  Geeta   29    Sydney
```

### Using pandas filter() for filtering
```python
print(df.filter(items=['Name', 'City']))
```

## Useful Methods

### Using apply()
```python
print(df['Age'].apply(lambda x: x * 2))
```
Output
```
0    56
1    70
2    84
3    58
Name: Age, dtype: int64
```

### Using describe()
```python
print(df.describe())
```
Output
```
             Age
count   4.000000
mean   33.500000
std     6.454972
min    28.000000
25%    28.750000
50%    32.000000
75%    36.750000
max    42.000000
```

### Using sort_values()
```python
print(df.sort_values(by='Age'))
```
Output
```
    Name  Age      City
0    Ram   28  New York
3  Geeta   29    Sydney
1  Shyam   35     Paris
2   Sita   42    London
```

### Using idxmin and idxmax
```python
print(df['Age'].idxmin())
print(df['Age'].idxmax())
```
Output
```
0
2
```
### Using value_counts()

```python
print(df['Age'].value_counts())
```
Output
```
Age
28    1
35    1
42    1
29    1
Name: count, dtype: int64
```

### Using replace()
```python
print(df.replace({'New York': 'NY', 'Paris': 'FR'}))
```
Output
```
    Name  Age    City
0    Ram   28      NY
1  Shyam   35      FR
2   Sita   42  London
3  Geeta   29  Sydney
```

### Using unique() and nunique()
```python
print(df['City'].unique())
print(df['City'].nunique())
```
Output
```
['New York' 'Paris' 'London' 'Sydney']
4
```

### Using map()
```python
mapping = {'Ram': 'R', 'Shyam': 'S', 'Sita':'Si', 'Geeta': 'G'}
print(df['Name'].map(mapping))
```
Output
```
0     R
1     S
2    Si
3     G
Name: Name, dtype: object
```

### Using duplicated() and drop_duplicates()
```python
print(df.duplicated())
print(df.drop_duplicates())
```
Output
```
0    False
1    False
2    False
3    False
dtype: bool
    Name  Age      City
0    Ram   28  New York
1  Shyam   35     Paris
2   Sita   42    London
3  Geeta   29    Sydney
```

### Using between()
```python
print(df['Age'].between(25, 30))
```
```
0     True
1    False
2    False
3     True
Name: Age, dtype: bool
```
## Handling Missing Data

Real-world data contains missing values. Missing data can look like:

* -999 or 99 
* empty string("") or (" ")
* NaN/NA
* -1
* very large number
* Symbols: dot(.), or question Mark(?) etc.

There are several different approaches to address missing values. Two of them are:

* **Delation** 
Delete all rows with missing value or delete rows that contains missing value for a
column.

* **Imputation**  
Fill missing value using mean or median or mode or any arbitrary number generated
from algorithm or EDA.


### Dropping Rows with Missing Values
To remove rows containing missing values, use the `dropna()` function.

Example 1
```python
# Creating DataFrame with missing data
data_missing = {'Name': ['John', 'Alice', 'Bob', None],
                'Age': [25, None, 35, 40],
                'City': ['New York', 'Paris', None, 'London']}
df_missing = pd.DataFrame(data_missing)
print(df_missing)

# Checking for missing values
print(df_missing.isna())

# Dropping rows with missing values
print(df_missing.dropna())

```
Output
```
    Name   Age      City
0   John  25.0  New York
1  Alice   NaN     Paris
2    Bob  35.0      None
3   None  40.0    London
    Name    Age   City
0  False  False  False
1  False   True  False
2  False  False   True
3   True  False  False
   Name   Age      City
0  John  25.0  New York
``` 

Example 2
```python
import pandas as pd
import numpy as np

missing_dictionary = {
    "name": ['egg', 'chowmein', 'momo', 'achar', 'tarkari', np.nan, 'puri'],
    "calorie": [500, 600, 300, 40, 500, np.nan, np.nan]
}

missing_data = pd.DataFrame(missing_dictionary)

replaced_data = missing_data.dropna(inplace=True)
```
Output
```
name	calorie
0	egg	500.0
1	chowmein	600.0
2	momo	300.0
3	achar	40.0
4	tarkari	500.0
```
### Filling Missing Values
Empty cells can also be filled with specific values using the `fillna()` function. For example, filling missing values with a constant:

```python
filled_data = missing_data.fillna(50)
```

Or filling missing values with column-specific values:

```python
missing_data.fillna({"calorie": 50, "name": "food"}, inplace=True)
```

### Filling with Mean, Median, or Mode
An alternative approach is to fill missing values with statistical measures like mean, median, or mode:

```python
mean_calorie = missing_data["calorie"].mean()
missing_data.fillna({"calorie": mean_calorie, "name": "food"}, inplace=True)
```

## Cleaning Data of Wrong Format
Data in incorrect formats need to be converted to the desired format or removed if conversion is not possible.

### Converting Data Types
To convert data types, such as converting strings to datetime objects:

```python
time_dictionary = {
    "date": ['2022/12/1', '2023/11/15', "20240520"],
    "day": ['sunday', 'monday', 'tuesday']
}
time_data = pd.DataFrame(time_dictionary)

time_data['date'] = pd.to_datetime(time_data['date'], errors='coerce')
```



 

## References
https://towardsdatascience.com/pandas-from-basic-to-advanced-for-data-scientists-aee4eed19cfe

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html
