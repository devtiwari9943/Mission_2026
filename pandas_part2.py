# how to read a dataset from a CSV file using pandas
import pandas as pd 
import numpy as np 



# reading a CSV file
df=pd.read_csv("Pokemon.csv")# pd.read_csv is used to read a CSV file, "Pokemon.csv" is the name of the CSV file.csv means comma separated values
print(df.head())# head() function is used to display the first 5 rows of the dataframe

# if the csv file is does not seperated by comma then we can use sep parameter to specify the separator
# df=pd.read_csv("file.txt",sep=";")# sep=";" means the file is separated by semicolon


# inbuilt functions in pandas

#1 df.info() - provides a summary of the dataframe including the number of non-null entries and data types of each column 
print(df.info())

# output:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 800 entries, 0 to 799
# Data columns (total 13 columns):
#  #   Column        Non-Null Count  Dtype 
# ---  ------        --------------  -----
#  0   #            800 non-null    int64
#  1   Name         800 non-null    object
#  2   Type 1       800 non-null    object
#  3   Type 2       414 non-null    object
#  4   Total        800 non-null    int64
#  5   HP           800 non-null    int64
#  6   Attack       800 non-null    int64
#  7   Defense      800 non-null    int64
#  8   Sp. Atk      800 non-null    int64
#  9   Sp. Def      800 non-null    int64
#  10  Speed        800 non-null    int64
#  11  Generation   800 non-null    int64
#  12  Legendary    800 non-null    boolean
# dtypes: boolean(1), int64(10), object(2)
# memory usage: 78.3+ KB    


#2 df.describe() - generates descriptive statistics that summarize the central tendency, dispersion and shape of a dataset's distribution, excluding NaN values
print(df.describe())# only numerical columns are considered in the output of describe() because it provides statistics like mean, std, min, max etc which are applicable to numerical data only
# output:
#                 #       Total         HP      Attack     Defense     Sp. Atk     Sp. Def      Speed  Generation
# count  800.000000   800.000000  800.000000  800.000000  800.000000  800.000000  800.000000  800.000000
# mean   400.500000   435.769375   69.258750   79.001250   73.842500   72.820000   68.277500    3.323750
# std    231.611701   119.963205   26.028564   28.475467   26.312776   26.161519   25.885389
#etc



# df['Column_Name'] to access a specific column in the dataframe
print(df['Name'])# this will print the 'Name' column of the dataframe   
# output:
# 0       Bulbasaur
# 1         Ivysaur
# 2        Venusaur         
#etc



# df[['Col1','Col2']] to access multiple columns in the dataframe
print(df[['Name','Type 1','HP']])# this will print the 'Name', 'Type 1' and 'HP' columns of the dataframe
# output:
#            Name Type 1  HP
# 0     Bulbasaur  Grass  45
# 1       Ivysaur  Grass  60
# etc


# if we want the unique categories in a column we can use the unique() function
print(df['Type 1'].unique())# this will print the unique categories in the 'Type 1' column
# output:
# ['Grass' 'Fire' 'Water' 'Bug' 'Normal' 'Poison' 'Electric' 'Ground' 'Fairy'
#  'Fighting' 'Psychic' 'Rock' 'Ghost' 'Ice' 'Dragon' 'Dark' 'Steel' 'Flying']
# etc


# get the unique category counts 
print(df['Type 1'].value_counts())# this will print the unique categories in the 'Type 1' column along with their counts
# output:
# Water       112
# Normal      98
# Grass       70
#etc




# if we have a datain string and want to convert into csv file we can use stringIO 
from io import StringIO
data = """A,B,C,D
1,2,3,4
5,6,7,8
9,10,11,12"""   
# use StringIO to convert the string data into a file-like object
data = StringIO(data)   
df2 = pd.read_csv(data)# read the data using pd.read_csv
print(df2)# print the dataframe
# output:
#    A   B   C   D
# 0  1   2   3   4
# 1  5   6   7   8





## read from specific columns in a csv file
df3=pd.read_csv("Pokemon.csv",usecols=['Name','Type 1','HP'])# usecols parameter is used to read specific columns from the csv file
print(df3.head())# print the first 5 rows of the dataframe
# output:
#           Name Type 1  HP         
# 0     Bulbasaur  Grass  45
# 1       Ivysaur  Grass  60
#etc




# read a specific number of rows from a csv file
df4=pd.read_csv("Pokemon.csv",nrows=10)# nrows parameter is used to read a specific number of rows from the csv file
print(df4)# print the dataframe
# output:
#     #         Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 0   1   Bulbasaur  Grass  Poison    318  45      49       49       65       65     45           1      False
# 1   2     Ivysaur  Grass  Poison    405  60      62       63       80       80     60
# etc




# specifying columns data types 
data = ("a,b,c,d\n"
        "1,2,3,4\n"
        "5,6,7,8\n"
        "9,10,11,12")
df5=pd.read_csv(StringIO(data),dtype=object)# dtype parameter is used to specify the data type of the columns and object means string
print(df5)# print the dataframe
# output:
#    a   b   c   d
# 0  1   2   3   4
# 1  5   6   7   8

# if we want to specify different data types for different columns we can use a dictionary
data = ("a,b,c,d\n"
        "1,2,3,4\n"
        "5,6,7,8\n"
        "9,10,11,12")
dtype_dict={'a':np.int64,'b':np.float64,'c':np.int8,'d':np.float64}
df6=pd.read_csv(StringIO(data),dtype=dtype_dict)# dtype parameter is used to specify the data type of the columns
print(df6)# print the dataframe
# output:
#    a     b   c     d
# 0  1   2.0   3   4.0
# 1  5   6.0   7   8.0
# 2  9  10.0  11  12.0  
print(df6.dtypes)# print the data types of the columns
# output:
# a      int64
# b    float64
# c       int8
# d    float64
# dtype: object 

# if we want to change the index column while reading the csv file we can use index_col parameter
df7=pd.read_csv("Pokemon.csv",index_col=0)# index_col parameter is used to specify the index column of the dataframe
print(df7.head())# print the first 5 rows of the dataframe
# output:
#               Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# # 0     Bulbasaur  Grass  Poison    318  45      49       49       65       65     45           1      False
# 1       Ivysaur  Grass  Poison    405  60      62       63       80       80     60           1      False
# etc

# if we want to make any column as index column we can use index_col parameter
df8=pd.read_csv("Pokemon.csv",index_col='Name')# index_col parameter is used to specify the index column of the dataframe
print(df8.head())# print the first          
# output:
#               # Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# Name      0     Bulbasaur  Grass  Poison    318  45      49       49       65       65     45           1      False
# Ivysaur   1       Ivysaur  Grass  Poison    405  60      62       63       80       80     60           1      False
# etc

# handling missing values while reading a csv file
data = ("A,B,C,D\n"
        "1,2,,4\n"
        "5,,7,8\n"
        "9,10,11,")