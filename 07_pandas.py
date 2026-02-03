# Pandas 
# Pandas is a powerful data manipulation and analysis library for Python. It provides data structures like Series and DataFrame that make it easy to work with structured data.
# It is widely used for data cleaning, transformation, and analysis tasks.


#  first step import pandas 
import pandas as pd 
import numpy as np 


# creating a dataframe (2D data structure with labeled axes)
df = pd.DataFrame(np.arange(1,21).reshape(5,4),index=['Row1', 'Row2', 'Row3', 'Row4', 'Row5'], columns=["Column1", "Column2", "Column3", "Column4"])# hear pd.dataframe is used to create a dataframe, np.arange(1,21).reshape(5,4) is used to create a 5x4 array with values from 1 to 20, index is used to set row labels, and columns is used to set column labels.
print(df.head())# for showing the dataframe 



## converting dataframe to csv file
c_file =df.to_csv("my_data.csv", index = False)# to_csv is used to convert dataframe to csv file, "my_data.csv" is the name of the csv file. index = False is used to avoid writing row indices to the csv file.
print("DataFrame has been converted to my_data.csv")# the csv file will be created in the current working directory.



# accessing elements in dataframe

# there are 2 main methods to access elements in dataframe.

# 1 - loc[] - label-based indexing(in this we use row and column labels to access elements)
# 2 - iloc[] - integer-based indexing(in this we use integer positions to access elements)

# first we have to know the difference between dataframe and data series 
# in dataframe (it consider more than one row and column )
# in series (it consider either one row or one column)

# example for loc

# accessing a single element using loc
element_loc= df.loc['Row2', 'Column3'] # accessing element at Row2 and Column3
print("Element at Row2, Column3 using loc:", element_loc)
# output: Element at Row2, Column3 using loc: 10    
print(type(element_loc))# it will show the type of the element


# accessing a single row using loc
row_loc=df.loc["Row3"]# accessing entire Row3
print("row 3 using loc[]" , row_loc)
# output: row 3 using loc[] Column1     9
# Column2    10
# Column3    11 
# Column4    12
# Name: Row3, dtype: int64
print(type(row_loc))# it will show the type of the row (series) because it consider one row


# accessing a single column using loc
column_loc =df.loc[:, "Column2"]# accessing entire Column2(here we have use :, because we want all rows of Column2)
print("Column 2 using loc[]")
print(column_loc)



# now example for iloc
# accessing a single element using iloc
element_iloc = df.iloc[1, 2] # accessing element at 2nd row and 3rd column (index starts from 0)
print("Element at 2nd row, 3rd column using iloc:", element_iloc)
# output: Element at 2nd row, 3rd column using iloc: 10
print(type(element_iloc))# it will show the type of the element  

# accessing a single row using iloc
row_iloc = df.iloc[2] # accessing entire 3rd row
print("3rd row using iloc[]")
print(row_iloc)
# output: 3rd row using iloc[]
# Column1     9
# Column2    10
# Column3    11         

# accessing both row and column using iloc
sub_df_iloc = df.iloc[1:4, 1:3] # accessing rows 2 to 4 and columns 2 to 3
print("Sub-dataframe using iloc[]")
print(sub_df_iloc)
# output: Sub-dataframe using iloc[]
#        Column2  Column3
# Row2       6        10
# Row3      10        11
# Row4      14        12    

print(type(sub_df_iloc))# it will show the type of the sub dataframe (dataframe) because it consider more than one row and column   

# to convert a dataframe into an array 

array_from_df = sub_df_iloc.values# using .values attribute to convert dataframe to array
print("Array converted from sub-dataframe:")
print(array_from_df)

# output: Array converted from sub-dataframe:
# [[ 6 10]
#  [10 11]
#  [14 12]]
print(type(array_from_df))# it will show the type of the array (numpy.ndarray)



# operations on dataframe

#1 to check the null condition in dataframe  
print(df.isnull())# isnull() is used to check for null values in the dataframe
# output: it will return a dataframe of same shape with boolean values (True for null and False for non-null)
#      Column1  Column2  Column3  Column4
# Row1    False    False    False    False 
# Row2    False    False    False    False
# Row3    False    False    False    False
# Row4    False    False    False    False
# Row5    False    False    False    False  

# 2 count function to count non-null values in each column
count_non_null = df.count()# count() is used to count non-null values in each column
print("Count of non-null values in each column:")
print(count_non_null)
# output: Count of non-null values in each column:
# Column1    5
# Column2    5
# Column3    5
# Column4    5
# dtype: int64

# 3 unique function to get unique values in a column( unique values means no duplicate values)
unique_values = df['Column1'].unique()# unique() is used to get unique values in a column
print("Unique values in Column1:")
print(unique_values)
# output: Unique values in Column1:
# [ 1  5  9 13 17] 
print(type(unique_values))# it will show the type of the unique values (numpy.ndarray)  
