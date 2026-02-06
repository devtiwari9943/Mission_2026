# NUMPY in PYTHON
# NumPy is a powerful library for numerical computing in Python.
# It provides support for arrays, matrices, and a wide range of mathematical functions.

##  Importing NumPy
import numpy as np

# Creating a NumPy array
my_lst = [1, 2, 3, 4, 5]
my_array = np.array(my_lst)# Converting a list to a NumPy array
print("Initial NumPy array:", my_array)
print("Type of my_array:", type(my_array))
# output: [1 2 3 4 5]  # it is a 1D array , if we have 1  bracket its 1D, 2 brackets its 2D and so on

# operations on NumPy arrays

# arr.shape - returns the dimensions of the array
print("Shape of my_array:", my_array.shape)
# output: (5,)  # 1D array with 5 elements


# 2 reshape - changing the shape of the array

# multi nested array
list_1 =[1,2,3,4,5]
list_2 =[6,7,8,9,10]
list_3 =[11,12,13,14,15]
arr=np.array([list_1,list_2,list_3])
print(arr)
# output:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]]# 2D array with 3 rows and 5 columns

print("Shape of arr before reshaping:", arr.shape)
# output: (3, 5)

reshaped_arr = arr.reshape(5, 3)  # Reshaping to 5 rows and 3 columns
print("Reshaped array:\n", reshaped_arr)
print("Shape of reshaped_arr:", reshaped_arr.shape)
# output:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]
#  [13 14 15]]
# output: (5, 3)

# 3 - Accessing elements

# first creating an  array

# example 1D array

arr_01= np.array([1,2,3,4,5,6,7,8,9,10])
print("Element at index 0:", arr_01[0])  # Accessing first element
print("Element at index 4:", arr_01[4])  # Accessing fifth element
# output: Element at index 0: 1
# output: Element at index 4: 5

# example 2D array
arr_02 = np.array([[1,2,3], [4,5,6], [7,8,9]])
# show the array
print("2D Array:\n", arr_02)

# output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# for accessing elements in 2D array we use row and column index
print("Element at row 0, column 1:", arr_02[0, 1])  # Accessing element at first row, second column
print("Element at row 2, column 2:", arr_02[2, 2])  # Accessing element at third row, third column
# output: Element at row 0, column 1 : 2
# output: Element at row 0, column 1: 2
# output: Element at row 2, column 2: 9 

# for retrieving a entire row ,column or both 

# Retrieving entire row
print("First row:", arr_02[0])  # Accessing first row
print("Third row:", arr_02[2])  # Accessing third row

# Retrieving entire column
print("First column:", arr_02[:, 0])  # Accessing first column
print("Third column:", arr_02[:, 2])  # Accessing third column
# output: First row: [1 2 3]
# output: Third row: [7 8 9]
# output: First column: [1 4 7]
# output: Third column: [3 6 9]

# retrieving sub-array (slicing)
sub_array = arr_02[0:2, 1:3]  # Slicing to get a sub-array, rows 0-1 and columns 1-2
print("Sub-array:\n", sub_array)
# output:
# [[2 3]
#  [5 6]]   

# 4 - Array operations

# 4.1 arrange - creating an array with a range of values 
arr_range = np.arange(0, 20)  # Creating an array with values from 0 to 20 
print("Array with range of values:", arr_range)
# output: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

# step value in arange( it means skipping values)

arr_range = np.arange(0, 20, 2)  # Creating an array with values from 0 to 20 with a step of 2
print("Array with range of values:", arr_range)
# output: [ 0  2  4  6  8 10 12 14 16 18]


# 4.2 - linspace - creating an array with evenly spaced values over a specified interval 
arr_linspace = np.linspace(0, 1, 5)  # Creating an array with 5 values between 0 and 1
print("Array with evenly spaced values:", arr_linspace)
# output: [0.   0.25 0.5  0.75 1.  ]    



# 4.3 copy function - creating a copy of an array 
original_array = np.array([1, 2, 3, 4, 5])
copied_array = original_array.copy()  # Creating a copy of the original array
print("Original array:", original_array)
print("Copied array:", copied_array)
# output: Original array: [1 2 3 4 5]
# output: Copied array: [1 2 3 4 5]


# copy and brodcasting example
original_array[3:] = 99  # Modifying the original array from index 3 onwards
print("Modified original array:", original_array)
print("Copied array after original modification:", copied_array)
# output: Modified original array: [ 1  2  3 99 99]
# output: Copied array after original modification: [1 2 3 4 5]
# This shows that the copied array remains unchanged after modifying the original array.

# 4.4 reference example
ref_array = original_array  # Creating a reference to the original array
original_array[0:2] = 77  # Modifying the original array from index 0 to 1
print("Modified original array:", original_array)
print("Reference array after original modification:", ref_array)
# output: Modified original array: [77 77  3 99 99]
# output: Reference array after original modification: [77 77  3 99 99]
# This shows that the reference array reflects changes made to the original array.





## some condition very useful in exploratory data analysis

# 1st condition : check which elements are equal to a specific value
val =2
print(original_array<val)  # Checking which elements are less than 2
# output: [False False False False False]  # All elements are not less than 2
# output will be in boolean format

# 2nd condition : array multiplication with some value (we can do any arithmetic operation like addition ,subtraction etc )
multiplied_array = original_array * 3  # Multiplying each element by 3
print("Array after multiplication by 3:", multiplied_array)
# output: Array after multiplication by 3: [231 231   9 297 297]


# 4.5 .ones and .zeros - creating arrays filled with ones or zeros 
ones_array = np.ones((2, 3))  # Creating a 2x3 array filled with ones
zeros_array = np.zeros((3, 2))  # Creating a 3x2 array filled with zeros
print("Array filled with ones:\n", ones_array)
print("Array filled with zeros:\n", zeros_array)
# output: Array filled with ones:
# [[1. 1. 1.]
#  [1. 1. 1.]]
# output: Array filled with zeros:
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]
# we can define any shape we want by changing the values in the tuple passed to ones() or zeros() functions and its data type will be float by default but we can change it by dtype parameter like np.ones((2,3), dtype=int)


# 4.6  random - generating random numbers
random_array = np.random.rand(2, 3)  # Creating a 2x3 array with random values between 0 and 1
print("Array with random values:\n", random_array)
# output: Array with random values:
# [[0.5488135  0.71518937 0.60276338]
#  [0.54488318 0.4236548  0.64589411]]
# Note: The actual output will vary each time you run the code since the values are randomly generated.

# randn - generating random numbers from a standard normal distribution (standard normal distribution  means a distribution with mean 0 and standard deviation 1)

randn_array = np.random.randn(2, 3)  # Creating a 2x3 array with random values from standard normal distribution
print("Array with random values from standard normal distribution:\n", randn_array)
# output: Array with random values from standard normal distribution:
# [[ 0.97873798  2.2408932   1.86755799]
#  [-0.97727788  0.95008842 -0.15135721]]
# Note: The actual output will vary each time you run the code


# randint - generating random integers within a specified range
randint_array = np.random.randint(0, 10, (2, 3))  # Creating a 2x3 array with random integers between 0 and 10
print("Array with random integers:\n", randint_array)
# output: Array with random integers:
# [[3 7 2]
#  [4 6 8]]
# Note: The actual output will vary each time you run the code  


# random_sample
random_sample_array = np.random.random_sample((2, 3))  # Creating a 2x3 array with random values between 0 and 1
print("Array with random values (random_sample):\n", random_sample_array)
# output: Array with random values (random_sample):
# [[0.5488135  0.71518937 0.60276338]
#  [0.54488318 0.4236548  0.64589411]]
# Note: The actual output will vary each time you run the code