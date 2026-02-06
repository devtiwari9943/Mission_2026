# LISTS IN PYTHON

# list is a data structure in python that is mutable, ordered collection of items.
# Lists are defined by enclosing elements in square brackets [] and separating them with commas.
 
# example of a list
# types to make a list
# 1 - using square brackets
my_list = [1, 2, 3, 4, 5]
print("List using square brackets:", my_list)
print(type(my_list))

# 2 - using the list() constructor
another_list = list((6, 7, 8, 9, 10))
print("List using list() constructor:", another_list)
print(type(another_list))

# basic operations on lists

# 1 - Accessing elements
print("First element of my_list:", my_list[0])
print("Last element of another_list:", another_list[-1])

# 2 - Modifying elements
my_list[2] = 99
print("Modified my_list:", my_list)

# 3 - Adding elements
my_list.append(6)
print("my_list after appending 6:", my_list)    
another_list.insert(0, 5)# inserting 5 at index 0
print("another_list after inserting 5 at index 0:", another_list)

# 4 - Removing elements
my_list.remove(99)
print("my_list after removing 99:", my_list)

popped_element = another_list.pop()# removing last element
print("another_list after popping last element:", another_list)
print("Popped element:", popped_element)

# 5 - Slicing
sliced_list = my_list[1:4]
print("Sliced my_list from index 1 to 3:", sliced_list)
# 6 - Iterating through a list
print("Iterating through my_list:")
for item in my_list:
    print(item)
a = 3
b = 4
print(a + b)        
a =3
b=4
print(a+b)

#7 exrtending a list
my_list.extend([7,8,9])# extending my_list by adding multiple elements
print("my_list after extending:", my_list)

#8 sum of elements in a list
total = sum(my_list)
print("Sum of elements in my_list:", total)

#9 counting occurrences of an element
count_of_4 = my_list.count(4)
print("Count of 4 in my_list:", count_of_4)

#10 length of a list
length_of_my_list = len(my_list)
print("Length of my_list:", length_of_my_list)

# 11 index of an element
index_of_5 = my_list.index(5)
print("Index of 5 in my_list:", index_of_5)

#for searching an element in specific range
index_of_8 = my_list.index(8, 5, 10) # searching for 8 between index 5 and 10
print("Index of 8 in my_list between index 5 and 10:", index_of_8)

# 12 minimum and maximum element in a list
min_element = min(my_list)
max_element = max(my_list)
print("Minimum element in my_list:", min_element)
print("Maximum element in my_list:", max_element)

# 13 multiplying a list
multiplied_list = my_list * 2
print("my_list multiplied by 2:", multiplied_list)
# output:# my_list multiplied by 2: [1, 2, 4, 5, 6, 7, 8, 9, 1, 2, 4, 5, 6, 7, 8, 9]